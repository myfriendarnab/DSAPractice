'''module for importing deque for stack implementation'''

class Solution3:
    '''class for valid parentheses problem'''
    def is_closing_parentheses(self, input_parentheses_sequence: str) -> bool:
        '''
            method works mainly by inserting '(','{','[' to a stack
            if next symbol in input doesnot have corresponding 'opening_parentheses', its not valid parentheses
        '''
        if len(input_parentheses_sequence)==1:
            return False

        stack=deque()
        opening_parentheses={
                ')':'(',
                '}':'{',
                ']':'['
            }

        for item in input_parentheses_sequence:
            if item in ('(','{','['):
                stack.append(item)
            else:
                if any(stack):
                    lastitem=stack.pop()
                    if opening_parentheses[item] != lastitem:
                        return False
                else:
                    return False
        return len(stack)==0

res=Solution3().is_closing_parentheses("){")
print(res)