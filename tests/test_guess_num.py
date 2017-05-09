#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/5/17 6:02 PM
# @Author  : xiaowa
import app.game.guess_num as guess_num
import app.ai.guess_num_ai as guess_num_ai

guess_length = 4
max_num = 10
max_judge_count = 10

game = guess_num.GuessNumGame(guess_length, max_judge_count=max_judge_count, max_num=max_num)
stupid_ai = guess_num_ai.StupidAI(guess_length=guess_length, max_num=max_num)
force_ai = guess_num_ai.EntropyAI(guess_length=guess_length, max_num=max_num)

# game.play(force_ai)


guess_num.experience(guess_num_ai.EntropyAI)
