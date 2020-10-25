from domainmodel.movie import Movie
from domainmodel.review import Review
from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director

class User:
    def __init__(self, user_name: str):
        self.__user_name = user_name.strip().lower()
        self.__watched_movies = []
        self.__reviews = []
        self.__time_spent_watching_movies_minutes = 0

    @property
    def user_name(self) -> str:
        return self.__user_name

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
        return f"<User {self.__user_name}>"

    def __eq__(self, other):
        return self.user_name == other.user_name

    def __lt__(self, other):
        return self.user_name < other.user_name

    def __hash__(self):
        return hash(self.user_name)

    def watch_movie(self, movie: Movie):
        self.__watched_movies.append(movie)
        self.__time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review: Review):
        self.__reviews.append(review)

    def update_last_review(self, review: Review):
        self.__reviews[-1] = review


#     def get_recommendation_score(self, movie):
#
#         if len(self.__watched_movies) < 5:
#             return None
#         else:
#             # Generate proportion of watched movie_library with common genres, actors and directors with the movie in question
#             genre_numerator = 0
#             actor_numerator = 0
#             director_numerator = 0
#
#             genre_denominator = sum(self.__watched_genres.values())
#             actor_denominator = sum(self.__watched_actors.values())
#             director_denominator = sum(self.__watched_directors.values())
#
#             for genre in movie.genres:
#                 if genre in self.__watched_genres:
#                     genre_numerator += self.__watched_genres[genre]
#             for actor in movie.actors:
#                 if actor in self.__watched_actors:
#                     actor_numerator += self.__watched_actors[actor]
#
#             if movie.director in self.__watched_directors:
#                 director_numerator += self.__watched_directors[movie.director]
#
#             # Take the average
#             watched_score = (actor_numerator / actor_denominator + director_numerator / director_denominator + genre_numerator / genre_denominator) / 3
#
#         # Only consider reviews when there is a sufficient sample size
#         if len(self.__reviews) >= 10:
#             genre_rating = []
#             actor_rating = []
#             director_rating = []
#             for r in self.__reviews:
#                 for genre in r.movie.genres:
#                     if genre in movie.genres:
#                         genre_rating.append(r.rating)
#                 for actor in r.movie.actors:
#                     if actor in movie.actors:
#                         actor_rating.append(r.rating)
#                 if r.movie.director == movie.director:
#                     director_rating.append(r.rating)
#
#             review_score = (sum(genre_rating) / (len(genre_rating) * 10) + sum(actor_rating) / (
#                         len(actor_rating) * 10) + sum(director_rating) / (len(director_rating) * 10)) / 3
#
#             return (watched_score + review_score) / 2
#         else:
#             return watched_score
#
#     def visualise_stats(self):
#         print("************************************")
#         print("****** YOUR STATS AT A GLANCE ******")
#         print("************************************")
#         print()
#
#         if len(self.__watched_movies) > 0:
#             print(self.user_name, ", we've spent many great times together! Here's exactly how many:", sep="")
#             print()
#             print("Number of movie_library watched on CS235Flix:", len(self.watched_movies))
#             print("Time spent watching on CS235Flix:", self.__time_spent_watching_movies_minutes, "minutes")
#             print()
#
#             print("We have laughed and cried together, but mainly:")
#             print()
#             for genre in self.__watched_genres:
#                 print(genre.genre_name, ": ", self.__watched_genres[genre], sep="")
#             print()
#
#             print("And you know, we always have your favorites.")
#             print()
#             print("Actors:")
#             print()
#             for actor in self.__watched_actors:
#                 print(actor.actor_full_name, ": ", self.__watched_actors[actor], sep="")
#             print()
#             print("Directors:")
#             print()
#             for director in self.__watched_directors:
#                 print(director.director_full_name, ": ", self.__watched_directors[director], sep="")
#             print()
#
#             print("We've been so lucky to share this time with you. Thank you for choosing CS235Flix!")
#         else:
#             print("Thank you for joining CS235Flix!")
#             print()
#             print("Number of movie_library watched on CS235Flix:", len(self.watched_movies))
#             print("Time spent watching on CS235Flix:", self.__time_spent_watching_movies_minutes, "minutes")
#             print()
#             print("Watch more of our great shows and movie_library to view your interesting stats!")
#
# class TestUser:
#     def test_init(self):
#         user1 = User('Martin', 'pw12345')
#         assert repr(user1) == "<User martin>"
#
#     def test_get_recommendation_score(self):
#         movie1 = Movie("Once Upon a Time in Hollywood",
#                        release_year = 2019,
#                        actors = [Actor("Brad Pitt"), Actor("Leonardo DiCaprio"), Actor("Margot Robbie")],
#                        director = Director("Quentin Tarantino"),
#                        genres = [Genre("Comedy"), Genre("Drama")],
#                        runtime_minutes = 60
#                        )
#
#         movie2 = Movie("Happy Friends",
#                        release_year=2009,
#                        actors=[Actor("James Doe"), Actor("Bob Lee"), Actor("Margot Robbie")],
#                        director=Director("John Tino"),
#                        genres=[Genre("Crime"), Genre("Drama")],
#                        runtime_minutes=120
#                        )
#
#         movie3 = Movie("Happy Friends 2",
#                        release_year=2011,
#                        actors=[Actor("James Doe"), Actor("Bob Lee")],
#                        director=Director("John Tino"),
#                        genres=[Genre("Crime"), Genre("Drama")],
#                        runtime_minutes=120
#                        )
#
#         movie4 = Movie("Hello World",
#                        release_year=2009,
#                        actors=[Actor("Cathy Tiffin"), Actor("Sara Boaton"), Actor("Misty Turnton")],
#                        director=Director("Rita Sanson"),
#                        genres=[Genre("Comedy"), Genre("Thriller")],
#                        runtime_minutes=60
#                        )
#
#         movie5 = Movie("Krish",
#                        release_year=2009,
#                        actors=[Actor("Aishwarya Rai"), Actor("Hrithik Roshan"), Actor("Misty Turnton")],
#                        director=Director("Karan Johar"),
#                        genres=[Genre("Action"), Genre("Bollywood")],
#                        runtime_minutes=180
#                        )
#
#         movie6 = Movie("Kabhi Khushi Kabhie Gham",
#                        release_year=2001,
#                        actors=[Actor("Hrithik Roshan"), Actor("Shahrukh Khan"), Actor("Kajol"), Actor("Amitabh Bachchan")],
#                        director=Director("Karan Johar"),
#                        genres=[Genre("Drama"), Genre("Bollywood")],
#                        runtime_minutes=200
#                        )
#
#         movie7 = Movie("Mohabbatein",
#                        release_year=2001,
#                        actors=[Actor("Aishwarya Rai"), Actor("Shahrukh Khan"), Actor("Amitabh Bachchan")],
#                        director=Director("Karan Johar"),
#                        genres=[Genre("Drama"), Genre("Bollywood"), Genre("Romance")],
#                        runtime_minutes=180
#                        )
#
#         movie8 = Movie("Pulp Fiction",
#                        release_year=1999,
#                        actors=[Actor("Uma Thurman"), Actor("Samuel L. Jackson"), Actor("John Travolta")],
#                        director=Director("Quentin Tarantino"),
#                        genres=[Genre("Comedy"), Genre("Crime")],
#                        runtime_minutes=100
#                        )
#
#         movie9 = Movie("Kill Bill",
#                        release_year=1999,
#                        actors=[Actor("Uma Thurman"), Actor("Samuel L. Jackson"), Actor("Vivica A. Fox")],
#                        director=Director("Quentin Tarantino"),
#                        genres=[Genre("Action")],
#                        runtime_minutes=150
#                        )
#
#         movie10 = Movie("Barfi",
#                         release_year=2020,
#                         actors=[Actor("Ranbir Kapoor"), Actor("Priyanka Chopra")],
#                         director=Director("Anurag Basu"),
#                         genres=[Genre("Romance"), Genre("Bollywood")],
#                         runtime_minutes=120
#                         )
#
#
#         user1 = User('Martin', 'pw12345')
#         assert user1.get_recommendation_score(movie1) == None
#         user1.watch_movie(movie2)
#         assert user1.get_recommendation_score(movie1) == None
#         user1.watch_movie(movie3)
#         user1.watch_movie(movie4)
#         user1.watch_movie(movie5)
#         user1.watch_movie(movie6)
#         assert user1.get_recommendation_score(movie1)
#         user1.watch_movie(movie7)
#         user1.watch_movie(movie8)
#         user1.watch_movie(movie9)
#         assert user1.get_recommendation_score(movie10)
#         assert user1.get_recommendation_score(movie1)
#         user1.add_review(Review(movie2, ))
#
