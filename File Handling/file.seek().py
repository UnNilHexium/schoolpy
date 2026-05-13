#relocating the file pointer to a new location with respect to a reference point
f1=open('myfile.txt','r')
f1.seek(0) # resets the pointer to begining of file
print(f1.tell())
f1.seek(5) # places the pointer on position 5
print(f1.tell())

# goes to end of file if:
#           (number of bytes to go to) > (number of bytes in file)