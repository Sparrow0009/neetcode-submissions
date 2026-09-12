class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen_set = {}

        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            if key not in seen_set:
                seen_set[key] = [strs[i]]
            else:
                seen_set[key].append(strs[i])

        return list(seen_set.values())