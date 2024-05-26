def isValid(s:str) -> bool:
    # stack algorithm
    """
    Will iterate through the list, append the opening to the stack list
    then after adding to stack, check last element of list, with current char
    then if equal return False as per leetcode, else return True if same.
    
    >>> isValid("[]")
    True
    
    >>> isValid("[)")
    False
    """
    
    stack = [] # Used for comapre 
    
    
    # Iterate through the string, check if open is one of 3, push, remove first element, compare last element with first element
    # if not same, return true, else return
    for s in s:
        if s == '{' or s == '(' or s == '[':
            stack.append(s) # push
        elif s == '}' or s == ')' or s == ']':
            if len(stack) == 0:
                return False
            top_element = stack.pop() 
            if not checkParenthesisType(top_element, s):
                return False
    if len(stack) != 0:
        return False
              
    return True

def checkParenthesisType(opening:str, closing:str) -> bool:
    if opening == '(' and closing == ')':
        return True
    if opening == '[' and closing == ']':
        return True
    if opening == '{' and closing == '}':
        return True  
    return False
        
def main():
    print(isValid("()"))
    
if __name__ == "__main__":
    main()