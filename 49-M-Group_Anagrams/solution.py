from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            key = str(sorted(string))
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(string)
            anagrams.setdefault(key, [])

        return list(anagrams.values())