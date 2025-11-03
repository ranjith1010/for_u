import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix

# 1. Load your CSV
# Example: discrepancy_text,label
df = pd.read_csv("discrepancies.csv")

# 2. Clean data
df.dropna(subset=['discrepancy_text', 'label'], inplace=True)

# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    df["discrepancy_text"],
    df["label"],
    test_size=0.2,
    random_state=42
)

# 4. Create model pipeline
model = Pipeline([
    ('tfidf', TfidfVectorizer(ngram_range=(1,2), stop_words='english')),
    ('clf', LogisticRegression(max_iter=200))
])

# 5. Train
model.fit(X_train, y_train)

# 6. Evaluate
preds = model.predict(X_test)
print(classification_report(y_test, preds))
print(confusion_matrix(y_test, preds))

# 7. Example prediction
sample = ["Total amount in grid does not match invoice total"]
print(model.predict(sample))

import skl2onnx
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import StringTensorType

# Define input type (string text input)
initial_type = [('input', StringTensorType([None, 1]))]

# Convert model
onnx_model = convert_sklearn(model, initial_types=initial_type)

# Save to file
with open("discrepancy_model.onnx", "wb") as f:
    f.write(onnx_model.SerializeToString())
