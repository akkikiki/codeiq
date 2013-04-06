#!/usr/bin/env python
# -*- coding: utf-8 -*-
# answer.txt: 
#　食べていいキノコ（本数不明）のみについて、柄の長さ(cm)と傘の直径(cm)をCodeIQ_data.txtと同じ要領で半角スペース区切りで記入したファイルをアップロードして下さい。

import random

# initialize needs some effort
from math import sqrt

def euclidean(v1, v2):
  temp = 0
  for e1 in v1:
    for e2 in v2:
      temp += pow(e1 - e2,2)
  distance = sqrt(temp)
  return distance

def readfile(filename, n):
  lines=[line for line in file(filename)]
  data=[]
  for line in lines:
    p=line.strip().split(' ')
    #data.append([float(x) for x in p[:n]])
    if len(p) > 2:
      temp = [float(x) for x in p[:n]]
      temp.append(p[2])
      data.append(temp)
    else: data.append([float(x) for x in p[:n]])
    #very task specific
    #up to nth element
  return data, lines #can be in any demention
'''
def kcluster(rows, distance = euclidean, k= 2):
  clusters = []
  clusters.append([length_safe, width_safe])
  clusters.append(
'''
if __name__=='__main__': 
  data_eaten, lines_eaten=readfile('CodeIQ_eaten.txt', 2)
  data_predict, lines_data=readfile('CodeIQ_data.txt', 2)
  print data_eaten
  print data_predict[0][0]
  length_safe = 0; width_safe = 0; length_dang = 0; width_dang = 0
  safe = 0; dang = 0
  for elem in data_eaten:
    if elem[2] == 'o':
      length_safe += elem[0]
      width_safe += elem[1]
      safe += 1
    else:
      length_dang += elem[0]
      width_dang += elem[1]
      dang += 1
  length_safe /= safe; width_safe /= safe; length_dang /= dang; width_dang /= dang

  #centroids
  clusters = [[data_eaten[j][i] for i in range(len(data_eaten[j]) - 1)] for j in range(len(data_eaten))]
  print clusters
  
  lastmatches=None
  for t in range(100):
    print 'Iteration %d' % t
    bestmatches=[[] for i in range(len(clusters))]
    
    # nearest points
    for j in range(len(data_predict)):
      bestmatch=0
      for i in range(len(clusters)):
        d=euclidean(clusters[i], data_predict[j])
        if d<euclidean(clusters[bestmatch], data_predict[j]): bestmatch=i
      bestmatches[bestmatch].append(j)
    #bestmatche[i]にクラスタiに所属する要素jを登録する

    if bestmatches==lastmatches: break
    lastmatches=bestmatches
    
    #print bestmatches
    #since the place is 2d, one more dimention is needed
    for i in range(len(clusters)):
      #print(len(clusters))
      avgs=[0.0, 0.0]
      
      if len(bestmatches[i]) > 0: 
      #存在条件
        for m in range(len(bestmatches[i])):
          #print data_predict[bestmatches[i][m]]
          #print data_predict[bestmatches[i][m]][0]
          avgs[0] += data_predict[bestmatches[i][m]][0]
          avgs[1] += data_predict[bestmatches[i][m]][1]
        avgs[0]/=len(bestmatches[i])
        avgs[1]/=len(bestmatches[i]) 
        clusters[i]=avgs
  
  #print bestmatches
  
  #safe mushroom clusters
  from heapq import merge
  predicted_safe = list(merge(bestmatches[2], bestmatches[5]))
  #print predicted_safe
  file_opened = open('safe_mushrooms.txt', 'w')
  for num in predicted_safe:
     file_opened.write(lines_data[num])
