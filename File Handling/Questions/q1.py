def display_word():
    f1=open("myfile.txt","r")
    line=f1.readline()
    while line:
        wordlist=line.split()
        for i in wordlist:
            if len(i)< 4:
                print(i)
        line=f1.readline()
    print("file ended")
    f1.close()
display_word()
