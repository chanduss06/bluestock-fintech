# Data Quality Summary

## Dataset Review

Files Loaded:

- fund_master.csv
- sbi_bluechip.csv
- icici_bluechip.csv
- nippon_large_cap.csv
- axis_bluechip.csv
- kotak_bluechip.csv

## Findings

- Data loaded successfully.
- NAV history available.
- Date field available.
- No major missing values in NAV data.
- Fund master contains scheme codes and scheme names.
- fund_house available through NAV metadata.
- scheme_category available through NAV metadata.
- Risk grade not provided by MFAPI.
- Sub-category not provided separately by MFAPI.

## Validation

- Selected scheme codes successfully matched NAV history endpoint.