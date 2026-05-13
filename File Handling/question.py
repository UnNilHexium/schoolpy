f1=open('myfile.txt','r')
text=f1.read(1)
charachters=0
words=1
lines=1
while text:
    charachters+=1
    if text.isspace():
        words+=1
    if text=="\n":
        lines+=1
    text=f1.read(1)
print (charachters, words, lines)
f1.close()