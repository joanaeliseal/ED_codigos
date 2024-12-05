def recursiveLength(string: str) -> int:
    if string == "":
        return 0
    return 1 + recursiveLength(string[1:])

def printstr(string: str):
    if string == "":
        return
    printstr(string[1:])
    print(string[0], end="")


def invertString(string: str) -> str:
    if string == "":
        return ""
    # return invertString(string[1:]) + string[0]
    return string[-1] + invertString(string[:-1])

if __name__ == "__main__":
    print(invertString("abc"))
    # print(f"recursiveLength() -> {recursiveLength("abc")}")
