n1 = 999
count = 0

flag = False
def palindrome():
    for i in reversed(range(999)):
        for j in reversed(range(999)):
            mul = i*j
            mul_str = str(mul)
            if len(mul_str) == 4 and mul_str[0] == mul_str[3] and mul_str[1] == mul_str[2]:
                print(mul_str)
                flag = True
                break
            elif len(mul_str) == 5 and  mul_str[0] == mul_str[4] and mul_str[1] == mul_str[3]:
                print(mul_str)
                flag = True
                break
            elif len(mul_str) == 6 and mul_str[0] == mul_str[5] and mul_str[1] == mul_str[4] and mul_str[2] == mul_str[3]:
                print(mul_str)
                flag = True
                break
        if flag == True:
            break


if __name__ == "__main__":
    print("Project Euler Problem 1")
    palindrome()            




        
