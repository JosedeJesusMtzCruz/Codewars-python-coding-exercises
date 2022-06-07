def abbrev_name(name):
    a=[]
    for i in range(len(name)):
        if name[i]==' ':
            a+=name[i:]
    return name[0].upper()+ '.' + a[1].upper()
