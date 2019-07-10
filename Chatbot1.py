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

#FILE_path = "data/cornell movie-dialogs corpus/"

FILE_lines = "data/cornell movie-dialogs corpus/movie_lines.txt"
FILE_convo = "data/cornell movie-dialogs corpus/movie_conversations.txt"

line_fields = ["lineID","CharacterID","MovieID","character","text"]
lines = {}
l = []
with open(FILE_lines,'rb') as f:
    for line in f:
        tempL = line
        try:
            if type(line) == type(b"123"):
                tempL = line.decode('utf-8')
        except Exception as e:
            x = []
            x.append(tempL)
            x.append(e)
            l.append(x)
        value = str(tempL.strip()).split("+++$+++")
        lineObj = {}
        for i,field in enumerate(line_fields):
            lineObj[field] = ' '.join(value[i].split())
        lines[lineObj["lineID"]] = lineObj
        
convo_fields = ["Character1ID","Character2ID","MovieID","UtteranceID"]
convo = {}

with open(FILE_convo,'rb') as f:
    for line in f:
        values = str(line.strip()).split(" +++$+++ ")
        convObj = {}
        for i, field in enumerate(convo_fields):
            convObj[field] = values[i]
        #print(convObj["UtteranceID"])
        temp = eval("\""+convObj["UtteranceID"])
        lineIds = eval(temp)
        convObj["lines"] = []
        for lineId in lineIds:
            try:
                convObj["lines"].append(lines[lineId])
            except:
                try:
                    convObj["lines"].append(lines[lineId+" "])
                except Exception as e:
                    print(e)
        