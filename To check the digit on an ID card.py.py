def Id():
    sum = 0
    arr = []
    arr2 = []
    while sum < 8:
        num = int(input("please enter a number "))
        arr.append(num)
        sum += 1
    for i in range(len(arr)):
        if i % 2 != 0:
            arr2.append(arr[i] * 2)
        else:
            arr2.append(arr[i])        
    sum2 = 0
    for i in arr2:
        if i > 9:
            f = i - 9
            sum2 += f
        else:
            sum2 += i
    if 10 - (sum2 % 10) != 10:
        return("the number is", 10 - (sum2 % 10))
    else:
        return("the number is", 1)
print(Id())
    

    

        