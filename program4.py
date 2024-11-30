def checkValidString(s: str) -> bool:
    balance1 = 0
    for char in s:
        if char == '(' or char == '*':
            balance1 += 1
        else:  # char == ')'
            balance1 -= 1
        if balance1 < 0:
            return False  

    balance2 = 0
    for char in reversed(s):
        if char == ')' or char == '*':
            balance2 += 1
        else:  
            balance2 -= 1
        if balance2 < 0:
            return False  
    
    return True

print(checkValidString("()"))  
print(checkValidString("(())"))  
print(checkValidString(")("))  
print(checkValidString("()("))  
