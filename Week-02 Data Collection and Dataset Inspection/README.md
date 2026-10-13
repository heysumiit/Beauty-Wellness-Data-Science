# Exploring Customer Feedback and Product Sentiment

**Internship:** Data Science with Python Analyst Internship  
**Domain:** Beauty & Wellness  
**Current phase:** Week 2 — Data Identification, Sourcing Strategy & Initial Analysis Planning

## Project Overview

This project explores customer feedback on beauty and wellness products using product-review data. The goal is to understand rating patterns, plan how review text can be examined for recurring customer themes, and establish a careful, reproducible workflow for data collection, quality assessment, and exploratory data analysis (EDA).

The project distinguishes between **observed results**, **source information that still needs verification**, and **planned analysis**. It does not claim that sentiment modelling or all EDA tasks have already been completed.

## Business Problem

Beauty and wellness reviews may discuss product experience, texture, fragrance, packaging, perceived performance, value, seller or delivery issues, and other factors. A star rating alone does not explain why a customer left a review. By combining rating analysis with careful review-text exploration, the project aims to identify patterns worth investigating—without treating reviews as representative of every buyer or as proof of product effectiveness or safety.

## Objectives

- Profile the available review dataset and document its structure.
- Identify and compare relevant public data sources.
- Verify source provenance, release/version, coverage, and permitted use.
- Assess missing values, rating validity, timestamp parsing, and duplicate-record risks.
- Plan reproducible EDA for ratings, text availability, review length, time patterns, helpful votes, and verified-purchase status.
- Document privacy, bias, and interpretation limitations.
- Prepare a clear roadmap for cleaning and further analysis.

## Current Dataset

**Local file:** `data/raw/amazon_beauty_reviews_dataset.csv`

The following values were reported by the Week 2 inspection script and visible in the VS Code console output. They have not been independently re-run while preparing this README.

| Item | Reported result |
|---|---:|
| Rows | 701,528 |
| Columns | 10 |
| Missing `title` values | 160 |
| Missing `text` values | 212 |
| Ratings outside the 1–5 range | 0 |
| Timestamps failing the script's parseability check | 0 |
| Duplicate rows detected within individual chunks | 7,166 |

**Important:** The 7,166 duplicate figure is a *within-chunk* count. Since the inspection script checks each chunk separately, it is not a confirmed global duplicate count; identical rows across different chunks may not be counted.

### Dataset Columns

| Column | Reported type | Purpose |
|---|---|---|
| `rating` | `int64` | Star rating from 1 to 5 |
| `title` | string | Review headline |
| `text` | string | Main review text |
| `images` | string | Image-related review field |
| `asin` | string | Product identifier |
| `parent_asin` | string | Parent product/variant identifier |
| `user_id` | string | Reviewer identifier; handle cautiously |
| `timestamp` | string | Review timestamp in the raw file |
| `helpful_vote` | `int64` | Helpful-vote count |
| `verified_purchase` | boolean | Purchase-verification indicator |

The exact source, release/version, coverage period, timestamp semantics, and license/terms for the local CSV still need to be verified. A matching filename or schema is not proof that the file came from a particular dataset release.

## Reported Rating Distribution

| Rating | Number of reviews | Approx. share |
|---:|---:|---:|
| 1 star | 102,080 | 14.55% |
| 2 stars | 43,034 | 6.13% |
| 3 stars | 56,307 | 8.03% |
| 4 stars | 79,381 | 11.31% |
| 5 stars | 420,726 | 59.97% |
| **Total** | **701,528** | **100.00%** |

The rating counts add up to the reported row count. Five-star reviews form the largest category, so later analysis and any predictive model must account for class imbalance. This distribution describes the records in this file, not all beauty and wellness customers.

## Data Source Strategy

Candidate sources are being evaluated for relevance, documentation, access conditions, freshness, reproducibility, and integration effort.

| Candidate source | Intended role | Important note |
|---|---|---|
| [UC San Diego McAuley Lab — Amazon Reviews 2023](https://mcauleylab.ucsd.edu/public_datasets/amazon_2023/) | Primary source to compare against the local review file | Verify exact local-file provenance and terms before claiming lineage |
| [UCSD Amazon Review Data (2018)](https://cseweb.ucsd.edu/~jmcauley/datasets/amazon_v2/index.html) | Optional historical review dataset | Older release; schema and coverage may differ |
| [Kaggle Datasets](https://www.kaggle.com/datasets) | Discover candidate beauty/skincare datasets | Verify the original publisher, license, and quality of each dataset |
| [Google Dataset Search](https://datasetsearch.research.google.com/) | Discover datasets hosted by other publishers | A search result is not itself a quality or license guarantee |
| [Data.gov](https://catalog.data.gov/?keyword=cosmetics) | Possible official context datasets | May not contain customer reviews |
| [openFDA Cosmetic Adverse Events API](https://open.fda.gov/apis/cosmetic/event/) | Optional regulatory-reporting context | Reports do not establish causation or product-risk incidence |
| [Google Trends](https://trends.google.com/explore) | Optional search-interest context | Relative search interest is not sales or customer satisfaction |
| [YouTube Data API v3](https://developers.google.com/youtube/v3/docs) | Optional creator/video metadata if relevant | Requires compliance with API rules and quotas |
| [Reddit Developer Platform](https://support.reddithelp.com/hc/en-us/articles/14945211791892-Developer-Platform-Accessing-Reddit-Data) | Optional community discussion data | Use authorized access methods and follow platform terms |

The core project will prioritize one well-understood review dataset rather than merging unrelated sources simply to increase dataset size. Sources measuring different things—such as customer reviews, search interest, and adverse-event reports—must remain separate unless a defensible comparison method is designed.

## Planned Workflow

1. **Source verification:** Record the official URL, publisher, release/version, access date, coverage period, schema, license/terms, and actual download route.
2. **Raw-data preservation:** Keep the original file unchanged in `data/raw/`.
3. **Profiling:** Record row count, data types, nulls, blank strings, identifier patterns, value ranges, timestamp behavior, and rating counts.
4. **Quality audit:** Run a global duplicate audit and document the duplicate definition before removing any rows.
5. **Preprocessing:** Create derived cleaned text and datetime fields while retaining the raw values; document each transformation.
6. **EDA:** Examine rating distribution, missingness, review length, review volume over time, verified-purchase differences, helpful votes, and terms/themes by rating group.
7. **Interpretation:** Report denominators, limitations, and sample sizes; distinguish association from causation.
8. **Reproducibility:** Save scripts, figures, run logs, source notes, and report updates.

## Initial EDA Plan

The following analyses are **planned, not all completed**.

| Question | Variables | Proposed method |
|---|---|---|
| What is the rating distribution? | `rating` | Counts, percentages, median, mode, bar chart |
| How much text is usable? | `title`, `text` | Null and blank checks, text-length distributions |
| What period does the dataset cover? | `timestamp` | Validate date semantics; aggregate by month/year |
| Does text length vary by rating? | `text`, `rating` | Character/token counts, histograms, boxplots, suitable group comparisons |
| Does rating composition differ by purchase verification? | `verified_purchase`, `rating` | Cross-tabulation, group percentages; test only if assumptions are met |
| How are helpful votes distributed? | `helpful_vote` | Zero share, median/IQR, skew and outlier checks |
| What themes appear in low- and high-rated reviews? | `rating`, `text` | Unigram/bigram exploration, TF-IDF if useful, manual review of examples |
| Do patterns differ by product? | `asin`, `parent_asin`, `rating`, `text` | Product summaries with minimum sample sizes and appropriate caveats |

A potential exploratory grouping is 1–2 stars as low ratings, 3 stars kept separate, and 4–5 stars as high ratings. This grouping must be documented if used; the original 1–5 rating distribution should remain available.

## Data Quality and Interpretation Notes

- A zero null count does not rule out empty strings, placeholder values, or semantically invalid entries.
- The current timestamp result only indicates that no values failed the script's selected parsing check; timezone and timestamp semantics still need verification.
- The duplicate count reported so far is not a global duplicate count.
- Reviewer IDs should not be exposed in public outputs or used to identify individuals.
- Platform reviews are self-selected and may not represent all buyers.
- High ratings do not prove objective product effectiveness; low ratings do not prove a product is defective or unsafe.
- Frequent words are not automatically sentiment labels; context, negation, sarcasm, and delivery-related complaints can change meaning.
- Raw datasets should not be published to GitHub unless the source terms permit redistribution. Never commit API keys or credentials.

## Repository Structure

```text
Beauty-Wellness-Data-Science/
├── README.md
├── data/
│   └── raw/
│       └── amazon_beauty_reviews_dataset.csv
├── notebooks/
├── visuals/
├── Week-1/
│   ├── screenshots/
│   ├── README.md
│   ├── Week1_Problem_Definition_Report.docx
│   └── week1_setup.py
├── Week-2/
│   ├── screenshots/
│   └── week2_data_inspection.py
├── Week-3/
├── Week-4/
├── Week-5/
└── Week-6/
```

This is a suggested structure based on the current repository layout; adjust paths if the actual files differ. If the raw dataset is restricted or too large for GitHub, leave it out of the repository and document how to obtain it from the verified source.

## Six-Week Roadmap

| Week | Focus | Expected deliverables |
|---|---|---|
| 1 | Data science orientation and business problem definition | Problem definition and environment setup evidence |
| 2 | Data identification, sourcing strategy, initial analysis planning | Source comparison, data dictionary, quality baseline, EDA plan |
| 3 | Data cleaning and preprocessing | Documented cleaning pipeline and processed data where permitted |
| 4 | Exploratory analysis and visualization | Reproducible charts, descriptive statistics, observations |
| 5 | Sentiment analysis/model experimentation if appropriate | Baseline method, evaluation plan, error analysis |
| 6 | Final report and project presentation | Final results, limitations, repository cleanup and presentation |

## Current Status

- [x] Local dataset located and inspected by the Week 2 script
- [x] Reported row/column counts and rating counts documented
- [x] Initial source candidates and official links listed
- [x] Initial EDA questions and methods planned
- [ ] Verify exact local dataset provenance, version, coverage, and license/terms
- [ ] Complete global duplicate audit
- [ ] Inspect blank strings, identifier consistency, timestamp semantics, and vote ranges
- [ ] Execute the full EDA plan and save reproducible figures
- [ ] Build and evaluate a sentiment model, if appropriate for the remaining project scope

## References

1. UC San Diego McAuley Lab, Amazon Reviews 2023: https://mcauleylab.ucsd.edu/public_datasets/amazon_2023/
2. UC San Diego McAuley Lab, Amazon Review Data (2018): https://cseweb.ucsd.edu/~jmcauley/datasets/amazon_v2/index.html
3. Kaggle Datasets: https://www.kaggle.com/datasets
4. Google Dataset Search: https://datasetsearch.research.google.com/
5. Data.gov: https://catalog.data.gov/
6. openFDA Cosmetic Adverse Events API: https://open.fda.gov/apis/cosmetic/event/
7. Google Trends: https://trends.google.com/explore
8. YouTube Data API v3: https://developers.google.com/youtube/v3/docs
9. Reddit Developer Platform: https://support.reddithelp.com/hc/en-us/articles/14945211791892-Developer-Platform-Accessing-Reddit-Data

---

**Project note:** This README records the current planning stage and observed console figures. It does not claim that source verification, complete cleaning, all EDA, or sentiment modelling has been finished.
