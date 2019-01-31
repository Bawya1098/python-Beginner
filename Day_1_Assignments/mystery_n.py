def mystery(numbers):
    sum = 1
    for i in range(0, numbers):
        if i < 6:
            for k in range(1, numbers):         #num1 to 5: sum=2^(numbers**2)
                sum *= 2
                print(sum)
        else:                                   #number6: sum=2^(5*number)*5
            if i < 10:                          #number7: sum=2^(5*number)*5^2
                sum *= 5                        #number8: sum=2^(5*number)*5^3
                print(sum)                      #number9: sum=2^(5*number)*5^4
            else:                               #number10: sum=2^(5*number)*(5^4)*(3^1)
                sum *= 3                        #number11: sum=2^(5*number)*(5^4)*(3^2)
                print(sum)
    return sum

    myserty(3)