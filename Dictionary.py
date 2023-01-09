#Create empty dictionary
# Dict={}
# print("Empty Dictionary")
# print(Dict)
#with dic() method
dict=dict({1:'java',2:'T',3:'Point'})
print(dict)
# dict1=dict([(1,'Anu'),(2,'Anju')])
# print(dict1)
# Employee={"Name":'John',"Age":24,"salary":25000,"Company":'Google'}
# print(type(Employee))
# print("Name:%s" % Employee["Name"])
# print("Age:%d" % Employee["Age"])
# print("Salary:%d" % Employee["salary"])
# print("Company:%s" % Employee["Company"])
# print(Employee.get("Company"))
# del Employee["Company"]
# print(Employee)
#Adding elements to dict
# Dict[0]='Peter'
# Dict[2]='Joseph'
# Dict[3]='Ricky'
# print(Dict)
#Adding set of values
# Dict['Emp ages']=20,33,24
# print(Dict)
#updating existing key
# Dict[3]='Javapoint'
# print(Dict)

# Employee["Name"]=input("Name")
# Employee["Age"]=input("Age")
# Employee["salary"]=input("salary")
# Employee["Company"]=input("Company")
# print(Employee)


"""iterating dictionary"""
#for loop to print all keys of dicttionary
# Employee={"Name":'John',"Age":24,"salary":25000,"Company":'Google'}
# for  x in Employee:
#     print(x)
#for loop to print all values of dictionary
# Employee={"Name":'John',"Age":24,"salary":25000,"Company":'Google'}
# for  x in Employee:
#     print(Employee[x])
#for loop to print the values of dictionary by using values() method
# Employee={"Name":'John',"Age":24,"salary":25000,"Company":'Google'}
# for  x in Employee.values():
#     print(x)
# for loop to print the items of dictionary by using items() method
Employee={"Name":'John',"Age":24,"salary":25000,"Company":'Google'}
for  x in Employee.items():
    print(x)