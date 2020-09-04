def countwordsfromfile():
    filename=input('enter the file name')
    file=open(filename,'r')
    noOfWords=0
    for line in file:
        words=line.split("%")
        noOfWords=noOfWords+len(words)
        print(words)
        print (noOfWords)
    print("no Of Words")
    print (noOfWords)
    print(words)
countwordsfromfile()
