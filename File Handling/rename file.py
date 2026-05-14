import os
f1=open('myfile.txt','r')
f2=open('backup.txt','r')
line=f1.readline()
while line:
    #condition for data to be retained to be stored here
    f2.write(line)
    line=f1.readline()
f1.close()
f2.close()
os.remove('myfile.txt')
os.rename('backup.txt','myfile.txt')