MAXN = 200000

def SieveofErastothenes(n):
    global MAXN
    primes = []
    prime = [True for i in range(MAXN)]
    p = 2
    while(p < MAXN):
        if(prime[p] == True):
            primes.append(p)
            if(len(primes)>=n):
                break
            for i in range(p*p, MAXN, p):
                prime[i] = False
        p += 1
    return primes[-1]


if __name__ == "__main__":
    sol = SieveofErastothenes(10001)
    print(sol)
