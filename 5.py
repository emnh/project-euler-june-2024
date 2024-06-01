#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: ft=python ts=4 sw=4 sts=4 et fenc=utf-8
# Original author: "Eivind Magnus Hvidevold" <hvidevold@gmail.com>
# License: GNU GPLv3 at http://www.gnu.org/licenses/gpl.html

'''
'''

import os
import sys
import re

def check(n):
    for i in range(1, 20 + 1):
        if n % i != 0:
            return False
    return True

def main():
    'entry point'
    s = 1
    for i in range(1, 10 + 1):
        s *= i
    print(s)
    n = 1
    while True:
        if check(n):
            break
        n += 1
    print(n)

if __name__ == '__main__':
    main()
