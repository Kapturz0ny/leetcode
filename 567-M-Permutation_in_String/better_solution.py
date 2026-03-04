class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        matches = 0
        ord_s1 = [0] * 26
        ord_s2 = [0] * 26

        for i in range(len(s1)):
            ord_s1[ord(s1[i]) - ord('a')] += 1
            ord_s2[ord(s2[i]) - ord('a')] += 1
        
        for i in range(26):
            if ord_s1[i] == ord_s2[i]:
                matches += 1

        for i in range(len(s1), len(s2), 1):
            if matches == 26:
                return True

            # remove left window char
            idx = ord(s2[i - len(s1)]) - ord('a')
            ord_s2[idx] -= 1
            if ord_s1[idx] == ord_s2[idx]:
                matches += 1
            elif ord_s1[idx] == ord_s2[idx] + 1:
                matches -= 1

            # add right window char
            idx = ord(s2[i]) - ord('a')
            ord_s2[idx] += 1
            if ord_s1[idx] == ord_s2[idx]:
                matches += 1
            elif ord_s1[idx] == ord_s2[idx] - 1:
                matches -= 1
            
        return matches == 26