class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""

        left = 0
        right = 0
        res = [0, float("inf")]

        tCount = {}
        need = 0

        for c in t:
            tCount[c] = 1 + tCount.get(c, 0)

        need = len(tCount)

        window = {}
        for c in tCount:
            window[c] = 0

        have = 0

        while right < len(s):
            c = s[right]

            if c in window:
                window[c] += 1

                if window[c] == tCount[c]:
                    have += 1

            right += 1

            while have == need:
                if right - left < res[1] - res[0]:
                    res = [left, right]

                c = s[left]

                if c in window:
                    if window[c] == tCount[c]:
                        have -= 1

                    window[c] -= 1

                left += 1

        if res[1] == float("inf"):
            return ""

        return s[res[0]:res[1]]


