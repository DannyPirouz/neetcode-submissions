class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        word1Length = len(word1)
        word2Length = len(word2)
        firstWord = 0
        secondWord = 0

        while firstWord < word1Length and secondWord < word2Length:
            output += word1[firstWord]
            output += word2[secondWord]
            firstWord += 1
            secondWord += 1
        if firstWord < word1Length:
            # while firstWord < word1Length:
            #     output += word1[firstWord]
            #     firstWord += 1
            output += word1[firstWord:]
        if secondWord < word2Length:
            while secondWord < word2Length:
                output += word2[secondWord]
                secondWord += 1
        return output