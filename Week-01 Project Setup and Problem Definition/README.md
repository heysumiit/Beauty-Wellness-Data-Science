# Exploring Customer Feedback and Product Sentiment

**Domain:** Beauty & Wellness\
**Project:** Data Science with Python Analyst Internship\
**Internship Program:** Yuva Intern by Henry Harvin\
**Project Duration:** 6 Weeks\
**Status:** Week 1 --- Orientation and Business Problem Definition

## Overview

This project proposes a Python-based workflow for exploring customer
reviews and product ratings in the Beauty & Wellness domain. The goal is
to understand how review text and numerical ratings can be analyzed
together to identify recurring feedback themes, describe rating
patterns, and establish a reproducible foundation for sentiment
analysis.

**Important:** No customer dataset was analyzed during the Week 1
problem-definition work. Dataset selection, data cleaning, exploratory
data analysis (EDA), and model evaluation are planned activities unless
later project evidence documents their completion.

## Business Problem

Customer reviews can contain comments about product attributes such as
texture, fragrance, packaging, price, and overall experience. Manually
reviewing large collections can be time-consuming and inconsistent.

The project asks:

> How can customer review text and associated product ratings be
> organized and analyzed to identify recurring feedback themes, examine
> rating patterns, and generate transparent, evidence-based insights
> about Beauty & Wellness products?

Online reviews are voluntary and platform-dependent. They should not
automatically be treated as representative of all customers, and review
text alone cannot establish medical safety, product effectiveness, or
causal relationships.

## Objectives

-   Define the business problem, scope, research questions, and
    hypotheses.
-   Compare candidate review datasets and verify their provenance and
    usage terms.
-   Assess data quality, including missing values, duplicates, invalid
    ratings, and text issues.
-   Prepare a documented and reproducible data-cleaning workflow.
-   Explore rating distributions, review lengths, common terms, and
    available product/time patterns.
-   Investigate sentiment classification or rating prediction only if
    the selected data supports it.
-   Evaluate any implemented model with suitable metrics and error
    analysis.
-   Document findings, assumptions, limitations, and references.

## Candidate Data Sources

These are candidate sources for evaluation, not confirmation that a
dataset has been downloaded or selected.

  --------------------------------------------------------------------------------------------------------------------
  Source                                                               Purpose                 Key checks before use
  -------------------------------------------------------------------- ----------------------- -----------------------
  [UCSD Amazon Reviews                                                 Candidate source for    Confirm the
  2023](https://mcauleylab.ucsd.edu/public_datasets/amazon_2023/)      review text, ratings,   Beauty-related category
                                                                       and product metadata    file, schema, file
                                                                                               size, access
                                                                                               conditions, and
                                                                                               permitted use

  [Historical Amazon                                                   Historical              Confirm version, date
  Reviews](https://mcauleylab.ucsd.edu/public_datasets/data/amazon/)   category-specific       coverage, fields, and
                                                                       review data             data-use restrictions

  [Kaggle Datasets](https://www.kaggle.com/datasets)                   Discover potentially    Verify the exact
                                                                       smaller datasets        listing, original
                                                                                               provenance, license,
                                                                                               schema, and collection
                                                                                               period

  [Google Dataset Search](https://datasetsearch.research.google.com/)  Discover datasets       Verify details and
                                                                       hosted by research      terms with the original
                                                                       institutions and other  dataset host
                                                                       publishers              
  --------------------------------------------------------------------------------------------------------------------

The final dataset must be chosen only after checking relevance, required
fields, provenance, usage terms, accessibility, size, and suitability
for the project questions. Public discoverability does not automatically
grant permission to reuse or redistribute data.

## Proposed Workflow

1.  **Dataset discovery:** Identify and compare candidate sources.
2.  **Source verification:** Record the original URL, version, access
    date, citation requirements, and usage restrictions.
3.  **Initial inspection:** Inspect dimensions, column names, data
    types, and a small sample.
4.  **Data-quality assessment:** Measure missing values, duplicates,
    blank text, invalid ratings, date parsing issues, and category
    relevance.
5.  **Preprocessing:** Apply documented, justified cleaning rules while
    preserving raw text where permitted.
6.  **EDA:** Summarize ratings, review length, missingness, time
    coverage, and product/category coverage where available.
7.  **Text exploration:** Examine frequent words and phrases and inspect
    representative examples using documented selection rules.
8.  **Sentiment or rating modeling:** Consider a baseline only if valid
    labels and suitable data are available.
9.  **Evaluation:** Use appropriate metrics, a clear train/test split,
    leakage prevention, and error analysis.
10. **Reporting:** Publish reproducible scripts/notebooks,
    visualizations, limitations, and source references.

## Proposed Data Fields

The exact schema depends on the selected source. The following fields
are useful if available:

  Field                          Purpose
  ------------------------------ ---------------------------------------------
  `review_id`                    Review record identifier, if supplied
  `product_id` / `parent_asin`   Connect reviews to products
  `product_title`                Human-readable product name
  `review_title`                 Short review summary
  `review_text`                  Main text for analysis
  `rating`                       Numerical rating supplied by the source
  `review_timestamp`             Temporal analysis
  `verified_purchase`            Optional source-provided purchase indicator
  `helpful_vote_count`           Optional helpfulness measure
  `product_category`             Category relevance and group comparisons
  `source_dataset`               Data provenance

Do not assume every candidate source contains every field. Document
absent fields rather than fabricating them.

## Planned EDA Outputs

Subject to the selected dataset containing the necessary fields, the
planned outputs include:

-   Dataset dimensions, column types, and memory usage
-   Missing-value counts and percentages
-   Exact duplicates and duplicate identifier checks
-   Rating counts and percentages
-   Review-length histogram and box plot
-   Review volume over time
-   Verified-purchase and helpful-vote summaries, if available
-   Review length by rating
-   Review counts by product or category, if identifiers exist
-   Frequent words and bigrams
-   Comparison of text themes across rating groups
-   Class-distribution analysis and sentiment/rating agreement, if
    labels are created

These are planned analyses, not completed findings. Charts and numerical
conclusions should be generated from actual data only.

## Sentiment Analysis: Important Distinction

-   **Sentiment classification** assigns a text category such as
    positive, neutral, or negative.
-   **Rating prediction** estimates a numerical rating, such as a 1--5
    star score.
-   **Theme analysis** identifies topics such as texture, fragrance,
    packaging, or price.

A star rating is not a perfect sentiment label. Reviews can contain
mixed opinions, sarcasm, ambiguous wording, or disagreement between text
and rating. Any labels derived from ratings must be described as
rating-based labels rather than independently verified emotional states.

If a model is implemented, report accuracy alongside precision, recall,
macro F1-score, per-class metrics, a confusion matrix, and error
analysis as appropriate. Accuracy alone can be misleading when classes
are imbalanced.

## Technology Stack

The verified Week 1 environment reported the following versions:

  Component      Version
  ------------ ---------
  Python          3.14.6
  Pandas           3.0.6
  NumPy            2.5.3
  Matplotlib      3.11.2
  Seaborn         0.13.2

The environment setup script completed with the message
`Project Environment Setup Successful!`. This confirms that the packages
imported successfully in that environment; it does **not** mean a
dataset was analyzed or a model was trained.

Tools planned for the project include Python, Pandas, NumPy, Matplotlib,
Seaborn, Jupyter Notebook or VS Code, and Git/GitHub for version
control.

## Six-Week Roadmap

  -----------------------------------------------------------------------
  Week                    Focus                   Expected outputs
  ----------------------- ----------------------- -----------------------
  1                       Orientation and         Problem statement,
                          business problem        research questions,
                          definition              environment
                                                  verification

  2                       Dataset discovery and   Source comparison,
                          initial inspection      source/terms record,
                                                  initial data inspection
                                                  and EDA plan

  3                       Cleaning and            Cleaning script and
                          preprocessing           data-quality summary

  4                       Exploratory data        Notebook, descriptive
                          analysis                tables, visualizations

  5                       Baseline model, if      Model script/notebook
                          feasible                and documented
                                                  evaluation setup

  6                       Evaluation and          Error analysis, final
                          reporting               report, verified
                                                  outputs,
                                                  reproducibility
                                                  instructions
  -----------------------------------------------------------------------

This is a proposed roadmap. It is not evidence that all weekly
activities have been completed.

## Ethics, Privacy, and Limitations

-   Check the original dataset's terms and licensing before use or
    redistribution.
-   Avoid unnecessary reviewer identifiers and personal information.
-   Describe sampling and platform limitations; do not generalize beyond
    the evidence.
-   Treat automated sentiment output as uncertain and potentially
    biased.
-   Do not infer medical safety or product effectiveness from reviews.
-   Record cleaning decisions and exclusions so results can be
    reproduced.
-   Do not publish raw data unless the applicable terms permit it.

Relevant guidance: - [NIST AI Risk Management
Framework](https://www.nist.gov/itl/ai-risk-management-framework) -
[Google PAIR Guidebook --- Data Collection and
Evaluation](https://pair.withgoogle.com/guidebook-v2/chapter/data-collection/) -
[FTC --- Consumer Reviews and Testimonials Rule: Questions and
Answers](https://www.ftc.gov/business-guidance/resources/consumer-reviews-and-testimonials-rule-questions-answers)

## Acceptance Criteria

A project deliverable is ready for review when:

-   The dataset source, version, provenance, and usage terms are
    documented.
-   The schema and required fields are described.
-   Data-quality counts are calculated from actual data.
-   Cleaning rules and row-count changes are recorded.
-   Visualizations have titles, labels, and understandable captions.
-   Model metrics, if applicable, can be traced to verified predictions
    and labels.
-   Assumptions, limitations, and potential bias are explicit.
-   Scripts/notebooks and dependency instructions support
    reproducibility.
-   Findings are clearly separated from hypotheses and planned work.

## References

1.  Hou, Y. et al. *Amazon Reviews 2023 / Recommender Systems Datasets*.
    UC San Diego.
    https://mcauleylab.ucsd.edu/public_datasets/amazon_2023/
2.  McAuley Lab, UC San Diego. *Amazon Review Data --- Historical
    Dataset Documentation*.
    https://mcauleylab.ucsd.edu/public_datasets/data/amazon/
3.  Federal Trade Commission. *The Consumer Reviews and Testimonials
    Rule: Questions and Answers*.
    https://www.ftc.gov/business-guidance/resources/consumer-reviews-and-testimonials-rule-questions-answers
4.  Federal Trade Commission. *Rulemaking on the Use of Consumer Reviews
    and Testimonials*.
    https://www.ftc.gov/legal-library/browse/rules/rulemaking-use-consumer-reviews-testimonials
5.  National Institute of Standards and Technology. *AI Risk Management
    Framework*. https://www.nist.gov/itl/ai-risk-management-framework
6.  Google PAIR. *People + AI Guidebook --- Data Collection and
    Evaluation*.
    https://pair.withgoogle.com/guidebook-v2/chapter/data-collection/
7.  Kaggle. *Datasets*. https://www.kaggle.com/datasets
8.  Google. *Dataset Search*. https://datasetsearch.research.google.com/

------------------------------------------------------------------------

**Project status:** Week 1 problem definition and environment
verification documented. Dataset selection, cleaning, EDA, and model
evaluation remain pending until supported by subsequent project
evidence.
