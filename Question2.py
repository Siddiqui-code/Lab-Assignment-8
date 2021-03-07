# Nousheen Siddiqui
# 03/03/2021
# Write a function that takes two inputs from a user and prints whether the sum is greater than 10,
# less than 10, or equal to 10

def numbers():
    x=int(input("Mention an input"))
    y=int(input("Mention an input"))
    sum=x+y
    if sum>10:
        print("Greater than 10")
    elif sum<10:
        print("Less than 10")
    else:
        print("Equal to 10")

numbers()