#1.Remove empty string from a list of strings
# str1=["John","","Jack","Emma","","Jins","Lina"]
# str2=[]
# for i in str1:
#     if i:
#         str2.append(i)
# print(str2)
#2.Write a python code to remove all the repeating letters from a each words of a given sentence
# str="Let's google the pineapple"
# str1=str.split(" ")
# str2=[]
# for i in str1:
#     t=''
#     for j in i:
#         if j in t:
#             continue
#         else:
#             t=t+j
#     str2.append(t)
# print(' '.join(str2))







#3.Replace each special symbol with # in the followinf string
str="/* Jon is @ developer & musician!!"
str1=['/','*','&','@','!']
for i in str1:
    if i in str:
        str=str.replace(i,'#')
print(str)






# replace={"/":"#","*":"#","@":"#","&":"#","!":"#"}
# a=" "
# for i in str:
#     if i in replace:
#         a+=replace[i]
#     else:
#         a+=i
# print(a)
#














#4.Reverse a list in python
# list1=[100,200,300,400,500]
# list1.reverse()
# print(list1)
#5.Extend nested list by adding sublist
# list1=["a","b",["c",["d","e",["f","g"],"k"],"l"],"m","n"]
# sublist=["h","i","j"]
# list1[2][1][2].extend(sublist)
# print(list1)










