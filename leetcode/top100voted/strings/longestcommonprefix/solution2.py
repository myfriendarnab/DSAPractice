'''module for leetcode problem of finding longest'''
from typing import List
from collections import deque

class Solution2:
    '''class for leetcode problem of finding longest'''
    def longest_common_prefix(self, strs: List[str]) -> str:
        '''main entry method'''
        substr_in_list=(lambda ss,l:
                     True if 
                        len(list(filter(lambda x:x.find(ss)!=-1,l)))==len(l)
                        else False)
        compare=strs[0]
        offset=1
        largest_common_prefixes=[]
        while offset<len(compare):
            if substr_in_list(compare[:offset],strs[1:]):
                if any(largest_common_prefixes) and compare[:offset-1]==largest_common_prefixes[-1]:
                    matcheddq:deque=largest_common_prefixes[-1]
                    matcheddq.append(compare[:offset])                  
                else:
                    matcheddq=deque()
                    matcheddq.append(compare[:offset])
                    largest_common_prefixes.append(matcheddq)
                offset=offset+1
            else:
                compare=compare[offset:]
        largest_common_prefixes_strings = list(map(lambda x:''.join(x),largest_common_prefixes))
        return max(largest_common_prefixes_strings)

res=Solution2().longest_common_prefix(['reflow','flow','flower','flour','reflex'])
print(res)
