from typing import List
from functools import reduce

class Solution4:
 
    def __create_list(self, i:int, x: int, k:int)-> List[int]:
        z=lambda x,k: (list(range(x,x+k)))
        l=[i]
        l.extend(z(x,k))
        return l
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k==1:
            return list(map(lambda x:[x], list(range(1,n+1))))

        effective_range = n-k+2
        lookup=dict.fromkeys(range(1,effective_range),[])
        res=[]
        
        for key in lookup.keys():
            val=list(map(lambda x: self.__create_list(key,x,k), range(key+1,effective_range)))
            if val:
                res.extend(val)
        return res

result = Solution4().combine(7,1)
print(result)
            
