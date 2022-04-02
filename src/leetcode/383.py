"""TODO doc and test"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_counter = dict()
        for s in magazine:
            if s not in magazine_counter:
                magazine_counter[s] = 1
            else:
                magazine_counter[s] += 1

        for s in ransomNote:
            if s not in magazine_counter or magazine_counter[s] <= 0:
                return False
            else:
                magazine_counter[s] -= 1

        return True
