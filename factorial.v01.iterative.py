def factorial(n):
    total = 1

    for i in range(0,n):
        total = total * (n - i)
        print("Current i is: " + str(i))
        #First time total = 1
        #increment each time up to n

    return total
    #return the final total at the end of everything

factorialNum = input("Please enter a number to factorialize: ")
userNum = int(factorialNum,10)
        
print(str(userNum) + "! is " + str(factorial(userNum)))