#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/8/17 8:09 PM
# @Author  : xiaowa

import os
import sys


def get_full_combination(lists):
    return get_iter_combination([], lists)


def get_iter_combination(acc, lists):
    if len(lists) == 0:
        return acc
    rs = []
    for item in lists[0]:
        sub_rs = get_iter_combination(acc + [item], lists[1:])
        if len(lists) == 1:
            rs.append(sub_rs)
        else:
            rs.extend(sub_rs)
    return rs


def get_distinct_combination(elements, times):
    rs = []
    get_iter_distinct_combination(rs, [], elements, times)
    return rs


def get_iter_distinct_combination(collect, current, elements, times):
    candidate = list(set(elements) - set(current))
    if times == 0 or len(candidate) == 0:
        collect.append(current)
        return
    for item in candidate:
        get_iter_distinct_combination(collect, current + [item], elements, times - 1)


def count_group_by(items):
    keys = set(items)
    rs_dict = dict(map(lambda x: (x, items.count(x)), keys))
    return rs_dict


def column_slice(items, idx):
    return list(map(lambda x: x[idx], items))


def get_class(module_path, class_name):
    module = sys.modules[module_path]
    clazz = getattr(module, class_name)
    return clazz

def get_instance(module_path, class_name):
    clazz = get_class(module_path, class_name)
    obj = clazz()
    return obj
