#!/usr/bin/env python3
"""
Template Cleanup Script
Prepares this repository to be a clean template for NFL data analysis
"""

import os
import shutil

def cleanup_for_template():
    """Remove project-specific files, keep only template essentials"""
    print("🧹 Cleaning up repository for template use...")
    
    # Files to KEEP for template
    keep_files = {
        '.devcontainer/',
        '.git/',
        'nfl_data_manager.py',
        'session_manager.py', 
        'new_project.py',
        'requirements.txt',
        'WORKFLOW_GUIDE.md',
        'TEMPLATE_README.md',
        'template_cleanup.py'  # This script itself
    }
    
    # Files to REMOVE (project-specific)
    remove_files = {
        'qb_stats_2018_2024.csv',
        'veteran_qbs_clustered.csv',
        'new_qbs_classified.csv',
        'qb_clustering_analysis.png',
        'collect_qb_stats.py',
        'qb_analysis.py',
        'check_data_range.py',
        'explore_columns.py',
        'comprehensive_data_check.py',
        'search_historical_qbs.py',
        'collect_all_data.py',
        'quick_analysis_setup.py',
        'nfl_data_cache/',
        'datasets/'
    }
    
    print("\n📁 Current files:")
    all_files = set(os.listdir('.'))
    for file in sorted(all_files):
        status = "🟢 KEEP" if file in keep_files else "🔴 REMOVE" if file in remove_files else "❓ UNKNOWN"
        print(f"   {status} {file}")
    
    # Ask for confirmation
    print(f"\n⚠️  This will remove {len(remove_files & all_files)} files/folders")
    response = input("Continue with cleanup? (y/N): ")
    
    if response.lower() != 'y':
        print("❌ Cleanup cancelled")
        return
    
    # Remove project-specific files
    removed_count = 0
    for item in remove_files:
        if os.path.exists(item):
            try:
                if os.path.isdir(item):
                    shutil.rmtree(item)
                    print(f"🗂️  Removed directory: {item}")
                else:
                    os.remove(item)
                    print(f"🗑️  Removed file: {item}")
                removed_count += 1
            except Exception as e:
                print(f"❌ Error removing {item}: {e}")
    
    # Replace README
    if os.path.exists('TEMPLATE_README.md'):
        if os.path.exists('README.md'):
            os.remove('README.md')
        os.rename('TEMPLATE_README.md', 'README.md')
        print("📝 Updated README.md for template")
    
    print(f"\n✅ Cleanup complete!")
    print(f"   Removed: {removed_count} items")
    print(f"   Kept: {len(keep_files)} template files")
    
    print(f"\n🎯 Next steps:")
    print(f"   1. Review the cleaned repository")
    print(f"   2. git add .")
    print(f"   3. git commit -m 'Clean up for template'")
    print(f"   4. git push")
    print(f"   5. Go to GitHub → Settings → Template repository ✅")

def preview_cleanup():
    """Show what would be removed without actually removing"""
    print("🔍 Preview of template cleanup...")
    
    keep_files = {
        '.devcontainer/',
        '.git/',
        'nfl_data_manager.py',
        'session_manager.py',
        'new_project.py', 
        'requirements.txt',
        'WORKFLOW_GUIDE.md',
        'TEMPLATE_README.md',
        'template_cleanup.py'
    }
    
    all_files = set(os.listdir('.'))
    
    print("\n🟢 Files to KEEP:")
    for file in sorted(all_files & keep_files):
        size = "DIR" if os.path.isdir(file) else f"{os.path.getsize(file)/1024:.1f}KB"
        print(f"   📁 {file} ({size})")
    
    print("\n🔴 Files to REMOVE:")
    remove_files = all_files - keep_files
    for file in sorted(remove_files):
        if file.startswith('.'):
            continue  # Skip hidden files
        size = "DIR" if os.path.isdir(file) else f"{os.path.getsize(file)/1024:.1f}KB"
        print(f"   🗑️  {file} ({size})")
    
    print(f"\n📊 Summary:")
    print(f"   Keep: {len(all_files & keep_files)} items")
    print(f"   Remove: {len(remove_files)} items")

def main():
    """Main cleanup function"""
    print("🏈 NFL Data Analysis Template Cleanup")
    print("=" * 50)
    
    print("Choose an option:")
    print("1. Preview cleanup (see what would be removed)")
    print("2. Perform cleanup (actually remove files)")
    print("3. Cancel")
    
    choice = input("\nChoice (1/2/3): ")
    
    if choice == "1":
        preview_cleanup()
    elif choice == "2":
        cleanup_for_template()
    else:
        print("👋 Goodbye!")

if __name__ == "__main__":
    main()
