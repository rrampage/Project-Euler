#Project Euler - Problem 22
#Language: Python2
#Time of Completion: 21-08-2012 02:10 IST

#Name Weights!

#----IMPORT SPACE-------#

d = dict(A=1,B=2,C=3,D=4,E=5,F=6,G=7,H=8,I=9,J=10,K=11,L=12,M=13,N=14,O=15,P=16,Q=17,R=18,S=19,T=20,U=21,V=22,W=23,X=24,Y=25,Z=26)

lines = []
for line in open("P22-Data.txt","r").read().strip(",").split('\n'):
    lines.append(line.split("\""))
dat = lines[0]
dat = [dat[x] for x in xrange(1,len(dat),2)]
dat = sorted(dat)
sum2 = []
for x in xrange(len(dat)):
    sum1 = 0
    for char in xrange(len(dat[x])):
	sum1 = sum1 + d[dat[x][char]]
    sum2.append([dat[x],sum1])

sum3 = 0

for x in range(len(sum2)):
    sum3 = sum3 + (x+1)*sum2[x][1]

print sum3

#Really succinct code
#names = map(lambda x: x.strip('"'), open('P22-Data.txt').read().strip().split(','))
#names.sort()
#print sum(sum(map(lambda x: ord(x)-64, names[index])) * (index+1) for index in range(len(names)))
