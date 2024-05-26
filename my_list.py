my_list = []

#append elements 10,20,30,40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#insert 15 at the second position
my_list.insert(1, 15)
print("New list after inserting 15:",my_list)

#extend with 50,60,70
my_list.extend([50,60,70])
print("New list after extending", my_list)

#remove the last element
my_list.pop()
print("New list after removing last element", my_list)

#sort my_list in ascending order
my_list.sort()
print("List after sorting in ascending order ", my_list)

#find the index of 30
index = my_list.index(30)
print("The index of 30 is:", index)
