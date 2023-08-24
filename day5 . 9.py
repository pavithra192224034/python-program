def shuffle(l1, l2):
    result = []
    
    # Find the length of the longer list
    max_length = max(len(l1), len(l2))
    
    for i in range(max_length):
        if i < len(l1):
            result.append(l1[i])
        if i < len(l2):
            result.append(l2[i])
    
    return result

# Example usage
list1 = [1, 3, 5]
list2 = [2, 4, 6, 8]

shuffled_list = shuffle(list1, list2)
print(shuffled_list)



