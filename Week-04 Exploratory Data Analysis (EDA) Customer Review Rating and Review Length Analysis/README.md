# Week 4: Exploratory Data Analysis (EDA)

**Project:** Exploring Customer Feedback and Product Sentiment  
**Domain:** Beauty & Wellness  
**Internship:** Data Science with Python Analyst Internship

## Objective
Explore the cleaned customer-review dataset by inspecting its structure, summarizing missing values and rating frequencies, calculating review length in characters, generating charts, and exporting reusable CSV outputs.

## Input
`data/processed/beauty_reviews_cleaned.csv`

Required columns: `rating` and `text`.

## Run from the project root
```bash
python Week-4/eda_analysis.py
```

Install direct dependencies if required:
```bash
python -m pip install pandas matplotlib
```

## What the script does
1. Loads the cleaned CSV with Pandas.
2. Prints dataset dimensions, columns, data types, DataFrame information, and descriptive statistics.
3. Exports per-column missing-value counts.
4. Converts rating values to numeric form and exports rating frequencies.
5. Calculates `review_length` as the number of characters in each review.
6. Exports review-length descriptive statistics.
7. Saves a copy of the dataset with the new `review_length` column.
8. Generates a rating bar chart and review-length histogram at 300 DPI.

## Outputs

### CSV files
- `data/processed/week4_missing_values_summary.csv`
- `data/processed/week4_rating_distribution.csv`
- `data/processed/week4_review_length_summary.csv`
- `data/processed/week4_reviews_with_length.csv`

### Charts
- `visuals/week4_rating_distribution.png`
- `visuals/week4_review_length_distribution.png`

## Results shown in the supplied terminal screenshot
| Metric | Value |
|---|---:|
| Total rows | 693,443 |
| 1-star reviews | 100,752 |
| 2-star reviews | 42,576 |
| 3-star reviews | 55,687 |
| 4-star reviews | 78,532 |
| 5-star reviews | 415,896 |
| Mean review length | 173.304723 characters |
| Standard deviation | 247.244966 |
| Minimum | 1 character |
| 25th percentile | 4 characters |
| Median | 102 characters |
| 75th percentile | 209 characters |
| Maximum | 14,989 characters |

## Interpretation
Five-star reviews form the largest rating category in the displayed dataset. Review lengths are right-skewed: many are relatively short and a smaller number are much longer. These are descriptive observations only; they do not prove product quality or establish causation.

## Important validation note
An older draft used 69,343 rows and a maximum review length of 1,489 characters. The supplied terminal screenshot instead shows 693,443 rows and a maximum of 14,989 characters. Rerun the script against the current input CSV and make sure the report, charts, and exported CSVs all represent the same execution before submitting.

## Limitations
- Character length is not the same as word count or sentiment.
- The script measures missing values but does not explain why values are missing.
- Rating counts may be affected by dataset composition and should not be generalized to every customer or product.
- No sentiment model is trained by this script.

## Final checks
- Confirm the input file path and required columns.
- Rerun the script and inspect the console output.
- Check that rating counts match the rating CSV.
- Check that the review-length maximum matches the histogram range.
- Confirm all outputs are current and README/report figures agree.
