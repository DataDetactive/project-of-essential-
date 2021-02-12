from math import pi

def reverse_full_name():
    fname= input("enter your first name: ")
    lname = input("enter your last name: ")
    print(f"{lname.strip()} {fname.strip()}")

def computes_n():
    n =int(input("enter your number"))
    print((1*n)+(11*n)+(111*n)) 
 
def sphere_volumn():
    r = int(input("enter radius: "))
    result = (4/3) * (pi * r ** 3)
    print(result)

def area_of_triangle():
    height = int(input("enter the height of triangle: "))
    base = int(input(" enter the base of triangle: "))
    result = (1/2*base)*height
    print(result)

def print_pattern():
    n = int(input("enter number of rows you want: "))
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end="")
        print()

    for k in range(n+1 , 0, -1):    
         for g in range(0, k - 1):  
                print("*", end="")  
         print()      

def reverse_word():
    word = input("enter your word: ")
    print(word[::-1])


def print_numbers():
    for i in range(6):
        if i==6 or i==3:
            continue
        else: print(i)


def fib(n):
   if n <= 1:
       return n
   else:
       return(fib(n-1) + fib(n-2))


def printing_fibonacci():
    n = int(input("enter the number: "))
    if n<=0:
        print("enter positive integer")
    else:
        print("Fibonacci sequence:")
        for i in range(n):
                print(fib(i))


def count_digits_letters():
    s = input("Input a string: ")
    d=l=0
    for c in s:
        if c.isdigit():
            d=d+1
        elif c.isalpha():
            l=l+1
        else:
            pass
    print("Letters", l)
    print("Digits", d)





#reverse_full_name() 
#computes_n()
#sphere_volumn()
#area_of_triangle()
#print_pattern()
#reverse_word()
#print_numbers()
#printing_fibonacci()
#count_digits_letters()   
"""
the answer of the question number 3
This is a comment
written in
more than just one line
"""
