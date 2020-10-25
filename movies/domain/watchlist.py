from domainmodel.movie import Movie

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

