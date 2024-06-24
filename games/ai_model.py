# ai_model.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn import metrics
import joblib

# Sample data
data = {
    'question': ["What is 2+2?", "Explain the theory of relativity.", "What is the capital of France?"],
    'difficulty': ['novice', 'expert', 'beginner']
}

df = pd.DataFrame(data)

# Text processing and model pipeline
X = df['question']
y = df['difficulty']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression())
])

pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

print(metrics.classification_report(y_test, y_pred))

# Save the model
joblib.dump(pipeline, 'question_classifier.pkl')

