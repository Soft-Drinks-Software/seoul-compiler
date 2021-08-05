import time

filename = input("Provide a valid .seoul file")

print("Running on Seoul Compiler v1\n")

seoul_properties = {
    "seoul[__version__]": "1.0.0",
    "seoul[__author__]": "threesodas",
    "seoul[__license__]": "idk"
}

if ".seoul" not in filename:
    print("Please provide a valid .seoul file!")
    exit()

with open(filename) as content:
    try:
        start = time.time()

        for line in content:
            if "sys << " in line:
                if line[7:] in list(seoul_properties.keys()):
                    print(seoul_properties[line[7:]])
                else:
                    print(">> " + line[7:].replace("\"", ""))

        end = time.time()

        print(f"Process finished in {int(start - end)}ms")
    except FileNotFoundError:
        print("File not found!")
