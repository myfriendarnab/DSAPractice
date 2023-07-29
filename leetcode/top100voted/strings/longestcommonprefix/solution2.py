'''module for leetcode problem of finding longest'''
from typing import List
from collections import deque
from functools import reduce

class Solution2:
    '''class for leetcode problem of finding longest'''
    def longest_common_substring(self, strs: List[str]) -> str:
        '''this method comapares first string with others in following way:
            input:['reflow','flow','flower','flour','reflex']; first string:'reflow'
            we are incrementing an offset till iterating through whole 'reflow' and taking those substrings -> 'reflow'[:2]='re'
            if substr_in_list and previous char is also pesent in list of LinkedList
                appending the value to linked list
            else
                creating a new linked list entry to the list
            if NOT substr_in_list
                trimming the offset characters from first string and checking the rest --> 'reflow'[2:]='flow'
            largest_common_prefixes[0]=''
            largest_common_prefixes[1]='f'
            largest_common_prefixes[1]='f'>>'l'

            longest linked list is the result
        '''
        # initializations
        substr_in_list=(lambda ss,l:
                     True if 
                        len(list(filter(lambda x:x.find(ss)!=-1,l)))==len(l)
                        else False)
        strs = sorted(strs)
        compare=strs[0]
        offset=1
        largest_common_prefixes=[''] # initializing for no match as first item

        # calculation
        while offset<=len(compare):
            if substr_in_list(compare[:offset],strs):
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

    def longest_common_prefix(self, strs: List[str]) -> str:
        '''
        Lets take strs=['flow','flower','flour'] as an example
            1. create a lookup, 'c' such that
                a. tranposed list --> ,list(zip(*strs))
                b. unique values of above transpose --> list(set(list(x)))
        this will give a list like: [['f'], ['l'], ['o'], ['u', 'w']]
            2. collecting all list with exactly one element, till a list encountered with more than 1 element
        this will give a list like: [[''],['f'], ['l'], ['o']]
            3. concatinating the content to a string --> 'flo'
        '''
        common_prefix=[['']]
        c=(list
            (map
             (lambda x:list(set(list(x)))
              ,list(zip(*strs)))))
        for l in c:
            if len(l)==1:
                common_prefix.append(l)
            else:
                break
        r=list(reduce(lambda x,y:x+y, common_prefix))
        return ''.join(r)

# work around for debugging failed tests as test explorer is not working
# res=Solution2().longest_common_prefix(['reflow','flow','flower','flour','reflex'])
res=Solution2().longest_common_prefix(["flower","flow","flight"])
print(res)
