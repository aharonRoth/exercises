def sum(counter):
    if counter == 0:
        return 0 
    else:
        return counter + sum(counter - 1)

counter = 1
total = sum(counter)
print(total)




def sum_arr(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] - sum_arr(arr[1:])
arr = [2, 3]
sum = sum_arr(arr)
print(sum)



def sum_factorial(num):
    if num == 1:
        return 1
    else:
        return num * sum_factorial(num - 1)
    
num = 4
sum = sum_factorial(num)
print(sum)



def sum_even_numbers(num):
    if num % 2 != 0:
        num -= 1
    if num == 0:
        return 0
    else:
        return num + sum_even_numbers(num - 1) 
    

num = 9
sum = sum_even_numbers(num)
print(sum)




def Fibonacci(num):
    if num == 0:
        return 0 
    if num == 1:
        return 1
    else: 
        return Fibonacci(num - 1) + Fibonacci(num - 2)
    
sum = Fibonacci(6)
print(sum)


def sum_arr(arr):
    if len(arr) == 0:
        return 0
    elif isinstance(arr[0], list):
        return sum_arr(arr[0]) + sum_arr(arr[1:])
    else:
        return arr[0] + sum_arr(arr[1:])
    

arr = [1, 2, [5,[5, 3],8],4]
print(sum_arr(arr))



def Calc_Road(arr, i, j):
    if i == len(arr) - 1 and j == len(arr[i]) - 1:
        return 1
    elif i >= len(arr) or j >= len(arr[i]):
        return 0
    else:
        return Calc_Road(arr, i+1, j ) + Calc_Road(arr, i, j+1)
    



arr = [
    ['x', 'x'],
    ['x', 'x']
  
]
print(Calc_Road(arr, 0, 0))




