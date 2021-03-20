import os
import pathlib

from renamer.rename import FileRenamer


class TestFileRenamer:

    @classmethod
    def setup_class(cls):
        cls.file_renamer = FileRenamer()

    def test_rename(self, tmpdir):
        src_file_path = os.path.join(tmpdir, 'file1.txt')
        dst_file_path = os.path.join(tmpdir, 'file2.txt')
        pathlib.Path(src_file_path).touch()
        self.file_renamer.rename(src_file_path, dst_file_path)
        assert os.path.exists(src_file_path) is False
        assert os.path.exists(dst_file_path) is True

    def test_name_as(self):
        test_case = {
            'src': './tmp/file1.jpg',
            'dst': 'file2',
            'want': './tmp/file2.jpg'}
        dst_path = self.file_renamer.name_as(test_case['src'],
                                             test_case['dst'])
        assert dst_path == test_case['want']

    def test_get_file_path(self):
        test_case = {
            'file': './tmp/file1.jpg',
            'want': ('./tmp', 'file1', '.jpg')}

        dir_name, file_name, ext_name = self.file_renamer._get_file_path(
            test_case['file'])
        assert (dir_name, file_name, ext_name) == test_case['want']
