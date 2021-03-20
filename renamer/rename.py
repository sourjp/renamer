from abc import ABC, abstractmethod
import os


class Renamer(ABC):

    @abstractmethod
    def rename(self, src_item: str, dst_item: str) -> None:
        pass

    @abstractmethod
    def name_as(self, src_item: str, dst_name: str) -> str:
        pass


class FileRenamer(Renamer):

    def rename(self, src_file: str, dst_file: str) -> None:
        if os.path.exists(dst_file):
            print(f'Skip rename duplicate file: {dst_file}')
            return
        os.rename(src_file, dst_file)

    def name_as(self, src_path: str, dst_base: str) -> str:
        src_dir, _, src_ext = self._get_file_path(src_path)
        dst_file_name = os.path.join(src_dir, dst_base + src_ext)
        return dst_file_name

    def _get_file_path(self, file: str) -> tuple[str, str, str]:
        dir_name = os.path.dirname(file)
        base_name = os.path.basename(file)
        file_name, ext_name = os.path.splitext(base_name)
        return dir_name, file_name, ext_name
