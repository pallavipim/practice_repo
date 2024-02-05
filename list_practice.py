# 3-4 guest list

person_list=['Pratik','Adam','Eliza','Ressellar']

for person in person_list:
    print(f"Welcome to dinner party {person.title()}")

print(f"{person_list[2]} won't come to party today")

print("\n++++++++++++++++++++++++++++++++++\n")

person_list[2] = 'George'

person_list.insert(0,'Brrok')

person_list.insert(2,'Belly')

person_list.append('Sharukh')

for peer in person_list:
    print(f"{peer} will come to party")

print("Removing\n+++++++++++++++++++++++++++++++++++++++++++++")

print("with pop()\n",person_list)
print(f"{person_list.pop(2)}")
print("after pop\n",person_list)

person_list.remove('Adam') # need to provide string value in remove function
print("after remove\n",person_list)

del person_list[3]
print("after delete\n",person_list)

