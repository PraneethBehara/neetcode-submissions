class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # sort | O(n+m), O(1)
        # return sorted(s) == sorted(t)

        # hash map
        sCount = {}
        for each in s:
            sCount[each] = sCount.get(each, 0) + 1

        for each in t:
            if each in s:
                sCount[each] = sCount.get(each, 0) - 1

        print(sCount.values())
        return all(v == 0 for v in sCount.values())

        return False

        # for i in range(len(s)):
            

        # hash table (const size)

