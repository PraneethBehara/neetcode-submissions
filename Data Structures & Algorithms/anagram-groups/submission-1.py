class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     groups: List[List[str]] = []
    #     new_group = True

    #     for each in strs:
    #         new_group = True
    #         # check if str is anagram of first str in the List        
    #         for group in groups:
    #             if self.is_anagram(each, group[0]):
    #                 group.append(each)
    #                 new_group = False
    #                 break
            
    #         if new_group:
    #             groups.append([each])
            
    #     print(groups)
    #     return groups

    # def is_anagram(self, s, t):
    #     if len(s) != len(t):
    #         return False

    #     countS = self.get_str_count(s)
    #     countT = self.get_str_count(t)

    #     return countS == countT


    # def get_str_count(self, s: str) -> dict[str, int]:
    #     countS = {}
    #     for i in range(len(s)):
    #         countS[s[i]] = 1 + countS.get(s[i], 0)

    #     return countS

        groups = defaultdict(list)

        for s in strs:
            signature = [0] * 26
            for c in s:
                signature[ord(c) - ord('a')] += 1

            groups[tuple(signature)].append(s)

        return list(groups.values())
