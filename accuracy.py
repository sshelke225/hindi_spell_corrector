import csv
import numpy as np
import pandas as pd
from rapidfuzz.distance import Levenshtein
def levenst_dist(pred_seq,label_seq):
    ld = Levenshtein.distance(pred_seq.lower(),label_seq.lower())
    length = max(len(pred_seq),len(label_seq))
    nld = (length - ld) / length
    return nld

r = open('ground_truth.txt', encoding='utf-8').read().split('\n')
d = open('output.txt',encoding='utf-8').read().split('\n')


lst1,lst2 = [],[]
for line in r:
    line = line.removesuffix('.')
    lst1.append(line)
for sent in d:
    lst2.append(sent)

lst = []
for j in range(len(lst1)):
    lst_a = [lst1[j],lst2[j],levenst_dist(lst1[j],lst2[j])]
    lst.append(lst_a)
lst = np.array(lst)
print(lst.shape)

df = pd.DataFrame(lst,columns=['Ground Truth','Output','Accuracy'])
print(df[:][:])
df.to_csv('Accuracy.csv')