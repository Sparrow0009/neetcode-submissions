class Solution:
    # Solving this problem again to see if I can solve problems again
    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s  += str(len(i)) + "#" + i
        return s
    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            word_len = int(s[i:j])
            i = j + 1
            j = i + word_len
            word = s[i:j]
            output.append(word)
            i = j
        return output

