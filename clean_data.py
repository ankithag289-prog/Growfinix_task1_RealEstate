from pathlib import Path
import pandas as pd

# Define folders
data_folder = Path("data")
output_folder = Path("output")
output_folder.mkdir(parents=True, exist_ok=True)

# Find the dataset
csv_files = list(data_folder.glob("*.csv"))

if not csv_files:
    raise FileNotFoundError(
        "No CSV file found inside the data folder."
    )

file_path = csv_files[0]

print("Loading dataset...")
print("Dataset:", file_path.name)

# Load the dataset
df = pd.read_csv(
    file_path,
    dtype={"zip_code": "string"},
    low_memory=False
)

print("Original rows:", len(df))

# Step 1: Remove completely empty rows
df = df.dropna(how="all")

# Step 2: Clean text columns
text_columns = df.select_dtypes(
    include=["object", "string"]
).columns

for column in text_columns:
    df[column] = df[column].str.strip()
    df[column] = df[column].replace("", pd.NA)

# Step 3: Remove exact duplicate rows
before = len(df)
df = df.drop_duplicates()
print("Exact duplicate rows removed:", before - len(df))

# Step 4: Standardize selected text columns
for column in ["city", "state", "status", "street"]:
    if column in df.columns:
        df[column] = df[column].astype("string").str.title()

# Step 5: Preserve ZIP codes as text
if "zip_code" in df.columns:
    df["zip_code"] = df["zip_code"].str.strip()
    df["zip_code"] = df["zip_code"].replace("", pd.NA)

# Step 6: Save the cleaned dataset
output_path = output_folder / "cleaned_realtor_data.csv"

print("Saving cleaned dataset...")
df.to_csv(output_path, index=False)

# Step 7: Display cleaning results
print("\nCleaning completed!")
print("Rows after cleaning:", len(df))
print("\nMissing values by column:")
print(df.isna().sum().to_string())
print("\nCleaned file saved to:", output_path)