Growfinix Task 1: Real Estate Market Data Cleaning

Project Overview

This project focuses on cleaning and analyzing real estate property listing data using Python and spreadsheet tools as part of the Growfinix internship.

Objectives

- Remove duplicate property records.
- Handle missing values, including ZIP codes.
- Standardize text formatting.
- Prepare property data for analysis.
- Integrate historical sales information where matching records are available.
- Generate visualizations to understand property prices.

Tools and Technologies

- Python
- Pandas
- Matplotlib
- Microsoft Excel
- Power Query

Project Structure

- "data/" – Property listing dataset and historical sales CSV.
- "output/" – Cleaned dataset, analysis report, data profile, and charts.
- "screenshots/" – Project Python scripts and supporting screenshots.
- "clean_data.py" – Data cleaning.
- "analyze_data.py" – Exploratory data analysis.
- "inspect_data.py" – Dataset inspection.
- "profile_data.py" – Data profiling.
- "visualize_data.py" – Chart generation.

Outputs

- Cleaned property dataset.
- Data quality and analysis reports.
- Property price distribution chart.
- Average property price by number of bedrooms chart.

Historical Sales Integration

A historical sales CSV was added to the project. Records should be merged using a compatible property identifier or matching address fields. The merge results should be validated before reporting successful matches.

How to Run

Install the required packages:

pip install pandas matplotlib

Run the scripts from the project root:

python inspect_data.py
python clean_data.py
python profile_data.py
python analyze_data.py
python visualize_data.py

Note

The analysis and charts depend on the available dataset and the results produced by the scripts. Verify the outputs before reporting final numerical findings.