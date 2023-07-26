class Solution():
    
    def __init__(self) -> None:
        pass
    
    def romanToInt(self, s: str) -> int:
        if len(s)<=1:
            return self.__get_number(s[0])
        sign = -1 if self.__get_number(s[0])<self.__get_number(s[1]) else 1
        return self.__get_number(s[0])*sign + self.romanToInt(s[1:])

    def __get_number(self, first_char:chr) -> int:
        switch={
            # '':0,
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        return switch.get(first_char,"Invalid input")
    

if __name__=='__main__':
    r=Solution().romanToInt('MMMDCCXXIV')
    print(r)
