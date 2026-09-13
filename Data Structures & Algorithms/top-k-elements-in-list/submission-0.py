from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = defaultdict(int)
        for num in nums:
            count_dict[num] += 1
        return heapq.nlargest(k, count_dict, key=count_dict.get)
        
        
        