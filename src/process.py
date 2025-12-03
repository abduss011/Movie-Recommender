import pandas as pd
import os
import re
import nltk
import joblib
import logging
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("preprocess.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)
logging.info("Starting...")
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

stop_words = set(stopwords.words('english'))
try:
    base_path = os.path.dirname(os.path.abspath(__file__))
    df = pd.read_csv(os.path.join(base_path, "movies.csv"))
    logging.info("Dataset loaded successfully. Total rows: %d", len(df))
except Exception as e:
    logging.error("Failed to load dataset: %s", str(e))
    raise e

def process(text) : 
  text = re.sub(r"[^a-zA-Z\s]" , "" , text)
  text = text.lower()
  tokens = word_tokenize(text)
  tokens = [word for word in tokens if word not in stop_words]
  return " ".join(tokens)
required_columns = ["genres" , "keywords" , "overview" , "title"]
df = df[required_columns]
df = df.dropna().reset_index(drop=True)
df["combined"] = df["genres"] + "  " + df["keywords"] + "  " + df["overview"]

logging.info("Cleaning...")
df["cleaned_text"] = df["combined"].apply(process)
logging.info("Text cleaning completed.")

logging.info("Vectorizing...")
vectorizer = TfidfVectorizer(max_features = 5000)
matrix = vectorizer.fit_transform(df["cleaned_text"])
logging.info("TF-IDF matrix shape: %s", matrix.shape)

import json

logging.info("Calcularting cosine similarity...")
cosine_sim = cosine_similarity(matrix , matrix)
logging.info("Cosine similarity calculation completed.")

logging.info("Pre-computing recommendations...")
recommendations_dict = {}

indices = pd.Series(df.index, index=df['title']).drop_duplicates()

for title in df['title']:
    try:
        idx = indices[title]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:6]
        movie_indices = [i[0] for i in sim_scores]
        
        recs = []
        for i in movie_indices:
            rec_title = df['title'].iloc[i]
            recs.append(rec_title)
            
        recommendations_dict[title] = recs
    except Exception as e:
        logging.warning(f"Could not generate recommendations for {title}: {e}")
with open('recommendations.json', 'w') as f:
    json.dump(recommendations_dict, f)

logging.info("Recommendations saved to recommendations.json")
logging.info("Processing completed.")