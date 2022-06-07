def get_count(sentence):
    b=0
    vowel=['a','e','i','o','u']
    for i in range(len(sentence)):
        if sentence[i]==vowel[0]:
            print(sentence[i])
            b+=1
        elif sentence[i]==vowel[1]:
            b+=1
            print(sentence[i])
        elif sentence[i]==vowel[2]:
            b+=1
            print(sentence[i])
        elif sentence[i]==vowel[3]:
            b+=1
            print(sentence[i])
        elif sentence[i]==vowel[4]:
            b+=1
            print(sentence[i])
    print(b)
    return b

get_count('hola')
