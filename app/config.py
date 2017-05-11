#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/9/17 8:37 PM
# @Author  : xiaowa

import os

APP_HOME = os.path.split(os.path.realpath(__file__))[0]
PROJECT_HOME = os.path.dirname(APP_HOME)

AI_HOME = os.environ.get("AI_HOME", PROJECT_HOME)
LOG_HOME = os.path.join(AI_HOME, "logs")
