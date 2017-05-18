#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/16/17 11:23 AM
# @Author  : xiaowa
import math
import random
import app.lib.mylog as mylog
import app.lib.common as common
import copy
from enum import Enum

logger = mylog.get_logger("twok")

SMALL_PER = 0.5


class Direction(Enum):
    LEFT = 10
    RIGHT = 20
    UP = 30
    DOWN = 40


OPPOSITE_DIRECTION_MAP = {
    Direction.LEFT: Direction.LEFT,
    Direction.RIGHT: Direction.RIGHT,
    Direction.UP: Direction.DOWN,
    Direction.DOWN: Direction.UP
}

ALL_DIRECTION = [Direction.LEFT, Direction.RIGHT, Direction.UP, Direction.DOWN]


def can_move(seq):
    for idx in range(len(seq) - 1):
        v1 = seq[idx]
        v2 = seq[idx + 1]
        if v1 == 0 and v2 != 0:
            return True
        if v1 != 0 and v1 == v2:
            return True
    return False


def can_move_board(board):
    for seq in board:
        if can_move(seq):
            return True
    return False


def get_direction_board(direction, board):
    if direction == Direction.LEFT:
        return board
    if direction == Direction.RIGHT:
        return revolve(board)
    if direction == Direction.UP:
        return left_revolve(board)
    if direction == Direction.DOWN:
        return right_revolve(board)


def right_revolve(board):
    rs_board = copy.deepcopy(board)
    for i in range(len(board)):
        for j in range(len(board[0])):
            rs_board[j][len(board[0]) - 1 - i] = board[i][j]
    return rs_board


def left_revolve(board):
    rs_board = copy.deepcopy(board)
    for i in range(len(board)):
        for j in range(len(board[0])):
            rs_board[len(board) - 1 - j][i] = board[i][j]
    return rs_board


def revolve(board):
    rs_board = copy.deepcopy(board)
    for i in range(len(board)):
        for j in range(len(board[0])):
            rs_board[i][len(board[0]) - 1 - j] = board[i][j]
    return rs_board


def move(seq):
    cur_idx = 0
    tar_idx = 0
    net_list = list(filter(lambda x: x != 0, seq))
    while cur_idx < len(net_list):
        if cur_idx == len(net_list) - 1:
            seq[tar_idx] = net_list[cur_idx]
        elif net_list[cur_idx] == net_list[cur_idx + 1]:
            seq[tar_idx] = net_list[cur_idx] * 2
            cur_idx += 1
        else:
            seq[tar_idx] = net_list[cur_idx]
        tar_idx += 1
        cur_idx += 1
    while tar_idx < len(seq):
        seq[tar_idx] = 0
        tar_idx += 1

    return seq


def possible_direction(board):
    return list(filter(lambda d: can_move_board(get_direction_board(d, board)), ALL_DIRECTION))


def move_direction(direction, board):
    tmp_board = get_direction_board(direction, board)
    for seq in tmp_board:
        move(seq)
    return tmp_board


class Twok:
    def __init__(self, board_size=4, target_exp=11):
        self.board = []
        self.board_size = board_size
        self.target = math.pow(2, target_exp)
        self.step = 0
        for idx in range(self.board_size):
            self.board.append([0] * board_size)

    def generate_num(self):
        num = 2
        if random.random() > SMALL_PER:
            num = 4
        flat_list = common.flatmap(lambda x: x, self.board)
        empty_list = list(filter(lambda x: x[1] == 0, enumerate(flat_list)))
        empty_len = len(empty_list)
        if empty_len == 0:
            logger.info("nowhere to put new number")
            return -1
        choose_idx = empty_list[random.randint(0, empty_len - 1)][0]
        self.board[int(choose_idx / self.board_size)][choose_idx % self.board_size] = num
        return num

    def summary(self):
        tmp_list = common.flatmap(lambda x: x, self.board)
        max_num = max(tmp_list)
        total_score = sum(tmp_list)
        is_win = max_num > self.target
        return max_num, total_score, self.step, is_win

    def show_board(self):
        logger.info("current board")
        for seq in self.board:
            logger.info(", ".join(map(lambda x: str(x), seq)))

    def play(self, ai):
        logger.info("2k game started")
        while True:
            self.step += 1
            logger.info("step{}".format(self.step))
            self.generate_num()
            self.show_board()

            tmp_board = self.board
            directions = possible_direction(tmp_board)
            if len(directions) == 0:
                logger.info("game over")
                return self.summary()
            # logger.info("possible directions {}".format(str(directions)))
            direction = ai.direction(copy.deepcopy(self.board), directions)
            logger.info("move {}".format(direction))
            self.board = move_direction(direction, self.board)
            self.board = get_direction_board(OPPOSITE_DIRECTION_MAP[direction], self.board)
            # self.show_board()
