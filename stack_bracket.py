"Stack Problem on the Brackets"

def valid_expression(expr):
    
    
    dic = {"]":"[","}":"{",")":"("}
    
    stack = []
    
    for char in expr :
        if char in dic.values() :
            stack.append(char)
        
        elif char in dic.keys():
            if not stack or stack[-1] != dic[char]:
                
                return False
            
            else :
                stack.pop()
            
    return not stack



expression = "[{()}]"
expression1 = "[{)}]"

print(valid_expression(expression1))