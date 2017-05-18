#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/9/17 9:09 PM
# @Author  : xiaowa

import app.config as config
import app.commands as commands

if __name__ == '__main__':
    commands.guess_num_commandline()
    # import codecs
    # import collections
    #
    # rs_dict = collections.defaultdict(int)
    #
    # with codecs.open("/Users/jerry/test.dat") as src:
    #     for line in src:
    #         fields = line.split("\t")
    #         key = int(int(fields[0]) / 3600)
    #         value = int(fields[1])
    #         rs_dict[key] += value
    #
    #     total = sum(rs_dict.values())
    #     acc = 0
    #     thresh = 0.0
    #
    #     for k, v in rs_dict.items():
    #         acc += v
    #         if acc >= thresh * total:
    #             msg = "hour:%d, order_num:%d, percent %2.2f" % (k, acc, thresh)
    #             print(thresh, k)
    #             thresh += 0.01
    #
    #     # thresh = 0.90
    #     # acc = 0
    #     # for k, v in rs_dict.items():
    #     #     acc += v
    #     #     if acc >= thresh * total:
    #     #         msg = "hour:%d, order_num:%d, percent %2.2f" % (k, acc, thresh)
    #     #
    #     #         print(msg)
    #     #         thresh += 0.01
