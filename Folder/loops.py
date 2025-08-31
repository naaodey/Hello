n  = int(input("Enter a natural number"))
i = 0
sum = 0
count = 0
while i < n:
    i = i + 1
    sum = sum + i
    count = count + 1
    average = sum/count
print(f'The average of {n} natural numbers is {average}')



m = int(input("Enter a positve number..."))
n = int(input("Enter a positve number..."))
if m == 0 and n == 0:
    print("Invalid statement")
if m == 0:
    print(f"The GCD is {n}")
if n== 0:
    print(f"The GCD is {m}")
while m!=n:
    if m > n:
        m = m-n
    if n > m:
        n = n-m
print(f"The GCD of the numbers is {n}")



nterms = int(input("Number of terms..."))
current = 0
previous = 1
count = 0
next_term = 0
if nterms <= 0:
    print('Please enter a positive number')
elif nterms == 1:
    print('Fibonacci sequence')
    print('0')
else:
    print('The fibonacci sequence of the nterms is:')
while count < nterms:
    print(next_term)
    current = next_term
    next_term = previous + current
    previous = current
    count += 1



number = int(input('Enter a number...'))
factorial = 1
if number < 0:
    print("Factorial doesn't exist for negative numbers")
elif number == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, number+1):
        factorial = factorial * i
print(f'The factorial of {number} is {factorial}') 





largest_number = int(input('Enter the initial number...'))
check_number = input('Enter a number to check whether it is the largest or not...')
while check_number !="done":
    if largest_number > int(check_number):
        print(f'The largest number is {largest_number}')
    else:
        largest_number = int(check_number)
        print(f'The larget number is the {largest_number}')
    check_number = input('Enter a number to check whether it is the largest or not...')   
            
       
    
        

largest = None
smallest = None

while True:
    try:
        num = input("Enter a number: ")
        if num == 'done':
            break
        num = int(num)
        if largest is None or num > largest:
            largest = num
        elif smallest is None or num < smallest:
            smallest = num

    except:
        print("Invalid input")
        continue

print("Maximum is", largest)
print("Minimum is", smallest)        
    