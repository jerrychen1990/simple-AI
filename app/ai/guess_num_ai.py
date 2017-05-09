#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/5/17 5:59 PM
# @Author  : xiaowa
import random
import copy
import itertools
from app.lib.myrandom import random_pick
from app.lib.mymath import get_entropy
from app.lib.common import get_full_combination, get_distinct_combination, count_group_by, column_slice
from app.game.guess_num import judge_num, format_judge_dict


def random_guess(guess_length, max_num=10):
    num_list = list(range(0, max_num))
    random.shuffle(num_list)
    return num_list[:guess_length]


class StupidAI:
    def __init__(self, guess_length, max_num=10):
        self.guess_length = guess_length
        self.max_num = max_num

    def guess(self):
        return random_guess(self.guess_length, self.max_num)

    def notice(self, judge_dict):
        pass



class EntropyAI:
    def __init__(self, guess_length=4, max_num=10):
        self.guess_history = []
        self.guess_length = guess_length
        self.max_num = max_num
        self.answer_set = get_distinct_combination(list(range(0, max_num)), self.guess_length)

    def guess(self):
        guess = [-1] * self.guess_length
        tmp_answer_set = copy.copy(self.answer_set)
        for idx in range(0, self.guess_length):
            group_list = list(
                    map(lambda x: count_group_by(column_slice(tmp_answer_set, x)), range(0, self.guess_length)))
            entropy_list = list(map(lambda x: get_entropy(x.values()), group_list))
            choose_idx = max(filter(lambda x: guess[x[0]] == -1, enumerate(entropy_list)))[0]
            candidate_list = list(group_list[choose_idx].items())
            random.shuffle(candidate_list)
            choose_num = max(candidate_list, key=lambda x: x[1])[0]
            guess[choose_idx] = choose_num
            tmp_answer_set = list(filter(lambda x: x[choose_idx] == choose_num, tmp_answer_set))
        self.guess_history.append(guess)
        return guess

    def notice(self, judge_dict):
        last_guess = self.guess_history[-1]
        self.answer_set = list(
                filter(lambda x: format_judge_dict(judge_num(x, last_guess)) == format_judge_dict(judge_dict),
                       self.answer_set))
