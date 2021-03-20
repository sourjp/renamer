from collections import namedtuple
import os

from renamer.search import Searcher, FileSearcher
from renamer.rename import Renamer, FileRenamer

DISPLAY_MESSAGE = 'Candidate to rename files (before ---> after).'

Candidate = namedtuple('Candidate', ['src', 'dst'])


class Operator:
    """Operator get candidates and rename files.

    >>> operator = Operator(Searcher, Renamer)
    # Get files list.
    >>> files = operator.get_files(src_dir)
    # Get name mapping src and dst files.
    >>> candidates = operator.get_candidates(files)
    # Rename src to dst files.
    >>> operator.rename(candidates)
    """

    def __init__(self, searcher: Searcher, renamer: Renamer):
        self.searcher: Searcher = searcher
        self.renamer: Renamer = renamer

    def get_files(self,
                  src_dir: str,
                  regex: str = '**',
                  recursive: bool = False) -> list[str]:
        key = os.path.join(src_dir, regex)
        return self.searcher.search(key, recursive=recursive)

    def get_candidates(self,
                       files: list[str],
                       start: int = 1,
                       digit: int = 3) -> list[Candidate]:
        """Create mapping src and dst path.

        Args:
            files : Src files list.
            start : Define start number to count like 001, 002.
            digit : To create file name like 001, 002.

        Returns:
            Mapping src and dst path like [Candidate('a.txt', '001.txt')]
        """
        candidates: list[Candidate] = []
        for index, src_file_path in enumerate(files, start=start):
            dst_file_name = str(index).zfill(digit)
            dst_file_path = self.renamer.name_as(src_file_path, dst_file_name)
            candidates.append(Candidate(src_file_path, dst_file_path))
        return candidates

    def display(self, candidates: list[Candidate]) -> None:
        print(DISPLAY_MESSAGE)
        print('~' * len(DISPLAY_MESSAGE))
        for index, candidate in enumerate(candidates):
            print(f'{index}: {candidate.src} ---> {candidate.dst}')

    def rename(self, candidates: list[Candidate]) -> None:
        for candidate in candidates:
            self.renamer.rename(candidate.src, candidate.dst)


def operator(src_dir: str, index: int, recursive: bool) -> None:
    operator = Operator(FileSearcher(), FileRenamer())
    files = operator.get_files(src_dir, recursive=recursive)
    candidates = operator.get_candidates(files, start=index)
    operator.display(candidates)

    if not candidates:
        print('No candidate files to rename.')
        return

    while True:
        ok = input('Rename files? [y/N]: ')
        if ok in ('y', 'yes', 'Y'):
            break
        elif ok in ('n', 'no', 'N'):
            print('Cancelled.')
            return
    operator.rename(candidates)
    print('Done!')
