
from domainmodel.movie import Movie
from datetime import datetime
class Review:
    def __init__(self, movie: Movie, rating: int, review_text: str):
        self.__movie = movie
        self.__review_text = review_text
        if type(rating) == int or type(rating) == float:
            if rating <= 10 and rating > 0:
                self.__rating = rating
            else:
                self.__rating = None
        else:
            self.__rating = None

        self.__timestamp = datetime.now()

    @property
    def movie(self) -> Movie:
        return self.__movie

    @property
    def review_text(self) -> str:
        return self.__review_text

    @property
    def rating(self) -> int:
        return self.__rating

    @property
    def timestamp(self) -> datetime:
        return self.__timestamp

    def __eq__(self, other):
        return self.movie == other.movie and self.review_text == other.review_text and self.rating == other.rating and self.timestamp == other.timestamp


class TestReview:

    def test_init(self):
        movie = Movie("Moana", 2016)
        review_text = "This movie was very enjoyable."
        rating = 8
        review = Review(movie, review_text, rating)

        assert repr(review.movie) == "<Movie Moana, 2016>"
        assert review.review_text == "This movie was very enjoyable."
        assert review.rating == 8