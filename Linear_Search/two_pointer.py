# Two pointer technique 
# we used this to solve the time from O n square to to O(n)

# 1. let finde the sum of two number 
def find_number(number, target):

    left = 0 
    right = len(number) - 1

    while left < right:
        curr_sum = number[left] + number[right]

        if curr_sum == target:
            return number[left], number[right]
        
        elif curr_sum < target:
            left += 1

        else:
            right -= 1

    return []

numbers = [1,2,5,6,8,11]
print(find_number(numbers,19))


# reverseing the array 
my_array = [1,2,3,4,5,6,7,8,9,10]
my_array.reverse()
print(my_array) # for short size of arrays not for real time porjects


my_array1 = [1,2,3,4,5,6,7,8,9,10]
my_array1 = my_array1[::-1]
print(my_array1) # alos not recommeded

# two pointer technique 
my_arr = [10,11,12,13,14,15]

letf = 0 
right = len(my_arr) - 1

while letf < right:
    my_arr[letf], my_arr[right] = my_arr[right], my_arr[letf]

    letf += 1
    right -= 1

print(my_arr)