# ai_service.py
import joblib

# Load the saved model
model = joblib.load('question_classifier.pkl')

def classify_question(question):
    return model.predict([question])[0]

# Example usage
question = "What is the boiling point of water?"
difficulty = classify_question(question)
print(f"The question '{question}' is classified as '{difficulty}'")


