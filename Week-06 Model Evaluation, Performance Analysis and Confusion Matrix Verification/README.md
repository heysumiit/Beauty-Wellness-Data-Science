# Week 6 — Model Evaluation and Final Verification

**Project:** Exploring Customer Feedback and Product Sentiment  
**Domain:** Beauty & Wellness  
**Internship:** Data Science with Python Analyst Internship

## Objective
Evaluate the saved Week 5 test predictions, calculate classification metrics, inspect class-level errors, and verify that the confusion matrix and test-record counts agree.

## Input
`data/processed/week5_test_predictions.csv`

Columns used:
- `actual_rating` — actual test rating
- `logistic_regression_prediction` — Logistic Regression prediction
- `multinomial_naive_bayes_prediction` — Naive Bayes prediction (also compared in the notebook)

The prediction CSV has **138,689 rows and 3 columns**.

## Run
Open `Week-6/week6_evaluation.ipynb` from the project structure and run the notebook cells in order. The notebook reads the saved Week 5 prediction and model-comparison CSVs.

Dependencies used by the notebook:
```bash
python -m pip install pandas matplotlib seaborn scikit-learn
```

## Logistic Regression metrics

| Metric | Score | Percentage |
|---|---:|---:|
| Accuracy | 0.726518 | 72.65% |
| Macro Precision | 0.511134 | 51.11% |
| Macro Recall | 0.437938 | 43.79% |
| Macro F1-score | 0.441833 | 44.18% |

## Confusion-matrix verification

The notebook reports:
- Actual records: **138,689**
- Predicted records: **138,689**
- Confusion-matrix total: **138,689**
- Classification-report support total: **138,689**

Row totals (actual ratings 1–5): `20,151; 8,515; 11,137; 15,707; 83,179`  
Column totals (predicted ratings 1–5): `24,291; 2,260; 6,493; 5,691; 99,954`

Both sets of totals sum to 138,689. The earlier 13,869 figure was incorrect and has been corrected in this README.

## Class-level findings

| Actual rating | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| 1 | 0.64 | 0.77 | 0.70 | 20,151 |
| 2 | 0.30 | 0.08 | 0.13 | 8,515 |
| 3 | 0.38 | 0.22 | 0.28 | 11,137 |
| 4 | 0.43 | 0.16 | 0.23 | 15,707 |
| 5 | 0.80 | 0.96 | 0.87 | 83,179 |

The model performs best on rating 5 and poorly on rating 2. Many actual four-star reviews are predicted as five stars, so class-wise performance should be considered alongside overall accuracy.

## Generated outputs
- `data/processed/week6_evaluation_metrics.csv`
- `data/processed/week6_logistic_regression_classification_report.json`
- `visuals/week6_confusion_matrix.png`

## Screenshots
Keep the supplied verification screenshots in `Week-6/screenshots/`:
- `05_week6_confusion_matrix.png`
- `06_confusion_matrix_verification.png`

## Limitations and next steps
The dataset is imbalanced, and TF-IDF-based Logistic Regression does not fully capture context or nuanced language. Week 5 also recorded a convergence warning at `max_iter=300`; Week 6 does not resolve that training warning. If the model is retrained, regenerate predictions, metrics, the classification report, and the confusion matrix together. Consider class weighting, tuning on training-only validation data, and ordinal-aware metrics as future experiments.

## Submission checks
- Confirm the prediction CSV has 138,689 rows.
- Confirm actual and predicted array lengths match.
- Confirm confusion-matrix sum and classification-report support total equal 138,689.
- Confirm row totals match actual class counts and column totals sum to the same total.
- Ensure report, README, notebook, screenshots, and saved outputs correspond to the same run.
