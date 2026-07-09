# Mutual Fund Analytics Platform

**Capstone Project I – Bluestock Fintech**

---

## Project Overview

This project is an end-to-end Mutual Fund Analytics Platform developed as part of the Bluestock Fintech Capstone Internship. It demonstrates a complete data analytics pipeline, starting from raw mutual fund datasets through data cleaning, database creation, exploratory data analysis, performance analytics, advanced risk metrics, and an interactive Power BI dashboard.

The project analyzes Indian mutual fund data to generate insights into fund performance, investor behavior, portfolio allocation, SIP trends, and market performance using Python, SQLite, SQL, Jupyter Notebook, and Power BI.

---

## Objectives

- Build a complete ETL pipeline for mutual fund datasets.
- Clean and preprocess raw financial data.
- Store processed data in a relational SQLite database.
- Perform Exploratory Data Analysis (EDA).
- Compute mutual fund performance metrics.
- Perform advanced risk and investor analytics.
- Build an interactive Power BI dashboard.
- Generate analytical reports and visualizations.

---

## Dataset

The project uses publicly available Indian mutual fund datasets, including:

- Fund Master
- NAV History
- AUM by Fund House
- Monthly SIP Inflows
- Category Inflows
- Industry Folio Count
- Scheme Performance
- Investor Transactions
- Portfolio Holdings
- Benchmark Indices

---

## Technology Stack

- Python
- Pandas
- NumPy
- SQLite
- SQL
- Matplotlib
- Seaborn
- Plotly
- Jupyter Notebook
- Power BI
- Git & GitHub

---

## Project Workflow

```
Raw CSV Files
        │
        ▼
Data Cleaning & Validation
        │
        ▼
ETL Pipeline
        │
        ▼
SQLite Database
        │
        ▼
EDA Analysis
        │
        ▼
Performance Metrics
        │
        ▼
Advanced Analytics
        │
        ▼
Power BI Dashboard
        │
        ▼
Final Report & Presentation
```

---

## Project Structure

```
bluestock-fintech/
│
├── dashboard/
│   └── bluestock_mf.pbix
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
│
├── docs/
│   └── data_dictionary.md
│
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb
│
├── reports/
│   ├── charts/
│   ├── dashboard/
│   ├── performance/
│   ├── Dashboard.pdf
│   ├── Final_Report.pdf
│   └── Presentation.pptx
│
├── scripts/
│   ├── etl_pipeline.py
│   ├── compute_metrics.py
│   ├── recommender.py
│   └── live_nav_fetch.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── src/
│   ├── analysis/
│   ├── database/
│   └── utils/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Exploratory Data Analysis

The EDA notebook includes:

- NAV Trend Analysis
- AUM Growth Analysis
- SIP Inflow Analysis
- Category Inflow Heatmap
- Investor Demographics
- Geographic Distribution
- Portfolio Holdings Analysis
- Sector Allocation
- NAV Correlation Matrix
- Folio Growth Analysis

---

## Performance Analytics

Performance metrics computed include:

- CAGR
- Alpha
- Beta
- Sharpe Ratio
- Sortino Ratio
- Maximum Drawdown
- Tracking Error
- Benchmark Comparison

Generated outputs include:

- performance_metrics.csv
- fund_scorecard.csv
- alpha_beta.csv
- returns_computed.csv
- cagr_comparison_table.csv

---

## Advanced Analytics

Advanced analytical models include:

- Historical VaR (95%)
- Conditional VaR (CVaR)
- Rolling 90-Day Sharpe Ratio
- Investor Cohort Analysis
- SIP Continuity Analysis
- Fund Recommendation Engine
- Sector HHI Concentration Analysis

---

## Interactive Dashboard

The Power BI dashboard consists of five interactive pages:

1. Industry Overview
2. Fund Performance
3. Investor Analytics
4. SIP & Market Trends
5. NAV Detail

Features:

- KPI Cards
- Interactive Slicers
- Cross-filtering
- Fund Scorecards
- Performance Charts
- Risk Analysis
- Geographic Insights
- Market Trend Analysis

---

## Key Outputs

- SQLite Database
- ETL Pipeline
- SQL Queries
- Five Jupyter Notebooks
- Performance CSV Reports
- Interactive Power BI Dashboard
- Dashboard PDF
- Final Technical Report
- Project Presentation

---

## Future Enhancements

- Automated NAV Fetch using API
- Streamlit Web Dashboard
- Portfolio Optimization
- Monte Carlo NAV Simulation
- Automated Weekly Email Reports

---

## Author

**Chandra Shekar Chegondi**

Bluestock Fintech Internship

Capstone Project I – Mutual Fund Analytics