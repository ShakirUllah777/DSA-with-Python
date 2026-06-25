# Same pointer 
# other in which left and right and compared in the sequene from left to right

# used 
#  - remove duplicate 




my_names = ['shaki','shakir','ali','ali','malik','malik']


def clean(names):
    # names.sort()

    left = 0

    for right in range(1, len(names)):
        if names[right] != names[left]:
            left += 1
            names[left] = names[right]

    return left + 1


# my_list = [1,2,3,1,2,3,4,5,6,4,5,6]

length = clean(my_names)

print(my_names[:length])
