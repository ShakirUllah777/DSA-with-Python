my_list = [1,2,3,4,5,10,20,30,40,50]

# finsing the 1st and last and any number O(1)
print(my_list[1])
print(my_list[-1])
print(my_list[3])

# adding the data set last and random 
my_list.append(100)
my_list.append(200) # O(1) add at the end 

my_list.insert(1,1000) # shift the data set O(n) notation
my_list.insert(2,2000)

print(my_list)

# deleting item is same as the inserting the data set 

# Accessing the items 
print(my_list[1:5]) # O(k)
print(my_list[::2])
print(my_list[::-2])


# Transversing the list 
for mark in my_list:
    print(mark)

print('\n')

for i in range(len(my_list)):
    print(i)

print('Reversing the list')
# reverse transversing the list 
for i in reversed(my_list):
    print(i)
