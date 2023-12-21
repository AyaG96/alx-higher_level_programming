#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    n = len(argv) - 1
    text = "argument" if n == 1 else "arguments"

    print(f"{n} {text}", end="")
    print("." if n == 0 else ":")

    i = 1
    while i <= n:
        print(f"{i}: {argv[i]}")
        i += 1

