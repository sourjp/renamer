import tempfile
import pathlib
import os

from renamer.search import FileSearcher


class TestFileSearcher:

    @classmethod
    def setup_class(cls):
        cls.file_searcher = FileSearcher()

    def test_search(self):
        with tempfile.TemporaryDirectory() as tempdir:
            file1_path = os.path.join(tempdir, 'file1.txt')
            file2_path = os.path.join(tempdir, 'tmp', 'file2.txt')
            os.makedirs(os.path.join(tempdir, 'tmp'))
            pathlib.Path(file1_path).touch()
            pathlib.Path(file2_path).touch()

            key = os.path.join(tempdir, '**')
            result = self.file_searcher.search(key)
            assert result == [file1_path]

    def test_search_recursive(self):
        with tempfile.TemporaryDirectory() as tempdir:
            file1_path = os.path.join(tempdir, 'file1.txt')
            file2_path = os.path.join(tempdir, 'tmp', 'file2.txt')
            os.makedirs(os.path.join(tempdir, 'tmp'))
            pathlib.Path(file1_path).touch()
            pathlib.Path(file2_path).touch()

            key = os.path.join(tempdir, '**')
            result = self.file_searcher.search(key, recursive=True)
            assert result == [file1_path, file2_path]
