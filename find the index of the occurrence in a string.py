
test_str = "Geeksforgeeks"


print ("The original string is : " + str(test_str))


test_str = list(test_str)
res = len(test_str) - 1 - test_str[::-1].index('e')


print ("The index of last element occurrence: " + str(res))
