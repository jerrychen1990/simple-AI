#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/8/17 11:39 AM
# @Author  : xiaowa

import os
import app.lib.common as common
import app.ai.guess_num_ai as guess_num_ai
import app.game.guess_num as guess
import app.config as config


def test_get_full_combination():
    rs = common.get_full_combination([[1, 2], [5, 6], [9, 8, 0]])
    print(rs)


def test_get_distinct_combination():
    rs = common.get_distinct_combination([1, 2, 3, 4], 2)
    print(len(rs))


def test_count_group_by():
    src = [1, 2, 1, 3, 3, 3, 0]
    rs = common.count_group_by(src)
    print(rs)


def test_get_instance():
    cur_path = ".".join(["app", "ai", "guess_num_ai"])
    rs = common.get_instance(cur_path, "EntropyAI")
    print(rs)


test_get_instance()

# test_get_distinct_combination()


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
