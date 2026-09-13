from collections import defaultdict, Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        # Solution using min-heap
        
        count_dict = defaultdict(int)
        for num in nums:
            count_dict[num] += 1
        return heapq.nlargest(k, count_dict, key=count_dict.get)  #O(nlogk)
        '''

        # Solution using Counter
        count = Counter(nums)
        return [num for num, freq in count.most_common(k)]

        
        
        