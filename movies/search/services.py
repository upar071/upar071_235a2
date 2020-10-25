from movies.adapters.repository import AbstractRepository
from movies.domain.domainmodel import make_review, Movie, Review, Actor, Director, Genre

def search_exists(search, select, repo: AbstractRepository):

    if select == "Actor":
        if Actor(search) not in repo.get_actors():
            return False
        else:
            return True

    elif select == "Genre":
        if Genre(search) not in repo.get_genres():
            return False
        else:
            return True

    elif select == "Director":
        if Director(search) not in repo.get_directors():
            return False
        else:
            return True
