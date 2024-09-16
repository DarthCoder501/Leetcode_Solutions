class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = [] # creates a stack 
        # iterates through each element in the list 
        for tok in tokens: 
            if tok in "+-*/": # if element is an operator 
                # removes last & second to last num from the stack and assigns it to b & a
                b, a = stk.pop(), stk.pop() 
                # conditionals to do the correct operation 
                if tok == "+":
                    stk.append(a + b)
                elif tok == "-":
                    stk.append(a - b)
                elif tok == "*":
                    stk.append(a* b)
                elif tok == "/":
                    stk.append(int(a/b))
            else: 
                stk.append(int(tok)) # if not operator its a int so add it to the stack 
        # returns the remaining element in the stack 
        return stk[0]
