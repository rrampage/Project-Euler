#Project Euler - Problem 67
#Language: Python2
#Time of Completion: 20-08-2012 15:00 IST

#Maximum Sum Path from top to bottom of a Triangle

#----IMPORT SPACE-------#
import time

lines = []
for line in open("P67-Data.txt").read().strip().split('\n'):
    lines.append(map(int, line.split()))

def test(line, index):
    global cache
    if line > len(lines)-1:
        return 0
    key = str(line) + "|" + str(index)
    if not key in cache:
        cache[key] = lines[line][index] + max(test(line+1, index), test(line+1, index+1))
    return cache[key]

def bottomUp(lines):
    c = lines
    for x in xrange(1,len(c)):
	for y in xrange(len(c[-x])-1):
	    c[-x-1][y] = c[-x-1][y] + max(c[-x][y],c[-x][y+1])
    return c[0][0]

time_start = time.time()
cache = {}
#print "highest path sum", test(0, 0)
print "Highest Sum Path"+ str(bottomUp(lines))
time_end = time.time()
print "time taken", time_end-time_start
