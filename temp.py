from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(ngram_range=(1,2))),
    ('clf', LogisticRegression())
])

pipeline.fit(train_texts, train_labels)
preds = pipeline.predict(test_texts)


from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import Dataset

# Prepare data
data = Dataset.from_dict({"text": texts, "label": labels})
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

def tokenize(batch):
    return tokenizer(batch["text"], padding=True, truncation=True)

tokenized = data.map(tokenize, batched=True)

# Train-test split
train_test = tokenized.train_test_split(test_size=0.2)
train_set, test_set = train_test["train"], train_test["test"]

# Model
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased", num_labels=2)

# Fine-tune
args = TrainingArguments(output_dir="./results", evaluation_strategy="epoch", num_train_epochs=3)
trainer = Trainer(model=model, args=args, train_dataset=train_set, eval_dataset=test_set)
trainer.train()


