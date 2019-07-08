#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 14:57:15 2019

@author: mohnishdevadiga
"""

import torch
from torch.jit import script, trace
import torch.nn as nn
from torch import optim
import torch.nn.functional as F
import csv
import random
import re
import os
import unicodedata
import codecs
from io import open
import itertools
import math

USE_CUDA = torch.cuda.is_available()
device = torch.device("cuda" if USE_CUDA else "cpu")

FILE_path = "data/cornell movie-dialogs corpus/"

FILE_lines = "data/cornell movie-dialogs corpus/movie_lines.txt"
FILE_convo = "data/cornell movie-dialogs corpus/movie_conversations.txt"

line_fields = ["lineID","CharacterID","MovieID","character","text"]
lines = {}

with open(FILE_lines,'rb') as f:
    for line in f:
        value = str(line.strip()).split("+++$+++")
        lineObj = {}
        for i,field in enumerate(line_fields):
            lineObj[field] = value[i]
        lines[lineObj["lineID"]] = lineObj
        