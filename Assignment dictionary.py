#1.Write a python program to sort a dictionary by value
dict1={1:2,3:4,4:3,2:1,0:0}
print("original dict :",dict1)
l=list(dict1.items())
list1=[]
list2=[]
for i in l:
    reverse=i[::-1]
    list1.append(reverse)
l.clear()
list1.sort()
for i in list1:
    reverse1=i[::-1]
    l.append(reverse1)
for i in (list1[::-1]):
    i=i[::-1]
    list2.append(i)
print("Ascending order is",l)
print('Descending order is',dict(list2))



#2.Write a python script to concatenate two dictionaries to create a new one
# dict1={'name':'Anu','Age':'24','Course':'Python Django'}
# dict2={'fees':'29500','Qualification':'Msc'}
# dict1.update(dict2)
# print("concatenated dict",dict1)
#


#1.Write a python program to print all unique values in a dictionary
# list_dict=[{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"},{"VII":"S005"},{"V":"S009"},{"VII":"S007"}]
# unique_values=set()
# for i in list_dict:
#     for value in i.values():
#         unique_values.add(value)
# print(unique_values)










# list_dict=[{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"},{"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
# l=[]
# for i in l:
#     l.extend(list(i.values()))
# x=(set(l))
# print(x)
#5.Write a python program to print a dictionary line by line
# dict={"Anjaly":'python',"Mintu":'Datascience','Aisha':'Mearn stack','Sifna':'Software testing'}
# for i, j in dict.items():
#     print("Name is",i,"Course is ",j)
# Employee={'Name':"Anu" ,"Age":24 ,"Salary":25000,"Company":'TCS'}
# for key,value in Employee.items():
#     print(key, '  :  ',value)

#3.Write a python program to create a dictionary from a string
# str="Luminar"
# dic={}
# l=len(str)
# for i in range(1,l+1):
#     dic.setdefault(i,str[i-1])
# print(dic)


# str="Luminar"
# dict={}
# for char in str:
#     if char in dict:#if next chr is already in the dict
#         dict[char]+=1
#     else:
#         dict[char]=1#if ch appears for the first time
# for key in dict:
#     print(key,' : ',dict[key])


#2.Write a python program to combine values in python list of dictionaries
# list_dict=[{'item':'item1','amount':400,},{'item':'item2','amount':300},{'item':'item1','amount':750}]
# new_dic={}
# for i in list_dict:
#     if i['item'] not in new_dic:
#         new_dic[i['item']]=i['amount']
#     else:
#         new_dic[i['item']] += i['amount']
# print(new_dic)
















# list_dict=[{'item':'item1','amount':400,},{'item':'item2','amount':300},{'item':'item1','amount':750}]
# new=[]
# for i in list_dict:
#     a=(i.values())
#     new.append(a)
# b=dict(new)
# c=b.get("item1")
# c=c+400
# b["item1"]=c
# print(b)

#4.Write a python program to print a dictionary in table format

# dict={"Anjaly":'python',"Mintu":'Datascience','Aisha':'Mearn stack','Sifna':'Software testing'}
# print("NAME","                  ","COURSE")
# print("*******************************")
# for i,j in dict.items():
#     if i =="Anjaly":
#         print(i,"       ",j)
#     else:
#         print(i, "       ",j)
# dic={'Anu':40,'Sam':33,'Anju':55}
# print("STUDENT\t\t\t\tTOTAL MARKS")
# for key,value in dic.items():
#     print(key,"\t\t\t\t",value)

