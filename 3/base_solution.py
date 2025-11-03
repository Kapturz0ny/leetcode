class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substr_len = 0
        
        for i in range(len(s)):
            appeared_chars = set()
            substr_len = 0
            for letter in s[i:]:
                if letter in appeared_chars:
                    break
                appeared_chars.add(letter)
                substr_len += 1

            max_substr_len = max(max_substr_len, substr_len)

        return max_substr_len
