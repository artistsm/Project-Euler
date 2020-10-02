import math
def largest_prime_factor(N):
    while N%2 == 0: # checking if the number is divisible by 2
        N = N/2 # reducing the number by 2 till the time it is divisible by 2
    for i in range(3,int(math.sqrt(N)),2): # checking for odd numbers only till yhe sqrt of N
        while N%i == 0 and N!= i:
            N = N/i #updating N everytime it is divisible by a number
    print(int(N))
                


if __name__ == "__main__":
    print("Project Euler Problem 3")
    largest_prime_factor(600851475143)