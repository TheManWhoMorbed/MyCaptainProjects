def most_frequent():
    freq={}
    l=len(word)
    for i in word:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    print(str(freq))
word=input("Enter a string: ")
most_frequent()
