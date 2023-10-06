### Functions -- block to define a process

### avoid code repetation
### program arrangement


### create defination block
### call the function


### Types of functions:
               # Built in function
                      # print,input,sum,max,min,len.....etc
               # user defined function

# def display():
#     print("hello world")

# display()

# *
# **
# ***
# ****
# *****
# ***
# ***
# ***
# *
# **
# ***
# ****
# *****  

# def triangle():                                   # parameter
#     for x in range(1,6):
#         for y in range(1,x+1):
#             print('*',end=" ")
#         print()
# def rectangle():
#     for x in range(1,4):
#         for y in range(1,4):
#             print('*',end=" ")
#         print()     


# triangle()                                        # arguments
# rectangle()
# triangle()


# def triangle(n):                                   # parameter
#     for x in range(1,n+1):
#         for y in range(1,x+1):
#             print('*',end=" ")
#         print()
# def rectangle(r,c):
#     for x in range(1,r+1):
#         for y in range(1,c+1):
#             print('*',end=" ")
#         print()    


# triangle(4)                                        # arguments
# triangle(7)

# rectangle(3,5)
# rectangle(r=5,c=6)                       ## used (forget resource)


# def check_prime(n):                      ## check prime or not prime
#     for i in range(2,n):
#         if n%i==0:
#             print(n,"is not a prime number")
#             break
#     else:
#         print(n,"is a prime number")
 
# check_prime(19)        
        
# def add(a=0,b=0):                            ## Default parameter
#     print("result:",a+b)
 
# add()
# add(4)
# add(3+5)    


# def add(a=0,b=0):                            
#      return a+b

# print(add(4,20))

# def add(a=0,b=0):
#     global c
#     c= a+b
#     return c
 
# print(add(4+8))
# print(c)

### arbitrary arguments

# def fun(*param):
#     print(param)

# fun(1,2,2,3,4,5,2,6,3,7,8,5,3,4,6,9,1)
# fun()    

### keyword arbitrary arguments

# def fun(**param):
#     print(param)

# fun(a=12,b=9,c=45)
# fun(x=18,y=45)

# def add(a=0,b=0):
#     global c
#     c= a+b
#     return c

# l=[5,6]

# print(add(l[0],l[1]))

# add(*l)

# def count_upperlower(s):
#     u,l=0,0
#     for x in s:
#         if x.islower():
#             l+=1
#         elif x.isupper():
#             u+=1
#     print("Upper cases:",u)
#     print("Lower cases:",l)

# count_upperlower("Python program")  


## feature of functions

# display=print

# display(1,2,3,4,5)
# print(4,5,6,7,8,9)


## Nested functions

# def outer():
#     def inner():
#         print("inner function")
#     print("outer function")
#     inner()

# outer()        

# def outer():
#      global inner
#      def inner():
#          print("inner function")
#      print("outer function")
      
# outer()
# inner()

# def outer():
#      def inner():
#          print("inner function")
#      print("outer function")
#      return inner

# x=outer()
# x()


#  def getfun(f):
#      f()
 
#  def alpha():
#      print("alpha")
#  def beta():
#      print("beta")
  
#  getfun(alpha)
#  getfun(beta)            


## Recursion

def display():
    print("python")
    display()

display()        


# def display(n):
#     if n>=1:
#        print('python')
#        display(n-1)
 
# display(10)

   

### lambda function -- one liner function
##                  -- unnamed function

# x=lambda : print('hello world')
# x()

# x=lambda n:print("data=",n)
# x(9)

# x=lambda a,b:a*b
# print(x(4,5))

