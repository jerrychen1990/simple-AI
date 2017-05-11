#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/11/17 3:14 PM
# @Author  : xiaowa

import argparse
from app.game.guess_num import experience
from app.ai.guess_num_ai import get_ai_class


def get_guess_name_parser():
    parser = argparse.ArgumentParser(description='guess num game engine')
    parser.add_argument('-l', '--guess_length', type=int,
                        help='how many numbers to guess')
    parser.add_argument('-m', '--max_judge_count', type=int,
                        help='max rounds to guess')
    parser.add_argument('-t', '--times', type=int,
                        help="execute how many times of game")
    parser.add_argument('ai_name', type=str,
                        help="the ai's name")
    return parser


def command_line_runner(parser_func, exe_func):
    parser = parser_func()
    kwargs = vars(parser.parse_args())
    kwargs = dict(list(filter(lambda x: x[1] is not None, kwargs.items())))
    exe_func(**kwargs)


def guess_num_exec(**kwargs):
    ai_class = get_ai_class(kwargs["ai_name"])
    kwargs["ai_class"] = ai_class
    del (kwargs["ai_name"])
    return experience(**kwargs)


def guess_num_commandline():
    return command_line_runner(get_guess_name_parser, guess_num_exec)
