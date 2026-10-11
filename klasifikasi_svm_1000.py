"""Klasifikasi MAGIC: tepat 1.000 baris dan 10 fitur, tanpa ID/label."""
from pathlib import Path
import json
import platform
import numpy as np
import pandas as pd
import sklearn
from sklearn.impute import SimpleImputer
from sklearn.metrics import (accuracy_score, classification_report,
                             confusion_matrix, roc_auc_score)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

ROOT = Path(__file__).resolve().parent
FEATURES = ["fLength", "fWidth", "fSize", "fConc", "fConc1",
            "fAsym", "fM3Long", "fM3Trans", "fAlpha", "fDist"]
df = pd.read_csv(ROOT / "dataset_magic_1000.csv")
assert list(df.columns) == FEATURES + ["class"]
assert len(df) == 1000 and len(FEATURES) == 10
print("INFO KOLOM SEBELUM PEMROSESAN")
df.info()
original_types = df.dtypes.astype(str)
original_labels = df["class"].copy()
assert original_labels.notna().all()
# Rapikan spasi dan kapitalisasi label tanpa mengubah arti kategori.
df["class"] = df["class"].astype("string").str.strip().str.lower()
label_corrections = int((original_labels != df["class"]).sum())
for col in FEATURES:
    df[col] = pd.to_numeric(df[col], errors="raise").astype("float64")
column_audit = pd.DataFrame({
    "kolom": df.columns, "tipe_awal": original_types.to_numpy(),
    "tipe_hasil": df.dtypes.astype(str).to_numpy(),
    "nilai_kosong": df.isna().sum().to_numpy(),
    "peran": ["fitur"] * 10 + ["label"],
})
column_audit.to_csv(ROOT / "audit_kolom.csv", index=False)
print("\nTIPE KOLOM DAN MISSING VALUES\n",
      column_audit.to_string(index=False))
print("\nKATEGORI AWAL:", original_labels.unique().tolist())
print("KATEGORI HASIL:", df["class"].unique().tolist())
print("Koreksi ejaan/kapitalisasi/spasi:", label_corrections)
assert set(df["class"]) == {"g", "h"}
assert df.duplicated().sum() == 0
X, y = df[FEATURES], df["class"]
assert np.isfinite(X.dropna().to_numpy()).all()
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y)
model = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
    ("svm", SVC(kernel="rbf", C=1.0, gamma="scale",
                class_weight="balanced")),
])
model.fit(X_train, y_train)
pred = model.predict(X_test)
prep = model[:-1]
names = [f + "_z" for f in FEATURES]
processed = pd.DataFrame(prep.transform(X), columns=names, index=X.index)
assert processed.shape == (1000, 10)
assert not processed.isna().any().any()
processed.insert(0, "row_id", X.index)
processed["class"] = y
processed["split"] = np.where(X.index.isin(X_train.index), "latih", "uji")
processed.to_csv(ROOT / "dataset_magic_hasil_pemrosesan.csv", index=False)
q1, q3 = X_train.quantile(.25), X_train.quantile(.75)
lower, upper = q1 - 1.5 * (q3 - q1), q3 + 1.5 * (q3 - q1)
outliers = (X_train.lt(lower) | X_train.gt(upper))
stats = pd.DataFrame({"fitur": FEATURES,
    "median_latih": model["imputer"].statistics_,
    "mean_latih": model["scaler"].mean_,
    "std_latih": model["scaler"].scale_,
    "batas_bawah_iqr": lower.to_numpy(),
    "batas_atas_iqr": upper.to_numpy()})
stats.to_csv(ROOT / "statistik_data_latih.csv", index=False)
predictions = pd.DataFrame({"row_id": X_test.index,
                           "aktual": y_test, "prediksi": pred})
predictions.to_csv(ROOT / "prediksi_data_uji.csv", index=False)
# decision_function positif menuju classes_[1] yaitu h.
# Balik tandanya agar skor ROC positif menuju gamma (g).
assert list(model["svm"].classes_) == ["g", "h"]
auc = roc_auc_score((y_test == "g").astype(int),
                    -model.decision_function(X_test))
report = classification_report(y_test, pred, labels=["g", "h"],
    target_names=["gamma", "hadron"], output_dict=True, zero_division=0)
result = {
    "rows": len(df), "feature_count": len(FEATURES),
    "output_features": names, "missing": int(X.isna().sum().sum()),
    "duplicates": int(df.duplicated().sum()),
    "label_corrections": label_corrections,
    "class_counts": y.value_counts().to_dict(),
    "train_counts": y_train.value_counts().to_dict(),
    "test_counts": y_test.value_counts().to_dict(),
    "train_rows": len(X_train), "test_rows": len(X_test),
    "outlier_rows_train": int(outliers.any(axis=1).sum()),
    "train_accuracy": accuracy_score(y_train, model.predict(X_train)),
    "test_accuracy": accuracy_score(y_test, pred), "roc_auc_gamma": auc,
    "classification_report": report,
    "confusion_matrix": confusion_matrix(y_test, pred, labels=["g", "h"]).tolist(),
    "python": platform.python_version(), "numpy": np.__version__,
    "pandas": pd.__version__, "sklearn": sklearn.__version__,
}
(ROOT / "hasil_evaluasi.json").write_text(json.dumps(result, indent=2))
print("MAGIC GAMMA TELESCOPE - 1.000 BARIS DAN 10 FITUR")
print("ID dan label tidak dihitung sebagai fitur.")
print("Jumlah awal dan setelah pemrosesan:", len(df), len(processed))
print("Nilai kosong:", result["missing"], "Duplikat:", result["duplicates"])
print("Distribusi kelas:", result["class_counts"])
print("Data latih:", len(X_train), "Data uji:", len(X_test))
print("Kandidat pencilan latih:", result["outlier_rows_train"])
print("\nSTATISTIK DARI DATA LATIH\n", stats.to_string(index=False))
print("\n5 TERATAS HASIL PEMROSESAN\n",
      processed.head().to_string(index=False, float_format=lambda v: f"{v:.6f}"))
print("\n5 TERBAWAH HASIL PEMROSESAN\n",
      processed.tail().to_string(index=False, float_format=lambda v: f"{v:.6f}"))
print(f"\nAkurasi latih: {result['train_accuracy']:.4%}")
print(f"Akurasi uji: {result['test_accuracy']:.4%}")
print(f"ROC AUC gamma: {auc:.6f}")
print("Confusion matrix (urutan g, h):\n", result["confusion_matrix"])
print(classification_report(y_test, pred, labels=["g", "h"],
    target_names=["gamma", "hadron"], digits=4, zero_division=0))
