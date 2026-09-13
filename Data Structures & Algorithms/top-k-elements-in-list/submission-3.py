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

        '''
        # Solution using Counter
        count = Counter(nums)
        return [num for num, freq in count.most_common(k)]
        '''

        # Solution using Bucket Sort Algorithm
        count = {}
        frequency_buckets = [[] for i in range(len(nums) + 1)]

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        for num, cnt in count.items():
            frequency_buckets[cnt].append(num)

        length_buckets = len(frequency_buckets)
        res = []

        for i in range(length_buckets - 1, 0, -1):
            for num in frequency_buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res




        
        
        