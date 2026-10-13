# Week 3 — Data Cleaning and Preprocessing

**Project:** Exploring Customer Feedback and Product Sentiment  
**Internship:** Data Science with Python Analyst Internship  
**Domain:** Beauty & Wellness  
**Week 3 focus:** Data cleaning, preprocessing, and quality validation

## Overview

Week 3 prepares the customer-review dataset for exploratory data analysis (EDA) and later sentiment-related work. The preprocessing workflow shown in the VS Code execution evidence removes exact duplicate rows, checks rating values, fills missing titles, removes rows with missing review text, trims whitespace, removes blank review text, and exports a cleaned dataset and quality-summary file.

This README reports the figures shown in the supplied execution screenshots. Before final submission, rerun the exact saved `data_cleaning.py` version and confirm that the script, output CSV, summary CSV, screenshots, and report all match.

## Reported Results

| Metric | Reported result |
|---|---:|
| Original rows | 701,528 |
| Original columns | 10 |
| Exact duplicate rows removed | 7,275 |
| Invalid rating rows removed | 0 |
| Missing titles filled | 159 |
| Rows with missing review text removed | 211 |
| Rows with blank review text removed | 599 |
| Final cleaned rows | 693,443 |
| Total rows removed | 8,085 |
| Retention rate | 98.848% |
| Removal rate | 1.152% |

The row-count reconciliation is:

```text
701,528 - 7,275 - 0 - 211 - 599 = 693,443
Total rows removed = 8,085
```

Filling missing titles changes cell values but does not remove rows.

## Cleaning Steps

1. Load the raw CSV with pandas and record the original row count.
2. Remove exact duplicate rows.
3. Convert ratings to numeric values and retain ratings from 1 through 5.
4. Replace missing review titles with empty strings.
5. Remove rows where review text is null.
6. Strip leading/trailing whitespace from review text.
7. Remove rows whose review text is blank after trimming.
8. Save the cleaned CSV and quality-summary CSV.

## Input and Output Files

| Path | Description |
|---|---|
| `data/raw/amazon_beauty_reviews_dataset.csv` | Original input dataset; keep unchanged |
| `Week-3/data_cleaning.py` | Python preprocessing script |
| `data/processed/beauty_reviews_cleaned.csv` | Cleaned review data |
| `data/processed/week3_quality_summary.csv` | Before/after quality summary |
| `Week-3/screenshots/` | Code and execution evidence |
| `Week-3/Week3_Data_Cleaning_and_Preprocessing_Report.docx` | Detailed Week 3 report |

## Data Fields

The dataset schema documented during Week 2 contains 10 fields:

- `rating` — star rating
- `title` — review title
- `text` — review body
- `images` — image-related field
- `asin` — product identifier
- `parent_asin` — parent product/variant identifier
- `user_id` — reviewer identifier; handle cautiously
- `timestamp` — raw review timestamp
- `helpful_vote` — helpful-vote count
- `verified_purchase` — purchase-verification indicator

The Week 3 script does not demonstrate a full audit of every field. Timestamp semantics, identifier completeness, helpful-vote outliers, and post-cleaning field-level distributions remain follow-up checks.

## Important Validation Note

The figures above reconcile mathematically: 7,275 + 0 + 211 + 599 = 8,085 rows removed, and 701,528 − 8,085 = 693,443 rows remaining.

However, the uploaded script copy may not be identical to the version that produced the detailed console output. Verify this before submitting: save the final script, rerun it, and regenerate the screenshots and summary file from that exact version.

## Limitations and Responsible Use

- Exact duplicate removal does not detect near-duplicate or paraphrased reviews.
- Removing records without usable text creates a text-analysis subset that may differ from the full review dataset.
- Posted reviews are self-selected and should not be treated as representative of all customers.
- Review ratings and text do not prove product effectiveness, safety, or causation.
- Do not publish reviewer IDs or upload the full raw dataset to GitHub unless source terms allow redistribution.
- Verify the dataset's exact publisher, release/version, source URL, and license/terms.

## Week 4 Handoff

Planned EDA includes:

- Rating counts and percentages
- Review-text length and missingness
- Timestamp parsing and review-volume trends
- Verified-purchase comparisons
- Helpful-vote distribution and outlier checks
- Frequent terms/themes by rating group
- Product-level summaries with sample-size caveats

These analyses are planned; they should only be marked complete after scripts/notebooks and figures have been produced and checked.

## Run

From the repository root, run:

```bash
python Week-3/data_cleaning.py
```

Confirm that the script's configured paths match the repository layout before running.

## Project Status

- [x] Cleaning workflow executed according to supplied screenshots
- [x] Cleaned CSV and quality-summary CSV reported as saved
- [x] Row counts transcribed and reconciled
- [ ] Confirm the saved script exactly matches the evidenced run
- [ ] Rerun and regenerate final evidence
- [ ] Complete timestamp, identifier, and helpful-vote audits
- [ ] Perform Week 4 EDA and save reproducible visualizations

## References and Provenance

The local file is named `amazon_beauty_reviews_dataset.csv`. Its exact upstream release/version and redistribution terms must be confirmed and recorded before the source can be described as verified. Candidate documentation to check includes:

- UC San Diego McAuley Lab — Amazon Reviews 2023: https://mcauleylab.ucsd.edu/public_datasets/amazon_2023/
- UC San Diego McAuley Lab — Amazon Review Data (2018): https://cseweb.ucsd.edu/~jmcauley/datasets/amazon_v2/index.html

A matching filename or column schema alone does not prove that the local CSV came from a particular release.
