def SieveofErasthothenes(N):
    prime = [True for i in range(N+1)]
    p=2
    while(p*p <= N):
        if prime[p] == True:
            for i in range(p*p, N+1, p):
                prime[i] = False
        p = p+1

    primes = []
    for j in range(2, N+1):
        if prime[j] == True:
            primes.append(j)
    sum = 0
    for k in primes:
        sum = sum+k

    return sum

if __name__ == "__main__":
    sol = SieveofErasthothenes(2000000)
    print(sol)



