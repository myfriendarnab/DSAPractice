class SolutionRecursion:
 
    def roman_to_int(self, s: str) -> int:
        if not s:
            return 0
        if len(s)<=1:
            return self.__get_number(s[0])
        sign = -1 if self.__get_number(s[0])<self.__get_number(s[1]) else 1
        return self.__get_number(s[0])*sign + self.roman_to_int(s[1:])

    def __get_number(self, first_char:chr) -> int:
        switch={
            '':0,
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        return switch.get(first_char,"Invalid input")

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
            
            s=s.replace("IV", "IIII").replace("IX", "IIIIIIIII")
            s=s.replace("XL", "XXXX").replace("XC", "XXXXXXXXX")
            s=s.replace("CD", "CCCC").replace("CM", "CCCCCCCCC")

            return sum(map(lambda x: parse[x],s))