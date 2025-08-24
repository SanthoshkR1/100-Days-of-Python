x=45
print(type(x))
x="santh"
print(type(x))
print(x[0])

x=True
print(type(x))

personaldetails =["Manoj",21,"bengalore"]
print(personaldetails[1])
personaldetails [0]="eshai"

personaldetails.append("karnataka")
personaldetails.extend([22,44,66])

print(personaldetails)
var=("santh",101,2356321)
print(type(var),var)
#="var[0]rakesh"#individual 

dic={
    "name": "Santhosh",
    "age" : 21,
    "city" : "Bangalore",
    "marks" : [77,88,99,66]

}
print(type(dic),dic)
print(dic["name"])
print(dic["age"])

dic["marks"] = [77,88,99,36]
print(dic["marks"])
dic["marks"][0]=55
print(dic)
