import configparser

DEMO_CONFIG_INI_FILE="demo-config.ini"

def demo_config():
    config=configparser.ConfigParser()
    config.read(DEMO_CONFIG_INI_FILE)

    print(config)
    print(config.sections()) #print sections without DEFAULT because it's default lol
    print(config['DEFAULT'])

    print(config['DEFAULT'].get("environ"))

    port=config["mysql"].get("port")
    print(port, repr(port)) #port in str view

    port = config["mysql"].getint("port")
    print(port, repr(port)) #port in int view
    port+=1
    print(port)

    config['mysql']["port"]=str(port) #change data
    config['files']["home"] = "/home/sasha" #add new data

    with open(DEMO_CONFIG_INI_FILE, "w") as f: #rewrite data in the file
        config.write(f)


def main():
    demo_config()

if __name__=="__main__":
    main()