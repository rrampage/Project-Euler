#Project Euler - Problem 19
#Language: Python2
#Time of Completion: 19-08-2012 22:14 IST

#Number of Sundays on the 1st of the month for the Twentieth Century

sun1 = 6 #1st Sunday of the 20th Century was 6th January
count = 0

for x in xrange(1901,2001):
    for y in xrange(1,13):
        if (y==4)or(y==6)or(y==9)or(y==11):
            days = 30
            if (sun1 == 1):
                count = count+1
                sun1 = 6
            else:
                sun1 = (sun1+28)-30
            if sun1 == 0:
                sun1 = 7
            
        if (y==2):
            if (x%4 != 0):
                days = 28
                if (sun1 == 1):
                    count = count+1
            else:
                if (sun1 == 1):
                    count = count+1
                    sun1 = 7
                else:
                    sun1 = sun1 - 1
        if (y==1) or (y==3) or (y==5) or (y==7) or (y==8) or (y==10) or (y==12) :
            if (sun1 == 1):
                count = count + 1
                sun1 = 5
            else:
                sun1 = (sun1 + 28)-31
                if sun1 == 0 :
                    sun1 = 7
                if sun1 == -1:
                    sun1 = 6

print count
print sun1 #The First sunday of the 21st Century