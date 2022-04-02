"""TODO Doc and test"""


symbols_map = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    'IV': 4,
    'IX': 9,
    'XL': 40,
    'XC': 90,
    'CD': 400,
    'CM': 900,
}


class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        i = 0
        while i < len(s):
            if i + 1 == len(s):
                result += symbols_map[s[i]]
                return result
            if s[i:i + 2] in symbols_map:
                result += symbols_map[s[i:i + 2]]
                i += 2
                continue
            else:
                result += symbols_map[s[i]]
                i += 1
                continue

        return result
