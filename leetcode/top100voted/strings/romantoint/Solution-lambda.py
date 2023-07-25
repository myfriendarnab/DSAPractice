class Solutionlambda:
        def roman_to_int_lambda(self, s: str) -> int:
            parse={
                'I':1,
                'V':5,
                'X':10,
                'L':50,
                'C':100,
                'D':500,
                'M':1000
            }
            if len(input)<=1:
                return parse[s[0]]
            sign = -1 if parse[s[0]]<parse[s[1]] else 1
            return parse[s[0]]*sign + self.roman_to_int_lambda(s[1:])
    
r=Solutionlambda().roman_to_int_lambda('MMMDCCXXIV')
print(r)