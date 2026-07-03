class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS: dict[str, int] = {}
        countT: dict[str, int] = {}
        
        for i in range(len(s)):
            if not s[i] in countS:
                countS[s[i]] = 1
            else:
                countS[s[i]] += 1

            if not t[i] in countT:
                countT[t[i]] = 1
            else:
                countT[t[i]] += 1

        #print (countS)
        #print (countT)
        return countS == countT