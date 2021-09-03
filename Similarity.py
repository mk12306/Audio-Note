#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 13:50:51 2021

计算两个音频的相似程度
分数越大，代表越相似，建议设置临界值为0.7

@author: wangkai62
"""
from scipy.io import wavfile

def preprocess(data1, data2):
    # sr1, data1 = wavfile.read(path1)
    # sr2, data2 = wavfile.read(path2)
    
    # if len(data1.shape) > 1:
    #     data1 = np.mean(data1, axis=1) #声道转换为1维

    # if len(data2.shape) > 1:
    #     data2 = np.mean(data2, axis=1) #声道转换为1维
        
    leng = min(len(data1), len(data2))
    data1 = data1[:leng]
    data2 = data2[:leng]
    
    return data1, data2

def dHash(data):
    """
    统计波形的变化情况，上坡为1，下坡为0
    """
    hashVal = []
    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            hashVal.append(1)
        else:
            hashVal.append(0)
    return hashVal

def Hamming_distance(hashVal1, hashVal2):
    num = 0
    for index in range(len(hashVal1)):
        if hashVal1[index] != hashVal2[index]:
            num += 1
    return num

def score(data1, data2):
    data1, data2 = preprocess(data1, data2)
    hashVal1 = dHash(data1)
    hashVal2 = dHash(data2)
    dist = Hamming_distance(hashVal1, hashVal2)
    sim = 1 - dist * 1.0 / len(data1)
    return dist, sim
    
if __name__ == '__main__':
    path1 = '/Users/wangkai62/Desktop/Test/origin.wav'
    path2 = '/Users/wangkai62/Desktop/Test/clear.wav'
    
    sample_rate, data1 = wavfile.read(path1)
    sample_rate, data2 = wavfile.read(path2)   
    
    dist, sim = score(data1, data2)
    print('dist:', dist)
    print('similarity:', sim)