# big o(1) notation 
# the time remains the same regardless of the input size 
# used in the array indexing, hash table lookups, and basic arithmetic operations.
# we fetch the element by it index , no loop

def first_Number(arr):
    return arr[0]  # returns the first element of the array, O(1) time complexity

def last_Number(arr):
    return arr[-1]  # returns the last element of the array, O(1) time complexity

roll_bumber = [1, 2, 3, 4, 5]
f_number = first_Number(roll_bumber)
last_Number = last_Number(roll_bumber)
print(f_number)
print(last_Number)

contacts = {
    "Ali": "1234",
    "Ahmed": "5678",
    "Sara": "9999"
}

print(contacts["Sara"])
