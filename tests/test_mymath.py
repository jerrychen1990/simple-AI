#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/9/17 2:11 PM
# @Author  : xiaowa

import app.lib.mymath as mymath


def test_entropy():
    prob_list = [40, 3, 3]
    entropy = mymath.get_entropy(prob_list)
    print(entropy)

test_entropy()

