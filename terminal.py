line = input("Welcome to the Seoul Terminal! Please write your command down below.\n")

seoul_properties = {
    "seoul[__version__]": "1.0.0",
    "seoul[__author__]": "threesodas",
    "seoul[__license__]": "idk"
}

if line.startswith("sys << "):
    if line[7:].startswith("seoul[") and not line[7:].startswith("\""):
        print(f">> {seoul_properties[line[7:]]}")
    else:
        print(">> " + line[7:].replace("\"", ""))
elif line.startswith("throw << "):
    raise Exception(line[9:])
elif line.startswith("endthesuffering"):
    exit()