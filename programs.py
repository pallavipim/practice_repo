## how to find common elements between two list---------------------------------

# # Approach_1:
# list1=[10,20,30,40,50]
# list2=[15,10,20,40,55,30]
# list3=[]
#
# for element in list1:
#     if element in list2:
#         # print(element)
#         list3.append(element)
# print(list3)


# # Approach_2:
# common_list=list(set(list1)&set(list2))
# print(common_list)

#
# ##Sum of all elements in the list:----------------------------------------
#
# #Approach_1:
# list=[15,20,14,14]
#
# total=0
# for i in list:
#     total=total+i
# print(total)
#
# #Approach_2:
# list=[15,20,14,14]
# print(sum(list))
#
#
#
# ##Multiply all numbers in list:----------------------------------------------
#
# #Approach_1:
# list=[15,20,14,14]
# product=1
# for i in list:
#     product=product * i
# print(product)
#
#
# #Approach_2:
# import numpy
# list=[15,20,14,14]
# result=numpy.prod(list)
# print(result)
#
#
# ## Presence of elements in list:
#
# num=int(input("Enter the number:- "))
#
# list_x=[15,20,14,14]
#
# for i in list_x:
#     if i==num:
#         print("Element is present")
#         break
#
#     else:
#         print("Element is not present in list")
#         break
#
#
#
# ## How to swap two numbers:----------------------------------------------
##Approach1:
# num1=int(input("Enter num1 value"))
# num2=int(input("Enter num2 value"))
#
# print("Num1 value before swaping", num1)
# print("Num2 value before swaping", num2)
#
# temp=num1
# num1=num2
# num2=temp
#
# print("Num1 value after swaping", num1)
# print("Num2 value after swaping", num2)
#
##Approach_2:
# num1=int(input("Enter num1 value"))
# num2=int(input("Enter num2 value"))
#
# print("Num1 value before swaping", num1)
# print("Num2 value before swaping", num2)
#
# num1, num2=num2, num1
#
# print("Num1 value after swaping", num1)
# print("Num2 value after swaping", num2)


## How to swap 1st and last element in the list:
##Approach_1:
#
# list1=[15,20,14,14,100]
#
# print("list before swapping", list1)
#
# temp=list1[0]
# list1[0]=list1[-1]
# list1[-1]=temp
#
# print("list after swapping", list1)
#
# ##Approach_2:
#
# list1=[15,20,14,14,100]
#
# print("list before swapping", list1)
#
# list1[0], list1[-1]= list1[-1], list1[0]
#
# print("list after swapping", list1)
#
# ##Approach_3:
# list1=[45,20,14,14,100,78]
#
# start, *middle, end= list1
# list1=[end, *middle, start]
# print(list1)
#
# ##Approach_4:
# list2=[45,20,14,14,1,78]
#
# first=list2.pop(0)     #45
# last=list2.pop(-1)     #78
#
# list2.insert(0,last)
# list2.insert(-1,first)
# print(list2)
#
#
# ##How to swap any two elements in the list:----------------------------------------------
# ##Approach_1:
# list3=[1,2,3,4,5,6,7]
#
# list3[1],list3[4]=list3[4],list3[1]
#
# print(list3)
#
# ##Approach_2:
# list3=[1,2,3,4,5,6,7]
#
# ele1=list3.pop(3)
# ele2=list3.pop(3)
#
# list3.insert(3,ele2)
# list3.insert(4,ele1)
# print(list3)


##How to remove nth occurance of the element:--------------------

list_a=["apple", "mango", "orange", "apple", "Banana", "grapes", "apple"]
word="apple"
count=0
num=2
for i in range(0,len(list_a)):
    if list_a[i] ==word:
        count=count+1

        if (count==num):
            del list_a[i]
            break
print("updated list", list_a)



