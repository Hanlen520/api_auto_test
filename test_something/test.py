#!/usr/bin/python
# -*- coding:utf-8 -*-

import random


def longitude():
    a = random.uniform(120.52,122.11)
    return float(str(a)[:10])
for i in range(3,7):
    a = longitude()
    print(a)