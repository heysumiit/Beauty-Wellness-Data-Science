# Week 5 — Model Training and Evaluation

**Project:** Exploring Customer Feedback and Product Sentiment  
**Domain:** Beauty & Wellness  
**Internship:** Data Science with Python Analyst Internship

## Objective
Train and compare text-classification models that predict a review's star rating (1–5) from the review text.

## Input dataset
`data/processed/beauty_reviews_cleaned.csv`

The script uses:
- `text` — input feature
- `rating` — target label

It converts ratings to numeric values, keeps labels 1–5, strips review text, and removes empty text rows.

## Run from project root
```bash
python Week-5/model_training.py
```

Install dependencies if required:
```bash
python -m pip install pandas matplotlib scikit-learn joblib
```

## Methodology
1. Load and validate the dataset.
2. Keep the `text` and `rating` columns.
3. Remove invalid ratings and empty review text.
4. Split data into 80% training and 20% testing with `random_state=42` and stratification.
5. Apply TF-IDF vectorization with up to 20,000 features, unigram/bigram features, `min_df=2`, and English stop-word removal.
6. Train Multinomial Naive Bayes and Logistic Regression pipelines.
7. Compare accuracy, macro precision, macro recall, and macro F1-score.
8. Select the model with the highest macro F1-score.
9. Save classification reports, test predictions, model comparison, the best model, and a confusion matrix.

## Dataset split and rating counts

| Item | Count |
|---|---:|
| Total records | 693,443 |
| Training records | 554,754 |
| Testing records | 138,689 |
| Rating 1 | 100,752 |
| Rating 2 | 42,576 |
| Rating 3 | 55,687 |
| Rating 4 | 78,532 |
| Rating 5 | 415,896 |

The training and testing counts sum to 693,443.

## Model comparison

| Model | Accuracy | Macro Precision | Macro Recall | Macro F1-score |
|---|---:|---:|---:|---:|
| Multinomial Naive Bayes | 0.707655 | 0.520400 | 0.378670 | 0.372669 |
| Logistic Regression | 0.726518 | 0.511134 | 0.437938 | 0.441833 |

**Selected model:** Logistic Regression, based on the higher macro F1-score (0.441833). Naive Bayes has slightly higher macro precision, so Logistic Regression does not lead on every metric.

## Confusion matrix
The supplied Logistic Regression confusion-matrix image contains 138,689 test examples in total, matching the reported test-set size. The matrix should be regenerated whenever the model or input data changes.

## Output files
- `data/processed/week5_model_comparison.csv`
- `data/processed/week5_test_predictions.csv`
- `data/processed/week5_multinomial_naive_bayes_classification_report.json`
- `data/processed/week5_logistic_regression_classification_report.json`
- `models/week5_best_model.joblib`
- `visuals/week5_confusion_matrix.png`

## Warning and limitations
Logistic Regression reached the configured `max_iter=300` and displayed a convergence warning. The script still completed, but a future run should test a higher iteration limit or alternative solver and then re-evaluate the model. The dataset is imbalanced, with five-star reviews representing about 60% of records. Macro metrics are included to avoid relying only on accuracy, but class-wise performance still needs improvement. TF-IDF features do not fully capture context, sarcasm, or all multilingual patterns.

## Before submission
- Run the script from the project root.
- Check that training plus testing equals the total dataset size.
- Compare the CSV metrics with the console output.
- Check classification reports and confusion matrix.
- Ensure report, README, screenshots, and output files all correspond to the same execution.
