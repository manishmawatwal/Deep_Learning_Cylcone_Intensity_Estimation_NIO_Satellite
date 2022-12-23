import os
import pandas as pd

os.chdir(r'val')

folders = ['D(20-25)', 'DD(30-35)', 'CS(40-50)', 'SevereCS(55-65)', 'VSCS(70+)']

files = []

for folder in folders:
    for file in os.listdir(folder):
        files.append([file, folder])

pd.DataFrame(files, columns=['files', 'target']).to_csv('train.csv')