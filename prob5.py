import math
import argparse
from time import time_ns, sleep

parser = argparse.ArgumentParser(description = "the smallest positive number that is evenly divisible by all of the numbers from 1 to N")
parser.add_argument('-N', help = "Max number for which you want to be divisble by all numbers from 1 to that number",
 type = int, default = 20)
args = parser.parse_args()

# def factors(l):
#     list_fac = []
#     for k in range(1, l+1, 1):
#         for i in range(1, int(l/2), 1):
#             if (l % i == 0):
#                 list_fac.append(i)
#     return max(list_fac)  

primes = []

def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while(p*p <= n):
        if(prime[p] == True):
            for i in range(p*p, n+1, p):
                prime[i] = False

        p += 1

    for i in range(2, n+1):
        if(prime[i] == False):
            primes.append(i)
    return primes

   

class Solution():
    def __init__(self,N):
        self.N = N

    def __repr__(self):
        return str(self.N)  


    def LCM(self):  
        t = time_ns()
        primes = SieveOfEratosthenes(self.N)

        lcm = 1; 
        i = 0; 
        while (i < len(primes) and primes[i] <= self.N):  
            # Find the highest power of prime,  
            # primes[i] that is less than or  
            # equal to n  
            pp = primes[i];  
            while (pp * primes[i] <= self.N):  
                pp = pp * primes[i];  
    
            # multiply lcm with highest  
            # power of prime[i]  
            lcm *= pp;  
            lcm %= 1000000007; 
            i+=1; 
        print(time_ns()-t)
        return lcm

        

if __name__ == "__main__":
    print("Project Euler Problem 5")
    sol = Solution(20)
    print(sol.LCM())  
    # print(is_palindrome(989989)            

            

