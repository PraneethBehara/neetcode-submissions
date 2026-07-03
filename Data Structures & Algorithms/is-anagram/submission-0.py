class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        comp_hash = {}

        for each in s:
            if not each in comp_hash:
                comp_hash[each] = 1
            else:
                comp_hash[each] = comp_hash[each] + 1

        for each in t:
            if each not in comp_hash:
                return False
            else:
                comp_hash[each] = comp_hash[each] - 1

        if all(v==0 for v in comp_hash.values()):
            return True
        else:
            return False

                