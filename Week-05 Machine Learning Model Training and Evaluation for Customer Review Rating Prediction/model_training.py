
from pathlib import Path
import json
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)
import joblib


# --------------------------------------------------
# 1. Project paths
# --------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[1]

INPUT_FILE = PROJECT_ROOT / "data" / "processed" / "beauty_reviews_cleaned.csv"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
VISUALS_DIR = PROJECT_ROOT / "visuals"
MODELS_DIR = PROJECT_ROOT / "models"

for folder in [PROCESSED_DIR, VISUALS_DIR, MODELS_DIR]:
    folder.mkdir(parents=True, exist_ok=True)


# --------------------------------------------------
# 2. Load and validate data
# --------------------------------------------------
if not INPUT_FILE.exists():
    raise FileNotFoundError(f"Dataset not found: {INPUT_FILE}")

df = pd.read_csv(INPUT_FILE)

required_columns = {"text", "rating"}
missing_columns = required_columns - set(df.columns)

if missing_columns:
    raise ValueError(f"Required columns missing: {missing_columns}")

df = df[["text", "rating"]].copy()
df["text"] = df["text"].fillna("").astype(str).str.strip()
df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

df = df.dropna(subset=["rating"])
df = df[df["rating"].isin([1, 2, 3, 4, 5])]
df = df[df["text"].str.len() > 0]

df["rating"] = df["rating"].astype(int)

print("Dataset loaded successfully.")
print("Dataset shape:", df.shape)
print("\nRating distribution:")
print(df["rating"].value_counts().sort_index())


# --------------------------------------------------
# 3. Train-test split
# --------------------------------------------------
X = df["text"]
y = df["rating"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining records:", len(X_train))
print("Testing records:", len(X_test))


# --------------------------------------------------
# 4. Define models
# TF-IDF is kept inside each Pipeline to avoid
# fitting the vectorizer on test data.
# --------------------------------------------------
models = {
    "Multinomial Naive Bayes": Pipeline([
        ("tfidf", TfidfVectorizer(
            max_features=20000,
            ngram_range=(1, 2),
            min_df=2,
            stop_words="english"
        )),
        ("classifier", MultinomialNB())
    ]),

    "Logistic Regression": Pipeline([
        ("tfidf", TfidfVectorizer(
            max_features=20000,
            ngram_range=(1, 2),
            min_df=2,
            stop_words="english"
        )),
        ("classifier", LogisticRegression(
            max_iter=300,
            random_state=42
        ))
    ])
}


# --------------------------------------------------
# 5. Train and evaluate
# --------------------------------------------------
results = []
predictions = pd.DataFrame({
    "actual_rating": y_test.reset_index(drop=True)
})

best_model_name = None
best_model = None
best_macro_f1 = -1
best_predictions = None

for model_name, model in models.items():
    print(f"\nTraining: {model_name}")
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(
        y_test, y_pred, average="macro", zero_division=0
    )
    recall = recall_score(
        y_test, y_pred, average="macro", zero_division=0
    )
    macro_f1 = f1_score(
        y_test, y_pred, average="macro", zero_division=0
    )

    results.append({
        "model": model_name,
        "accuracy": accuracy,
        "macro_precision": precision,
        "macro_recall": recall,
        "macro_f1": macro_f1
    })

    safe_name = model_name.lower().replace(" ", "_")
    predictions[f"{safe_name}_prediction"] = y_pred

    report = classification_report(
        y_test,
        y_pred,
        output_dict=True,
        zero_division=0
    )

    report_path = PROCESSED_DIR / f"week5_{safe_name}_classification_report.json"
    with open(report_path, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    print(f"Accuracy: {accuracy:.4f}")
    print(f"Macro Precision: {precision:.4f}")
    print(f"Macro Recall: {recall:.4f}")
    print(f"Macro F1-score: {macro_f1:.4f}")

    if macro_f1 > best_macro_f1:
        best_macro_f1 = macro_f1
        best_model_name = model_name
        best_model = model
        best_predictions = y_pred


# --------------------------------------------------
# 6. Save evaluation results
# --------------------------------------------------
metrics_df = pd.DataFrame(results)
metrics_path = PROCESSED_DIR / "week5_model_comparison.csv"
metrics_df.to_csv(metrics_path, index=False)

predictions_path = PROCESSED_DIR / "week5_test_predictions.csv"
predictions.to_csv(predictions_path, index=False)

# Verify saved predictions
saved_predictions = pd.read_csv(predictions_path)

print("\nPrediction verification:")
print("Predictions before saving:", predictions.shape)
print("Saved CSV shape:", saved_predictions.shape)
print("Saved CSV location:", predictions_path.resolve())


# --------------------------------------------------
# 7. Save best model and confusion matrix
# --------------------------------------------------
model_path = MODELS_DIR / "week5_best_model.joblib"
joblib.dump(best_model, model_path)

cm = confusion_matrix(y_test, best_predictions, labels=[1, 2, 3, 4, 5])
display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=[1, 2, 3, 4, 5]
)

fig, ax = plt.subplots(figsize=(8, 6))
display.plot(ax=ax, cmap="Blues", values_format="d")
ax.set_title(f"Confusion Matrix - {best_model_name}")
plt.tight_layout()

confusion_path = VISUALS_DIR / "week5_confusion_matrix.png"
plt.savefig(confusion_path, dpi=300, bbox_inches="tight")
plt.close()


# --------------------------------------------------
# 8. Final summary
# --------------------------------------------------
print("\nMODEL COMPARISON")
print(metrics_df.to_string(index=False))

print("\nBest model by macro F1-score:", best_model_name)
print("Best macro F1-score:", round(best_macro_f1, 4))

print("\nSaved files:")
print(metrics_path)
print(predictions_path)
print(model_path)
print(confusion_path)

print("\nWeek 5 model training completed successfully!")