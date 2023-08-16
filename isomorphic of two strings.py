def areIsomorphic(str1,str2):
    fre=dict()
    size1=len(str1)
    size2=len(str2)
    if size1!=size2:
        return False
    for i in range(size1):
        if str1[i] not in fre:
            fre[str1[i]]=ord(str1[i])-ord(str2[i])
        else:
            if fre[str1[i]]!=(ord(str1[i])-ord(str2[i])):
                return False
    return True
s1="foo"
s2="bar"
print(areIsomorphic(s1,s2))
