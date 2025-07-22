#!/usr/bin/env python3
"""
New NFL Project Starter
Quick template for starting a new NFL data analysis project
"""

import os
from datetime import datetime

def create_new_project():
    """Create a new NFL analysis project"""
    print("🏈 New NFL Analysis Project Creator")
    print("=" * 40)
    
    # Get project details
    project_name = input("📝 Project name (e.g., 'qb_efficiency_2024'): ").strip()
    if not project_name:
        project_name = f"nfl_analysis_{datetime.now().strftime('%Y%m%d')}"
    
    project_description = input("📄 Brief description: ").strip()
    
    # Create project directory structure
    project_dir = f"projects/{project_name}"
    os.makedirs(project_dir, exist_ok=True)
    os.makedirs(f"{project_dir}/data", exist_ok=True)
    os.makedirs(f"{project_dir}/notebooks", exist_ok=True)
    os.makedirs(f"{project_dir}/outputs", exist_ok=True)
    
    # Create main analysis script
    analysis_script = f"""#!/usr/bin/env python3
\"\"\"
{project_name.replace('_', ' ').title()} Analysis
{project_description}

Created: {datetime.now().strftime('%Y-%m-%d')}
\"\"\"

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Import our NFL data utilities
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from nfl_data_manager import NFLDataManager

def load_data():
    \"\"\"Load NFL data for analysis\"\"\"
    print("📊 Loading NFL data...")
    
    dm = NFLDataManager()
    
    # Customize these years and columns for your specific analysis
    years = [2022, 2023, 2024]  # Adjust as needed
    
    weekly_data = dm.get_weekly_data(
        years=years,
        columns=[
            'season', 'week', 'player_name', 'position', 'recent_team',
            'passing_yards', 'passing_tds', 'interceptions', 'qb_rating',
            'completions', 'attempts', 'passing_epa'
        ]
    )
    
    return weekly_data

def analyze_data(data):
    \"\"\"Main analysis function\"\"\"
    print("🔍 Starting analysis...")
    
    # Filter for QBs (adjust for your position of interest)
    qb_data = data[data['position'] == 'QB']
    
    print(f"Analyzing {{len(qb_data)}} QB records from {{data['season'].min()}}-{{data['season'].max()}}")
    
    # Add your specific analysis here
    # Example: basic QB stats
    qb_stats = qb_data.groupby(['player_name', 'season']).agg({{
        'passing_yards': 'sum',
        'passing_tds': 'sum', 
        'interceptions': 'sum',
        'qb_rating': 'mean',
        'passing_epa': 'sum'
    }}).reset_index()
    
    return qb_stats

def create_visualizations(data):
    \"\"\"Create visualizations\"\"\"
    print("📈 Creating visualizations...")
    
    plt.figure(figsize=(12, 8))
    
    # Example visualization - customize for your analysis
    plt.subplot(2, 2, 1)
    plt.scatter(data['passing_yards'], data['qb_rating'], alpha=0.7)
    plt.xlabel('Passing Yards')
    plt.ylabel('QB Rating')
    plt.title('QB Rating vs Passing Yards')
    
    plt.tight_layout()
    plt.savefig('outputs/{project_name}_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()

def main():
    \"\"\"Main analysis pipeline\"\"\"
    print(f"🚀 Starting {{project_name.replace('_', ' ').title()}} Analysis")
    print("=" * 50)
    
    # Load data
    raw_data = load_data()
    
    # Analyze
    results = analyze_data(raw_data)
    
    # Visualize
    create_visualizations(results)
    
    # Save results
    results.to_csv('outputs/{project_name}_results.csv', index=False)
    
    print(f"✅ Analysis complete! Results saved to outputs/")

if __name__ == "__main__":
    main()
"""
    
    with open(f"{project_dir}/analysis.py", 'w') as f:
        f.write(analysis_script)
    
    # Create project README
    readme_content = f"""# {project_name.replace('_', ' ').title()}

{project_description}

## Project Structure
- `analysis.py` - Main analysis script
- `data/` - Project-specific data files
- `notebooks/` - Jupyter notebooks for exploration
- `outputs/` - Results, visualizations, and reports

## Quick Start
```bash
cd {project_dir}
python analysis.py
```

## Data Sources
- NFL weekly statistics (2022-2024)
- Cached via NFLDataManager for fast loading

Created: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
    
    with open(f"{project_dir}/README.md", 'w') as f:
        f.write(readme_content)
    
    print(f"✅ Project created: {project_dir}")
    print(f"📁 Structure:")
    print(f"   {project_dir}/")
    print(f"   ├── analysis.py      # Main analysis script")
    print(f"   ├── README.md        # Project documentation")
    print(f"   ├── data/            # Project-specific data")
    print(f"   ├── notebooks/       # Jupyter exploration")
    print(f"   └── outputs/         # Results and visualizations")
    
    print(f"\n🚀 Next steps:")
    print(f"   1. cd {project_dir}")
    print(f"   2. python analysis.py")
    print(f"   3. Customize the analysis for your specific research question")

if __name__ == "__main__":
    create_new_project()
