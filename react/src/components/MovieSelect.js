import React, { useState, useEffect, useRef } from "react";

function MovieSelect({ movies, selectedMovie, setSelectedMovie, onRecommend, loading }) {
  const [inputValue, setInputValue] = useState("");
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);
  const [filteredMovies, setFilteredMovies] = useState([]);
  const wrapperRef = useRef(null);
  useEffect(() => {
    if (selectedMovie) {
      setInputValue(selectedMovie);
    }
  }, [selectedMovie]);
  useEffect(() => {
    if (inputValue && isDropdownOpen) {
      const lowerInput = inputValue.toLowerCase();
      const filtered = movies.filter(movie =>
        movie.toLowerCase().includes(lowerInput)
      );
      setFilteredMovies(filtered);
    } else {
      setFilteredMovies(movies);
    }
  }, [inputValue, movies, isDropdownOpen]);
  useEffect(() => {
    function handleClickOutside(event) {
      if (wrapperRef.current && !wrapperRef.current.contains(event.target)) {
        setIsDropdownOpen(false);
      }
    }
    document.addEventListener("mousedown", handleClickOutside);
    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, [wrapperRef]);
  const handleInputChange = (e) => {
    setInputValue(e.target.value);
    setIsDropdownOpen(true);
    if (e.target.value === "") {
      setSelectedMovie("");
    }
  };
  const handleSelectMovie = (movie) => {
    setSelectedMovie(movie);
    setInputValue(movie);
    setIsDropdownOpen(false);
  };

  const handleInputFocus = () => {
    setIsDropdownOpen(true);
  };
  return (
    <div className="movie-select" ref={wrapperRef}>
      <label htmlFor="movie-input">Search for a movie:</label>
      <div className="autocomplete-container">
        <input
          id="movie-input"
          type="text"
          value={inputValue}
          onChange={handleInputChange}
          onFocus={handleInputFocus}
          placeholder="Type to search..."
          autoComplete="off"
          className="movie-input"
        />
        {isDropdownOpen && (
          <ul className="autocomplete-dropdown">
            {filteredMovies.length > 0 ? (
              filteredMovies.map((movie) => (
                <li
                  key={movie}
                  onClick={() => handleSelectMovie(movie)}
                  className={movie === selectedMovie ? "selected" : ""}
                >
                  {movie}
                </li>
              ))
            ) : (
              <li className="no-results">No movies found</li>
            )}
          </ul>
        )}
      </div>

      <button
        className="recommend-btn"
        onClick={onRecommend}
        disabled={!selectedMovie || loading}
      >
        {loading ? "Finding..." : "Recommend Similar Movies"}
      </button>
    </div>
  );
}

export default MovieSelect;
