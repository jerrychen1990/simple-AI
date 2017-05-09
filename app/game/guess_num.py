#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/5/17 5:39 PM
# @Author  : xiaowa

import random
import collections
import app.lib.mylog as mylog
logger = mylog.get_logger("guess_num")



def generate_num(guess_length, max_num):
    num_list = list(range(0, max_num))
    random.shuffle(num_list)
    return num_list[:guess_length]


def judge_num(to_guess, guess):
    if len(to_guess) != len(guess):
        raise ValueError("different number length!")

    rs_dict = collections.defaultdict(int)
    for idx, num in enumerate(guess):
        if num == to_guess[idx]:
            rs_dict["A"] += 1
        elif num in to_guess:
            rs_dict["B"] += 1
    return rs_dict


def format_judge_dict(rs_dict):
    rs_str = "{}A{}B".format(rs_dict["A"], rs_dict["B"])
    return rs_str


class GuessNumGame:
    def __init__(self, guess_length=4, max_judge_count=10, max_num=10):
        self.guess_length = guess_length
        self.to_guess = generate_num(guess_length, max_num)
        self.max_judge_count = max_judge_count

    def play(self, ai):
        idx = 1
        logger.info("game started, num to guess:{}".format(self.to_guess))
        while idx <= self.max_judge_count:
            logger.info("round {}:".format(idx))
            guess = ai.guess()
            judge_dict = judge_num(self.to_guess, guess)

            judge_str = format_judge_dict(judge_dict)
            logger.info("guess:{}, judge result:{}".format(guess, judge_str))

            ai.notice(judge_dict)
            if judge_dict["A"] == self.guess_length:
                logger.info("you win!")
                return idx
            idx += 1

        logger.info("you lose!")
        return -1


def experience(ai_class, guess_length=4, max_judge_count=10, max_num=10, times=100):
    lose_num = 0
    win_list = []

    for idx in range(1, times + 1):
        logger.info("experience{}:".format(idx))
        game = GuessNumGame(guess_length, max_judge_count, max_num)
        ai = ai_class()
        round_num = game.play(ai)
        if round_num == -1:
            lose_num += 1
        else:
            win_list.append(round_num)
        win_num = len(win_list)
        avg_round = sum(win_list) / win_num

    logger.info("win:{}, lose{}, avg_round:{}".format(win_num, lose_num, avg_round))

