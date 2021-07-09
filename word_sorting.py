#program to sort words without the sort function in python
words = ['phone', 'cone', 'tone',]
#expected output ['cone', 'phone', 'tone',]

for i in range(0,len(words)):
    for j in range(0,len(words)):
        if words[j] > words[i]:
            temp = words[i]
            words[i] = words[j]
            words[j] = temp
    
print(words)
