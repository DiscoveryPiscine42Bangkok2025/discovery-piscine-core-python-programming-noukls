import sys

args = sys.argv[1:]

if len(args) != 1:
    print("none")
else:
    string = args[0]
    result = ""
    for char in string:
        if char == "z":
            result += "z"
    if result == "":
        print("none")
    else:
        print(result)