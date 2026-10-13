from pathlib import Path
import pandas as pd

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]

RAW_FILE = PROJECT_ROOT / "data" / "raw" / "amazon_beauty_reviews_dataset.csv"
OUTPUT_DIR = PROJECT_ROOT / "data" / "processed"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

CLEAN_FILE = OUTPUT_DIR / "beauty_reviews_cleaned.csv"
SUMMARY_FILE = OUTPUT_DIR / "week3_quality_summary.csv"

# Load original dataset
df = pd.read_csv(RAW_FILE, low_memory=False)
original_rows = len(df)

print("Original rows:", original_rows)

cleaning_counts = {}

def record_step(name, before, after):
    removed = before - after
    cleaning_counts[name] = removed

    print(f"\n{name}")
    print("Rows before:", before)
    print("Rows after :", after)
    print("Rows removed:", removed)

# 1. Remove exact duplicates
before = len(df)
df = df.drop_duplicates().copy()
record_step("Duplicate removal", before, len(df))

# 2. Convert ratings and remove invalid ratings
df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

before = len(df)
df = df[df["rating"].between(1, 5)].copy()
record_step("Invalid rating removal", before, len(df))

# 3. Fill missing titles
missing_titles = df["title"].isna().sum()
df["title"] = df["title"].fillna("")
print("\nMissing titles filled:", missing_titles)

# 4. Remove missing review text
before = len(df)
df = df.dropna(subset=["text"]).copy()
record_step("Missing review text removal", before, len(df))

# 5. Remove blank review text
df["text"] = df["text"].astype(str).str.strip()

before = len(df)
df = df[df["text"] != ""].copy()
record_step("Blank review text removal", before, len(df))

# Save cleaned dataset
df.to_csv(CLEAN_FILE, index=False)

# Create before/after quality summary
summary_df = pd.DataFrame([
    {
        "stage": "Before Cleaning",
        "rows": original_rows,
        "columns": 10
    },
    {
        "stage": "After Cleaning",
        "rows": len(df),
        "columns": len(df.columns)
    }
])

summary_df.to_csv(SUMMARY_FILE, index=False)

# Final validation
total_removed = original_rows - len(df)
step_total = sum(cleaning_counts.values())

print("\n========== FINAL RESULTS ==========")
print("Original rows:", original_rows)
print("Final cleaned rows:", len(df))
print("Total rows removed:", total_removed)
print("Sum of cleaning steps:", step_total)

if total_removed == step_total:
    print("VALIDATION PASSED: Row counts match.")
else:
    print("VALIDATION FAILED: Check cleaning steps.")

print("\nCleaned dataset saved:", CLEAN_FILE)
print("Quality summary saved:", SUMMARY_FILE)
print("\nScript execution completed.")