with open('Sample for python.txt') as f:
    strings = f.read()

r = strings
L = len(r)
i = 0
j = 0
m = 0
vowels = ("a", "e", "ı", "i", "o","ö", "u","ü","A","E","I","İ","O","Ö","U","Ü")

for i in range  (L) :
    
    for j in range(16) :
        
        if r[i]==vowels[j]:

            print("One of the vowels is -->" , r[i])
            m = m + 1    
            
        j = j + 1
        
    i = i + 1

print("Total vowels we have is ", m)
