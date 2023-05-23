class MovieRecommendr:
    def __init__(self, movies):
        self.movies = movies

    def recommend_movies(self, genre, rating_threshold):
        recommended_movies = []
        for movie in self.movies:
            if movie['genre'] == genre and movie['rating'] >= rating_threshold:
                recommended_movies.append(movie['title'])
        return recommended_movies

# Sample data for movies
movies = [
    {
        'title': 'The Shawshank Redemption',
        'genre': 'Drama',
        'rating': 9.3
    },
    {
        'title': 'The Godfather',
        'genre': 'Crime',
        'rating': 9.2
    },
    {
        'title': 'The Dark Knight',
        'genre': 'Action',
        'rating': 9.0
    },
    {
        'title': 'Pulp Fiction',
        'genre': 'Crime',
        'rating': 8.9
    },
    {
        'title': 'Fight Club',
        'genre': 'Drama',
        'rating': 8.8
    }
]

# Create an instance of MovieRecommendr
movie_recommendr = MovieRecommendr(movies)

# Call the recommend_movies method
recommended_movies = movie_recommendr.recommend_movies('Drama', 9.0)

# Print the recommended movies
print("Recommended Movies:")
for movie in recommended_movies:
    print(movie)
