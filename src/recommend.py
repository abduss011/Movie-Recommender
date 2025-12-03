import json
import logging
import os
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)
try:
    base_path = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(base_path, 'recommendations.json'), 'r') as f:
        recommendations_dict = json.load(f)
    logging.info("Recommendations loaded successfully.")
except Exception as e:
    logging.error("Failed to load recommendations.json: %s", str(e))
    recommendations_dict = {}
movie_list = list(recommendations_dict.keys())

def recommend_movies(movie_name):
    logging.info("Looking up recommendations for: %s", movie_name)
    if movie_name in recommendations_dict:
        recs = recommendations_dict[movie_name]
        logging.info("Found %d recommendations.", len(recs))
        return [{"title": title} for title in recs]
    else:
        logging.warning("Movie not found: %s", movie_name)
        return None