# Week 2 --- Dataset Inspection and Data Quality Assessment

**Project:** Exploring Customer Feedback and Product Sentiment\
**Intern:** Sumit Kumar\
**Internship:** Data Science with Python Analyst Internship\
**Domain:** Beauty and Wellness\
**Submission date:** 02 October 2026

## Objective

Inspect the selected Amazon Beauty reviews CSV dataset, review its
structure and data types, identify missing values, and run initial
data-quality checks before preprocessing and exploratory analysis.

## Dataset

-   **File:** `data/raw/amazon_beauty_reviews_dataset.csv`
-   **Reported size:** 70,528 rows × 10 columns
-   **Fields:** `rating`, `title`, `text`, `images`, `asin`,
    `parent_asin`, `user_id`, `timestamp`, `helpful_vote`,
    `verified_purchase`

The dataset's original source, license, and collection documentation
have not yet been verified. Add these details once confirmed.

## Work Completed

1.  Confirmed the CSV file path and read a five-row sample.
2.  Printed column names, data types, and sample shape.
3.  Counted missing values and calculated missing-value percentages.
4.  Processed the file in chunks of 5,000 rows to check row count,
    within-chunk duplicate rows, rating distribution, ratings outside
    1--5, and timestamps that could not be parsed.
5.  Compared the sum of rating counts with the total row count.

## Initial Results

-   Total rows: **70,528**
-   Total columns: **10**
-   Missing values: `title` **160** (\~0.02%); `text` **212** (\~0.03%);
    all other listed fields **0**
-   Rating counts: 1 star **10,280**; 2 stars **4,304**; 3 stars
    **5,607**; 4 stars **7,931**; 5 stars **42,026**
-   Ratings outside 1--5: **0**
-   Unparseable timestamps: **0**
-   Duplicate rows detected within individual chunks: **716**. This is
    not a global full-file duplicate count.

## Files

-   `week2_data_inspection.py` --- dataset inspection and data-quality
    checks
-   `screenshots/dataset_overview.png` --- dataset sample, columns, and
    data types
-   `screenshots/missing_values.png` --- missing-value output
-   `screenshots/data_quality_checks.png` --- data-quality validation
    output
-   `Week2_Dataset_Inspection_Report_Sumit_Kumar_Same_Format.docx` ---
    detailed Week 2 report

## Run

From the project root in VS Code terminal:

``` bash
python Week-2/week2_data_inspection.py
```

Ensure the CSV exists at `data/raw/amazon_beauty_reviews_dataset.csv`
and that pandas is installed in the selected Python environment.

## Limitations and Next Steps

This work is an initial inspection only. Missing values have not been
imputed or removed, and duplicate handling has not been finalized. Next,
verify dataset provenance and usage terms, perform a global duplicate
assessment, inspect review-text quality, and prepare a documented
cleaned dataset for exploratory analysis.
