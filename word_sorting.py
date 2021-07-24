words = [ 'a', 'b', 'c']
def sorting(words):
   for i in range(0,len(words)):
       for j in range(0,len(words)):
           if words[j] > words[i]:
                temp = words[i]
                words[i] = words[j]
                words[j] = temp
    
       return words   
