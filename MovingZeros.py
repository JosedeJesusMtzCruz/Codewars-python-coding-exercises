def move_zeros(array):
    a=[]
    for i in range(len(array)):
        if array[i]!=0:
            a.append(array[i])
        else:
            pass
    for i in range(len(array)):
        if array[i]==0:
            a.append(array[i])
    return a
