# Week 02 — Dataset Inspection & Data Quality Assessment

### Data Science with Python Internship | Beauty & Wellness

## Overview

Week 2 focused on inspecting the selected Amazon Beauty customer-review dataset and assessing its initial data quality for the project **“Exploring Customer Feedback and Product Sentiment.”**

The objective was to understand the dataset structure, examine its columns and data types, identify missing values, and perform preliminary data-quality checks before data cleaning and exploratory data analysis.

## Objectives

- Load and inspect the customer-review dataset using Python and Pandas.
- Understand the dataset dimensions, column names, and data types.
- Identify missing values and calculate their percentages.
- Examine customer rating values and validate the expected 1–5 range.
- Check timestamp parsing.
- Perform preliminary duplicate detection.
- Document findings, limitations, and recommended next steps.

## Dataset Overview

- **Dataset:** `amazon_beauty_reviews_dataset.csv`
- **Location:** `data/raw/amazon_beauty_reviews_dataset.csv`
- **Reported dimensions:** 70,528 rows × 10 columns

The inspected fields include:

`rating`, `title`, `text`, `images`, `asin`, `parent_asin`, `user_id`, `timestamp`, `helpful_vote`, and `verified_purchase`.

## Work Completed

1. Loaded the dataset using Python and Pandas.
2. Read a sample of records to inspect the data.
3. Reviewed column names, data types, and dataset dimensions.
4. Calculated missing-value counts and percentages.
5. Processed the dataset in chunks for selected data-quality checks.
6. Checked rating values against the expected 1–5 range.
7. Examined timestamp parsing and performed preliminary duplicate detection.

## Initial Findings

- Missing values were identified in the `title` and `text` columns.
- No ratings outside the expected 1–5 range were reported.
- No unparseable timestamps were reported by the inspection script.
- Duplicate detection was performed within individual chunks; the result is not a complete global duplicate count.

These findings describe the initial inspection and do not imply that missing values or duplicates have already been removed.

## Tools & Technologies

- Python
- Pandas
- Visual Studio Code
- CSV data processing

## Project Files

- `week2_data_inspection.py` — dataset inspection and data-quality checks.
- `screenshots/dataset_overview.png` — dataset sample, columns, and data types.
- `screenshots/missing_values.png` — missing-value inspection output.
- `screenshots/data_quality_checks.png` — data-quality validation output.
- `Week2_Dataset_Inspection_Report.docx` — detailed Week 2 report.

## How to Run

From the project root directory, execute:

```bash
python Week-02_Data-Collection-and-Dataset-Inspection/week2_data_inspection.py
```

Ensure that the dataset exists at the configured path and Pandas is installed in the selected Python environment.

## Limitations & Next Steps

- Verify the dataset's original source, documentation, and usage terms.
- Perform a global duplicate assessment.
- Establish rules for handling missing titles and review text.
- Inspect review-text quality.
- Prepare a documented cleaned dataset for exploratory data analysis.

## Outcome

Week 2 established an initial understanding of the dataset's structure and data-quality characteristics. The findings provide a foundation for the next stage: **data cleaning and preprocessing**.

---

*Project: Exploring Customer Feedback and Product Sentiment*
