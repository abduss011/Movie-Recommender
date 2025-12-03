import React from "react";
function Recommendations({ recommendations }){
  if(!recommendations || recommendations.length === 0) return null;
  return(
    <div className="recommendations">
      <h2>Top Similar Movies</h2>
      <div className="recommendation-list">
        {recommendations.map((movie, idx) => (
          <div className="movie-card" key={idx}>
            <div className="poster">
              {movie.poster && movie.poster !== "N/A" ? (
                <img src={movie.poster} alt={movie.title} />
              ) : (
                <div className="no-poster">No Poster</div>
              )}
            </div>
            <div className="details">
              <h3>{movie.title}</h3>
              <p className="plot">
                {movie.plot && movie.plot !== "N/A" ? movie.plot : "Plot not available"}
              </p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
export default Recommendations;
