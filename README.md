# Mutual Fund Analytics

Capstone Project I – Bluestock Fintech

## Overview

This project analyzes Indian mutual fund data to understand fund performance, investor trends, portfolio allocation, and industry insights through data cleaning, SQL analysis, and exploratory data analysis (EDA).

## Objectives

* Clean and preprocess mutual fund datasets.
* Store processed data in a structured SQLite database.
* Perform exploratory data analysis using Python.
* Generate visual insights and export charts for reporting.

## Datasets

The project includes publicly available mutual fund datasets such as:

* SBI Bluechip Fund
* ICICI Prudential Bluechip Fund
* Axis Bluechip Fund
* Kotak Bluechip Fund
* Nippon India Large Cap Fund
* Mutual Fund Master Data
* SIP Statistics
* AUM Data
* Folio Data
* Portfolio Holdings

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* SQLite
* Jupyter Notebook
* Git & GitHub

## Exploratory Data Analysis

The notebook includes analysis of:

* NAV Trend Analysis
* AUM Growth Analysis
* SIP Inflow Analysis
* Category Inflow Heatmap
* Investor Demographics
* Geographic Distribution
* Portfolio Holdings Analysis
* Folio Growth Analysis
* NAV Return Correlation Matrix
* Sector Allocation Analysis

**Project Outputs**

* 16 analytical charts
* Exported PNG visualizations
* Data quality summary report
* SQLite database
* Documented insights for each major analysis

## Project Structure

```
bluestock-fintech/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
│
├── notebooks/
│   └── EDA_Analysis.ipynb
│
├── reports/
│   ├── charts/
│   └── data_quality_summary.md
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
├── dashboard/
├── README.md
└── requirements.txt
```

## Status

* Data Cleaning ✅
* SQL Database Design ✅
* Exploratory Data Analysis ✅

This project was developed as part of the **Bluestock Fintech Capstone Project I**.