def get_sum(a,b):
    if a < b:
        print(range(a,b))
        print(sum(range(a,b)))
        return sum(range(a,b+1))
    else:
        return sum(range(b,a+1))
