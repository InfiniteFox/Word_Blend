# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 05:51:21 2019

@author: IF
"""

true_blend = []
with open("blends.txt") as file:
    for line in file:
        w = line.split()
        true_blend.append(w[0])


predict_blend = []
#Read

with open("prediction_1.txt") as file:
    for line in file:
        w = line.rstrip()
        predict_blend.append(w)

print(len(predict_blend))
#Evaluation


#True Positive
tp = 0
#False Positive
fp = 0
for pb in predict_blend:
    if pb in true_blend:
        tp += 1
    else:
        fp += 1

        
#True Negative
tn = 0
#False Negative
fn = 0
for tb in true_blend:
    if tb not in predict_blend:
        fn += 1


accuracy = tp / len(predict_blend)
print('accuracy:', '%.5f' % accuracy, f'\t{tp}/{len(predict_blend)}')
recall = tp / len(true_blend)
print('recall:', '%.5f' % recall, f'\t{tp}/{len(true_blend)}')

