# Data Set: https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset

import pandas as pd
import numpy as np
import nltk
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')

# Load dataset
df = pd.read_csv("dataset.csv")

# Combine all symptom columns into one string per row
symptom_cols = [col for col in df.columns if 'Symptom' in col]
df['symptom_string'] = df[symptom_cols].apply(lambda x: ' '.join(x.dropna().astype(str)), axis=1)

# Drop any rows with no symptoms or disease
df.dropna(subset=['symptom_string', 'Disease'], inplace=True)

# Prepare training data
symptom_texts = df['symptom_string'].tolist()
disease_labels = df['Disease'].tolist()

# Vectorize symptom text using TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(symptom_texts)

# Chatbot response function
def diagnose(user_input):
    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, X)
    best_idx = similarity.argmax()
    confidence = similarity[0, best_idx]

    if confidence < 0.2:
        return "Sorry, I couldn't identify your condition. Please consult a doctor."
    else:
        disease = disease_labels[best_idx]
        return f"Based on your symptoms, you might have **{disease}** (confidence: {confidence:.2f}). Please consult a healthcare provider."

# Chat loop
print("👨‍⚕️ Real-Data Medical Chatbot")
print("Enter your symptoms (e.g., fever headache chills). Type 'exit' to quit.\n")

while True:
    user_input = input("You: ").lower()
    if user_input in ['exit', 'quit']:
        print("Bot: Take care! 👋")
        break
    print("Bot:", diagnose(user_input))
