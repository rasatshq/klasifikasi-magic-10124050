"""Opsional: unduh sumber UCI dan reproduksi sampel 1.000 baris."""
from pathlib import Path
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen
import pandas as pd
from sklearn.model_selection import train_test_split

ROOT = Path(__file__).resolve().parent
URL = "https://archive.ics.uci.edu/static/public/159/magic+gamma+telescope.zip"
COLS = ["fLength", "fWidth", "fSize", "fConc", "fConc1", "fAsym",
        "fM3Long", "fM3Trans", "fAlpha", "fDist", "class"]
with urlopen(URL, timeout=60) as response:
    archive = ZipFile(BytesIO(response.read()))
source = pd.read_csv(BytesIO(archive.read("magic04.data")), names=COLS)
clean = source.drop_duplicates()
sample, _ = train_test_split(clean, train_size=1000,
                            stratify=clean["class"], random_state=42)
sample = sample.sort_index()
assert len(sample) == 1000 and sample.duplicated().sum() == 0
sample.to_csv(ROOT / "dataset_magic_1000.csv", index=False)
pd.DataFrame({"row_id": range(1000), "source_row_id": sample.index}).to_csv(
    ROOT / "asal_baris_sampel.csv", index=False)
print("Sampel siap:", sample.shape, sample["class"].value_counts().to_dict())
