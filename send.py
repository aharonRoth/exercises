def gett(digits):
    num = 1
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] == 9:
            while digits[i] == 9:
                if i != 0 and digits[i - 1] < 9 and num == 1:
                    digits[i] = 0 
                    digits[i - 1] += num
                    num = 0
                    i -= 1
                elif i == 0 and num == 1:
                    digits[i] = 1
                    digits.append(0)
                    return digits
                elif num == 1:
                    digits[i] = 0
                    i -= 1 
                else:
                    i -= 1           
        elif digits[i] < 9 and num == 1:
            digits[i] += 1
            return digits
    return digits

        

digits = [8, 9, 9, 9]
print(gett(digits))