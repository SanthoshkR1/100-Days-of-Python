def gcd(a,b):
    if a>b :a,b =b,a
    while a%b !=0:
        a,b=b,a%b
    return b
print("GCD is : ",gcd(21,15))