#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/5/17 5:59 PM
# @Author  : xiaowa
import random
import itertools
from app.lib.myrandom import random_pick
from app.lib.common import get_full_combination, get_distinct_combination
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


class ProbAI:
    def __init__(self, guess_length, max_num=10):
        self.guess_history = []
        self.guess_length = guess_length
        self.b_coefficient = 1.0 / self.guess_length
        self.possible_lists = list()
        self.max_num = max_num
        for idx in range(self.guess_length):
            self.possible_lists.append([1.0] * self.max_num)
        self.num_info = [1.0] * 10

    def guess(self):
        guess = []
        for pl in self.possible_lists:
            guess_list = list(filter(lambda x: x[0] not in guess,
                                     map(lambda e: (e[0], e[1] * self.num_info[e[0]]), enumerate(pl))))
            picked = random_pick(guess_list)
            guess.append(picked[0])

        self.guess_history.append(guess)
        return guess

    def notice(self, judge_dict):
        last_guess = self.guess_history[-1]
        # add A possibility
        for pl, num in zip(self.possible_lists, last_guess):
            pl[num] += judge_dict["A"] * 0.25

        # add B possibility
        for idx, pl in enumerate(self.possible_lists):
            for g_idx, num in enumerate(last_guess):
                b_num = judge_dict["B"]
                if g_idx == idx:
                    b_num -= 1
                pl[num] += b_num * self.b_coefficient

        flat_guess = [item for sub in self.guess_history for item in sub]
        self.num_info = list(map(lambda x: x[1] / (flat_guess.count(x[0]) + 1), enumerate([1.0] * self.max_num)))


class ForceAI:
    def __init__(self, guess_length=4, max_num=10):
        self.guess_history = []
        self.guess_length = guess_length
        self.max_num = max_num
        self.answer_set = get_distinct_combination(list(range(0, max_num)), self.guess_length)

    def guess(self):
        guess = []
        flat_history = [item for subset in self.guess_history for item in subset]
        for idx in range(0, self.guess_length):
            tmp_slice = list(map(lambda x: x[idx], self.answer_set))
            candidate_list = list(filter(lambda x: x not in guess, range(0, self.max_num)))
            random.shuffle(candidate_list)
            picked = max(candidate_list, key=lambda e: tmp_slice.count(e) / (flat_history.count(e) * 2 + 1.0))
            guess.append(picked)
        self.guess_history.append(guess)
        return guess

    def notice(self, judge_dict):
        last_guess = self.guess_history[-1]

        self.answer_set = list(
                filter(lambda x: format_judge_dict(judge_num(x, last_guess)) == format_judge_dict(judge_dict),
                       self.answer_set))
