from pathlib import Path
import pandas as pd

input_path = Path("output/cleaned_realtor_data.csv")
report_path = Path("output/analysis_report.txt")

print("Loading cleaned dataset...")

df = pd.read_csv(
    input_path,
    dtype={"zip_code": "string"},
    low_memory=False
)

with open(report_path, "w", encoding="utf-8") as report:
    report.write("REAL ESTATE DATA ANALYSIS\n")
    report.write("=" * 30 + "\n\n")
    report.write(f"Total rows: {len(df):,}\n")
    report.write(f"Total columns: {len(df.columns)}\n\n")

    report.write("Column names:\n")
    report.write(", ".join(df.columns) + "\n\n")

    report.write("Missing values:\n")
    report.write(df.isna().sum().to_string() + "\n\n")

    if "price" in df.columns:
        prices = pd.to_numeric(df["price"], errors="coerce")
        report.write("Price summary:\n")
        report.write(prices.describe().to_string() + "\n")

print("Analysis completed!")
print("Report saved to:", report_path)