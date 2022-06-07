def capitals(word):
    Capitals1=['A','B','C','D','E','F','G'
              ,'H','I','J','K','L','M','N'
               ,'Ñ','O','P','Q','R','S','T'
               ,'U','V','W','X','Y','Z'
              ]
    n=[]
    for i in range(len(word)):
        for k in range(len(Capitals1)):
            if word[i] == Capitals1[k]:
                n.append(i)
                
    return n
