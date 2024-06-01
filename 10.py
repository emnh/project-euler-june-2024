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
from sympy import primerange

def main():
    'entry point'
    s = 0
    for p in primerange(1, 2000000):
        s += p
    print(s)

if __name__ == '__main__':
    main()

