from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director

class Movie:
    def __init__(self, movie_title: str, release_year: int, runtime_minutes: int):
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
        self.__actors = None
        self.__genres = None
        self.__description = None
        self.__runtime_minutes = runtime_minutes
        self.__id = None
        # A movie is considered to be uniquely defined by the combination of its title and release year

    @property
    def title(self) -> str:
        return self.__movie_title

    @property
    def director(self) -> Director:
        return self.__director

    @property
    def id(self) -> int:
        return self.__id

    @property
    def year(self) -> int:
        return self.__release_year

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

    def remove_actor(self, actor: Actor):
        actors_list = self.__actors
        if actor in actors_list:
            for i in range(len(actors_list) - 1, -1, -1):
                if actor == actors_list[i]:
                    actors_list.pop(i)
        self.__actors = actors_list

    def add_genre(self, genre: Genre):
        self.__genres.append(genre)

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


class TestMovie:

    def test_init(self):
        movie = Movie("Moana", 2016)
        assert repr(movie) == "<Movie Moana, 2016>"
        director = Director("Ron Clements")
        movie.director = director
        assert repr(movie.director) == "<Director Ron Clements>"
        actors = [Actor("Auli'i Cravalho"), Actor("Dwayne Johnson"), Actor("Rachel House"), Actor("Temuera Morrison")]
        for actor in actors:
            movie.add_actor(actor)
        assert repr(movie.actors) == "[<Actor Auli'i Cravalho>, <Actor Dwayne Johnson>, <Actor Rachel House>, <Actor Temuera Morrison>]"
        movie.remove_actor(Actor("Auli'i Cravalho"))
        assert repr(
            movie.actors) == "[<Actor Dwayne Johnson>, <Actor Rachel House>, <Actor Temuera Morrison>]"

        movie.runtime_minutes = 107
        assert repr(movie.runtime_minutes) == "107"
        # assert repr("Movie runtime: {} minutes".format(movie.runtime_minutes)) == "Movie runtime: 107 minutes"
