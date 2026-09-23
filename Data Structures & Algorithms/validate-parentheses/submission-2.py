class Solution:
    def isValid(self, s: str) -> bool:
       #create a hasmap with closing symbols as the key, adn its open as the value
       #for each iteration thru s, check if it is a closing symbol and if the top of the stack is its mathcing open, if it is a closing symbol and its open is NOT the top, return false
       #if the iteration is on an open symbol, append to stack 
       #if loop exits, check if stack is empty, return true, not, return false
        
        stack = []
        symbols = {")" : "(", "}" : "{", "]" : "[" }

        for c in s:
            if c in symbols:
                if stack and stack [-1] == symbols[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if stack:
            return False
        else:
            return True
        