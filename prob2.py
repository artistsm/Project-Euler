def even_fibo():
    a =1 
    b = 1
    even_sum = 0
    c =0
    while(c<= 4000000):
        c = a + b
        a = b
        b = c
        if(c %2 == 0):
            even_sum = c + even_sum 

    print(even_sum)

if __name__ == "__main__":
    print("Project Euler Problem 1")
    even_fibo()

