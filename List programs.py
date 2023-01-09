# list=["star","moon",[3,5,8]]
# print(list)
# print(list[1][3])
# print(list[-3])
# print(list[::-1])


# letters=[]
# for i in "Luminar":
#     letters.append(i)
# print(letters)

# even=[]
# for i in range(10):
#     if i%2==0:
#         even.append(i)
# print(even)
#1.list comprehensive
# list=[i*i for i in range(10)]
# print(list)

#2.
# letters=[i for i in "Luminar"]
# print(letters)
#3.
# even=[i for i in range(10) if i%2==0]
# print(even)
# odd=[i for i in range(10) if i%2!=0]
# print(odd)
# power=[i**2 for i in range(10) if i%2==0]
# print(power)

#4.prime or not
# prime=[x for x in range(2,20) if all (x % y!=0 for y in range(2,x))]
# print(prime)
#5.
# list1=[1,2,3]
# list2=[4,5,6]
# combinelist=[(x,y) for x in list1 for y in list2]
# print(combinelist)
#6.factorial
