import time
import os

print("Running on Seoul Compiler v1\n")
filename = input("Provide a valid .seoul file\n")


seoul_properties = {
    "seoul[__version__]": "1.0.0",
    "seoul[__author__]": "threesodas",
    "seoul[__license__]": "idk"
}


if ".seoul" != filename[-6:]:
    print("Please provide a valid .seoul file!")
    exit()

os.system("CLS")

with open(filename) as content:
    try:
        start = time.time()

        for line in content:
            line = line.replace("\n", "")

            if line.startswith("sys << "):
                if line[7:].startswith("seoul[") and not line[7:].startswith("\""):
                    print(f">> {seoul_properties[line[7:]]}")
                else:
                    if not line[7:].startswith("\""):
                        raise Exception("lol put some \" to print smh")
                    else:
                        print(">> " + line[7:].replace("\"", "").replace("\\n", "\n"))
            elif line.startswith("throw << "):
                raise Exception(line[9:])
            elif line.startswith("endthesuffering"):
                exit()
            else:
                raise Exception(f"idk what that means lol ({line})")

        end = time.time()

        print(f"\nProcess finished in {int(start - end)}ms")
    except FileNotFoundError:
        print("File not found!")
