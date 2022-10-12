filename= str(input("enter the file name: "))
f= open(filename,"r")
cons= 0
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for char in f.read():
    if char>='a' and char<='z' or char>='A' and char<='Z':
      if char not in vowels:
        cons=cons+1
f.close()
if cons>=1:
    print("consonants are",cons)
else:
    print("There is no any Consonant available in the File!")