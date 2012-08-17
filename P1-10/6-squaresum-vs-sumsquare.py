#Project Euler - Problem 6
#Language: Python2
#Time of Completion: 18-08-2012  IST

#Square of sum vs Sum of squares

#-----IMPORT SPACE-----------#

import sys

def sumOfSquares(n):
    """Gives sum of squares of first n natural numbers. Uses the induction formula"""
    n = int(n)
    return n*(n+1)*(2*n+1)/6

def squareOfSum(n):
    """Gives square of the sum of the first n natural numbers. Uses the Induction formula"""
    n = int(n)
    return n*n*(n+1)*(n+1)/4

def calculate(n):
    """Calculates and prints final answer"""
    print squareOfSum(n)-sumOfSquares(n)

calculate(sys.argv[1])