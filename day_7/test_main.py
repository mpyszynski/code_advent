from unittest import TestCase
from copy import deepcopy
from main import new_directory, Directory, File, new_filetree, new_file, is_file, is_dir, is_cd_command, \
    is_return_command, get_dir_name

test_dir = Directory(
    name='/',
    sub_dir_found=False,
    id=6,
    parent_id=0,
    files=[File(name='b.txt', size=14848514), File(name='c.dat', size=8504156)],
    sub_dirs=[
        Directory(
            name='a',
            sub_dir_found=False,
            id=12,
            parent_id=6,
            files=[File(name='f', size=29116), File(name='g', size=2557), File(name='h.lst', size=62596)],
            sub_dirs=[
                Directory(
                    name='e',
                    sub_dir_found=False,
                    id=15,
                    parent_id=12,
                    files=[File(name='i', size=584)],
                    sub_dirs=[]
                )
            ]
        ),
        Directory(
            name='d',
            sub_dir_found=False,
            id=24,
            parent_id=6,
            files=[File(name='j', size=4060174),
                   File(name='d.log', size=8033020),
                   File(name='d.ext', size=5626152),
                   File(name='k', size=7214296)],
        )
    ]
)

test_dir_extended = deepcopy(test_dir)
test_dir_extended.sub_dirs[1].sub_dirs = [
    Directory(
        name='d',
        sub_dir_found=False,
        id=26,
        parent_id=24,
        files=[File(name='l', size=4060174)],
        sub_dirs=[]
    )
]

the_smallest_test_dir = Directory(
    name='e',
    sub_dir_found=False,
    id=15,
    parent_id=12,
    files=[File(name='i', size=584)],
    sub_dirs=[]
)

medium_test_dir = Directory(
    name='a',
    sub_dir_found=False,
    id=12,
    parent_id=6,
    files=[File(name='f', size=29116), File(name='g', size=2557), File(name='h.lst', size=62596)],
    sub_dirs=[
        Directory(
            name='e',
            sub_dir_found=False,
            id=15,
            parent_id=12,
            files=[File(name='i', size=584)],
            sub_dirs=[]
        )
    ]
)


class Test(TestCase):
    def test_new_filetree(self):
        filesystem = [
            "$ cd /",
            "$ ls",
            "dir a",
            "14848514 b.txt",
            "8504156 c.dat",
            "dir d",
            "$ cd a",
            "$ ls",
            "dir e",
            "29116 f",
            "2557 g",
            "62596 h.lst",
            "$ cd e",
            "$ ls",
            "584 i",
            "$ cd ..",
            "$ cd ..",
            "$ cd d",
            "$ ls",
            "4060174 j",
            "8033020 d.log",
            "5626152 d.ext",
            "7214296 k",
            "dir d",
            "$ cd d",
            "$ ls",
            "4060174 l",
        ]
        expected_result = test_dir_extended
        directory = new_filetree(filesystem)
        assert directory == expected_result, f"Unexpected result, wanted {expected_result}, got \n {directory}"

    def test_mark_sub_dir_founded(self):
        directory = deepcopy(the_smallest_test_dir)
        directory.mark_sub_dir_founded()
        assert directory.sub_dir_found

    def test_update_dir(self):
        directory = deepcopy(the_smallest_test_dir)
        directory.sub_dirs.append(Directory(
            name="sub_dir1",
            parent_id=15
        ))
        new_dir = Directory(
            id=17,
            parent_id=15,
            name="sub_dir1",
            files=[File(name="sub_dir1_file1", size=100)]
        )
        directory.update_dir(new_dir)
        assert directory.sub_dirs[0].files == [File(name="sub_dir1_file1", size=100)]
        assert directory.sub_dirs[0].id == 17

    def test_update_dir_subdir(self):
        directory = deepcopy(medium_test_dir)
        sub_dir = directory.sub_dirs[0]
        sub_dir.sub_dirs.append(Directory(
            name="sub_dir1",
            parent_id=15
        ))
        new_dir = Directory(
            id=17,
            parent_id=15,
            name="sub_dir1",
            files=[File(name="sub_dir1_file1", size=100)]
        )
        directory.update_dir(new_dir)
        assert directory.sub_dirs[0].sub_dirs[0].files == [File(name="sub_dir1_file1", size=100)]
        assert directory.sub_dirs[0].sub_dirs[0].id == 17

    def test_files_size(self):
        directory = deepcopy(test_dir)
        res = directory.files_size()
        exp_res = 23352670
        assert res == exp_res, f"Unexpected result, got {res}, expected {exp_res}"

    def test_all_files_size_aggregated(self):
        directory = deepcopy(test_dir)
        res = directory.all_files_size_aggregated()
        exp_res = 48381165
        assert res == exp_res, f"Unexpected result, got {res}, expected {exp_res}"

    def test_directories_to_delete_size(self):
        test_cases = [
            {
                "directory": deepcopy(test_dir),
                "exp_res": 95437
            },
            {
                "directory": deepcopy(the_smallest_test_dir),
                "exp_res": 584
            },
            {
                "directory": deepcopy(medium_test_dir),
                "exp_res": 95437
            },
        ]
        for case in test_cases:
            directory = case["directory"]

            res = directory.directories_to_delete_size(100000)
            assert res == case["exp_res"], f"Unexpected result, got {res}, expected {case['exp_res']}"

    def test_all_dirs_size_list(self):
        directory = deepcopy(test_dir)
        size_list = directory.all_dirs_size_list()
        assert size_list == [48381165, 94853, 584, 24933642]

    def test_get_directory_to_delete(self):
        directory = deepcopy(test_dir)
        dir_to_delete_size = directory.get_directory_to_delete(70000000, 30000000)
        exp_res = 24933642
        assert dir_to_delete_size == exp_res, f"Unexpected res, wanted {exp_res}, got {dir_to_delete_size}"

    def test_new_file(self):
        file_details = "100 file.rar"
        f = new_file(file_details)
        assert f.size == 100
        assert f.name == "file.rar"

    def test_is_file(self):
        test_cases = [
            {"input": "100 file.rar", "exp_res": True},
            {"input": "dir dir_name", "exp_res": False},
        ]
        for case in test_cases:
            res = is_file(case["input"])
            assert res == case["exp_res"]

    def test_is_dir(self):
        test_cases = [
            {"input": "100 file.rar", "exp_res": False},
            {"input": "dir dir_name", "exp_res": True},
        ]
        for case in test_cases:
            res = is_dir(case["input"])
            assert res == case["exp_res"]

    def test_is_cd_command(self):
        test_cases = [
            {"input": "100 file.rar", "exp_res": False},
            {"input": "dir dir_name", "exp_res": False},
            {"input": "$ cd dir_name", "exp_res": True},
        ]
        for case in test_cases:
            res = is_cd_command(case["input"])
            assert res == case["exp_res"]

    def test_is_return_command(self):
        test_cases = [
            {"input": "$ cd dir_name", "exp_res": False},
            {"input": "$ cd ..", "exp_res": True},
        ]
        for case in test_cases:
            res = is_return_command(case["input"])
            assert res == case["exp_res"]

    def test_get_dir_name(self):
        test_cases = [
            {"input": "$ cd dir_name", "exp_res": "dir_name"},
            {"input": "dir dir_name", "exp_res": "dir_name"},
        ]
        for case in test_cases:
            res = get_dir_name(case["input"])
            assert res == case["exp_res"]
