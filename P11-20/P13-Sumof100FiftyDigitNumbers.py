#Project Euler - Problem 13
#Language: Python2
#Time of Completion: 19-08-2012 17:47 IST

#Sum of a 100 50-digit numbers

f = open("P13-Data.txt","r")
a = []
#The file has 100 lines

for x in xrange(100):
    s = f.readline()
    s = s.split('\n')
    s = s[0].split()
    for x in xrange(len(s)):
	s = int(s[0])
    a.append(s)
f.close()

print len(a)
print sum(a)