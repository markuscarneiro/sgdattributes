# 🌱 SDG Attributes - Green Port Complex

Interactive visualization tool for Sustainable Development Goals (SDG) indicators in the port sector, developed as part of the research project "Green Port Complex: Proposed Indicators Linked to the SDGs".

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io/)
[![Sustainability](https://img.shields.io/badge/SDG-Sustainability-green)](https://sdgs.un.org/)
[![Research](https://img.shields.io/badge/Research-FAPEMA-orange)](https://www.fapema.br/)

## 🎯 About the Project

This visualization tool is part of the research project **"Green Port Complex: Proposed Indicators Linked to the SDGs"**, developed with support from:

- **FAPEMA** (Foundation for Research and Scientific and Technological Development of Maranhão)
- **EMAP** (Maranhão Port Administration Company)

### Research Team

**Project Coordinators:**
- Darliane Cunha
- Clóvis Oliveira

**Model Development & Data Visualization:**
- Markus Carneiro Costa

## 📊 What This Tool Does

The application provides **interactive radar charts** (spider charts) to visualize and compare sustainability indicators across multiple ports, organized by SDG themes and specific areas.

### Key Features

1. **📋 SDG Attributes Table**
   - Browse all sustainability indicators by SDG category
   - Filter by specific areas (Environmental, Social, Economic, etc.)
   - View detailed metrics for each attribute

2. **📈 View by SDG**
   - Compare 6 ports across specific SDG themes
   - Filter by SDG area for focused analysis
   - Individual port vs. average comparisons
   - Interactive radar chart visualizations

3. **🏭 SDG per Port**
   - Comprehensive view of all SDGs for each port
   - Side-by-side comparison of 6 ports
   - Aggregate performance across all sustainability themes

4. **⚖️ SDG and Average**
   - Detailed port-by-port comparison with average performance
   - Theme-by-theme analysis for selected port
   - Benchmark individual ports against the overall average

## 🛠️ Technology Stack

- **Python 3.9+** - Programming language
- **Streamlit** - Interactive web framework
- **Pandas** - Data manipulation and analysis
- **Matplotlib** - Radar chart generation
- **NumPy** - Numerical computations

## 📦 Project Structure

```
sgdattributes/
├── Home.py                          # Main landing page
├── pages/
│   ├── 1_SDG_Attributes_Table.py    # Tabular view of indicators
│   ├── 2_View_by_SDG.py             # SDG-focused radar charts
│   ├── 3_SDG_per_Port.py            # Port-focused comparison
│   └── 4_SDG_and_Average.py         # Port vs. average analysis
├── BASE.csv                         # Main dataset (port indicators)
├── SDG_attributes_ANEXO.xlsx        # SDG attributes and metrics
├── requirements.txt                 # Python dependencies
├── Procfile                         # Deployment configuration
├── .streamlit/                      # Streamlit config
└── .devcontainer/                   # Development container setup
```

## 🚀 Installation and Usage

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)

### Local Installation

1. **Clone the repository:**
```bash
git clone https://github.com/markuscarneiro/sgdattributes.git
cd sgdattributes
```

2. **Create and activate virtual environment:**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the application:**
```bash
streamlit run Home.py
```

5. **Access in browser:**
```
http://localhost:8501
```

### Deployment

**Streamlit Cloud:**
- Connect your GitHub repository to Streamlit Cloud
- The app will be deployed automatically

**Heroku:**
```bash
heroku create your-app-name
git push heroku main
```

## 📖 How to Use

### 1. SDG Attributes Table
- Select an SDG category from the dropdown
- Optionally filter by specific area
- View all attributes and metrics in a structured table

### 2. View by SDG
- Choose an SDG theme (e.g., "Clean Water and Sanitation")
- Select an area or view all areas
- Compare all 6 ports simultaneously
- Scroll down to see individual port vs. average comparisons

### 3. SDG per Port
- View all SDG themes for each port at once
- Quickly identify strengths and weaknesses across sustainability dimensions
- Compare ports side-by-side

### 4. SDG and Average
- Select a specific port from the dropdown
- View detailed comparison with average for each SDG theme
- Identify areas where the port performs above/below average

## 📊 Data Structure

### BASE.csv
Contains performance scores (0-3 scale) for each port across multiple sustainability indicators:

```csv
TEMA;AREA;ITEM_AJUST;Port A;Port B;Port C;Port D;Port E;Port F
SDG 6 - Clean Water;Water Quality;Indicator 1;2.5;2.1;2.8;...
```

**Columns:**
- `TEMA` - SDG theme/category
- `AREA` - Specific area within the SDG
- `ITEM_AJUST` - Specific indicator/metric
- `Port A-F` - Performance scores (0-3 scale)

### SDG_attributes_ANEXO.xlsx
Reference table with detailed information about each indicator:

- `CATEGORY` - SDG category
- `ATTRIBUTE` - Sustainability attribute
- `AREA` - Thematic area
- `METRIC` - Specific measurement criteria

## 🎨 Visualization Types

### Radar Charts (Spider Charts)
The application uses **polar coordinate radar charts** to visualize multi-dimensional sustainability performance:

- **Axes**: Each axis represents a different sustainability indicator
- **Scale**: 0-3 rating scale (0 = poor, 3 = excellent)
- **Shape**: The larger the covered area, the better the overall performance
- **Color**: Green (#00A36C) for individual ports, gray for averages

## 🌍 Sustainable Development Goals Coverage

The tool covers multiple SDG themes relevant to port operations:
- SDG 6 - Clean Water and Sanitation
- SDG 7 - Affordable and Clean Energy
- SDG 8 - Decent Work and Economic Growth
- SDG 9 - Industry, Innovation and Infrastructure
- SDG 11 - Sustainable Cities and Communities
- SDG 12 - Responsible Consumption and Production
- SDG 13 - Climate Action
- SDG 14 - Life Below Water
- And others as defined in the dataset

## 🎓 Research Applications

### For Researchers
- Benchmark sustainability performance across ports
- Identify best practices and areas for improvement
- Generate publication-ready visualizations
- Support empirical sustainability studies

### For Port Administrators
- Monitor sustainability KPIs
- Compare performance with peer ports
- Prioritize sustainability investments
- Report to stakeholders and regulators

### For Policymakers
- Assess regional port sustainability
- Develop evidence-based policies
- Track progress toward SDG targets
- Allocate resources effectively

## 🔍 Technical Details

### Radar Chart Implementation
Custom radar chart implementation using Matplotlib with:
- Configurable number of axes (variables)
- Polar projection transformations
- Circle or polygon frames
- Automatic label positioning
- Grid customization

### Data Processing
- Automatic calculation of port averages
- Forward-fill for missing category/attribute values
- Dynamic filtering based on user selections
- Real-time chart generation

## 🤝 Contributing

This is an academic research project. Contributions are welcome:

- 🐛 Bug reports
- 💡 Feature suggestions
- 📝 Documentation improvements
- 🎨 Visualization enhancements
- 📊 Additional SDG indicators

**How to contribute:**
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/NewIndicator`)
3. Commit your changes (`git commit -m 'Add new sustainability indicator'`)
4. Push to the branch (`git push origin feature/NewIndicator`)
5. Open a Pull Request

## 📄 License

This project is available under the MIT License for academic and research purposes.

## 📚 References

- **UN Sustainable Development Goals**: [https://sdgs.un.org/](https://sdgs.un.org/)
- **UNCTAD - Sustainable Ports**: [https://unctad.org/](https://unctad.org/)
- **IMO - Green Voyage 2050**: [https://www.imo.org/](https://www.imo.org/)

## 👥 Authors & Acknowledgments

### Project Team

**Markus Carneiro Costa**
- Senior Internal Auditor | Data Science Specialist
- 💼 LinkedIn: [linkedin.com/in/markuscarneiro](https://linkedin.com/in/markuscarneiro)
- 🐙 GitHub: [@markuscarneiro](https://github.com/markuscarneiro)

**Darliane Cunha**
- Project Coordinator

**Clóvis Oliveira**
- Project Coordinator

### Funding & Support

- **FAPEMA** - Foundation for Research and Scientific and Technological Development of Maranhão
- **EMAP** - Maranhão Port Administration Company

### About This Tool

Developed as part of an applied research initiative to create measurable, actionable sustainability indicators for port operations in Maranhão, Brazil. The tool combines expertise in:
- Environmental sustainability assessment
- Port operations and logistics
- Data visualization and analytics
- Sustainable development frameworks

---

⭐ **Useful for your research?** Star this repository!

💬 **Questions or suggestions?** Open an [issue](https://github.com/markuscarneiro/sgdattributes/issues)

🌱 **Cite this work:** If used in academic publications, please credit the research team and funding agencies.

📊 **Use in teaching?** Feel free to use with proper attribution to the original research project.
