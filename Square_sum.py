def square_sum(numbers):
    for i in range(len(numbers)):
        numbers[i]=numbers[i]**2
    print(sum(numbers))
    return sum(numbers)

square_sum([1,2,3,4,5])
