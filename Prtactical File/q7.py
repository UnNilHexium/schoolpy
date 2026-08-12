line_with_a=[]
line_without_a=[]
with open("file.txt","r") as f:
    for i in f:
        if "a" in i.lower():
            line_with_a.append(i)
        else:
            line_without_a.append(i)

with open("file.txt","w") as f:
    f.writelines(line_without_a)
    print("Lines without a-", line_without_a)

with open("filewitha.txt","w") as f:
    f.writelines(line_with_a)
    print("Lines with a", line_with_a)