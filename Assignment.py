# #area of circle using function 
# pi = 3.14
# def areaOfCircle(r):
#     return pi*r*r
# r=int(input("Enter radius of circle:"))
# print(areaOfCircle(r))

#Program to write sum different product and using arguments with return value function

# def calculate(a,b):
#     total = a+b
#     diff = a -b
#     prod = a * b
#     div = a/b
#     mod = a%b
#     return total,diff,prod,div,mod
# a=int(input("Enter a value: "))
# b=int(input("Enter b value: "))

# s,d,p,q,m=calculate(a,b)
# #print("Sum=",s,"diff=",d,"mul=",p,"div=",q,"mod=",m)
# print("diff=",d)
# print("mul=",p)
# print("div=",q)
# print("mod=",m)
# print("Sum=",s)

#program to find biggest of two numbers using functions.
# def biggest(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# a=int(input("Enter a value: "))
# b=int(input("Enter b value: "))
# big = biggest(a,b)
# print("big number=",big)

#program to find biggest of two numbers using functions. (nested if)

# def biggest(a,b,c):
#     if a>b:
#         if a>c:
#             return a
#         else:
#             return c
#     else:
#         if b>c:
#             return b
#         else:
#             return c
# a=int(input("Enter a value: "))
# b=int(input("Enter b value: "))
# c=int(input("Enter c value: "))

# big=biggest(a,b,c)
# print("big number=",big)

#Writer a program to read one subject mark and print pass or fail use single return values function with argument.
def result(a):
    if a>40:
        return "pass"
    else:
        return "fail"
a = int(input("Enter one subject marks: "))
print(result(a))


    