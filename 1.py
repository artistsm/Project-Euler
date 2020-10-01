
def prob1():
    sum = 0
    i = 1
    for i in range(1000):
        if (((i % 3) == 0) or ((i % 5) == 0)):
            sum = sum +i 
    print(sum) 
    print(i)

if __name__ == "__main__":
    print("Project Euler Problem 1")
    prob1()