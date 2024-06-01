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

def main():
    'entry point'
    a, b = 1, 2
    s = 0
    lim = 4000000
    while b < lim:
        if b < lim and b % 2 == 0:
            s += b
        a, b = b, a + b
    print(s)

if __name__ == '__main__':
    main()

