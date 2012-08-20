#Project Euler - Problem 18
#Language: Python2
#Time of Completion: 20-08-2012 14:00 IST

#Maximum Sum Path from top to bottom of a Triangle

#----IMPORT SPACE-------#
import time

lines = []
for line in open("P18-Data.txt").read().strip().split('\n'):
    lines.append(map(int, line.split()))

def maxSumPath(a):
    if len(a) == 1 :
	return a[0][0]
    else :
	b = []
	c = []
	for x in xrange(1,len(a)):
	    d = []
	    e = []
	    for y in xrange(len(a[x])-1):
		d.append(a[x][y])
		e.append(a[x][y+1])
	    b.append(d)
	    c.append(e)
	t = maxSumPath(b)
	u = maxSumPath(c)
	return a[0][0]+ max(t,u)

#print maxSumPath(a)


def test(line, index):
    global cache
    if line > len(lines)-1:
        return 0
    key = str(line) + "|" + str(index)
    if not key in cache:
        cache[key] = lines[line][index] + max(test(line+1, index), test(line+1, index+1))
    return cache[key]

time_start = time.time()
cache = {}
print "highest path sum", test(0, 0)
time_end = time.time()
print "time taken", time_end-time_start

