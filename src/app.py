from flask import Flask,request,jsonify
from flask_cors import CORS
from recommend import recommend_movies, movie_list 
from utils import get_details
import json
import os

app = Flask(__name__, static_folder="../react/build", static_url_path="/")
CORS(app)

@app.route('/')
def index():
    return app.send_static_file('index.html')

try:
    base = os.path.dirname(os.path.abspath(__file__))
    config = os.path.join(base, "config.json")
    with open(config) as f:
        config = json.load(f)
    OMDB_API_KEY = config["OMDB_API_KEY"]
except FileNotFoundError:
    OMDB_API_KEY = None
except KeyError:
    OMDB_API_KEY = None

@app.route("/api/movies", methods=["GET"])
def get_movies():
    try:
        return jsonify({"movies": sorted(movie_list)})
    except Exception as e:
        return jsonify({"error": "Could not load movie data."}), 500

@app.route("/api/recommend", methods=["POST"])
def recommend():
    if OMDB_API_KEY is None:
        return jsonify({"error": "API key is missing or invalid."}), 503
    data = request.get_json()
    selected_movie = data.get("movie")
    if not selected_movie:
        return jsonify({"error": "No movie provided in request body."}), 400
    
    recommendations = recommend_movies(selected_movie)
    results = []
    
    if recommendations:
        for row in recommendations:
            movie_title = row['title']
            movie_year = None 
            try:
                plot, poster = get_details(movie_title, OMDB_API_KEY, movie_year)
            except Exception as e:
                plot, poster = "Plot details unavailable.", "N/A"
            if poster == "N/A":
                continue
            results.append({
                "title": movie_title,
                "plot": plot,
                "poster": poster
            })
    return jsonify({"recommendations": results})

if __name__ == "__main__":
    app.run(debug=True, port=5000)