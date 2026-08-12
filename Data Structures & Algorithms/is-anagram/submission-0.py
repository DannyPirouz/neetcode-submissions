class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        myMap = {}
        for i in s:
            myMap[i] = myMap.get(i, 0) + 1
        for j in t:
            myMap[j] = myMap.get(j, 0) - 1
        for value in myMap.values():
            if value != 0:
                return False
        return True