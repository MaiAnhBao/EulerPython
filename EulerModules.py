import math
#from Euler import primes_sieve

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
    
def sumDigits(n):
    return sum(map(int, str(n)))

def sumPowers(n):
    return sum([math.factorial(int(x)) for x in str(n)])

def isPerfectSquare(n):
    tst = int(math.sqrt(n) + 0.5)
    return tst*tst == n

def sieve_totient(n):
    phi = [0 for i in range(n)]
    phi[1] = 1
    i = 2
    while i<n:
        if phi[i] == 0: 
            phi[i] = i-1
            j = 2
            while j*i<n:
                if phi[j] != 0:
                    q = j
                    f = i-1
                    while q%i == 0:
                        f*=i
                        q //= i
                    phi[i*j] = f * phi[q]
                j += 1
        i += 1
    return phi#sum([phi[j] for j in range(n) if j%2 ==1])

def getDivisor(n):   
    l = [i for i in range(2,n//2+1) if n%i==0]
    l.append(n)
    l.append(1)
    return l

def getPrimeDivisor(n):
    s = set()
    for i in range(2,n//2+1):
        if checkPrime(i) and n%i==0:
            while n%i == 0:
                n = n//i
            s.add(i)
    return s

def Fibo(n):
    a,b = 1,1
    for i in range(1,n):
        a,b = b,a+b
    return a

def isPandigital(n):
    return set(str(n)) == {'1','2','3','4','5','6','7','8','9'}

def isPalindrome(n):
    return str(n) == str(n)[::-1]
    