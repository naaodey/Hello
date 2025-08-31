import math
dir(math)

import random
print(random.random(12))


a = int(input('Enter the first base...'))
b = int(input('Enter the second base...'))
h = int(input('Enter the height...'))

def area_trapezium(a,b,h):
    area = 0.5 * (a + b) * h
    print(f"Area of a Trapezium = {area} ")
    
def main():
    area_trapezium(a, b, h)
    
if __name__=="__main__":
    main()


# Return And Void
def my_fun(yam, okra, onion):
      """Documentation"""
      return yam * okra + onion
  

import math

degree = int(input('Enter the value of x...'))
nterm = int(input('Enter the nujmber of terms...'))

def sin():
    sine = 0
    for i in range(nterm):
       sign = (-1)**i
       radians = degree*(math.pi/180)
       sine += (radians**(2.0*i+1))/math.factorial(2*i+1)*sign
    return sine    
print(sin(degree,nterm))



import math
 
# Create sine function
def sin( x, n):
    sine = 0
    for i in range(n):
        sign = (-1)**i
        pi = 22/7
        y = x*(pi/180)
        sine += ((y**(2.0*i+1))/math.factorial(2*i+1))*sign
    return sine
 
# driver nodes
# Enter value in degree in x
x = 10
 
# Enter number of terms
n = 90
 
# call sine function
print(round(sin(x,n),2))



import math
degree =int(input('Enter the value of x...'))
nterm = int(input('Enter the n term...'))
radians = degree* math.pi/180
def calculate_sin():
    result = 0
    numerator = radians
    denominator = 1
    for i in range(1,nterm+1):
        single_term = numerator/denominator
        result = result + single_term
        numerator = -numerator*radians**2
        denominator = denominator*(2*i)*(2*i+1)
    return result

def main():
    result = calculate_sin()
    print(f'The value of sin{(degree)} of the {nterm} is {result}')

if __name__=="__main__":
    main()
    




    