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
    d = 999 + 1
    m = 0
    for i in range(d):
        for j in range(d):
            p = i * j
            if str(p) == ''.join(reversed(str(p))):
                m = max(p, m)
    print(m)

if __name__ == '__main__':
    main()

