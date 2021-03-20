import tempfile
import pathlib
import os
import shutil

from renamer.search import FileSearcher


class TestFileSearcher:

    @classmethod
    def setup_class(cls):
        cls.file_searcher = FileSearcher()
        cls.tmpdir = tempfile.mkdtemp()
        cls.file1_path = os.path.join(cls.tmpdir, 'file1.txt')
        cls.file2_path = os.path.join(cls.tmpdir, 'tmp', 'file2.txt')
        cls.keyword = os.path.join(cls.tmpdir, '**')

        os.makedirs(os.path.join(cls.tmpdir, 'tmp'))
        pathlib.Path(cls.file1_path).touch()
        pathlib.Path(cls.file2_path).touch()

    @classmethod
    def teardown_class(cls):
        shutil.rmtree(cls.tmpdir)

    def test_search(self):
        result = self.file_searcher.search(self.keyword)
        assert result == [self.file1_path]

    def test_search_recursive(self):
        result = self.file_searcher.search(self.keyword, recursive=True)
        assert result == [self.file1_path, self.file2_path]

    def test_select_file(self):
        test_case = {
            'files': [
                os.path.join(self.tmpdir, 'file1.txt'),
                os.path.join(self.tmpdir, 'tmp')],
            'want': [
                os.path.join(self.tmpdir, 'file1.txt')]}

        result = self.file_searcher._select_file(test_case['files'])
        assert result == test_case['want']
