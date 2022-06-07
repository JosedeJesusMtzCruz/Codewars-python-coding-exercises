def sum_array(arr):
    if arr==None:
        return 0
    else:
        arr2=sorted(arr)
        return sum(arr2[1:len(arr2)-1])
