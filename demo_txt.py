FILE_PATH="file.txt"

def main():
    #how to write
    f = open(FILE_PATH,'w')
    f.write("hello\n")
    f.close()

    #using a context manager (we don't need to close but can't write "==")
    with open(FILE_PATH,'w') as f:
        f.write("hello world\n")

    #how to read
    f=open(FILE_PATH,"r")
    print(f.readlines())
    f.close()

    with open(FILE_PATH,'r') as f:
        print(f.readlines())

    #how to append
    with open(FILE_PATH, 'a') as f:
        f.write("hello again\n")
        f.writelines(["cats\n", "dogs\n"])

    #how to read for lines
    with open(FILE_PATH, 'r') as f:
        for line in f:
            print(line, end="")
        print()

if __name__ == "__main__":
    main()
