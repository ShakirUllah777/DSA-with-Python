# Big O Log N 
# time increasy with the input increase 
# we find the target input in the steps , take less steps then the big O n notation 
# mostly the DS is divided into two parts and then ingore the other pats 

def find_number(number, target):
    left = 0
    right = len(number) - 1

    while left <= right:
        mid = (left + right) // 2
        if number[mid] == target:
            return mid 
        elif number[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Target not found

my_list = [1, 2, 3, 4, 5, 6, 7]
target = 5
result = find_number(my_list, target)
if result != -1:
    print(f"Target {target} found at index {result}.")
else:
    print(f"Target {target} not found in the list.")



