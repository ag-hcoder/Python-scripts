str = "Indians123"

SECURE = (('s', '$'), ('and', '&'),
          ('a', '@'), ('o', '0'),
          ('i', '1'), ('I', '|'))

if __name__ == "__main__":
    for a, b in SECURE:
        str = str.replace(a, b)
print(str)
