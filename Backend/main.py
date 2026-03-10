from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import recommend, newDf

app = FastAPI(title="Movie Recommendation API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

#  Routes 
@app.get("/")
def home():
    return {"message": "Movie Recommendation API is running"}


@app.get("/recommend")
def get_recommendations(movie_name: str):
    """
    Usage: /recommend?movie_name=Toy Story
    """
    try:
        recommendations = recommend(movie_name)
        return {
            "movie": movie_name,
            "recommendations": recommendations
        }
    except IndexError:
        raise HTTPException(status_code=404, detail=f"Movie '{movie_name}' not found")


@app.get("/movies")
def list_movies():
    """Returns all available movie titles (useful for search/autocomplete)."""
    return {"movies": newDf['title'].tolist()}