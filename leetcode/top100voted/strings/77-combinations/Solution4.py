from typing import List

class Solution4:
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k==1:
            return list(map(lambda x:[x], list(range(1,n+1))))
    
        def create_list(i:int, x: int, k:int)-> List[int]:
            z=lambda x,k: (list(range(x,x+k-1)))
            l=[i]
            l.extend(z(x,k))
            return l

        effective_range = n-k+2
        lookup=dict.fromkeys(range(1,effective_range),[])
        res=[]
        
        for key in lookup:
            val=list(map(lambda x: create_list(key,x,k), range(key+1,effective_range+1)))
            if val:
                res.extend(val)
        return res

result = Solution4().combine(4,3)
# [[1,2,3],[1,2,4],[1,3,4],[2,3,4]]
print(result)
