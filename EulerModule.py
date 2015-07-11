import math 
from math import factorial
from fractions import gcd

def checkPrime(n):
    if n < 0 or n == 1: return False
    elif n == 2: return True
    else:
        for i in range(2,int(math.sqrt(n)) + 1):
            if n%i == 0: return False
        return True
        
def primes_sieve(limit):
    limitn = limit+1
    primes = dict()
    for i in range(2, limitn): primes[i] = True

    for i in primes:
        factors = range(i,limitn, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i]==True]
    
def totient_sieve(n):
    s = 0
    phi = [0 for j in range(n+1)]
    phi[1] = 1
    i = 2
    while i < n:
        if phi[i] == 0:
            phi[i] = i - 1

            j = 2

            while j * i < n:
                if phi[j] != 0:
                    q = j
                    f = i - 1

                    while q % i == 0:
                        f *= i
                        q //= i

                    phi[i * j] = f * phi[q]
                j += 1
        s += phi[i]
        i += 1
    return phi

def getDivisor(n):
    s = []
    s += {n,1}
    for i in range(2,n//2+1):
        if n%i == 0:
            s.append(i)
    return s

def sigma2(n):
    if n == 1: 
        return 1
    if checkPrime(n):
        return n*n+1
    return sum([i*i for i in getDivisor(n)])

def isPerfectSquare(n):
    tst = int(math.sqrt(n) + 0.5)
    return tst*tst == n

def getPrimeDivisor(n):
    s = set()
    while n%2==0:
        s.add(2)
        n = n//2
    i = 3
    while n>1:
        if checkPrime(i):
            while n%i==0:
                s.add(i)
                n = n//i 
        i += 2
    return s

def maxPrime(n):
    if checkPrime(n): return n
    while n%2==0:
        n = n//2
    if n==1: return 2
    if n==3 or n==5:return n
    for num in range(3,n//3+1,2):
        if checkPrime(num):
            while n%num == 0:
                n = n//num
        
        if n == 1:
            return num
        
def totient(n):
    if checkPrime(n): return n-1
    t = maxPrime(n)
    print(t,n//t)
    return totient(n//t)*totient(t)

def sumFactorialDigits(n):
    return sum([factorial(int(x)) for x in str(n)])

s = {'1','2','3','4','5','6','7','8','9'}
def isPandigital(st):    
    return st == s #s.difference_update(set(str(n)) == None 

def Pythagores(N):
    _count = 0
    M = int(math.sqrt((N+1)//2))
    for n in range(1,M):
        P = int(math.sqrt(N-n*n))+1
        for m in range(n+1,P,2):
            if gcd(m,n) == 1:
                #print(m*m-n*n,2*m*n,m*m+n*n)
                _count += N//(m*m+n*n)
    return _count 

def sumDigits(n):
    return sum(map(int,str(n)))

def smpf(n):
    if n == 1: return 1
    if checkPrime(n): return n
    if n%2 == 0: return 2
    for i in range(3,n//2+1,2):
        if n%i == 0:
            return i