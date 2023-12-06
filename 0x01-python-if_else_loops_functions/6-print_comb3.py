#!/usr/bin/python3

for n in range(10):
    for n1 in range(n + 1, 10):
        print("{}{}".format(n, n1), end=', ' if n != 8 and n1 != 9 else '\n')
