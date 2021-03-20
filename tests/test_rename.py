import os
import tempfile
import pathlib

from renamer.rename import FileRenamer


class TestFileRenamer:

    @classmethod
    def setup_class(cls):
        cls.file_renamer = FileRenamer()

    def test_rename(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            src_file_path = os.path.join(tmpdir, 'file1.txt')
            dst_file_path = os.path.join(tmpdir, 'file2.txt')
            pathlib.Path(src_file_path).touch()

            self.file_renamer.rename(src_file_path, dst_file_path)

            assert os.path.exists(src_file_path) is False
            assert os.path.exists(dst_file_path) is True

    def test_name_as(self):
        case = ('./tmp/file1.jpg', 'file2')
        dst_path = self.file_renamer.name_as(case[0], case[1])

        assert dst_path == './tmp/file2.jpg'

    def test_get_file_path(self):
        case = './tmp/file1.jpg'
        dir_name, file_name, ext_name = self.file_renamer._get_file_path(case)

        assert (dir_name, file_name, ext_name) == ('./tmp', 'file1', '.jpg')
