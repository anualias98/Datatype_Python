#string operation with single variable and multiple values
str1=("Anu","Anju","Ammu","Anjaly","Amala")
print(len(str1))
#Slicing
print(str1[1:4])
print(str1[::-1])
#Concatenation
str2=("Aisha","Anna")
str3=str1+str2
print(str3)
#Count & index
print(str3.count("Ammu"))
print(str3.index("Anjaly"))

print(str3*2)


