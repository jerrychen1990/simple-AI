#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/8/17 11:39 AM
# @Author  : xiaowa

import app.lib.common as common
import app.game.guess_num as guess


def test_get_full_combination():
    rs = common.get_full_combination([[1, 2], [5, 6], [9, 8, 0]])
    print(rs)


def test_get_distinct_combination():
    rs = common.get_distinct_combination([1, 2, 3, 4], 2)
    print(len(rs))


test_get_distinct_combination()


# # test_get_full_combination()
# tmp = range(1,10)
# print(list(tmp))

# d1 = guess.judge_num([1, 3, 4], [0, 1, 4])
# d2 = guess.judge_num([1, 3, 4], [9, 1, 4])
#
#
# print(d1)
# print(d2)
# print(d1 == d2)
