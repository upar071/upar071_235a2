from datetime import date, datetime
class Actor:

    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()

        self.__colleagues_list = []

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    @property
    def colleagues(self) -> list:
        return self.__colleagues_list

    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, other):
        return self.actor_full_name == other.actor_full_name

    def __lt__(self, other):
        return self.actor_full_name < other.actor_full_name

    def __hash__(self):
        return hash(self.actor_full_name)

    def add_actor_colleague(self, colleague):
        self.__colleagues_list.append(colleague)

    def check_if_this_actor_worked_with(self, colleague):
        return colleague in self.__colleagues_list


class Director:

    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    def __repr__(self):
        return f"<Director {self.__director_full_name}>"

    def __eq__(self, other):
        return self.director_full_name == other.director_full_name

    def __lt__(self, other):
        return self.director_full_name < other.director_full_name

    def __hash__(self):
        return hash(self.director_full_name)


class Genre:
    def __init__(self, genre_name: str):
        if genre_name == "" or type(genre_name) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = genre_name.strip()

    @property
    def genre_name(self) -> str:
        return self.__genre_name

    def __repr__(self):
        return f"<Genre {self.__genre_name}>"

    def __eq__(self, other):
        return self.genre_name == other.genre_name

    def __lt__(self, other):
        return self.genre_name < other.genre_name

    def __hash__(self):
        return hash(self.genre_name)


class Movie:
    def __init__(self, movie_title: str, release_year: int):
        if movie_title == "" or type(movie_title) is not str:
            self.__movie_title = None
        else:
            self.__movie_title = movie_title.strip()

        if type(release_year) is not int:
            self.__release_year = None
        else:
            if release_year < 1900:
                self.__release_year = None
            else:
                self.__release_year = release_year

        self.__director = None
        self.__actors = list()
        self.__genres = list()
        self.__description = None
        self.__runtime_minutes = None
        self.__id = None
        self.__reviews = list()
        self.__imagelink = None

    @property
    def imagelink(self):
        return self.__imagelink
    @property
    def title(self) -> str:
        return self.__movie_title

    @property
    def year(self) -> int:
        return self.__release_year

    @property
    def director(self) -> Director:
        return self.__director

    @property
    def id(self) -> int:
        return self.__id

    @director.setter
    def director(self, director):
        self.__director = director

    @property
    def actors(self) -> list:
        return self.__actors

    @property
    def genres(self) -> list:
        return self.__genres

    @property
    def reviews(self) -> list:
        return self.__reviews

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description.strip()

    @property
    def runtime_minutes(self) -> int:
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, runtime_minutes):
        if type(runtime_minutes) is not int:
            raise ValueError
        else:
            if runtime_minutes >= 0:
                self.__runtime_minutes = runtime_minutes
            else:
                raise ValueError

    def add_id(self, rank: int):
        self.__id = rank

    def add_actor(self, actor: Actor):
        self.__actors.append(actor)

    def add_director(self, director: Director):
        self.__director = director

    def add_imagelink(self, link):
        self.__imagelink = link

    def remove_actor(self, actor: Actor):
        actors_list = self.__actors
        if actor in actors_list:
            for i in range(len(actors_list) - 1, -1, -1):
                if actor == actors_list[i]:
                    actors_list.pop(i)
        self.__actors = actors_list

    def add_genre(self, genre: Genre):
        self.__genres.append(genre)

    def add_review(self, review):
        self.__reviews.append(review)

    def remove_genre(self, genre: Genre):
        genres_list = self.__genres
        if genre in genres_list:
            for i in range(len(genres_list)-1, -1, -1):
                if genre == genres_list[i]:
                    genres_list.pop(i)
        self.__genres = genres_list

    def __repr__(self):
        return f"<Movie {self.__movie_title}, {self.__release_year}>"

    def __eq__(self, other):
        return self.title == other.title and self.__release_year == other.__release_year

    def __lt__(self, other):
        return f"{self.__movie_title}{self.__release_year}" < f"{other.__movie_title}{other.__release_year}"

    def __hash__(self):
        return hash(f"{self.__movie_title}{self.__release_year}")


class User:
    def __init__(self, username: str, password):
        self.__user_name = username.strip()
        self.__watched_movies = []
        self.__reviews = []
        self.__time_spent_watching_movies_minutes = 0
        self.__password = password
        self.__watchlist = []

    @property
    def username(self) -> str:
        return self.__user_name

    @property
    def watchlist(self) -> list:
        return self.__watchlist

    @property
    def password(self):
        return self.__password

    @property
    def watched_movies(self) -> list:
        return self.__watched_movies

    @property
    def reviews(self) -> list:
        return self.__reviews

    @property
    def time_spent_watching_movies_minutes(self) -> int:
        return self.__time_spent_watching_movies_minutes

    def __repr__(self):
        return f"<User {self.__user_name} {self.__password}>"

    def __eq__(self, other):
        return self.username == other.username

    def __lt__(self, other):
        return self.username < other.username

    def __hash__(self):
        return hash(self.username)

    def watch_movie(self, movie: Movie):
        self.__watched_movies.append(movie)
        self.__time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review):
        self.__reviews.append(review)

    def add_to_watchlist(self, movie):
        self.__watchlist.append(movie)

    def remove_from_watchlist(self, movie):
        watchlist = self.__watchlist
        if movie in watchlist:
            for i in range(len(watchlist) - 1, -1, -1):
                if movie == watchlist[i]:
                    watchlist.pop(i)
        self.__watchlist = watchlist

class WatchList:
    def __init__(self):
        self.__watch_list = []

    def add_movie(self, movie: Movie):
        if movie in self.__watch_list:
            pass
        else:
            self.__watch_list.append(movie)

    def remove_movie(self, movie: Movie):
        if movie not in self.__watch_list:
            pass
        else:
            for i in range(len(self.__watch_list)):
                if self.__watch_list[i] == movie:
                    self.__watch_list.pop(i)

    def select_movie_to_watch(self, index: int):
        if index >= 0 and len(self.__watch_list) > index:
            return self.__watch_list[index]
        else:
            return None

    def size(self):
        return len(self.__watch_list)

    def first_movie_in_watchlist(self):
        if len(self.__watch_list) != 0:
            return self.__watch_list[0]
        else:
            return None

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n >= len(self.__watch_list):
            raise StopIteration
        else:
            result = self.__watch_list[self.n]
            self.n += 1
            return result



class Review:
    def __init__(self, user: User, movie: Movie, review_text: str):
        self.__movie = movie
        self.__review_text = review_text
        self.__timestamp = datetime.now()
        self.__user = user

    @property
    def movie(self) -> Movie:
        return self.__movie

    @property
    def user(self) -> User:
        return self.__user

    @property
    def username(self) -> str:
        return self.__user.username

    @property
    def review_text(self) -> str:
        return self.__review_text

    @property
    def timestamp(self) -> datetime:
        return self.__timestamp

    def __eq__(self, other):
        return self.movie == other.movie and self.review_text == other.review_text and self.rating == other.rating and self.timestamp == other.timestamp


def make_review(review_text: str, user: User, movie: Movie):

    review = Review(user, movie, review_text)
    user.add_review(review)
    movie.add_review(review)

    return review

