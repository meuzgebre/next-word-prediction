import os
amh = open('amh.txt', encoding='utf-8').read().strip().split('\n')
eng = open('eng.txt', encoding='utf-8').read().strip().split('\n')
pairs = []
for idx in range(len(eng)):
  open('datasets.txt', encoding='utf-8').write(f'{amh[idx]}\t{eng[idx]}')