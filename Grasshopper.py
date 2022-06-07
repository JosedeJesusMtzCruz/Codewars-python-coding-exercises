def get_grade(s1,s2,s3):
    grade=['A','B','C','D','F']
    list=[s1,s2,s3]
    a=sum(list)/3
    b=100.0
    c=90
    for i in range(len(grade)):
        if a <= b-10*i: 
            if a>=c-10*i:
                print (grade[i])
                return grade[i]
            elif a<60:
                return grade[4]
        else:
            pass

