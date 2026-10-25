#Q1. Sum of first N natural numbers 

n = int(input("Enter a number: "))                     # Taking input from the user and converting it to an integer
sum = 0                                                 # Initializing sum to 0

for i in range(1 , n+1):                                           # Looping from 1 to n (inclusive)
    sum += i                                                # Adding the current number to sum

print("The sum of N natural numbers is : ", sum)
