# set={1,"star",(3,4,5)}
# print(set)
# set1=set([4,5,7])
# print(set1)
#update()
# set.update([90,56])
# print(set)
#add()
# set.add("moon")
# print(set)
#remove()
# set.remove(1)
# print(set)

# set1=set()
# print(set1)
# set1.update([9,12])
# set1.update((3,5))
# set1.update("Anu")
# print(set1)
#discard()
# set2={3,5,8,12,'INDIA','BHARAT'}
# set2.discard('INDIA')
# print(set2)
#Operators
# A={1,2,3,4,5}
# B={4,5,6,7,8}
# print('Union =',A|B)
# print('Intersection=',A & B)
# print('Difference=',A-B)
# print('Symmetric Diff=',A^B)

#SET Membership test
# my_set=set("apple")
# print('a' in my_set)
# print('p' not in my_set)
"""difference"""
# studentList={'danish','jaison','sangeetha','uma','amrutha','lohita','prasad','ashwathi'}
# placedStudList=["uma","danish","amrutha"]
# notPlacedStudList=set(studentList)-set(placedStudList)
# print(notPlacedStudList)

"""intersection"""
# batsmen=["virat","rohit","dhawan","dhoni","pandya","jadeja"]
# bowlers=["bhuvenashwar","shami","pandya","jadeja",'kuldeep']
# allrounders=set(batsmen) & set(bowlers)
# print("Batsmen :",batsmen)
# print("Bowlers: ",bowlers)
# print("All rounders :",allrounders)


"""union"""
# tcs=["uma","danish","amrutha"]
# infosys=["lohitha","danish","ashwathi"]
# wipro=["sangeetha","jaison","prasad","amrutha"]
# placed=set(tcs)|set(infosys)|set(wipro)
# print(placed)
# print("Number op people placed=",len(placed))



"""isdisjoint(),issubset(),issuperset()"""
numbers={1,2,3,4,5,6,7,8,9,10}
odd={1,3,5,7,9}
even={2,4,6,8,10}
print(odd.isdisjoint(even))#return true if two set have a nullintersection
print(numbers.issuperset(odd))##return true whether another set contain this set
print(odd.issuperset(numbers))
print(odd.issubset(numbers))#return true if this set contains another set