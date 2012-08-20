#Project Euler - Problem 25
#Language: Python2
#Time of Completion: 20-08-2012 15:28 IST

#First Fibonacci term having 1000 digits

#----IMPORT SPACE-------#

inp = 1
out = 1
count = 2
tmp = 0

while (out<10**999):
    t = inp
    inp = out
    out = t + inp
    count = count +1

print count