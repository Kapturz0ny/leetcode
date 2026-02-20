class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_bank = {}
        for letter in s:
            letters_bank[letter] = letters_bank.get(letter, 0) + 1
        
        for letter in t:
            letters_bank[letter] = letters_bank.get(letter, 0)
            if letters_bank[letter] > 0:
                letters_bank[letter] -= 1
            else:
                return False
        
        remaining_count = sum(letters_bank.values())
        return not (remaining_count > 0)