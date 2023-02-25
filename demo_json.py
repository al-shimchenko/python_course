import json

JSON_FILE_PATH = "file.json"
JSON_LINES_FILE_PATH = "file.jl" #jl ia json lines

#how to create a string from a python object
def demo_json_dump_to_string():
    data = {
        "users":[
            {
                "id": 42,
                "username": "john",
            },
            {
                "id": 11,
                "username": "sam",
            },
        ],
    }
    print(data)
    print(type(data))
    print((data["users"]))

    data_string=json.dumps(data)

    print(type(data_string))
    print(data_string)

#how to create a python object from a string
def demo_json_load_string():
    data_string = '{"users": [{"id": 42, "username": "john"}, {"id": 11, "username": "sam"}]}'
    print(data_string)

    data = json.loads(data_string)

    print(data)
    print(type(data))
    print((data["users"]))

def demo_json_dump_and_load_to_file():
    data = {
        "users": [
            {
                "id": 42,
                "username": "john",
            },
            {
                "id": 11,
                "username": "sam",
            },
        ],
    }

    #data_string=json.dumps(data)
    with open(JSON_FILE_PATH, "w") as f:
        json.dump(data, f,indent=2) #we can do it shorter with this function and "indent" can slice the text from 1 str to normal format
        #f.write(data_string)
    with open(JSON_FILE_PATH, "r") as f:
        data_from_file = json.load(f)

    print(data_from_file)
    print(type(data_from_file)) #dict

    print(data_from_file["users"]) #print the data from dict

#every str ia a separated json object
def demo_json_lines():
    user1={"id": 1, "name": "John", "friends": [2,3]}
    user2 = {"id": 2, "name": "Sam", "friends": [1]}
    user3 = {"id": 3, "name": "Nick", "friends": [1]}

    with open(JSON_LINES_FILE_PATH,"a") as f:
    #with open(JSON_LINES_FILE_PATH, "w") as f:
        for user_data in [user1, user2, user3]:
            json.dump(user_data,f)
            f.write("\n")

    with open(JSON_LINES_FILE_PATH, "r") as f:
        for line in f:
            if not line:
                continue #we need to ignore empty strings
            user_data=json.loads(line)
            print("user data:", user_data)
            print("id:", user_data["id"],"name:", user_data["name"])

def main():
    demo_json_dump_to_string()
    demo_json_load_string()
    demo_json_dump_and_load_to_file()
    demo_json_lines()

if __name__ == "__main__":
    main()
