#Project Euler - Problem 391
#Language: Python2
#Time of Completion(?): 21-08-2012 02:10 IST

#Binary Sequence Games - Predicting Winning Move

#---IMPORT SPACE------#
import sys

def dec_to_bin(x):
    return int(bin(x)[2:])

def ones_in_N(n):
    str1 = bin(n)[2:]
    count = 0
    for char in str1:
	if char == '1':
	    count = count+1
    return count

def bin_seq(n):
    return [dec_to_bin(x) for x in xrange(n+1)]

def seq_sum(n):
    binseq = [ones_in_N(x) for x in xrange(n+1)]
    sumseq = []
    sum = 0
    for x in xrange(n+1):
	sum = sum+binseq[x]
	sumseq.append(sum)
    return sumseq

def game(S,N):
    moves = [x for x in xrange(1,N+1)]
    P1_moves = []
    P2_moves = []
    #Returns M[n] - Highest first move for Player 1's assured victory
    return 0
	
#Start
#For max n = 1000, we initialize sequence to maximum of 1,000,000. (Can actually do 1000*1001/2 = 1001000/2 = 500500)

S = seq_sum(1000000) #Calculated once, used for all n upto N
N = int(sys.argv[1])
