#Project Euler - Problem 4
#Language: Python
#Time of Completion: 17-08-2012 21:37 IST

#Input: Array a containing product of all 3 digit numbers. Returns array of all palindromic numbers
def palindrome(a):
    d = []
    for x in a:
        if ((x%10 == int(x/100000)) and (int((x%100)/10) == int(x/10000)%10) and ((int((x%1000)/100) == int(x/1000)%10))):
            d.append(x)
    return d

#A set of all products of 3 digit numbers
a = [x*y for x in range(100,1000) for y in range(100,1000)]

d = palindrome(a)
print max(d)