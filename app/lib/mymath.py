#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/9/17 2:05 PM
# @Author  : xiaowa

import math

def get_entropy(prob_list):
    sum_prob = sum(prob_list)
    prob_list = list(map(lambda x: x/sum_prob, prob_list))
    entropy = -sum(map(lambda x: x * math.log2(x), prob_list))
    return entropy







