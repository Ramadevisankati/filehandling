from fileinput import filename


filename= str(input("enter the file name: "))
f=open(filename, "r")
v= 0
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for char in f.read():
  if char in vowels:
    v= v+1
f.close()
print("Total Vowels are:",v)