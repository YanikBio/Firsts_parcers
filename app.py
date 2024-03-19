import requests
from abc import ABC, abstractmethod

class AbstractParser(ABC):
    @abstractmethod  # заставляет иметь реализацию этого метода в каждом дочернем классе
    def _parse(self):
        ...

    @abstractmethod
    def _query_params():
        ...


class BaseParser:
    __storage: list | None = None  # аннотация говорит, что это или лист или None

    def __init__(self, url: str, query: str = None) -> None:
        self._url = url  # одно подчёркивание - лишь в рамках дочерникх классов можем исп.
        self._query = query

    def _get_data(self):
        url, params = self._query_params()
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.text

    def start(self):
        html = self._get_data()
        self.__storage = self._parse()

    def save(self):
        ...

    def __iter__(self):
        if isinstance(self.__storage, list):
            self._cursor = 0
            return self
        raise TypeError(f"{self.__class__.__name__} object is not iterable")

    def __next__(self):
        try:
            return self.__storage[self._cursor]
        except IndexError:
            raise StopIteration
        finally:
            self._cursor += 1


class Olx(BaseParser, AbstractParser):
    def _parse(self):
        ...

    def _query_params(self):
        return self._url.format(self._query), None


class Allegro(BaseParser, AbstractParser):
    def _parse(self):
        ...

    def _query_params(self):
        return self._url, {"string": self._query}


class Django(BaseParser, AbstractParser):
    def _parse(self):
        ...

    def _query_params(self):
        return self._url, {"q": self._query}


if __name__ == "__main__":
    olx = Olx("https://www.olx.pl/oferty/q-{}/", "sport")
    olx.start()
    olx.save()
    for obj in olx:
        if obj:
            print(obj)

    dj = Django("https://docs.djangoproject.com/en/5.0/search/", "sport")