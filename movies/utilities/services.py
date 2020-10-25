from typing import Iterable
import random

from movies.adapters.repository import AbstractRepository
from movies.domain.domainmodel import Movie, Director, Actor, Genre


def get_actor_names(repo: AbstractRepository):
    actors = repo.get_actors()
    actor_names = [actor.actor_full_name for actor in actors]

    return actor_names


def get_genre_names(repo: AbstractRepository):
    genres = repo.get_genres()
    genre_names = [genre.genre_name for genre in genres]

    return genre_names


def get_director_names(repo: AbstractRepository):
    directors = repo.get_directors()
    director_names = [director.director_full_name for director in directors]

    return director_names


def get_random_movies(quantity, repo: AbstractRepository):
    movie_count = repo.get_number_of_movies()

    if quantity >= movie_count:
        # Reduce the quantity of ids to generate if the repository has an insufficient number of movies.
        quantity = movie_count - 1

    # Pick distinct and random articles.
    random_ids = random.sample(range(1, movie_count), quantity)
    movies = repo.get_movies_by_id(random_ids)

    return movies_to_dict(movies)


# ============================================
# Functions to convert dicts to model entities
# ============================================

def movie_to_dict(movie: Movie):
    movie_dict = {
        'id': movie.id,
        'year': movie.year,
        'title': movie.title,
        # 'first_para': article.first_para,
        # 'hyperlink': article.hyperlink,
        # 'image_hyperlink': article.image_hyperlink,
        # 'reviews': reviews_to_dict(movie.reviews),
        # 'actors': tags_to_dict(movie.actors),
        'actors': movie.actors,
        'directors': movie.director,
        # 'genres': tags_to_dict(movie.genres),
        'genres': movie.genres,
        "description": movie.description,
        "imagelink": movie.imagelink
        # 'image_hyperlink': article.image_hyperlink
    }
    return movie_dict


def movies_to_dict(movies: Iterable[Movie]):
    return [movie_to_dict(movie) for movie in movies]


