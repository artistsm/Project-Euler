flag = False

def is_palindrome(N):
    N_str = str(N) #Converting the number to a string
    mid = int(len(N_str)/2)
    if(N_str[0:mid]==N_str[len(N_str)-1:mid-1:-1]):
        return True
    return False

def palindrome():
    for i in range(999*999, 100*100, -1): 
        flag = False           
        if is_palindrome(i) == True:
            for j in range(999,99,-1):
                if (i %j == 0) and (len(str(int(i/j))) == 3):
                    print(i) 
                    flag = True 
                    break  
        if flag == True:
            break
        


if __name__ == "__main__":
    print("Project Euler Problem 4")
    palindrome()   
    # print(is_palindrome(989989)         )




        
