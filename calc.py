#!/usr/bin/python

import sys
import re
import math

def sum(n):
    res = 0
    while n > 0:
        res += n % 10
        n = n // 10
    return res


def extract(n, digit):
    res = ''
    while n > 0:
        if n % 10 == digit:
            res += str(digit)
        n = n // 10
    return res if res != '' else '-'

def matrix(date):
    firstRow = re.sub(r"[^1-9]+", "", date)
    firstN = sum(int(firstRow))
    secondN = (firstN % 10) + math.floor(firstN / 10)
    firstCode = str(firstN) + str(secondN)
    thirdN = firstN - int(firstRow[0:1]) * 2
    fourthN = sum(int(thirdN))
    secondCode = str(thirdN) + str(fourthN)
    secondRow = firstCode + secondCode
    rows = firstRow + secondRow
    matrix = []
    for i in range(1, 10):
        matrix.append(extract(int(rows), i))
    return matrix