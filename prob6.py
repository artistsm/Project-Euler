import math
import argparse
from time import time_ns, sleep

parser = argparse.ArgumentParser(description = "the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.")
parser.add_argument('-N', help = "Max number for which you want to get the difference between the square of sums and sum of squares",
 type = int, default = 100)
args = parser.parse_args()

class Solution():
    def __init__(self,N):
        self.N = N

    def __repr__(self):
        return str(self.N)  

    def squard(self):
        sum = 0
        t = time_ns()
        for i in range(1, self.N + 1, 1):
            prod = 0
            for j in range(i+1, self.N+1,1):
                prod = prod+(i*j)
            sum = sum + prod
        print(time_ns()-t)
        return sum*2


if __name__ == "__main__":
    print("Project Euler Problem 6")
    sol = Solution(100)
    print(sol.squard())  
    # print(is_palindrome(989989)    

    