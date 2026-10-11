from pathlib import Path
import pandas as pd

data_folder = Path("data")
output_folder = Path("output")
output_folder.mkdir(exist_ok=True)

csv_files = list(data_folder.glob("*.csv"))

if not csv_files:
    raise FileNotFoundError(
        "No CSV file found inside the data folder."
    )

file_path = csv_files[0]

print("Dataset:", file_path.name)
print("Starting full dataset inspection...")

total_rows = 0
missing_counts = None
status_counts = {}

# Process the large CSV in smaller batches
for chunk in pd.read_csv(
    file_path,
    chunksize=100_000,
    dtype={"zip_code": "string"}
):
    total_rows += len(chunk)

    # Count missing values, including blank text cells
    chunk = chunk.replace(r"^\s*$", pd.NA, regex=True)
    chunk_missing = chunk.isna().sum()

    if missing_counts is None:
        missing_counts = chunk_missing
    else:
        missing_counts = missing_counts.add(
            chunk_missing, fill_value=0
        )

    if "status" in chunk.columns:
        counts = chunk["status"].value_counts(dropna=False)
        for label, count in counts.items():
            key = str(label)
            status_counts[key] = (
                status_counts.get(key, 0) + int(count)
            )

    print(f"Rows inspected: {total_rows:,}", end="\r")

report_path = output_folder / "data_profile.txt"

with open(report_path, "w", encoding="utf-8") as report:
    report.write(f"Dataset: {file_path.name}\n")
    report.write(f"Total rows: {total_rows:,}\n\n")
    report.write("Missing values by column:\n")
    report.write(missing_counts.to_string())
    report.write("\n\nProperty status counts:\n")
    report.write(str(status_counts))

print("\n\nInspection completed.")
print("Total rows:", f"{total_rows:,}")
print("\nMissing values by column:")
print(missing_counts.to_string())
print("\nStatus counts:")
print(status_counts)
print("\nReport saved to:", report_path)