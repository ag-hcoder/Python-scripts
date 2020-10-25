import os


def isName(filename):
    f = open(filename, 'r')
    fileContent = f.read()
    if "opensource" in fileContent.lower():
        return True
    else:
        return False


path = '/home/hardik/Python/'


if __name__ == "__main__":
    # os.getcwd()
    dir_contents = os.listdir(path)
    ct = 0
    for item in dir_contents:
        if item.endswith('txt'):
            flag = isName(item)
            if flag is True:
                ct += 1
                print(item)

    print(ct)
