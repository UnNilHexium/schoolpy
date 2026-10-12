with open("file.txt", "r") as f:
    line = f.readline()
    words=line.split()
    println="#".join(words)
    print(println)
    while line:
        words=line.split()
        println="#".join(words)
        print(println)
        line = f.readline()