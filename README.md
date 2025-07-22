# NFL Data Analysis Template

A ready-to-use template for NFL data analysis projects using Python and the `nfl_data_py` package.

## ✨ Features

- **🐳 Dev Container**: Automatic package installation in any codespace
- **📊 Data Manager**: Smart caching system for NFL data
- **🚀 Quick Setup**: Session manager for fast project startup
- **📁 Project Generator**: Template system for new analyses

## 🏈 What's Included

### Core Tools
- `nfl_data_manager.py` - Smart data caching and retrieval
- `session_manager.py` - Quick setup and status checker
- `new_project.py` - Generate new analysis projects
- `requirements.txt` - All necessary Python packages

### Dev Environment
- `.devcontainer/` - Automatic VS Code environment setup
- Pre-configured with all NFL data analysis packages
- Jupyter notebook support included

## 🚀 Quick Start

### 1. Create New Repository from Template
1. Click "Use this template" on GitHub
2. Create your new repository
3. Open in Codespace

### 2. Environment Setup (Automatic)
The dev container will automatically:
- Install Python packages
- Set up Jupyter environment
- Run initial setup script

### 3. Start Analyzing
```bash
# Check what's available
python session_manager.py

# Create a new project
python new_project.py

# Or start with data collection
python -c "from nfl_data_manager import NFLDataManager; dm = NFLDataManager(); print('Ready!')"
```

## 📊 Data Available

- **Years**: 1999-present (detailed statistics)
- **Positions**: All NFL positions
- **Stats**: Weekly, seasonal, play-by-play data
- **Advanced Metrics**: EPA, CPOE, air yards, etc.

## 🔧 Customization

### For Different Sports/Data
1. Update `requirements.txt` with your packages
2. Modify `nfl_data_manager.py` for your data sources
3. Adjust dev container if needed

### For Specific Analysis Types
1. Use `new_project.py` to generate project templates
2. Customize the analysis template in the script
3. Add your own utility functions

## 📁 Project Structure

```
your-new-project/
├── .devcontainer/          # Automatic environment setup
├── nfl_data_manager.py     # Data caching utility
├── session_manager.py      # Setup checker
├── new_project.py         # Project generator
├── requirements.txt       # Python dependencies
├── projects/              # Generated analysis projects
│   └── your_analysis/
│       ├── analysis.py
│       ├── data/
│       └── outputs/
└── nfl_data_cache/        # Cached API data
```

## 💡 Workflow Examples

### Quarterback Analysis
```python
from nfl_data_manager import NFLDataManager
dm = NFLDataManager()

qb_data = dm.get_weekly_data(
    years=[2022, 2023, 2024],
    columns=['player_name', 'passing_yards', 'qb_rating']
)
qb_only = qb_data[qb_data['position'] == 'QB']
```

### Team Performance
```python
team_data = dm.get_weekly_data(years=[2024])
team_stats = team_data.groupby('recent_team')['passing_yards'].sum()
```

## 🛠️ Troubleshooting

### Slow Data Loading
- Data manager automatically caches results
- First download may take 5-10 minutes
- Subsequent loads are instant

### Missing Packages
- Dev container should handle everything automatically
- If issues persist: `pip install -r requirements.txt`

### Data Cache Issues
```python
from nfl_data_manager import NFLDataManager
dm = NFLDataManager()
dm.clear_cache()  # Start fresh
```

## 📚 Resources

- [nfl_data_py Documentation](https://github.com/cooperdff/nfl_data_py)
- [NFL Data Field Descriptions](https://www.nflfastr.com/articles/field_descriptions.html)
- [Pro Football Reference](https://www.pro-football-reference.com/)

## 🤝 Contributing

1. Fork the template
2. Add your improvements
3. Submit a pull request

## 📄 License

MIT License - feel free to use for any projects!

---

**🏈 Ready to analyze some NFL data? Create a new repository from this template and start exploring!**
