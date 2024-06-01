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
    n = 100
    a = sum(x*x for x in range(n+1))
    b = sum(x for x in range(n+1))
    b *= b
    print(b - a)

if __name__ == '__main__':
    main()

