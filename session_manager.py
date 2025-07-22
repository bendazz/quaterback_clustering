#!/usr/bin/env python3
"""
Day-to-Day NFL Analysis Workflow
How to efficiently work with NFL data across multiple sessions/projects
"""

import os
import json
from datetime import datetime

def check_session_status():
    """Check what's available in current session"""
    print("🔍 Current Session Status Check")
    print("=" * 40)
    
    # Check if packages are installed
    try:
        import nfl_data_py as nfl
        import pandas as pd
        import sklearn
        print("✅ Core packages: nfl_data_py, pandas, sklearn available")
        packages_ready = True
    except ImportError as e:
        print(f"❌ Missing packages: {e}")
        packages_ready = False
    
    # Check for cached data
    cache_dirs = ['nfl_data_cache', 'datasets']
    cached_data = {}
    
    for cache_dir in cache_dirs:
        if os.path.exists(cache_dir):
            files = os.listdir(cache_dir)
            total_size = sum(os.path.getsize(os.path.join(cache_dir, f)) for f in files) / (1024*1024)
            cached_data[cache_dir] = {'files': len(files), 'size_mb': total_size}
            print(f"✅ {cache_dir}: {len(files)} files ({total_size:.1f} MB)")
        else:
            print(f"❌ {cache_dir}: Not found")
    
    # Check for previous analysis results
    analysis_files = ['qb_stats_2018_2024.csv', 'veteran_qbs_clustered.csv']
    previous_work = []
    for file in analysis_files:
        if os.path.exists(file):
            mod_time = datetime.fromtimestamp(os.path.getmtime(file))
            previous_work.append(f"{file} (modified: {mod_time.strftime('%Y-%m-%d %H:%M')})")
            print(f"✅ Previous work: {file}")
        else:
            print(f"❌ Previous work: {file} not found")
    
    return {
        'packages_ready': packages_ready,
        'cached_data': cached_data,
        'previous_work': previous_work
    }

def new_project_workflow():
    """Workflow for starting a new NFL data project"""
    print("\n🚀 New Project Workflow")
    print("=" * 40)
    
    status = check_session_status()
    
    if status['packages_ready']:
        print("📦 Packages ready - dev container working!")
        
        # Quick data strategy decision
        print("\n📊 Data Strategy Options:")
        print("1. 🔄 Fresh download (latest data, slower start)")
        print("2. 📂 Use cached data (faster start, might be outdated)")
        print("3. 🎯 Specific new data (targeted download)")
        
        choice = input("\nWhich option? (1/2/3): ")
        
        if choice == "1":
            fresh_data_workflow()
        elif choice == "2":
            cached_data_workflow()
        elif choice == "3":
            targeted_data_workflow()
        else:
            print("Invalid choice, defaulting to cached data workflow")
            cached_data_workflow()
    else:
        print("❌ Packages not ready - installing...")
        print("💡 This shouldn't happen with dev container!")
        print("🔧 Run: pip install -r requirements.txt")

def fresh_data_workflow():
    """Download fresh data for new analysis"""
    print("\n🌐 Fresh Data Download")
    print("-" * 30)
    print("Running: python collect_all_data.py")
    print("⏱️  This will take 5-10 minutes but gives you latest data")
    
    # You would run: python collect_all_data.py

def cached_data_workflow():
    """Use existing cached data"""
    print("\n📂 Using Cached Data")
    print("-" * 30)
    
    from nfl_data_manager import NFLDataManager
    dm = NFLDataManager()
    dm.list_cached_files()
    
    print("\n💡 Cached data found - ready for analysis!")
    print("🚀 Run: python quick_analysis_setup.py")

def targeted_data_workflow():
    """Download specific data for new project"""
    print("\n🎯 Targeted Data Download")
    print("-" * 30)
    
    print("What specific data do you need?")
    print("1. Specific years (e.g., 2022-2024)")
    print("2. Specific positions (e.g., just QBs)")
    print("3. Play-by-play data")
    print("4. Draft/historical data")
    
    # Example for specific years
    print("\nExample for QB data 2022-2024:")
    print("""
from nfl_data_manager import NFLDataManager
dm = NFLDataManager()

# This will be fast if cached, download if not
qb_data = dm.get_weekly_data(
    years=[2022, 2023, 2024],
    columns=['player_name', 'position', 'passing_yards', 'passing_tds', 'qb_rating']
)
qb_only = qb_data[qb_data['position'] == 'QB']
""")

def save_session_info():
    """Save information about current session for future reference"""
    session_info = {
        'timestamp': datetime.now().isoformat(),
        'status': check_session_status(),
        'workspace_files': os.listdir('.'),
        'last_analysis': 'quarterback_clustering_project'
    }
    
    with open('.session_info.json', 'w') as f:
        json.dump(session_info, f, indent=2)
    
    print("💾 Session info saved to .session_info.json")

def main():
    """Main workflow function"""
    print("🏈 NFL Data Analysis - Session Manager")
    print("=" * 50)
    
    print("\n💡 Dev Container Benefits:")
    print("   ✅ Packages installed automatically")
    print("   ✅ Consistent environment every time")
    print("   ✅ No manual pip installs needed")
    
    print("\n📋 Typical Workflow:")
    print("   1. Create new codespace (dev container auto-builds)")
    print("   2. Choose data strategy (fresh/cached/targeted)")
    print("   3. Start analysis immediately")
    
    new_project_workflow()
    save_session_info()

if __name__ == "__main__":
    main()
