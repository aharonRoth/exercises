def is_valid(s):
   arr = ['()', '[]', '{}']
   check_arr = []
   for i in range(len(s)):
      if s[i] == '(' or s[i] == '[' or s[i] == '{':
            check_arr.append(s[i])
      else:
          if len(check_arr) == 0 or check_arr.pop() + s[i] not in arr:
              return False
    
   return len(check_arr) == 0
    

s = "()"
print(is_valid(s))