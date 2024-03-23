from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

class ContentBasedFiltering:
    def __init__(self, movies):
        self.movies = movies
        self.movie_ids = {movie['title']: idx for idx, movie in enumerate(movies)}
        self.tfidf_matrix = None
        
    def fit(self):
        genres_list = [' '.join(movie['genres']) for movie in self.movies]

        tfidf_vectorizer = TfidfVectorizer()
        self.tfidf_matrix = tfidf_vectorizer.fit_transform(genres_list)
        
    def recommend_movies(self, liked_movies, top_n=5):
     
        liked_movies_ids = [self.movie_ids[movie] for movie in liked_movies if movie in self.movie_ids]
        liked_movies_tfidf = self.tfidf_matrix[liked_movies_ids]
        cosine_similarities = linear_kernel(liked_movies_tfidf, self.tfidf_matrix)
        
        similar_indices = cosine_similarities.argsort(axis=1)[:, ::-1]
        recommended_movies = [movie for movie in similar_indices.ravel() if movie not in liked_movies_ids][:top_n]
        
        return [self.movies[movie]['title'] for movie in recommended_movies]

movies = [
    {'title': 'Movie1', 'genres': ['Action', 'Adventure']},
    {'title': 'Movie2', 'genres': ['Comedy', 'Romance']},
    {'title': 'Movie3', 'genres': ['Action', 'Thriller']},
    {'title': 'Movie4', 'genres': ['Drama', 'Romance']},
    {'title': 'Movie5', 'genres': ['Comedy', 'Drama']},
    {'title': 'Movie6', 'genres': ['Horror', 'Thriller']},
    {'title': 'Movie7', 'genres': ['Action', 'Adventure']},
    {'title': 'Movie8', 'genres': ['Comedy', 'Family']},
    {'title': 'Movie9', 'genres': ['Drama', 'Thriller']},
    {'title': 'Movie10', 'genres': ['Action', 'Sci-Fi']}
]

content_model = ContentBasedFiltering(movies)
content_model.fit()

liked_movies = ['Movie1', 'Movie3','Movie6']

recommended_movies = content_model.recommend_movies(liked_movies)
print("Recommended Movies:", recommended_movies)

