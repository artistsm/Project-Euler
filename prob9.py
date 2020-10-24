def PythogoreanTriplet(N):
    a_max = int(N/3)
    b_max = int(N/2)
    for i in range(1,a_max, 1):
        # print(i)
        for j in range(1,b_max,1):
            c = 1000- i-j
            # print('i=',i,'\tj=',j,'\tc=',c)
            if (i*i + j*j == c*c):
                return i*j*c

if __name__ == "__main__":
    sol = PythogoreanTriplet(1000)
    print(sol)