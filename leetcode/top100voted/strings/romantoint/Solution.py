class Solution:
    def romanToInt(self, s: str) -> int:
        num=0
        if not s:
            return num
        num=num + self.__get_number(s[0])
        self.romanToInt(s[1:len(s)])

    def __get_number(self,c:chr) -> int:
        switch={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        return switch.get(c,"Invalid input")
