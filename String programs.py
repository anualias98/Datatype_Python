#1.to print 1st,middle,last letter of a string
# str="james"
# result=str[0]
# l=len(str)
# middle=int(l/2)
# result=result+str[middle]
# result=result+str[l-1]
# print("New string is",result)

#2.to append new string
# s1="Hello"
# s2=" World"
# print(s1+s2+" Hi")

#3.append to the middle of string
# s1="Hello"
# s2="world"
# middle=int(len(s1)/2)
# res=s1[0:middle]
# res=res+s2
# res=res+s1[middle:]
# print("New string is :",res)
#
#
# a="Hello"
# b="world"
# result=a[0:2]+b+a[2:5]
# print("New String: ",result)


#4.arrange string characters such that lowercase letters should come first
# s1="LuMInaR tEcHnoLaB"
# lower=[]
# upper=[]
# for char in s1:
#     if char.islower():
#         lower.append(char)
#     else:
#         upper.append(char)
# sorted_str=''.join(lower+upper)
# print('Result:',sorted_str)
# print("lower is",lower)
# print("upper is",upper)

#5.Count all letters digits and special symbol from a given string
# str1="P@#$yn26at^i5ve"
# letters=0
# digits=0
# symbol=0
# for i in str1:
#     if i.isalpha():
#         letters+=1
#     elif i.isdigit():
#         digits+=1
#     else:
#         symbol+=1
# print("letters=",letters,"digits=",digits,"symbol=",symbol)

#6.Remove special symbols/puntuation from a string

str = "/*Jon is  2developer & music director"
str2=" "
for i in str:
    if i.isalnum() and i.isalpha():
        str2=str2+i
        str3=str2.split()
print('  '.join(str3))



# import string
# str="/*Jon is @ developer & musician"
# print(str.translate(str.maketrans('','',string.punctuation)))