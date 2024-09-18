class MinStack:

    def __init__(self):
       self.stk = [] # create stack to hold all elements
       self.minstk = [] # create stack to hold min element 

    def push(self, val: int) -> None:
        self.stk.append(val)
        # if minstk empty add the number
        if not self.minstk: 
            self.minstk.append(val)
        # if new number greater than current min maintain current min at top of stk
        elif self.minstk[-1] < val: 
            self.minstk.append(self.minstk[-1])
        # otherwise new number less than current min add to top of the stack 
        else: 
            self.minstk.append(val)

    def pop(self) -> None:
        self.stk.pop() # remove top element from stack 
        self.minstk.pop() # pop to match other stack 
        
    def top(self) -> int:
        return self.stk[-1] # return top element from stack 

    def getMin(self) -> int:
        return self.minstk[-1] # return min element from stack 
