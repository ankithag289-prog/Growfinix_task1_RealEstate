from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
file_path = Path("output/cleaned_realtor_data.csv")
df = pd.read_csv(file_path)

# Convert price to numeric
df["price"] = pd.to_numeric(df["price"], errors="coerce")

# Create output folder for charts
chart_folder = Path("output/charts")
chart_folder.mkdir(parents=True, exist_ok=True)

# Chart 1: Distribution of property prices
prices = df["price"].dropna()
prices = prices[prices > 0]

plt.figure(figsize=(8, 5))
plt.hist(prices.clip(upper=prices.quantile(0.99)), bins=30)
plt.title("Distribution of Property Prices")
plt.xlabel("Property Price")
plt.ylabel("Number of Properties")
plt.tight_layout()
plt.savefig(chart_folder / "price_distribution.png")
plt.close()

# Chart 2: Average price by number of bedrooms
bedrooms = pd.to_numeric(df["bed"], errors="coerce")
summary = (
    pd.DataFrame({"bedrooms": bedrooms, "price": df["price"]})
    .dropna()
    .query("price > 0 and bedrooms >= 0")
    .groupby("bedrooms")["price"]
    .mean()
    .sort_index()
)

plt.figure(figsize=(8, 5))
summary.plot(kind="bar")
plt.title("Average Property Price by Bedrooms")
plt.xlabel("Number of Bedrooms")
plt.ylabel("Average Price")
plt.tight_layout()
plt.savefig(chart_folder / "average_price_by_bedrooms.png")
plt.close()

print("Visualizations created successfully.")
print("Charts saved in:", chart_folder)