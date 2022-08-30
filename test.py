#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input()

dict_item = {}
string = list(s)
string.sort()
count = 1
for i in range(len(string) - 1):
    if string[i] != string[i + 1]:
        if count > 1:
            dict_item[string[i]] = count
            count = 1
    else:
        count += 1

sort = sorted(dict_item.values(), reverse=True)

for key in dict_item:
    if dict_item[key] == sort[0]:
        print(key, sort[0])
        del dict_item[key]
        del sort[0]
# print(sort)
