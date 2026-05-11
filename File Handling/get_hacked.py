f2 =open("Passwords_heh.txt", 'a')
a= input("Please enter you username- ")
b= input("Please enter you password- ")
c=" Login : " + a + "  Password: " + b
f2.write(c)
f2.write("\n")
f2.close()

# f1.writelines([list of strings])
f1=open("my lines",'a')
L=["a", "b", "c", "d","\n","x"]
f1.writelines(L)
f1.close()
