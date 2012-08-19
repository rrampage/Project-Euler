#Project Euler - Problem 11
#Language: Python2
#Time of Completion: 19-08-2012 14:52 IST

#Largest Product in a 20x20 array horizontally, vertically, diagonally

f = open("P11-data.txt","r")
a = []
#The file has 20 lines

for x in xrange(20):
    s = f.readline()
    s = s.split('\n')
    s = s[0].split()
    for x in xrange(len(s)):
	s[x] = int(s[x])
    a.append(s)
f.close()

def largest_prod(a):
    max_pro = 0
    #Linear search:
    for x in xrange(len(a)):
        for y in xrange(len(a[0])-3):
            prod = a[x][y]*a[x][y+1]*a[x][y+2]*a[x][y+3]
            if prod > max_pro :
                max_pro = prod
    for x in xrange(len(a)-3):
        for y in xrange(len(a)):
            prod = a[x][y]*a[x+1][y]*a[x+2][y]*a[x+3][y]
            if prod > max_pro :
                max_pro = prod
    for x in xrange(len(a)-3):
        for y in xrange(len(a[0])-4):
            prod = a[x][y]*a[x+1][y+1]*a[x+2][y+2]*a[x+3][y+3]
            if prod > max_pro :
                max_pro = prod
        for y in xrange(len(a)-3):
            prod = a[x][19-y]*a[x+1][18-y]*a[x+2][17-y]*a[x+3][16-y]
            if prod > max_pro :
                max_pro = prod
    return max_pro

print largest_prod(a)