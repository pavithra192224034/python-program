statement=input('give a sentence')
vowels="aeiouAEIOU"
count=0
for char in statement:
    if char in vowels:
        count+=1
print('number of vowels in a statement:',count)        
