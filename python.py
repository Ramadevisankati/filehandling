def uppercount():
    upper=0
    lower=0
    f1=open("python.txt",'r')
    line=f1.read()
    for i in line:
        if (i.isupper() == True):
            upper+=1
        elif (i.islower()== True):
            lower+=1
    print("Total no. of upper-case alphabets :",upper)
    print("lower-case alphabets: ",lower)
uppercount()