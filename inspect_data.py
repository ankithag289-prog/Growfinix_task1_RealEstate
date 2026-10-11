from pathlib import Path
import pandas as pd

# Locate the dataset
data_folder = Path("data")
csv_files = list(data_folder.glob("*.csv"))

if not csv_files:
    print("No CSV file found inside the data folder.")
else:
    file_path = csv_files[0]

    print("Dataset:", file_path.name)

    # Read only 10 rows first
    df = pd.read_csv(
        file_path,
        nrows=10,
        dtype={"zip_code": "string"}
    )

    print("\nColumn names:")
    print(df.columns.tolist())

    print("\nFirst 10 rows:")
    print(df.to_string(index=False))

    print("\nData types:")
    print(df.dtypes)