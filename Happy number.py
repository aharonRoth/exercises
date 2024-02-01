def is_Happy(n):
    sum = 0
    arr = []
    if n >= 1 and n != 2 ** 31 - 1:
        while n != 0:
            sum += (n % 10) ** 2
            n = n // 10
            if n == 0:
                while sum != 0:
                    if sum in arr:
                        return False
                    else:
                        arr.append(sum)
                    if sum == 1:
                        return True
                    n = sum
                    sum = 0       


n = 3
print(is_Happy(n))
 
        
