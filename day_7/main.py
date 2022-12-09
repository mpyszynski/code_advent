from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class File:
    name: str
    size: int


@dataclass
class Directory:
    name: str
    sub_dir_found: Optional[bool] = False
    id: Optional[int] = 0
    parent_id: Optional[int] = 0
    files: Optional[List[File]] = field(default_factory=list)
    sub_dirs: Optional[List[Directory]] = field(default_factory=list)

    def mark_sub_dir_founded(self) -> None:
        self.sub_dir_found = True

    def update_dir(self, directory: Directory) -> None:
        for i, sub_dir in enumerate(self.sub_dirs):
            if sub_dir.parent_id == directory.parent_id and sub_dir.name == directory.name:
                self.sub_dirs[i] = directory
                return
            sub_dir.update_dir(directory)

    def files_size(self) -> int:
        size = 0
        for file in self.files:
            size += file.size
        return size

    def all_files_size_aggregated(self) -> int:
        size = self.files_size()
        for sub_dir in self.sub_dirs:
            size += sub_dir.all_files_size_aggregated()
        return size

    def directories_to_delete_size(self, max_size: int) -> int:
        size = 0
        own_files_size = self.all_files_size_aggregated()
        if own_files_size < max_size:
            size += own_files_size
        for sub_dir in self.sub_dirs:
            size += sub_dir.directories_to_delete_size(max_size)
        return size

    def all_dirs_size_list(self) -> List[int]:
        sizes = [self.all_files_size_aggregated()]
        for sub_dir in self.sub_dirs:
            sizes.extend(sub_dir.all_dirs_size_list())
        return sizes

    def get_directory_to_delete(self, max_size: int, need_space: int):
        dir_sizes = self.all_dirs_size_list()
        dir_sizes.sort(reverse=True)
        the_biggest_dir = dir_sizes[0]
        free_space = max_size - the_biggest_dir
        dirs_to_delete = [directory for directory in dir_sizes if free_space + directory > need_space]
        return dirs_to_delete[len(dirs_to_delete) - 1]


def new_file(file_info: str) -> File:
    f = file_info.split(" ")
    return File(f[1], int(f[0]))


def is_file(val: str) -> bool:
    return val[0].isdigit()


def is_dir(val: str) -> bool:
    if "dir" in val:
        return True
    return False


def is_cd_command(val: str) -> bool:
    if "$ cd" in val:
        return True
    return False


def is_return_command(val: str) -> bool:
    if ".." in val:
        return True
    return False


def get_dir_name(command: str) -> str:
    split_command = command.split(" ")
    return split_command[len(split_command) - 1]


def new_directory(dir_id: int, dir_content: List[str], parent_id: int = 0) -> Directory:
    directory = Directory(
        name=get_dir_name(dir_content[0]),
        id=dir_id,
        parent_id=parent_id,
        files=[],
        sub_dirs=[]
    )
    for content in dir_content[1:]:
        if is_file(content):
            directory.files.append(new_file(content))
        if is_dir(content):
            directory.sub_dirs.append(Directory(
                parent_id=dir_id,
                name=get_dir_name(content)
            ))
    return directory


def find_parent_id(dirs: List[Directory], dir_name: str) -> int:
    for directory in reversed(dirs):
        for sub_dir in directory.sub_dirs:
            if sub_dir.name == dir_name:
                if not sub_dir.sub_dir_found:
                    sub_dir.mark_sub_dir_founded()
                    return sub_dir.parent_id
    return 0


def add_dir(dir_id: int, dir_content: List[str], dirs: List[Directory]) -> None:
    parent_id = find_parent_id(dirs, get_dir_name(dir_content[0]))
    dirs.append(new_directory(dir_id, dir_content, parent_id))


def match_directories(directories: List[Directory]) -> Directory:
    main_dir = directories[0]
    for directory in directories[1:]:
        main_dir.update_dir(directory)
    return main_dir


def handle_cd_command(command: str, dir_id: int, dir_content: List[str], dirs: List[Directory]) -> List[str]:
    if is_return_command(command):
        return handle_return_command(dir_id, dir_content, dirs)

    if "/" in command or len(dir_content) == 0:
        dir_content.append(command)
        return dir_content

    add_dir(dir_id, dir_content, dirs)
    return [command]


def handle_return_command(dir_id: int, dir_content: List[str], dirs: List[Directory]) -> List[str]:
    if len(dir_content) == 0:
        return []
    add_dir(dir_id, dir_content, dirs)
    return []


def new_filetree(filesystem: List[str]) -> Directory:
    dir_content = []
    dirs = []
    for i, line in enumerate(filesystem):
        if is_cd_command(line):
            dir_content = handle_cd_command(line, i, dir_content, dirs)
            continue
        dir_content.append(line)
        if i + 1 == len(filesystem):
            add_dir(i, dir_content, dirs)

    filetree = match_directories(dirs)
    return filetree


def get_input_data(source: str) -> List[str]:
    f = open(source, "r")
    content = []
    for line in f:
        content.append(line.strip())
    f.close()
    return content


def main():
    data = get_input_data("./input.txt")
    directory = new_filetree(data)
    print(directory)
    dirs_to_delete_size = directory.directories_to_delete_size(100000)
    dir_to_delete_size = directory.get_directory_to_delete(70000000, 30000000)

    print(f"Directories size to delete {dirs_to_delete_size}")
    print(f"Smallest directory to delete has size {dir_to_delete_size}")


if __name__ == '__main__':
    main()
