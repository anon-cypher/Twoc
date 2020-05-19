def possible_word(dic,char):
    for word in dic:
        count=1
        for i in word:
            if i not in char:
                count=0
            else:
                if char.count(i)!=word.count(i):
                    count=0
        if count==1:
            print(word)



dic = ["hello","python","me","goal","go"]
char = ['h','e','l','t','p','g','m','a','n','o']
possible_word(dic,char)
