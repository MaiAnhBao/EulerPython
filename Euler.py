import math
import time
from EulerModules import *
#import threading
import itertools
from cmath import log10
from _ast import Num
from macpath import join
import string
from decimal import *
from fractions import gcd
from math import factorial
from time import sleep
getcontext().prec = 100
import threading
from queue import Queue
import datetime
from functools import reduce
#from itertools import chain
#from timeit import timeit
start = time.time()

def checkPrime(n):
    if n <= 0:
        return False
    elif n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i == 0:
                return False
        return True
# 
def primes_sieve(limit):
    limitn = limit+1
    primes = dict()
    for i in range(2, limitn): primes[i] = True
 
    for i in primes:
        factors = range(i,limitn, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i]==True]
# 
# def countDiv(n):
#     _count = 0
#     for i in range(1,n+1):
#         if n%i == 0:
#             _count += 1
#     return _count

# listPrime = primes_sieve(10**6)
# print(listPrime)

# _result = 0
# for i in listPrime:
#     for j in listPrime:
#         if 10**12/i/j > j:
#             print(primes_sieve(int(10**12/i/j)))
#             _result += len(primes_sieve(int(10**12/i/j))) - len(primes_sieve(j))  
#                         #_result += 1
# print(_result)        
#for i in range(1,1000000):
#    if countDiv(i) == countDiv(i+1):
#        _result += 1
#        print(_result,i)
       
#print(_result)

#Problem 179

# L = 10**7
# 
# n = [0]*(L)
# for i in range(2, L//2):
#     for j in range(i*2, L, i):
#         n[j] += 1
# 
# print("Consecutive divisors =", sum(n[i] == n[i - 1] for i in range(3, L)))

#Problem 16

# L = 2**1000
# _sum = 0
# while L>=1:
#     _sum += L%10
#     L = L // 10
#    
# print(_sum)                      

#Problem 15

# import math
# print( math.ceil((1000 - 1 + math.log10(5)/2)/math.log10((1+math.sqrt(5))/2)) )

#Problem 27

# listPrime = [x for x in range(2,1000) if checkPrime(x)]
#  
# _max = 0
# for b in listPrime:
#     for a in range(-b,b,2):
#         n = 1        
#         while checkPrime(n*n + a*n + b)==1: 
#             n += 1
#         if n > _max: 
#             _max = n
#             p = a*b
#          
# print(p,_max) 

#Problem 92

# L = 10**7
# 
# def SquareDigit(n):
#     _sum = 0
#     while n>=1:
#         _sum += (n%10)**2
#         n = n//10
#     return _sum
#  
# def getList(n):
#     a = [n]
#     while SquareDigit(n) > 1 and SquareDigit(n) != 89:
#         n = SquareDigit(n)
#         a.append(n)
#     a.append(SquareDigit(n))    
#     return a       
#          
# _count = 0
# for i in range(1,L):
#     if 89 in getList(i):
#         _count += 1
#         
# print(_count)        

#Problem 87

# L = 50000000
# list1 = [x for x in range(int(math.sqrt(L))) if checkPrime(x)]
# 
# list2 = set()
# 
# for a in list1:
#     for b in list1:
#         _sum = a**4 + b**3
#         if _sum >= L:
#             break
#         for c in list1:
#             _num = _sum + c**2
#             if _num >= L:
#                 break
#             list2.add(_num)
#             
# print(len(list2))

#Problem 203

# def nCr(n,r):
#     f = math.factorial
#     return f(n) // f(r) // f(n-r)
# 
# _list =  [x**2 for x in range(10) if checkPrime(x)]
# 
# def checkFQ(n):
#     for i in _list:
#         if n % i == 0:
#             return False
#     return True
# 
# _set = set()
# 
# for i in range(50):
#     for j in range(i):
#         _set.add(nCr(i,j))
#     
# print(sum(x for x in _set if checkFQ(x) == True))

#Problem 35

# def filterPrime(n):
#     if set(str(n)) & {'2','4','5','6','8','0'}:
#         return False
#     return True
# 
# def checkRotate(n):
#     s = str(n)
#     listRotate = [int(s[i:] + s[:i]) for i in range(len(s))]
#     for i in listRotate:
#         if checkPrime(i) == 0:
#             return False
#     return True    

# listPrime = [x for x in range(100,1000000) if checkPrime(x) and filterPrime(x)]
# 
# print(len(listPrime))
# 
# result = [x for x in listPrime if checkRotate(x)]
# 
# print(len(result) + 13)        

# palindrom = {'1','2','3','4','5','6','7','8','9'}
# 
# def Fibo(n):
#     a, b = 1, 1
#     for i in range(n-1):
#         a, b = b, a+b 
#     return a
# 
# def getLeft(n):
#     _list = set(str(n)[:9]) 
#     return _list.symmetric_difference(palindrom) == set()
# 
# def getRight(n):
#     _list = set(str(n)[-9:])
#     return _list.symmetric_difference(palindrom) == set()

# k = 1
# a,b = 1,1
# while not getLeft(a) or not getRight(a):
#     a, b = b, (a+b) 
#     k += 1 
#     
# print(k)    

#Problem 123
# listPrime = [x for x in range(300000) if checkPrime(x)]
# 
# for k in range(7000,len(listPrime),2):
#     if 2* (k+1) * listPrime[k] > 10**10:
#         print(k + 1,listPrime[k],2* (k+1) * listPrime[k])
#         break
    
#Problem 124    
# listPrime = [x for x in range(100000) if checkPrime(x)]
# def getRad(n):    
#     result = 1
#     for i in listPrime:
#         if n%i == 0:
#             result *= i
#             n = n //i 
#     return result
# 
# E = [[getRad(x),x] for x in range(1,100000)]
# 
# print(sorted(E)[0],sorted(E)[9998])

#Problem 57
# _t = [1,1]
# 
# def getNext(l):
#     return (l[0]+2*l[1],l[0]+l[1])
# 
# _result = 0
# t = 1
# while t<1000:
#     if int(math.log10(getNext(_t)[0])) > int(math.log10(getNext(_t)[1])):
#         _result += 1
#         print(getNext(_t)[0],getNext(_t)[1])
#     t += 1
#     _t =  getNext(_t)
# 
# print(_result)

# listPenta = [] #[x*(3*x-1)//2 for x in range(1,10000)]
# 
# for i in range(len(listPenta)):
#     for j in range(i+1,len(listPenta)):
#         if listPenta[j]-listPenta[i] in listPenta and listPenta[j]+listPenta[i] in listPenta:
#             print(i+1,j+1)
#             break   
    
#listPrime = [x for x in range(5 * 10**7) if checkPrime(x)]    
#187
# count = 0    
# for a in range(2,5* 10**7):
#     for b in range(a,10**8 // a):
#         if checkPrime(b) and checkPrime(a):
#             count += 1
# 
# print(count)

#206
# def match(n):
#     s = str(n)
#     return not all(int(s[x*2]) == x+1 for x in range(9))
# 
# n = 138902663    # sqrt(19293949596979899)
# while match(n*n): n -= 2
# 
# print( "Project Euler 206 Solution =", n*10)            

# count = 0
# for a in range(1000,10000):
#     for b in range(10000-a):
#         for c in range(10000-a-b):
#             if (1-2*a)**3 == 27*(a*a - b*b*c):
#                 count += 1
#                 print(a,b,c)
# print(count)      

# from fractions import gcd
# 
# def PowerTwo(n):
#     return len(str(bin(n))) - str(bin(n)).rfind('1') - 1
# 
def maxPrime(n):
    i = 2
    while i * i <= n:
        while n % i == 0:
            n = n // i
        if n ==1: return i
        i = i + 1
    return n
 
def totient(n):
    if n == 1: return 1
    elif checkPrime(n): return n-1
    else:
        p = maxPrime(n)
        _result = n* (p-1)//p
        while n>1: 
            while n%p == 0:
                n = n//p
            if n == 1: break
            p = maxPrime(n)
            _result = _result * (p-1)//p
        return _result

#Problem 243
# for d in range(300000,400000):
#     if totient(d)/(d-1) < 15499/94744:
#         print(d)
#         break

#Problem 214

# def chainTotient(n):
#     if n == 1: return 1
#     else:
#         r = 2
#         while n > 2:
#             r += 1
#             n = totient(n)
#         return r

# _result = 0
# for num in range(10000001,40000001,2):
#     if checkPrime(num) == True:
#         p = PowerTwo(num - 1)
#         t = (num - 1)// 2**p
#           
#         if chainTotient( 2**(p-1) * totient(t) ) == 23:
#             _result += num
#             print(num)
# print(_result + 28702671)        
#1677366278943

#Problem 512

def f(n):
    if n%2 == 0: return 0
    return totient(n)
 
def g(n):
    _sum = 0
    for i in range(5*10**7+1,n+1,2):
        _sum += f(i)
    return _sum

# phi = sieve_totient(10**7)
# print(sum([phi[i] for i in range(10**7) if  i%2 == 1]))
#10**7 20264235150261
# s = 0
# for i in range(6*10**7+1,10**8,2):
#     s += (totient(i) % (5*10**8))
#     print(i)
# print(s)
# 10**7 to 3*10**7 to 6*10**7: 162113895981154 + 547134393399774


#print(sum([i for i in sieve_totient(10**7) if i%2==1]))
#print(g(10**8))

# n = 10**8
# phi = [0 for j in range(n)]
#xi = [0 for j in range(int(n/2),n)]

# def summarum(phi):
#     n = 10**8
#     phi = [0 for j in range(n)]
#     s = 0
#     phi[1] = 1
# 
#     i = 2
#     while i < n:
#         if phi[i] == 0:
#             phi[i] = i - 1
#             j = 2
# 
#             while j * i < n:
#                 if phi[j] != 0:
#                     q = j
#                     f = i - 1
#                     while q % i == 0:
#                         f *= i
#                         q //= i
#                     phi[i * j] = f * phi[q]
#                 j += 1
#         s += phi[i]
#         i += 1
#     return sum(phi[i] for i in range(len(phi)) if i%2 == 1)

#print(summarum(phi))
#506611649  + 50154048544 + 5015399109066
#506605921933035 5*10**7

#Problem 69
# _max = 0            
# result = 0
# for num in range(2,10**6):
#     if _max < num / totient(num):
#         _max = num / totient(num)
#         result = num
#         print(num)
#  
# print(result,_max)

#Problem 51
# def Replace(n,t):
#     c = 0
#     for d in '0123456789':
#         p = int(str(n).replace(str(t), d))
#         if checkPrime(p) and p>100000: 
#             c += 1
#           #  print(p)
#     return c==8
# 
# count_ = 0
# for num in range(100000,999999):
#     if checkPrime(num):
#         for t in range(4):
#             if str(num).count(str(t)) == 3:
#                 if num % 10 != int(t):
#                     if Replace(num, str(t)):
#                         print(num)
#                         break
            
#problem 56            
# def sum_digits3(n):
#     r = 0
#     while n:
#         r, n = r + n % 10, n // 10
#     return r# print(sum_digits3(123456))
# _max = 0
# for a in range(90,100):
#     for b in range(90,100):
#         if sum_digits3(a**b) > _max:
#             _max = sum_digits3(a**b)
# print(_max)            

#Problem 60
#listPrime = [x for x in range(1000) if checkPrime(x)]

# list1 = []
# for x in listPrime:
#     if checkPrime(int(str(3) + str(x))) and checkPrime(int(str(x) + str(3))):
#         list1.append(x)
#  
# list2 = []
# for x in listPrime:
#     if checkPrime(int(str(7) + str(x))) and checkPrime(int(str(x) + str(7))):
#         list2.append(x)
         
# print(set(list1).intersection(set(list2)))

# for p in primes_sieve(10000):
#     chain = []
#     chain += [p]
#     for pp in primes_sieve(10000):
#         if pp > chain[-1] and all([checkPrime(int(str(check[0]) + str(check[1]))) for check in itertools.permutations(chain + [pp],2)]):
#             #print(checkPrime(int(str(check[0]) + str(check[1]))) for check in itertools.permutations(chain + [pp],2))
#             chain += [pp] 
#         if len(chain) == 4: 
#             print(chain)
#             break
    #if len(chain) == 4: break
# a = [[11, 23, 743, 1871],[19, 31, 181, 9679],[23, 47, 1481, 4211],
# [43, 97, 1381, 8521],[89, 107, 1061, 4973],[467, 587, 617, 6323],
# [1283, 1619, 4127, 7949]
# ]    
# for tup in a:
#     for p in primes_sieve(10000):
#         print(all([checkPrime(int(str(check[0]) + str(check[1]) )) for check in itertools.permutations(tup + [p],2)]))
#         if p > tup[-1] and all([checkPrime(int(str(check[0]) + str(check[1]) )) for check in itertools.permutations(tup + [p],2)]):
#             tup += [p]
#             print(tup)
            
#Problem 58
# a = [[x*x,x*x - x + 1,x*x-2*x+2,x*x-3*x+3] for x in range(3,30000,2)]
# 
# _count = 0
# n = 1
# ratio = 1
# 
# for tup in a:
# #    print(tup)
#     for num in tup:
#         if checkPrime(num):
#             _count += 1
# #            print(num)            
#     n += 2
#     ratio = _count/(2*n-1)        
#     if ratio < 0.1: break
# 
# print(n,ratio,_count)

# def sieve_mobius(limit):
#     limitn = limit+1
#     primes = dict()
#     primes[1] = 1
#     for i in range(2, limitn): primes[i] = 1
# 
#     for i in primes:
#         if i>1:
#             factors = range(i*i,limitn, i*i)
#             for f in factors[0:]:
#                 primes[f] = 0
#     return primes

#print(sieve_mobius(200))

#Problem 521

def sieves_smpf(n):
    phi = [i for i in range(n+1)]   
    for k in range(2,(n+1)//2):
        phi[2*k] = 2
    i = 2
    while i < n:
        if phi[i] == i:
            for j in range(i,n+1,i):
                if phi[j] > i:
                    phi[j] = i            
     
        i +=1
    phi = list(filter((2).__ne__,phi))
    phi = list(filter((3).__ne__,phi))
    return sum(phi) + n + n//2



#10^7: 714961609

# i = 1
# r = 1
# s = 0
# while i*i < 1000:    
#     while not checkPrime(i):
#         i += 1
#     if i*i > 1000: break
#     s += i* int(1000/i * r + 0.5)
#     r = (1-1/i)*r
#     i += 1
#  
# print(s)
# s1 = 0
# for i in range(35,1001):
#     if checkPrime(i):
#         s1+=i
# print(s1 + s)
# _sum = sieves_smpf(10**7) % 10**9

# def is_prime(n):
#     if n <= 3:
#         return n >= 2
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     for i in range(5, int(n ** 0.5) + 1, 6):
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#     return True
# 
# 
# def smpf(n):
#     l = primes_sieve(10**6)
#     if n%2 == 0:
#         return 2
#     elif n%3 == 0:
#         return 3
#     elif is_prime(n):
#         return n
#     for i in l:
#         if n%i == 0:
#             return i
#     return n

# _sum = 0 ***
# f = open('Primes.txt','a')
# for num in range(8*10**7 + 1,10**8,2):
#     if checkPrime(num):
#         #_sum += num
#         f.write(str(num) + ' ')
# print(num)

# _sum = 0
# for i in range(10**7+5*10**7 + 1,10**7+10**8,2):
#     if is_prime(i):
#         _sum += i % 10**9
#     _sum += smpf(i)
#     _sum = _sum % 10**9
#       
#     print(_sum)
#190509578 + 342907138 + 795224457 + 646608328

#Problem 37
# def checkLeft(n):
#     while n>=1:
#         if not is_prime(n): return False
#         n = n//10
#     return True
# 
# def checkRight(n):
#     while n >= 1:
#         if not is_prime(n): return False
#         if str(n)[1:] != '':
#             n = int(str(n)[1:])
#         else: 
#             n=0
#     return True
# 
# _sum = 0
# t = 0
# num = 11
# while t < 11:
#     if checkLeft(num) and checkRight(num):
#         t += 1
#         _sum += num
#         print(num)
#     num += 2
# print(_sum)

#problem 63
# def checkDigitCount(n):
#     return (int(n**(1/len(str(n)))+ 0.5))**len(str(n)) == n
# 
# c = 0
# num = 2
# while num<10**8:
#     if checkDigitCount(num):
#         c += 1
#         print(c,num)
#     num += 1
#     
# print(c) 33

# def sieve_totient(n):
#     phi = [0 for i in range(n)]
#     phi[1] = 1
#     i = 2
#     while i<n:
#         if phi[i] == 0: 
#             phi[i] = i-1
#             j = 2
#             while j*i<n:
#                 if phi[j] != 0:
#                     q = j
#                     f = i-1
#                     while q%i == 0:
#                         f*=i
#                         q //= i
#                     phi[i*j] = f * phi[q]
#                 j += 1
#         i += 1
#     return sum([phi[j] for j in range(n) if j%2 ==1])

#20264235150261
# _sum = 0
# for num in range(10**7+1,5*10**8,2):
#     _sum += totient(num)
# print(_sum)

#Problem 70
# num = 0
# r = 3
# l = sieve_totient(10**7)
# for i in range(10**7-1,10**6,-2):
#     if not is_prime(i):
#         l1 = [int(''.join(k)) for k in itertools.permutations(str(i))]
#         if l[i] in l1:
#             print(i,l[i])
#             if r > i/l[i]:
#                 r = i/l[i]
#                 num = i
# print(r,num)
# r = 3
# num = 0
# for i in range(2000,5000):
#     if is_prime(i):
#         for j in range(i+1,5000):
#             if is_prime(j):
#                 if i*j > 10**7: break
#                 phi = (i-1)*(j-1)
#                 l1 = [int(''.join(k)) for k in itertools.permutations(str(i*j))]
#                 if phi in l1:
#                     if r > i*j/phi:
#                         r = i*j/phi
#                         num = i*j
# print(num,r,totient(num))
                    
#print(sieve_totient(10**7))

#Problem 513

def checkTriangle(a,b,c):
    if a+b>c: return True
    return False
   
def isPerfectSquare(n):
    tst = int(math.sqrt(n) + 0.5)
    return tst*tst == n
   
def findTriangle(n):
    _count = 0
    for c in range(2,n+1,2):
        #print(c)
        for a in range(1,c+1):
            p = 2*a*a - c*c
            for b in range(a,c+1,2):
                if checkTriangle(a,b,c) and isPerfectSquare((p + 2*b*b)/4):
                    _count += 1
                    #print(a,b,c)
    return _count
#print(findTriangle(100000))
#1000: 149869

# def getPythagores(N):
#     s =set()
#     for n in range(1,int((N/2)**0.5)):
#         for m in range(n+1,N,2):
#             if m*m+n*n > N: break
#             if gcd(m, n) == 1:
#                 s.add((m*m-n*n,2*m*n,m*m+n*n))
#     return s
# 
#  
# def getTriangle(N):
#     s = 0
#     l = getPythagores(N)
#     for i in l:
#         s += N//(max(i))
#         if 2*min(i) > max(i):
#             s += 2* N//(2*min(i))
#         else:
#             s +=  N//(2*min(i))
#     return s
# print(getTriangle(1000))  

#Problem 42       
# letter_count = dict(zip(string.ascii_uppercase, range(1,27)))
#  
def readWord(w):
    s = 0
    for c in w:
        s += letter_count[c]
#        print(c,letter_count[c])
    return s
#  
# s = set()
# for i in range(1,27):
#     s.add(i*(i+1)//2)
#  
# f = open('p042_words.txt','r')
# line = f.read()
# #print(line)
# _count = 0
# while line != '':
#     p1 = line.find('"')
#     p2 = line.find('"',p1+1)
#     w = line[p1+1:p2]
#     line = line[p2+1:]
#     t = readWord(w)
#     if t in s: _count += 1   
# print(_count)

#Problem 48
# _sum = 0
# for i in range(1,1001):
#     _sum += (i**i % 10**10)
# print(_sum %10**10)

#Problem 80
#print(sum(map(int, str(12323400000000))))

#print(sum(map(int,str(int((Decimal(2).sqrt() - 1)*10**99)))))
# s = set([i*i for i in range(1,11)])
# c = 0
# _sum = 0
# for i in range(2,100):
#     if not i in s:
#         t = int((Decimal(i).sqrt() - int(Decimal(i).sqrt()))*10**99)
#         print(sum(map(int, str(t))),i)
#         _sum += sum(map(int, str(t)))
# print(_sum)

#Problem 71
# _res = 2/5
# _don, _nom = 2, 5
#  
# for i in range(10**6,10**6-7,-1):
#     if int(i*3/7)/i < 3/7 and int(i*3/7)/i > _res:
#         _res = int(i*3/7)/i
#         _don, _nom = i, int(i*3/7)
# print(_nom)
#428570

#Problem 63
# s = 0
# for n in range(1, 10):
#     s += int(1 / (1 - math.log10(n)))
# print(s)
#49

#Problem 41
# _max = 0
# lst = [i for i in range(1,8)]
# s = set(itertools.permutations(lst))
# for l in s:
#     t = int(''.join(str(i) for i in l))
#     print(t)
#     if checkPrime(t):
#         if t>_max: _max = t
# print(_max)
#7652413

#Problem 33
# def subsList(a,b):
#     return [item for item in a if item not in b]
# for i in range(10,100):
#     for j in range(i,100):
#         k = set(str(i)) & set(str(j))
#         if k != set() and k!={'0'}:
#             a = subsList(set(str(i)),k)
#             b = subsList(set(str(j)),k)
#             if a != [] and b!= []:
#                 p = int(''.join(i for i in a))
#                 q = int(''.join(i for i in b))
#                 if q!=0:
#                     if p/q == i/j:
#                         print(i,j)
#100

#Problem 484
# def getPower(n):
#     s = dict()
#     for i in range(2,n//2+1):
#         if checkPrime(i) and n%i==0:
#             _c = 0
#             while n%i==0:
#                 n = n//i
#                 _c += 1
#             s[i] = _c
#     return s
# print(getPower(20))
# 
# def arthDer(n):
#     if checkPrime(n): return 1
#     else: 
#         for i in range(2,n//2+1):
#             if n%i==0: break
#         return arthDer(i)*n//i + i*arthDer(n//i)
# _sum = 0
# 
# for i in range(2,10**2+1):
#     _sum += gcd(i,arthDer(i)) 
# print(_sum)

#Problem 23
# def sumDivisor(n):
#     s = 0
#     for i in range(1,n//2+1):
#         if n%i==0:
#             s+=i
#     return s
# 
# def FindAbundant(n):
#     p = set()
#     for i in range(12,n):
#         if i < sumDivisor(i):
#             p.add(i)
#     return p
# l = FindAbundant(28123)
# p = set()
# for x in l:
#     for y in l:
#         p.add(x+y)
# 
# print(sum([i for i in range(28123) if not i in p]))
# 4179871

#Problem 29
# print(len({a**b for a in range(2,101) for b in range(2,101)}))
# 9183

#Problem 73
# def ReduceFrac(a,b):
#     return (a//gcd(a,b),b//gcd(a,b))
# s = set()
# for d in range(4,12001):
#     for n in range(d//3+1,int(d/2+0.5)):
#         s.add(ReduceFrac(n, d))
# print(len(s))
# 7295372
# f = open('Primes.txt','a')
# for i in range(6*10**7+1,8*10**7,2):    
#     if checkPrime(i):
#         f.write(str(i) + ' ')

# s =set()
# for i in range(1,30000):
#     for j in range(i+1,30000):
#         if isPerfectSquare(i+j) and isPerfectSquare(j-i):
#             for k in range(j+1,30000):
#                 if isPerfectSquare(k+j) and isPerfectSquare(k-j):
#                     #if isPerfectSquare(k+i) and isPerfectSquare(k-i):
#                         s.add((i,j,k))
# print(s)

#Problem 381
def Primek(p):
    t = 0
    for i in range(1,p-1):
        if (p*i+1) %6 == 0: 
            t = (p*i+1)//6
            break 
    u, v = 0, 24%p
    for i in range(1,p-1):
        if (p*i+1) % v == 0: 
            u = p - (p*i+1) // v
            break
    return ((p-1)//2 + t + u)%p 


# s = 0
# for i in range(10**7+1,10**8,2):
#     if checkPrime(i):
#         s += Primek(i)
#         print(i)
#print(s)
# 10**7 1601954022810 10**7-10**8 138000989297012 : 139602943319822

#modulo =1 + 1 + (p-1)//2 + 

#Problem 513
def gcd3(a,b,c):
    return gcd(gcd(a,b),c)
# _count = 0
# s = set()
# for c in range(2,2501,2):
#     for a in range(1,c+1):
#         p = 2*a*a - c*c
#         for b in range(a,c+1,2):
#             if a+b > c and isPerfectSquare((2*b*b + p)//4):
#                 _count += 1
#                 t = gcd3(a, b, c)
#                 s.add((a//t,b//t,c//t))
#                 #print(a,b,c)
# print(_count)
# print(len(s),len(s)/_count)
# Problem 76
# target = 100
# ways = [1] + [0]*target
# 
# for n in range(1,100):
#     for i in range(n,101):
#         ways[i] += ways[i-n]
#     print(ways)
#         
# print(ways[100])
# 190569291

#Problem 39
# L, pmax, tmax = 1000,0,0
# for p in range(L//4*2, L+1, 2):
#     t = 0
#     for a in range(2, int(p/3.4142) + 1):
#         if  p*(p - 2*a) % (2*(p - a)) == 0: 
#             t += 1
#             if t >= tmax: tmax, pmax = t, p
# print(pmax)

#Problem 146
# s = 0
# for num in range(3*10**5,4*10**5,10):
#     if num%3 == 0 or num%7==0 or num%7==1 or num%13==0 or num%17==0: continue
#     #print(num)
#     sq = num * num
#     if checkPrime(sq+1) and checkPrime(sq+3) and checkPrime(sq+7) and checkPrime(sq+9) and checkPrime(sq+13) and checkPrime(num+27):
#         s += num
#         print(num)
# print(s)


#Problem 516

#Problem 43
# r = '0123456789'
# t = 10**6
# s = ''
# j = 9
# while j > 0:    
#     c = 0
#     while t - c*factorial(j)>0:
#         c += 1
#     t -= (c-1)*factorial(j)
#     j -= 1
#     s += str(c-1)
# print(s)
# u = ''
# for i in s:
#     c = 0
#     for j in u:        
#         if int(j) < int(i):
#             c += 1
#     k = 0
#     t = r[int(i) + c]
#     while t in u:
#         k += 1
#         t = r[int(i) + c + k]
#     u += r[int(i)+c + k]
#     
# print(u)

#Problem 81
# f = open ( 'p081_matrix.txt' , 'r')
# lines = [line.rstrip('\n') for line in f]
# m = [ list(map(int,line.split(','))) for line in lines]
# 
# l = len(m)
# 
# for i in range(l-2,-1,-1):
#     m[l-1][i] += m[l-1][i+1]
#     m[i][l-1] += m[i+1][l-1]
#     
# for i in range(l-2,-1,-1):
#     for j in range(l-2,-1,-1):
#         m[i][j] += min(m[i+1][j],m[i][j+1])
# 
# print(m[0][0])

#Problem 243
# p = primes_sieve(40)
# r = 15499/94744
# 
# s = 1
# t = 1
# for num in p:
#     s *= num
#     t *= (num-1)
#     for i in range(2,num):
#         if t*i/(s*i-1) <r:
#             print(s*i)
#             break  

#Problem 38
# for i in range(9182,9487):
#     if set(str(i) + str(i*2)) == {'1','2','3','4','5','6','7','8','9'}: 
#         print(str(i) + str(i*2))

#Problem 65
# s = []
# s.append(2)
# for k in range(1,34):
#     s.append(1)
#     s.append(2*k)
#     s.append(1)
# a = 0
# t = 0
# for i in range(len(s)):
#     u = (1,s[i])
#     for j in range(i-1,-1,-1):
#         u = (u[1],u[1]*s[j] + u[0])
#     a += u[1]
#     u = (u[1],u[0])
#     t += 1
#     
# print(a,t)    

# u = [1,s[99]]
# for j in range(98,-1,-1):
#     u = (u[1],u[1]*s[j] + u[0])
# print(sumDigits(u[1]))

# l = primes_sieve(1000)
# s = 5*10**3 * (5*10**3+1)
# #print(len(l))
# for i in range(1,len(l)):
#     for j in range(1,(10**6//l[i] + 1)):
#         t = l[i] * j
#         #print(t)
#  #       print(l[i],j,t)
#         k = 0
#         while t % l[k] != 0:
#  #          print(l[k])
#             k += 1
#         if k >= i:
#             #print(t)
#             s += t
#             #print(t)
# #            print(t)
#     #print(s)
# 
# 
# 
# print(s)         

#Problem 347
# def LI2p(a,b,N):
#     t = int(math.log(N)/math.log(a))
#     v = int(math.log(N)/math.log(b))
#     s = 0
#     for i in range(1,t+1):
#         p = a**i
#         for j in range(1,v+1):
#             p *= b
#             if p > N: break
#             if p > s: s = p
#     return s
# 
# t = int(10**(7/2))
# l = primes_sieve(t+1)
# s = 0
# for i in l:
#     for j in range(i+1,10**7//i+1):
#         if checkPrime(j):
#             s += LI2p(i, j, 10**7)
# print(s)
#11109800204052

#Problem 216
# s = 0 #(7, 17,31)
# for n in range(1008394,5*10**7):
#     if n%7==2 or n%7==5 or n%17==3 or n%17== 14 or n%23==9 or n%23==14 or n%31 ==4 or n%31==27: continue
#     if checkPrime(2*n*n-1):
#         s += 1
#         print(n,s)
# print(s)
#410367 62370 + 1008393 80160 + 1131059 15779

# print([(2*i*i-1) %31 for i in range(1,31)])
# print((2*14*14-1)%17)

#Problem 101
# def Lagrange(x,l):
#     s = 0
#     for i in range(len(l)):
#         t = l[i]
#         for j in range(len(l)):
#             if j != i:
#                 t *= (x-j)/(i-j)
#         s += t 
#     return s 
# 
# def u(n):
#     return  1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10
# 
# l = [u(n) for n in range(1,12)]
# print(len(l))
# 
# s = 0
# for i in range(1,len(l)):
#     p = l[:i:]
#     t = [Lagrange(j, p) for j in range(i+1)]
#     print(t)
#     s += int(Lagrange(i, p) + 0.5)
# print(s)
# 37076114526

#Problem 102
# def signLine(a,b,c,d,e,f): 
#     return (e-a)*(d-b)-(f-b)*(c-a)
# 
# def ckTr(a,b,c,d,e,f):
#     t = signLine(a, b, c, d, 0, 0)
#     t1 = signLine(a, b, c, d, e, f)
#     u = signLine(a, b, e, f, 0, 0)
#     u1 = signLine(a, b, e, f, c, d)
#     v = signLine(c, d, e, f, 0, 0)
#     v1 = signLine(c, d, e, f, a, b)
#     if t*t1 > 0 and u*u1>0 and v*v1>0:
#         return True
#     else:
#         return False
#     
# f = open('p102_triangles.txt','r')
# s = []
# l = [line.rstrip('\n') for line in f]
# 
# t = 0
# for tr in l:
#     k = [int(x) for x in tr.split(',')]
#     if ckTr(k[0],k[1],k[2],k[3],k[4],k[5]):
#         t += 1
# print(t)
# 228

#Problem 104
# i = 2749
# a,b = Fibo(2749),Fibo(2750) 
# while True:
#     if isPandigital(a % 10**9) and isPandigital(int(str(a)[0:9:])):
#         print(i)
#         break
#     i += 1
#     a, b = b, a+b
# 329468

#Problem 129
def A(n):
    if gcd(n, 10) != 1:
        return 0
    x,k = 1,1
    while x!= 0:
        x = (x*10+1)%n
        k += 1
    return k

# n = 1000001
# while A(n) < (10**6+1):
#     n += 2
# print(n)
# 1000023

#Problem 130
def B(n):
    if checkPrime(n): return False
    if gcd(n, 10) != 1: return False
    if (n-1) % A(n) == 0: return True
    else:
        return False

# i = 0
# s = 0
# n = 90
# while i<25:
#     if B(n):
#         s += n
#         i += 1
#     n += 1
# print(s)
# 149253

# Problem 132
# s = set()
# n = 5
# L = 10**9
# while len(s)<40:
#     if checkPrime(n) and pow(10, L, n) == 1:
#         s.add(n)
#     n += 2
# print(sum(s))
# 843296

#Problem 133
# l = primes_sieve(10**5)[2:]
# s = 5
# q = pow(10,20)
# t = pow(10,30)
# 
# s += sum(p for p in l if pow(10,t,p) != 1)
# print(s)
# 453647705

#Problem 157
#print(getDivisor(100))

def numDivisor(n):
    if checkPrime(n): return 2
    s,t = 1,0
    while n%2 == 0:
        t += 1
        n = n//2
    s = s*(t+1) 
    i = 3
    while n > 1:
        t = 0
        while n%i==0:
            n = n//i
            t += 1
        s = s* (t+1)
        i += 2
    return s

def Sol(n):
    s = 0
    for i in range(n+1):
        for j in range(n+1):
            t = int((2**i + 5**j) * 2**(n-i) * 5**(n-j))
            #print(t)
            #print(i,j,t,numDivisor(t))            
            s += (numDivisor(t))
#    print(numDivisor(10**n + 1))
    for i in range(1,n+1):
        for j in range(1,n+1):
            t = int((1 + 2**i * 5**j)* 2**(n-i) * 5**(n-j))
            #print(t)
            s += (numDivisor(t))
    
    return s

#print(sum(Sol(i) for i in range(1,10)))
# s = 0
# for i in range(1,10):
#     print(Sol(i))
#     s += Sol(i)
# print(s)
# 53490

#Problem 127
def Rad(n):
    s = 1
    if n%2 == 0: s*=2
    while n%2 == 0:
        n = n//2
    t = 3
    while n > 1:
        if n%t == 0: s*=t
        while n%t == 0:
            n = n//t
        t += 2
    return s

def Rad_Sieve(N):
    l = [1]*(N)
    for i in range(1,N):
        if l[i] == 1:
            l[i] = i
            for j in range(2*i,N,i):
                l[j] *= i   
    return l

# l = Rad_Sieve(12000 0)
# 
# s = 0
# for a in range(1,120000):
#     for b in range(a+1,120000-a):
#         if gcd(a,b) != 1: continue
#         if l[a] *l[b]*l[a+b] >= (a+b): continue
#         s += (a+b)
# print(s)
# 18407904
  
#Problem 266
# l = primes_sieve(190)
# s = reduce(lambda x,y:x*y,l)
# s = s//2
# t = int(s**0.5)
# for i in range(t+1,s,2):
#     if i%16 == 3 or i%16==5 or i%16==11 or i%16==13:
#         if isPerfectSquare(i*i - s):
#             print(i)
#             break

#Problem 105
def FirstCondition(s):
    _sum = [] 
    for i in range(1,len(s)):
        for r in set(itertools.combinations(s,i)):
            if sum(r) in _sum:
                return False
            else:
                _sum.append(sum(r))
    return True

def SecondCondition(s):
    for i in range(1,len(s)):
        for r in set(itertools.combinations(s,i)):
            p = s - set(r)
            for j in range(1,i):
                for q in set(itertools.combinations(p,j)):
                    if sum(q) > sum(r):
                        return False
    return True
        
# f = open ( 'p105_sets.txt' , 'r')
# lines = [line.rstrip('\n') for line in f]
# m = [list(map(int,line.split(','))) for line in lines]
# 
# _sum = 0
# for line in lines:
#     s = set(list(map(int,line.split(','))))
#     if FirstCondition(s) and SecondCondition(s):
#         _sum += sum(s)
# print(_sum)
# 73702

#Problem 108
def numSol(n):
    if checkPrime(n): return 2
    s = set()
    l = getDivisor(n)
    for x in l:
        for y in l:
            if gcd(x, y) != 1 or x>y: continue
            s.add((x,y))
    return len(s)

# n = 180180
# while True:
#     if numSol(n) > 1000:
#         print(n)
#         break
#     n += 1
#     print(n)
# 180180
    
#Problem 36
# def checkPalidrome(n):
#     return str(n) == str(n)[::-1]
# 
# def checkPalidrome2(n):
#     t = bin(n)
#     return str(t)[2::] == str(t)[:1:-1]
# 
# s = 0
# for n in range(10**6):
#     if checkPalidrome(n) and checkPalidrome2(n):
#         s+=n
# print(s)
# 872187

#Problem 47
# n = 78590
# nf = 4
# nc = 4
# ci = 1
# while ci != nc:
#     n += 1
#     if len(getPrimeDivisor(n)) == nf: ci+=1
#     else: ci = 0
#     print(n)
# print(n-nf+1) 

#Problem 211
def sigma2(n):
    return sum([i*i for i in getDivisor(n)])

def sieve_sigma2(n):
    l = [1]*n
    for i in range(2,n):
        for j in range(i,n,i):
            l[j] += (i)*(i)
    return l

# l = sieve_sigma2(6*10**7 + 4*10**6)
# s = 0
# for i in range(1,6*10**7 + 4*10**6):
#     if isPerfectSquare(l[i]):
#         s += i
#         print(i)
# print(s) 
#10**7 211234335
#2*10**7 458704650
#3*10**7 833095400
#6*10**7 1735803653
#1922364685

#Problem 118
s =  {'1','2','3','4','5','6','7','8','9'}
# for l in itertools.permutations(s):
#     print(l)
    
# t = 0
# for i in range(0,10):
#     for j in range(0,10):
#         for k in range(0,10):
#             if i+j+k <= 9:
#                 print(i,j,k)
#                 t += 1
# print(t)

#Problem 22
# letter_count = dict(zip(string.ascii_uppercase, range(1,27)))
# f = open ( 'p022_names.txt' , 'r')
# m = f.read()
# n = m.split('"')
# l = sorted([x for x in n if x!='' and x!=','])
# 
# s = 0
# for i in range(len(l)):
#     s += readWord(l[i]) * (i+1)
# print(s)
#871198282

#Problem 125
# pas = set()
# for i in range(1,10**4):
#     s = i*i
#     while s < 10**8:
#         i += 1
#         s += i*i
#         if isPalindrome(s):
#             pas.add(s)
# print(sum(pas))
# 2906969179

#Problem 136
# s ,t, c = 0, 0, 0
# n, m = 1, 1
# #while c <= 12:
# for n in range(1,100000):
#     for m in range(n+1,100000,2):
#         if m*m - n*n == 4*m*n + 1 or m*m - n*n == 4*m*n - 1 or 2*(m*m - n*n)+1 == 2*m*n or 2*(m*m - n*n) -1 == 2*m*n:
#             s += min(m*m - n*n, 2*m*n)
#             t += 1
#             c += 1
#             print(m*m - n*n, 2*m*n)
# print(s,t)
# 15 8
# 273 136
# 4895 2448
# 87841 43920
# 1576239 788120
# 28284465 14142232
# 507544127 253772064
#9107509825 4553754912

#Problem 66
#https://en.wikipedia.org/wiki/Chakravala_method

def Pell(N):
    y = 1
    x1 = int(N**0.5)+1
    k = x1*x1 - N*y*y
    while k != 1:
        m = 1
        s = m*m - N
        for t in range(N):
            if (x1+y*t) % abs(k) == 0:
                u = t*t - N 
                if abs(u) < abs(s):
                    m = t
                    s = u
        x = (x1*m + N*y)//abs(k)
        y = (x1 + y*m)//abs(k)
        k = (m*m-N)//k
        x1 = x
    return x

# l = [(Pell(N),N) for N in primes_sieve(1000) if N > 5]
# 
# print(max(l))
#661

#Problem 138
# x,y,t,s = 0, -1, 0, 0
# while t < 12:
#     x1 = -9*x -4*y + 4
#     y1 = -20*x -9*y + 8
#     x = x1
#     y = y1
#     t += 1
#     s += abs(y)
# print(s)
# 1118049290473932

# l = [x for x in primes_sieve(150) if x%4 == 1]
# 
# print(reduce(lambda x,y:x*y, l))

#Problem 134
# def ConnectPrime(p,q):
#     i = 0
#     d = int(math.log(p)) 
#     s = i*10**d + p
#     while s%q != 0:
#         i+=1
#         s = i*10**d + p
#     return s
# 
# l = primes_sieve(10**6)
# s = 0
# for i in range(2,len(l)-1):
#     s += ConnectPrime(l[i], l[i+1])
#     print(i,s)
# print(s)
#30405 2052779690346739152740

#Problem 136
# t = [0] * (50000001)
#  
# for i in range(1,50000001):
#     for j in range(1,50000001//i+1):
#         if (i+j)%4 == 0 and i > (i+j)//4:
#             t[i*j] += 1
#             #print(t[i*j])
# #             
# s = [i for i in t if i == 1]
# print(len(s))
# 2544559
end = time.time()
    
print(end-start)          