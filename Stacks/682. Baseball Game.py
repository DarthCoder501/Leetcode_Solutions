class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = [] #initializes empty stack 

        for ops in operations: #loops through each item(which is a string) in the list 
            if ops == "+": 
                stk.append(stk[-1] + stk[-2]) #get last two items in stk and add them together
            elif ops == "C":
                stk.pop() #remove last element from the stack 
            elif ops == "D":
                stk.append(2 * stk[-1]) #double the last item in stack 
            else: 
                stk.append(int(ops)) #if element in list is a num convert to int and add to stack 

        return sum(stk) #add up all the values in the stack and return the sum 
