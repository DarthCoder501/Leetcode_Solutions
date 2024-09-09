class Solution:
    def isValid(self, s: str) -> bool:
        stk = []  # initialize a stack to store opening brackets
        hmap = {'}': '{', ']': '[', ')': '('}  # initialize a hashmap for mapping closing to corresponding opening brackets

        for i in s:  # iterate through each character in the string
            if i not in hmap:  # if the character is an opening bracket (not in hmap), push it onto the stack
                stk.append(i)
            else:  # if it's a closing bracket
                if not stk:  # if the stack is empty, it means there's no matching opening bracket for this closing one, so return False
                    return False
                else:  # if the stack is not empty
                    x = stk.pop()  # pop the top element from the stack (should be an opening bracket)
                    if x != hmap[i]:  # if the popped opening bracket does not match the current closing bracket, return False
                        return False
        return not stk  # if the stack is empty after processing all characters, all brackets were matched, so return True
