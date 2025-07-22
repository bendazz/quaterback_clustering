# 🏈 NFL Data Analysis - Codespace Workflow Guide

## The Problem
Every new codespace requires reinstalling packages and re-downloading data, which takes 5-10 minutes of building wheels and API calls.

## 🎯 Recommended Solutions

### Option 1: Dev Container (Best for Consistent Setup)
**Pros:** Automatic package installation, consistent environment
**Cons:** Initial build time, but only once per container

1. Use the `.devcontainer/devcontainer.json` I created
2. Codespace will automatically install all packages on creation
3. No manual installation needed

### Option 2: Data Collection + Analysis Separation (Best for Data Workflows)
**Pros:** Fast analysis sessions, data persistence
**Cons:** Requires planning and file management

#### Workflow:
1. **Data Collection Codespace** (Run once per week/month):
   ```bash
   python collect_all_data.py  # Downloads and caches everything
   ```
   This creates:
   - `nfl_data_cache/` - Raw cached API data
   - `datasets/` - Processed CSV files ready for analysis

2. **Analysis Codespace** (Daily work):
   ```bash
   # Copy datasets folder from data collection codespace
   python quick_analysis_setup.py  # Verify data and start analyzing
   ```

### Option 3: Hybrid Approach (Most Flexible)

1. **Use the Data Manager** for smart caching:
   ```python
   from nfl_data_manager import NFLDataManager
   dm = NFLDataManager()
   
   # This will cache data locally, so subsequent calls are instant
   qb_data = dm.get_weekly_data(years=[2020, 2021, 2022, 2023, 2024])
   ```

2. **Export key datasets** for backup:
   ```bash
   python collect_all_data.py  # Run once to create datasets/
   ```

3. **In new codespaces**, just copy the `datasets/` folder

## 🚀 Quick Start Commands

### First Time Setup (Data Collection):
```bash
# Install packages (only needed once with dev container)
pip install -r requirements.txt

# Collect all data
python collect_all_data.py
```

### Subsequent Sessions:
```bash
# Quick verification
python quick_analysis_setup.py

# Start your analysis
python qb_analysis.py
```

## 📁 File Structure After Setup
```
quaterback_clustering/
├── .devcontainer/          # Automatic codespace setup
├── nfl_data_cache/         # Raw API data cache (large files)
├── datasets/               # Processed CSV files (portable)
│   ├── qb_weekly_data.csv
│   ├── qb_draft_data.csv
│   └── team_seasonal_stats.csv
├── nfl_data_manager.py     # Smart caching system
├── collect_all_data.py     # One-time data collection
├── quick_analysis_setup.py # Fast analysis startup
└── requirements.txt        # All dependencies
```

## 💡 Pro Tips

1. **Keep datasets/ folder small** - Only processed data you actually use
2. **Use the cache manager** - Automatically handles API rate limits and storage
3. **Export final results** - Save your analysis outputs for easy sharing
4. **Version your data** - Include collection date in filenames for reproducibility

## 🔄 Recommended Workflow

### Data Collection Codespace (Weekly):
- Install all packages once
- Download fresh data
- Export to `datasets/` folder
- Keep this codespace for data updates

### Analysis Codespace (Daily):
- Copy `datasets/` folder
- Focus on analysis and visualization
- No API calls or package installation needed
- Quick startup and iteration
