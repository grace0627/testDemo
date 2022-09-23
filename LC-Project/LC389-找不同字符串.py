class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hash = dict()
        for ch1 in t:
            hash[ch1] = 1
        for key in hash.keys():
            for cha2 in s:
                if cha2 == key:
                    hash[key] = hash[key] - 1
            if hash.get(key) > 0:
                return key


            