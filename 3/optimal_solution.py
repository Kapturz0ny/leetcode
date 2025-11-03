class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		appeared_chars = dict()
		max_substr_len = 0
		start_idx = 0
		
		for idx, letter in enumerate(s):
			if letter in appeared_chars.keys() and appeared_chars[letter] >= start_idx:
				start_idx = appeared_chars[letter] + 1
				
			appeared_chars[letter] = idx
			max_substr_len = max(max_substr_len, idx - start_idx + 1)

		return max_substr_len