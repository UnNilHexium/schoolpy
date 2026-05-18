f1=open("myfile.txt","r")
a="backup"
i=0
while True:
    f2=open(a+str(i),'w')
    f2.write(f1.read())
    i+=1
