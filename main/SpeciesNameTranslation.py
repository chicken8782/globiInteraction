#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import pandas as pd
import numpy as np
import csv

with open("/Users/outou1/Python/GLoBI/YList20170621.csv", encoding="utf8", errors='ignore') as f:
	csv_reader = csv.reader(f)
	for row in csv_reader:
		print(row)

with codecs.open("/Users/outou1/Python/GLoBI/YList20170621.csv", "r", "Shift-JIS", "ignore") as file:
    df = pd.read_table(file, delimiter=",")
    print(df)