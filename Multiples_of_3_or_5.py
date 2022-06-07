def solution(number):
    if number < 0:
        return 0
    list=[]
    for i in range (number):
        if i % 5 == 0:
            list.append(i)
        elif i % 3 == 0:
            list.append(i)
    return sum(list)
