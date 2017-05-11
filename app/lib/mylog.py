#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/9/17 8:30 PM
# @Author  : xiaowa
import logging
import logging.handlers
import os
from app.config import LOG_HOME

FILE_FORMAT = logging.Formatter("%(asctime)s %(name)s [%(levelname)s]  %(filename)s:%(lineno)d - %(message)s")
NAKED_FORMAT = logging.Formatter("%(message)s")

CONSOLE_HANDLER = logging.StreamHandler()
CONSOLE_HANDLER.setFormatter(NAKED_FORMAT)
CONSOLE_HANDLER.setLevel(logging.INFO)


def get_logger(name, is_print=True, level=logging.DEBUG, log_home=LOG_HOME):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    if is_print:
        logger.addHandler(CONSOLE_HANDLER)
    if not os.path.exists(log_home):
        os.mkdir(log_home)
    log_path = os.path.join(log_home, name + ".log")
    info_handler = logging.handlers.TimedRotatingFileHandler(log_path + ".info",
                                                             when="D",
                                                             backupCount=7)
    info_handler.setFormatter(FILE_FORMAT)
    info_handler.setLevel(logging.INFO)
    debug_handler = logging.handlers.TimedRotatingFileHandler(log_path + ".debug",
                                                              when="D",
                                                              backupCount=7)
    debug_handler.setFormatter(FILE_FORMAT)
    debug_handler.setLevel(logging.DEBUG)
    error_handler = logging.handlers.TimedRotatingFileHandler(log_path + ".error",
                                                              when="D",
                                                              backupCount=7)
    error_handler.setFormatter(FILE_FORMAT)
    error_handler.setLevel(logging.ERROR)
    logger.addHandler(info_handler)
    logger.addHandler(debug_handler)
    logger.addHandler(error_handler)
    return logger


ROOT_LOG = get_logger("root")
