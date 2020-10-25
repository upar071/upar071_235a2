import abc
from typing import List

from movies.domain.domainmodel import Movie, Genre, Director, Actor, Review, User


repo_instance = None


class RepositoryException(Exception):

    def __init__(self, message=None):
        pass


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add_user(self, user: User):
        """" Adds a User to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, username) -> User:
        """ Returns the User named username from the repository.
        If there is no User with the given username, this method returns None.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def add_movie(self, movie: Movie):
        """ Adds an movie to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie(self, id: int) -> Movie:
        """ Returns movie with id from the repository.

        If there is no movie with the given id, this method returns None.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_year(self, target_year: int) -> List[Movie]:
        """ Returns a list of movie_library that are from target_year.

        If there are no movie_library of the given year, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_number_of_movies(self):
        """ Returns the number of movie_library in the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_first_movie(self) -> Movie:
        """ Returns the first Movie from the repository.

        Returns None if the repository is empty.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_last_movie(self) -> Movie:
        """ Returns the last movie from the repository.

        Returns None if the repository is empty.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_id(self, id_list):
        """ Returns a list of movie_library, whose ids match those in id_list, from the repository.

        If there are no matches, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_ids_for_actor(self, actor_name: str):
        """ Returns a list of ids representing movie_library that have actor.

        If there are movie_library that are tagged by actor_name, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_ids_for_director(self, director_name: str):
        """ Returns a list of ids representing movie_library that have Director.

        If there are movie_library that are tagged by actor_name, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_ids_for_genre(self, genre_name: str):
        """ Returns a list of ids representing movie_library that have Genre.

        If there are movie_library that are tagged by Genre_name, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_actors(self) -> List[Actor]:
        """ Returns the Actors stored in the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_directors(self) -> List[Director]:
        """ Returns the directors stored in the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_genres(self) -> List[Genre]:
        """ Returns the Genres stored in the repository. """
        raise NotImplementedError


    @abc.abstractmethod
    def get_id_of_previous_movie(self, movie: Movie):
        """ Returns the id of a Movie that immediately precedes movie.

        If movie is the first Movie in the repository, this method returns None.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_id_of_next_movie(self, movie: Movie):
        """ Returns the id of a Movie that immediately follows movie.

        If movie is the last Movie in the repository, this method returns None.
        """
        raise NotImplementedError


    @abc.abstractmethod
    def add_review(self, review: Review):
        """ Adds a Review to the repository.

        If the Review doesn't have bidirectional links with an Article and a User, this method raises a
        RepositoryException and doesn't update the repository.
        """
        if review.user is None or review not in review.user.reviews:
            raise RepositoryException('Comment not correctly attached to a User')
        if review.movie is None or review not in review.movie.reviews:
            raise RepositoryException('Comment not correctly attached to an Article')

    @abc.abstractmethod
    def get_reviews(self):
        """ Returns the reviews stored in the repository. """
        raise NotImplementedError







