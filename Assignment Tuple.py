#1.write a python program to convert a string to tuple
str="Hello world"
tpl=tuple(str)
print(tpl)
#2.Write a python program to convert a list to a tuple
list=[2,5,"star",8,"moon"]
tpl=tuple(list)
print(tpl)
#3.Write a python program to find repeated items from a tuple
tpl=(4,9,2,4,5,2,1)
for i in tpl:
    if tpl.count(i)>1:
        print(i)