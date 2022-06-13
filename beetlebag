 import numpy as np
import random as rand
test_cases = int(input())

def choose(gadget_number,chosen):
    indexi = rand.randint(0,gadget_number-1)
    if indexi in chosen:
        return choose(gadget_number,chosen[0:indexi]+chosen[indexi+1:])
    return indexi

def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
 
    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1]+ K[i-1][w-wt[i-1]],K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
 
    return K[n][W]
for i in range(0,test_cases):
    capacity, gadget_number = input().split(' ')
    capacity, gadget_number = [int(capacity), int(gadget_number)]
    weight, power = [[],[]]
    for i in range(0,gadget_number):
        case = input().split(' ')
        weight.append(int(case[0]))
        power.append(int(case[1]))
    maximum_power = knapSack(capacity,weight,power,gadget_number)
    print(maximum_power)
