list1=[10,20,30,40,50,60,70,80,90]
list2=[5,15,25,35,45,55,65,75,85,95,96,97,98,99]
list3=list1+list2
print(list3)
list=[]
for i in range (len(list3)):
    a=min(list3)
    list.append(a)
    list3.remove(a)
print(list)






