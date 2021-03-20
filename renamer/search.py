from abc import ABC, abstractmethod
from collections.abc import Callable
import glob
import os


class Searcher(ABC):

    @abstractmethod
    def search(self, key: str, recursive: bool) -> list[str]:
        pass


class FileSearcher(Searcher):

    def __init__(self):
        self.filters: list[Callable] = [self._select_file]

    def search(self,
               key: str,
               recursive: bool = False) -> list[str]:
        # Sorted items are easier to adjust numbering.
        globed = sorted(glob.glob(key, recursive=recursive))
        for func in self.filters:
            globed = func(globed)
        return globed

    def _select_file(self, data: list[str]) -> list[str]:
        selected: list[str] = []
        for item in data:
            if os.path.isfile(item):
                selected.append(item)
        return selected
