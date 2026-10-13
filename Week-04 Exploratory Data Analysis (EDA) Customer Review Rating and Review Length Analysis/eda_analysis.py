from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------------
# 1. PROJECT PATHS
# -----------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "beauty_reviews_cleaned.csv"
)

OUTPUT_DIR = PROJECT_ROOT / "visuals"
SUMMARY_DIR = PROJECT_ROOT / "data" / "processed"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
SUMMARY_DIR.mkdir(parents=True, exist_ok=True)

# -----------------------------------------
# 2. LOAD DATASET
# -----------------------------------------

df = pd.read_csv(DATA_FILE, low_memory=False)

print("Cleaned dataset loaded successfully!")
print("Dataset shape:", df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

# Check required columns
required_columns = ["rating", "text"]
missing_columns = [
    col for col in required_columns
    if col not in df.columns
]

if missing_columns:
    raise ValueError(
        f"Required columns missing: {missing_columns}"
    )

# -----------------------------------------
# 3. BASIC DATA SUMMARY
# -----------------------------------------

print("\nDataset Information:")
df.info()

print("\nDescriptive Statistics:")
print(df.describe(include="all").to_string())

# Missing values summary
missing_summary = df.isnull().sum().reset_index()
missing_summary.columns = ["column", "missing_values"]

missing_summary.to_csv(
    SUMMARY_DIR / "week4_missing_values_summary.csv",
    index=False
)

# -----------------------------------------
# 4. RATING DISTRIBUTION
# -----------------------------------------

df["rating"] = pd.to_numeric(
    df["rating"],
    errors="coerce"
)

rating_counts = (
    df["rating"]
    .value_counts()
    .sort_index()
)

print("\nRating Distribution:")
print(rating_counts)

rating_counts.to_csv(
    SUMMARY_DIR / "week4_rating_distribution.csv",
    header=["review_count"]
)

plt.figure(figsize=(8, 5))
rating_counts.plot(kind="bar")

plt.title("Customer Review Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Reviews")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "week4_rating_distribution.png",
    dpi=300
)
plt.close()

# -----------------------------------------
# 5. REVIEW TEXT LENGTH ANALYSIS
# -----------------------------------------

df["review_length"] = (
    df["text"]
    .fillna("")
    .astype(str)
    .str.len()
)

print("\nReview Length Statistics:")
print(df["review_length"].describe())

df["review_length"].describe().to_csv(
    SUMMARY_DIR / "week4_review_length_summary.csv"
)

plt.figure(figsize=(8, 5))
plt.hist(
    df["review_length"],
    bins=50,
    edgecolor="black"
)

plt.title("Distribution of Customer Review Length")
plt.xlabel("Review Length (Characters)")
plt.ylabel("Number of Reviews")
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "week4_review_length_distribution.png",
    dpi=300
)
plt.close()

# -----------------------------------------
# 6. SAVE ANALYSIS DATA
# -----------------------------------------

df.to_csv(
    SUMMARY_DIR / "week4_reviews_with_length.csv",
    index=False
)

print("\nEDA completed successfully!")
print("Charts saved in:", OUTPUT_DIR)
print("Summary files saved in:", SUMMARY_DIR)


print("\nExact Rating Counts:")
print(df["rating"].value_counts().sort_index().to_string())

print("\nTotal Ratings:", df["rating"].value_counts().sum())
print("Total Dataset Rows:", len(df))