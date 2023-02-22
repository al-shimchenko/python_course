import os

# uppercase variables are constants

IS_MAC = "posix" in os.name
BASE_DIR = os.path.dirname(__file__)


def demo_paths():
    print(__file__)  # print the current dir
    print(os.name)  # code word for os
    print("base dir", BASE_DIR)  # dir of the current file
    print("is mac?", IS_MAC)
    print("os path sep:", os.path.sep)  # print a classic separator for the os

    folder_name = "pictures"
    file_name = "cat.jpg"
    print("|".join(("foo", "bar")))  # using the separator
    print(os.path.sep.join((BASE_DIR, folder_name, file_name)))  # dir + new folder + new file
    print(os.path.join(BASE_DIR, folder_name, file_name))  # same


def demo_cwd():
    # get current working directory
    cwd = os.getcwd()
    print("cwd:", cwd)  # same as the BASE_DIR in this case


def demo_list_dir():
    # the list of directories
    print(os.listdir("."))  # point is our directory - listdir cwd
    print(os.listdir(".idea"))
    if os.path.isdir("qwerty"):
        print(os.listdir("qwerty"))  # print if we have "qwerty" in the list of directories
    if os.path.isfile(__file__):
        print("Sure we have the current file!)")

    file_name = "file.txt"

    if os.path.isfile(file_name):
        os.unlink(file_name)  # same as remove

    with open(file_name, "w") as f:  # creating a new file and writing a text
        f.write("hello\n")
        f.writelines(["world\n", "fizz\n", "buzz\n"])  # the list of lines

    with open(file_name, "r") as f:
        print(f.readlines())


def main():
    print("hello")
    demo_paths()
    demo_cwd()
    demo_list_dir()


# the right way to call a function
if __name__ == '__main__':
    main()
