class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        charMap = {}

        for char in magazine:
            charMap[char] = charMap.get(char, 0) + 1
        
        for char in ransomNote:
            if char not in charMap:
                return False
            charMap[char] = charMap.get(char, 0) - 1
            if charMap[char] < 0:
                return False
        return True

