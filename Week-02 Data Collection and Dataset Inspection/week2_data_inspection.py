import pandas as pd
from pathlib import Path

# Dataset location
file_path = Path("data/raw/amazon_beauty_reviews_dataset.csv")

# Check whether the file exists
if not file_path.exists():
    print("Dataset file not found. Please check the file path.")
else:
    print("Dataset found successfully!")

    # Read a small sample first
    df = pd.read_csv(file_path, nrows=5)

    print("\n--- First 5 Rows ---")
    print(df)

    print("\n--- Column Names ---")
    print(df.columns.tolist())

    print("\n--- Data Types ---")
    print(df.dtypes)

    print("\n--- Sample Shape ---")
    print(df.shape)
    

file_path = Path("data/raw/amazon_beauty_reviews_dataset.csv")

if not file_path.exists():
    print("Dataset file not found.")
else:
    total_rows = 0
    missing_counts = None
    total_columns = None

    for chunk in pd.read_csv(file_path, chunksize=50000):
        total_rows += len(chunk)

        if missing_counts is None:
            missing_counts = chunk.isna().sum()
            total_columns = chunk.columns.tolist()
        else:
            missing_counts += chunk.isna().sum()

    print("\n--- Full Dataset Inspection ---")
    print("Total rows:", total_rows)
    print("Total columns:", len(total_columns))

    print("\n--- Missing Values ---")
    print(missing_counts)

    print("\n--- Missing Value Percentage ---")
    print((missing_counts / total_rows * 100).round(2))
    
    file_path = "data/raw/amazon_beauty_reviews_dataset.csv"

total_duplicates = 0
rating_counts = {}
invalid_ratings = 0
timestamp_errors = 0
total_rows = 0

for chunk in pd.read_csv(file_path, chunksize=50000):
    total_rows += len(chunk)

    # Check duplicate rows within each chunk
    total_duplicates += chunk.duplicated().sum()

    # Count rating values
    counts = chunk["rating"].value_counts()
    for rating, count in counts.items():
        rating_counts[rating] = rating_counts.get(rating, 0) + count

    # Check ratings outside 1–5
    invalid_ratings += (~chunk["rating"].between(1, 5)).sum()

    # Check timestamp values that cannot be parsed
    parsed_time = pd.to_datetime(chunk["timestamp"], errors="coerce")
    timestamp_errors += parsed_time.isna().sum()

print("\n--- Data Quality Checks ---")
print("Total rows:", total_rows)
print("Duplicate rows detected within chunks:", total_duplicates)
print("Rating distribution:", rating_counts)
print("Sum of rating counts:", sum(rating_counts.values()))
print("Matches total rows:", sum(rating_counts.values()) == total_rows)
print("Ratings outside 1–5:", invalid_ratings)
print("Unparseable timestamps:", timestamp_errors)

print("\n--- Verified Rating Counts ---")
for rating, count in sorted(rating_counts.items()):
    print(f"Rating {rating}: {count}")

print("Total rating counts:", sum(rating_counts.values()))
print("Total rows:", total_rows)

print("\n--- Rating Count Validation ---")

for rating in sorted(rating_counts):
    print(f"Rating {rating}: {rating_counts[rating]:,}")

print("Sum of rating counts:", f"{sum(rating_counts.values()):,}")
print("Total rows:", f"{total_rows:,}")
print("Difference:", f"{total_rows - sum(rating_counts.values()):,}")