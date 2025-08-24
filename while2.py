# # #i = 1
# # #while i<=5:
# #  #   print("Teluskoi")
# #   #  i=i+1
    
# # names = ["BJohn","Mary"]

# # for name in names:
# #     if name.startswith("J"):
# #         print("Found")
# #         break 
# # else:
# #     print("Not Found")
         
         
# i = 1
# while i<=5:
#      print("Telusko")
#      i=i+1

# print("mreet is an antonomonus (\")")
# def hello():
#      print("good morning")
#      print("mrcet")
# print("hi")
# print("hello")    
# hello()
# print("done!")

# def add_sub(x,y):
#      c=x+y
#      d=x-y
#      return c,d
# print(add_sub(10,5))

# def      wish(*names):
#        for name in names:
#           print("Hello",name)
# wish("MRCET","CSE","SIR","MADAM")
     
#       """this function greets to
#    the person with the provided messgage"""
# #name is a tuple with arguments
#      for name in names:
#      print("Hello",name)
# wish("MRCET","CSE","SIR","MADAM")


# #keyword arguments -through 
# def func(a,b=5,c=10):
#      print('a is',a,'and b is',b,'and c is',c)
# func(3,7)
# func(25,c=24)
# func(c=50,a=100)

pi=3.14
def areaOfCircle(r):
     return pi*r*r
r=int(input("Enter radius of circle"))
print(areaOfCircle(r))

def calculate(a,b):
     total =a+b
     diff=a-b
     prod=a*b
     div=a/b
     mod=a%b
     return total,diff,prod,div,mod
a=int(input("Enter a value"))
b=int(input("Enter b value"))
s,d,p,q,m =calculate(a,b)
#print("Sum=",s,"diff=",d,)"mul=",p,"div=",q,"mod=",m)
print("diff=",d)
print("mul=".p)
print("div=",q)
print("mod",m)
