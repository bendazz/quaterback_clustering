#!/usr/bin/env python3
"""
NFL Data Manager - Handles data collection, caching, and persistence
Use this to collect data once and reuse across sessions
"""

import os
import pandas as pd
import pickle
from datetime import datetime, timedelta
import nfl_data_py as nfl

class NFLDataManager:
    def __init__(self, data_dir='nfl_data_cache'):
        """Initialize the data manager with a cache directory"""
        self.data_dir = data_dir
        os.makedirs(data_dir, exist_ok=True)
        
    def get_cache_path(self, data_type, years):
        """Generate cache file path"""
        year_str = f"{min(years)}-{max(years)}" if len(years) > 1 else str(years[0])
        return os.path.join(self.data_dir, f"{data_type}_{year_str}.pkl")
    
    def is_cache_valid(self, cache_path, max_age_days=7):
        """Check if cached data is still valid"""
        if not os.path.exists(cache_path):
            return False
        
        cache_time = datetime.fromtimestamp(os.path.getmtime(cache_path))
        return datetime.now() - cache_time < timedelta(days=max_age_days)
    
    def get_weekly_data(self, years, force_refresh=False, columns=None):
        """Get weekly data with caching"""
        cache_path = self.get_cache_path('weekly', years)
        
        if not force_refresh and self.is_cache_valid(cache_path):
            print(f"📂 Loading weekly data from cache: {cache_path}")
            with open(cache_path, 'rb') as f:
                return pickle.load(f)
        
        print(f"🌐 Downloading weekly data for years {years}...")
        data = nfl.import_weekly_data(years=years, columns=columns)
        
        print(f"💾 Caching data to: {cache_path}")
        with open(cache_path, 'wb') as f:
            pickle.dump(data, f)
        
        return data
    
    def get_pbp_data(self, years, force_refresh=False):
        """Get play-by-play data with caching"""
        cache_path = self.get_cache_path('pbp', years)
        
        if not force_refresh and self.is_cache_valid(cache_path):
            print(f"📂 Loading PBP data from cache: {cache_path}")
            with open(cache_path, 'rb') as f:
                return pickle.load(f)
        
        print(f"🌐 Downloading play-by-play data for years {years}...")
        data = nfl.import_pbp_data(years=years, include_participation=False)
        
        print(f"💾 Caching data to: {cache_path}")
        with open(cache_path, 'wb') as f:
            pickle.dump(data, f)
        
        return data
    
    def get_draft_data(self, years, force_refresh=False):
        """Get draft data with caching"""
        cache_path = self.get_cache_path('draft', years)
        
        if not force_refresh and self.is_cache_valid(cache_path):
            print(f"📂 Loading draft data from cache: {cache_path}")
            with open(cache_path, 'rb') as f:
                return pickle.load(f)
        
        print(f"🌐 Downloading draft data for years {years}...")
        data = nfl.import_draft_picks(years=years)
        
        print(f"💾 Caching data to: {cache_path}")
        with open(cache_path, 'wb') as f:
            pickle.dump(data, f)
        
        return data
    
    def list_cached_files(self):
        """List all cached data files"""
        print("📁 Cached Data Files:")
        print("-" * 40)
        
        if not os.path.exists(self.data_dir):
            print("   No cache directory found")
            return
        
        files = os.listdir(self.data_dir)
        if not files:
            print("   No cached files found")
            return
        
        for file in sorted(files):
            file_path = os.path.join(self.data_dir, file)
            size_mb = os.path.getsize(file_path) / (1024 * 1024)
            mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            print(f"   📄 {file}")
            print(f"      Size: {size_mb:.1f} MB")
            print(f"      Modified: {mod_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    def clear_cache(self, confirm=True):
        """Clear all cached data"""
        if confirm:
            response = input("⚠️  Are you sure you want to clear all cached data? (y/N): ")
            if response.lower() != 'y':
                print("Cache clearing cancelled")
                return
        
        if os.path.exists(self.data_dir):
            import shutil
            shutil.rmtree(self.data_dir)
            os.makedirs(self.data_dir, exist_ok=True)
            print("🗑️  Cache cleared successfully")
        else:
            print("📁 No cache directory to clear")

def main():
    """Example usage of the NFLDataManager"""
    print("NFL Data Manager - Example Usage")
    print("=" * 50)
    
    # Initialize the data manager
    dm = NFLDataManager()
    
    # List current cached files
    dm.list_cached_files()
    
    # Get some data (this will cache it for future use)
    print("\n🔄 Getting QB data for analysis...")
    
    years = list(range(2020, 2025))  # Recent years
    
    # Get weekly data (cached automatically)
    weekly_data = dm.get_weekly_data(
        years=years,
        columns=[
            'season', 'week', 'player_id', 'player_name', 'position', 'recent_team',
            'completions', 'attempts', 'passing_yards', 'passing_tds', 'interceptions',
            'qb_rating', 'passing_epa'
        ]
    )
    
    # Filter for QBs
    qb_data = weekly_data[weekly_data['position'] == 'QB']
    print(f"\n📊 Retrieved {len(qb_data)} QB records from {years[0]}-{years[-1]}")
    
    # Show cache status
    print("\n" + "="*50)
    dm.list_cached_files()
    
    print("\n💡 Next time you run this, data will load from cache instantly!")

if __name__ == "__main__":
    main()
