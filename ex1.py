# f=open("new_file.txt","a")
# f.write("i'm in bangalore now")
# f.close()

# f=open("second_file.txt","r")
# f.read()
# # f.write("this is second file in python")
# print(f.seek(7))
# f.close()

# open both files
with open('new_file.txt','r') as firstfile, open('second_file.txt','w') as secondfile:
	for line in firstfile:
		secondfile.write(line)
