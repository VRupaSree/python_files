number = int(input("enter number of terms to print Fibonacci series? "))

# First intial terms
f = 0
s = 1
count = 0

# we will check if the number of terms is valid or not  ?
if number <= 0:
    print("Please enter a correct integer")
# if there is only one term, it will return f
elif number == 1:
    print("The Fibonacci sequence of the numbers up to", f, ": ")
    print(f)
# Fibonacci sequence of number is
else:
    print("The fibonacci sequence of the numbers is:")
    while count < number:
        print(f)
        n = f + s
        # At last, we will update values
        f = s
        s = n
        count += 1
