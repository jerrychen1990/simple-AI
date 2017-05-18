#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/16/17 8:13 PM
# @Author  : xiaowa
import app.game.twok as twok
import app.ai.twok_ai as twok_ai
import copy


# from app.game.twok import Twok

#
def test_move():
    seq = [2, 2, 2, 2]
    print(twok.move(seq))
    print(seq)


def test_right_revolve():
    board = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

    print(twok.revolve(board))


def test_play():
    twok_game = twok.Twok()
    ai = twok_ai.RandomAI()
    max_num, total_score, step, is_win = twok_game.play(ai)
    print(max_num, total_score, step, is_win)


test_play()
