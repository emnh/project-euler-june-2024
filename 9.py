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
    for a in range(1, 1000+1):
        for b in range(1, 1000+1):
            c = 1000 - a - b
            if a * a + b * b == c * c:
                print(a * b * c)
                return

if __name__ == '__main__':
    main()

