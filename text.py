# -*- coding: utf-8 -*
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

file = pd.read_excel('153.xlsx')

file = file.iloc[::2]

text = file [1].values

for count, row in enumerate(text):
    row[0::]
    with open('153_' + str(count + 1) + '_YH.txt', "w") as text_file:
        print(str(row), file=text_file)
