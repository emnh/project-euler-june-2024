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
    s = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            s += i
    print(s)

if __name__ == '__main__':
    main()

