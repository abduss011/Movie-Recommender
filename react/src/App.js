import React, { useEffect, useState } from "react";
import MovieSelect from "./components/MovieSelect";
import Recommendations from "./components/Recommendations";
import "./App.css";

function App() {
  const [movies, setMovies] = useState([]);
  const [selectedMovie, setSelectedMovie] = useState("");
  const [recommendations, setRecommendations] = useState([]);
  const [loading, setLoading] = useState(false);
  useEffect(() => {
    fetch("/api/movies")
      .then((res) => res.json())
      .then((data) => setMovies(data.movies))
      .catch(() => setMovies([]));
  }, []);
  const handleRecommend = () => {
    if (!selectedMovie) return;
    setLoading(true);
    fetch("/api/recommend", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ movie: selectedMovie }),
    })
      .then((res) => res.json())
      .then((data) => {
        setRecommendations(data.recommendations);
        setLoading(false);
      })
      .catch(() => {
        setRecommendations([]);
        setLoading(false);
      });
  };
  return (
    <div className="container">
      <h1>Movie Recommender System</h1>
      <MovieSelect
        movies={movies}
        selectedMovie={selectedMovie}
        setSelectedMovie={setSelectedMovie}
        onRecommend={handleRecommend}
        loading={loading}
      />
      <Recommendations recommendations={recommendations} />
    </div>
  );
}
export default App;
