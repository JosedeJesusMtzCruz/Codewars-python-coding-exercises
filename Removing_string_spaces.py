def no_space(x):
    c=''
    for i in range(len(x)):
        if x[i]!=' ':
            c+=x[i]
        else:
            pass
    return c
