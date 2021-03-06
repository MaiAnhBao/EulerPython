import math
from fractions import Fraction
import time
import itertools
from operator import mul
from decimal import *
from EulerModule import *

getcontext().prec = 102

start = time.time()


    
#Project 72    
# def P(L):
#     phi = range(L+1)
#     for n in range(2, L+1):
#         if phi[n] == n:
#             for k in range(n, L+1, n):
#                 phi[k] -= phi[k] // n
#     return sum(phi) - 1
# 
# print "Project Euler 72 Solution =", P(1000000)
            
#Project 73

# a = set()
# for d in xrange(4,12000):
#     for n in xrange(int(d/3),int(d/2)):
#         a.add(Fraction(n,d))
#         print Fraction(n,d)
# print len(set)

#Problem 501



# _result = 0
# for i in primes_sieve(10**5):
#     for j in primes_sieve(10**10/i):
#         if 10**12 /i/j < j: break
#         if j > i:
#             _result += len(set(primes_sieve(10**12/ i/j))-set(primes_sieve(j)))
#             #print(i,j,set(primes_sieve(10**3/ i/j))-set(primes_sieve(j)),len(set(primes_sieve(10**3/ i/j))-set(primes_sieve(j))))
#         
# for i in primes_sieve(10000):
#     if i in primes_sieve(10**12/i**3):
#         _result += len(primes_sieve(10**12/i**3)) -1
#     else:
#         _result += len(primes_sieve(10**12/i**3))  
#     
# for i in primes_sieve(50):
#     if i**7 < 10**12:
#         _result += 1
# 
# print(_result)


#Problem 512



#Problem 521
def sieve_smpf(n):
    phi = [i for i in range(1,n+1)]
    i = 1
#    phi[0], phi[1] = 0,0
    while i < n:
        if phi[i] == i+1:
            for j in range(i,n,i+1):
                if phi[j] > i:
                    phi[j] = i+1
        i += 1
    return sum(phi)-1

#print(sieve_smpf(1000))
#print(sieve_smpf(1000) - sum(primes_sieve(1000)) + sum(primes_sieve(34)))
#10**7 : 3203714961609


# s = 5*10**11 * (5*10**11 +1)
# p = 1000
# for i in range(1,len(l)):
#     c = 1
#     s += l[i]
#     for j in range(i+1,10**12//l[i]+1):
#         t = j*l[i]
#         k = 0
#         while t%l[k] != 0:
#             k += 1
#         if k == i: 
#             s += t
#             c += 1
#     p += c*l[i]
# #            print(t)
# print(s , p, sum(l))
# print( (s- sum(l)+1)%10**9 + (p-sum(l))%10**9)
#Problem 70

#Problem 516

def getPrime23(n):
    phi=set()
    i = 4
    while 2**i < n:
        if checkPrime(2**i +1):
            phi.add(2**i+1)
        i += 1
    for j in range(40):
        for k in range(25):
            for l in range(17):
                if 2**j * 3**k * 5**l +1 > n: break
                if checkPrime(2**j * 3**k * 5**l + 1):
                    phi.add(2**j * 3**k * 5**l + 1)
#     phi.remove(2)
#     phi.remove(3)
#     phi.remove(5)
    phi.add(1)
    return phi

def forloop(l):
    r = 1
    for x in l:
        r *= x
    return r

def check(n,L):
    _sum = 0
    for  i in range(10):
        for j in range(10):
            for k in range(10):
                t = 2**i * 3**j * 5**k * n
                if 2**i * 3**j * 5**k * n < L:
                    _sum += t
    return _sum
_sum = 0

def checklist(l,N):
    for i in l:
        if i < N: return True
    return False

def res(n):
    l = getPrime23(n)
    print(l)
    phi = set() | l
    for i in range(10):
        l = set([t *2 for t in l])
        if not checklist(l, n): 
            break
        phi = phi | l
    l = getPrime23(n)    
    for i in range(5):
        l = set([t *3 for t in l])
        if not checklist(l, n): 
            break
        phi = phi | l
    l = getPrime23(n)    
    for i in range(6):
        l = set([t *5 for t in l])
        if not checklist(l, n): 
            break
        phi = phi | l
    l = getPrime23(n)    
    for i in range(6):
#        l = set([t * 2 for t in l])
        for j in range(6):
 #           l = set([t * 3 for t in l])
            for k in range(6):
                l = set([t * 2**i * 3**j * 5**k for t in l])
                if not checklist(l, n): 
                    break
                phi = phi | l
#             for k in range(2):
#                 l = set([t* 2**i * 3**j * 5**k for t in l])
#                 if checklist(l, n): break
#                 print(l)
#                 phi = phi | l
#            m.remove(i)
    return [i for i in phi if i<=n]
#print(sum(res(100)))

#Problem 513
def checkTriangle(a,b,c):
    if a+b>c: return True
    return False

def Find(n):
    #_count = 0
    dic = set()
    for c in range(2,n+1,2):
        v = c*c
        for a in range(1,c+1):
            t = 2*a*a-v
            for b in range(a,c+1,2):
                if not (a,b,c) in dic:
                    if checkTriangle(a, b, c) and isPerfectSquare((t + 2*b*b )/4):
                        #_count += 1
                        i = 1
                        while(i <= n//c):                            
                            dic.add((a*i,b*i,c*i))
                            i+=1
                        #print(a,b,c,' ------------ ',math.sqrt((t + 2*b*b )/4))
                    #print(a,b,c)
    return len(dic)# + 2*Pythagores(n//2+1)
#print(Find(1000))
# 149869
# 111.87836599349976

#Problem 47

def findFactor(n):
    s = set()
    while n%2 == 0:
        s.add(2)
        n = n//2
    for i in range(3,n//2+1,2):
        if n%i == 0:
            s.add(i)
            while n%i==0: n = n//i
    return s
# 
# t = 1
# num = 210
# while t != 3:
#     num += 1
#     if len(findFactor(num)) == 3:
#         print(num)
#         t += 1
#     else:
#         t = 0
# print(num)
# print(findFactor(210))

#Problem 80
#t = int(Decimal(2).sqrt()* 10**99)
# print(sum(map(int,str(t))))
# print(len(str((Decimal(2).sqrt()))))
# #print(sum(map(int,str(123))))
# 
# s = set([i*i for i in range(1,11)])
# 
# _sum = 0
# for i in range(2,100):
#     if not i in s:
#         t = int((Decimal(i).sqrt()) *10**99)#- int(Decimal(i).sqrt())
#         _sum += sum(map(int,str(t)))
# #        print(i,sum(map(int,str(t))))
# 
# print(_sum)
# 40886

#Problem 187
# _count = 0
# for i in primes_sieve(10000):
#      _count += len(primes_sieve(10**8//i))
# print(_count)

#Problem 91
# s = set()
# 
# for i in range(1,10):
#     for j in range(1,10):
#         s.add((0,i,j,0))
#         s.add((i,j,i,0))
#         s.add((0,i,j,i))
#         if j <= 2*i and i!=j and 2*i-j<6: 
#             s.add((i,i,j,2*i-j))
#             s.add((i,i,0,2*i))
#             s.add((i,i,2*i,0))
#             s.add((i,i,2*i-j,j))
# #3*n**2+ n**2 - n
# #        
# print(len(s) == (4*9*9 - 9))
# for a in range(1,10):
#     for b in range(1,10):
#         for c in range(1,10):
#             for d in range(1,10):
#                 if c*c + d*d == a*c + b*d and a!=c and a!=b and c!=d:
#                     s.add((a,b,c,d))
#                     #s.add((c,d,a,b))
# 
# 
#     
# 
# print(len(s))

#20558

#Problem 432
# for i in range(1000,2000):
#     if isPerfectSquare(sigma2(i)):
#         print(i,sigma2(i))


#Problem 74
# def getChain(n):
#     s = []
#     t = sumFactorialDigits(n)
#     s.append(n)
#     while not t in s:
#         s.append(t)
#         n= t
#         t = sumFactorialDigits(n)
#     return s
# 
# 
# _count = 0
# s = set()
# for n in range(100):
#     s = s & set(getChain(n))
# print(sorted(s))
        
#200000 51

#Problem 32
# s =set()
# for i in range(2,100):
#     if i<10: 
#         N = 1234
#     else:
#         N = 123
#     for j in range(N,10000//i):
#         if isPandigital(set(str(i*j) +str(i) +str(j))): s.add(i*j)
# print(sum(s))
# 45228

#Problem 170
# s = {'0','1','2','3','4','5','6','7','8','9'}
# 
# def getNum(s):
#     a = ''
#     for i in s:
#         a = a + i
#     return int(a)
# 
# for num in range(9876543210,9846371502,-1):
#     if set(str(num)) == s:
#         for i in range(20,40):
#             if i != 10:
#                 if num%i == 0:
#                     if set(str(i)) & set(str(num//i)) == None and set(str(i) + str(num//i)) == s:
#                         print(num,i,num//i)
#                         break

#Problem 47


# c = 1
# n = 10**6
# while c != 4:
#     n += 1
#     if len(getPrimeDivisor(n)) == 4 :
#         c+=1
#         print(n)
#     else: c = 0
# print(n)

#Problem 211
# s = 0
# try:
#     for i in range(2,100000):
#         if isPerfectSquare(sigma2(i)):
#             s += i
# #            print(i,getDivisor(i),sigma2(i))
# except OverflowError:
#     print(i)
# print(s)
#20000: 36445 + 18330

#Probelm 112
# def bouncy(n):
#     inc, dec ,s = False, False, str(n)
#     for i in range(len(s)-1):
#         if s[i] < s[i+1]: inc = True
#         elif s[i] > s[i+1]: dec = True
#         if  inc and dec: return True
#     return False
# 
# n = 21780
# p = 0.9
# b = n*p
# while p != 0.99:
#     n += 1
#     if bouncy(n): b += 1
#     p = b/n 
# print(n)  
# 1587000 

#Problem 119
# a = []
# 
# for b in range(2,100):
#     for e in range(2,10):
#         p = b**e
#         if sumDigits(p) == b: 
#             a.append(p)
#                 
# a.sort()
# print(a[29])
# 248155780267521

#Problem 120
# def SquareReminder(a):
#     s = [2*n*a%(a*a) for n in range(1,a)]
#     return max(s)
# 
# print(sum([SquareReminder(i) for i in range(3,1001)]))
# 333082500

#Problem 146
# _sum = 0
# for num in range(10,10**6,10):
#     if num%3==0 or num%7==0: continue
#     print(num)
#     t = num*num
#     if checkPrime(t+1):
#         if checkPrime(t+3):
#             if checkPrime(t+7):
#                 if checkPrime(t+9):
#                     if checkPrime(t+13):
#                         if checkPrime(t+27):
#                             _sum += num
# print(_sum)
s = 0
# for num in range(100,10**12,2100):
#     if isPerfectSquare(num):
#         print(num)
#         #if num % 7 == 0: continue
#         if checkPrime(num + 19) or checkPrime(num+21): continue
#         if checkPrime(num+1):
#             if checkPrime(num+3):
#                 if checkPrime(num+7):
#                     if checkPrime(num+9):
#                         if checkPrime(num+13):
#                             if checkPrime(num+27):
#                                 print(num)
#                                 s += num
# for num in range(1600,10**12,2100):
#     if isPerfectSquare(num):
#         print(num)
#         #if num % 7 == 0: continue
#         if checkPrime(num + 19) or checkPrime(num+21): continue
#         if checkPrime(num+1):
#             if checkPrime(num+3):
#                 if checkPrime(num+7):
#                     if checkPrime(num+9):
#                         if checkPrime(num+13):
#                             if checkPrime(num+27):
#                                 print(num)
#                                 s += num


#Problem 145
# def revNum(n):
#     return int(str(n)[::-1])
# 
# s = {'1','3','5','7','9'}
# r = {'2','4','6','8','0'}
# def checkRev(n):
#     for i in str(n):
#         if not i in s: return False
#     return True
# 
# print(20+100+600+18000+50000+20*30*30*30)
#10000001 : 720 + 68000

#Problem 13
# f = open('Euler13.txt','r')
# 
# mylines = [line.rstrip('\n') for line in f]
# 
# s = 0
# for l in mylines:
#     s += int(l[:11]) 
# print(str(s)[:10])

#problem 50
# p = primes_sieve(1000000)
# 
# t = []
# for i in range(len(p)):
#     s = p[i]
#     c = 1
#     pr, l = s, 1
#     for j in range(i+1,len(p)):
#         s += p[j]
#         c+=1
#         #print(s)
#         if s > 1000000: break
#         if checkPrime(s): 
#              pr, l = s, c
#     t.append((pr,l))
#print(t)

#print(max(t, key = lambda item:item[1]))

#Problem 43
# s = []
# for i in range(500,600):
#     if i % 11 == 0:
#         s.append(i)
# p = []
# for i in s:
#     t = i%100
#     for j in range(0,10):
#         if str(j) in set(str(i)): continue
#         if (t*10 + j) % 13 == 0:
#             p.append(i*10+j)
# q = []
# for i in p:
#     t = i % 100
#     for j in range(0,10):
#         if str(j) in set(str(i)): continue
#         if (t*10+j) % 17 == 0:
#             q.append(i*10+j)
# a =[]
# for i in q:
#     t = int(str(i)[:2])
#     for j in range(0,10):
#         if str(j) in set(str(i)): continue
#         if (j*100 + t) % 7 == 0:
#             a.append(j*10**5 + i)
# #print(a)
# b = []
# for i in a:
#     for j in range(0,10):
#         if str(j) in set(str(i)): continue
#         b.append(j*10**6+i)
# #print(b)
# c = []
# for i in b:
#     if len(str(i)) == 6: 
#         t = int(str(i)[:1])
#         for j in range(0,10):
#             if str(j) in set(str(i) + '0'): continue
#             if (j*100+t)%3==0:
#                 c.append(j*10**7+i)
#     else:
#         t = int(str(i)[:2])
#         for j in range(0,10):
#             if str(j) in set(str(i)): continue
#             if (j*100+t)%3==0:
#                 c.append(j*10**7+i)
# print(c)
# d = []
# for i in c:
#     if len(str(i)) == 7: 
#         t = int(str(i)[:1])
#         for j in range(0,10):
#             if str(j) in set(str(i) + '0'): continue
#             if (j*100+t)%2==0:
#                 d.append(j*10**8+i)
#     else:
#         t = int(str(i)[:2])
#         for j in range(0,10):
#             if str(j) in set(str(i)): continue
#             if (j*100+t)%2==0:
#                 d.append(j*10**8+i)
# print(d)
# e = []
# for i in d:
#     for j in range(0,10):
#         if str(j) in set(str(i)): continue
#         e.append(j*10**9+i)
# print(e,'\n',sum(e))

#Problem 347
def LI2P(a,b,N):
    s = 0
    t = int(math.log(N)/math.log(a))
    v = int(math.log(N)/math.log(b))
    for i in range(1,t+1):
        p = a**i
        for j in range(1,v+1):
            p *= b
            if p <= N:
                if s < p:
                    s = p
            else: break
    return s

# l =primes_sieve(100000)
# s = set()
# for i in l:
#     for j in l:
#         if j >i and j < 100000//i:
#             s.add(LI2P(i, j, 100000))
#              
# print(sum(s))

print(sum([i*i for i in range(0,10)])*9**15 %10**9)
end = time.time()
print(end-start)