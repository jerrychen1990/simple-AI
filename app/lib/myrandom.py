#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/8/17 7:22 PM
# @Author  : xiaowa
import random


def random_pick(items):
    random.shuffle(items)
    total_prob = sum(map(lambda d: d[1], items))

    target_prob = random.uniform(0, total_prob)
    accumulate_prob = 0.0
    for item in items:
        accumulate_prob += item[1]
        if accumulate_prob >= target_prob:
            return item

    return None
