# import pathlib
from pathlib import Path


def demo_cwd():
    cwd = Path.cwd()
    print("cwd:", cwd)  # current work dir

    print('file:', repr(Path(__file__)))  # WindowsPath view
    print("file:", repr(__file__))  # srt view

    for path in cwd.iterdir():  # dirs of files (names)
        print(path.name, path.is_dir(), path.is_file())


def demo_home():
    print(Path.home())
    home = Path.home()

    for path in home.iterdir():  # print home files and dirs
        print(path.name)


def demo_check_existence():
    users = Path("/Users")
    print(users)
    print('exists?', users.exists())  # print False but idk bc it's True...

    cats = Path("/Cats")
    print('cats exists?', cats.exists())
    cats.unlink(missing_ok=True)  # if we haven't the folder it'll be ok


def demo_file_path():
    print("__file__", __file__)  # current file path
    current_file = Path(__file__)
    print(repr(current_file))
    base_dir = current_file.parent
    print(base_dir)
    print(base_dir.parent)  # parent of parent
    print(list(base_dir.parents))  # all parents


def demo_build_path():
    current_file = Path(__file__)
    base_dir = current_file.parent

    folder_name = "pictures"
    file_name = "cats.jpg"

    cats_filepath = base_dir / folder_name / file_name  # to build a path we use "/" but this file doesn't exist
    print(cats_filepath)

    cats_pic_filepath = base_dir.joinpath(folder_name, file_name)
    print(repr(cats_pic_filepath))
    print("eq?", cats_pic_filepath == cats_filepath)  # yeah

    print("suffix:", cats_filepath.suffix)  # the end of file (.jpg)
    print("name:", cats_filepath.name)  # name+suffix
    print("stem:", cats_filepath.stem)  # name before a suffix
    print("anchor:", cats_filepath.anchor)  # how we build a path


def demo_files():
    filename = "file.txt"
    file = Path(filename)
    print(repr(file))

    file = file.resolve()  # full way to file
    print(repr(file))

    file.unlink(missing_ok=True)  # delete
    file.write_text("hello\n")  # write
    print(file.read_text())  # read


def main():
    demo_cwd()
    demo_home()
    demo_check_existence()
    demo_file_path()
    demo_build_path()
    demo_files()


if __name__ == "__main__":
    main()
