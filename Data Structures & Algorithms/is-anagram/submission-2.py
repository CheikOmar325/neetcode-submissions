class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            Hash_t = Counter(t)
            Hash_s = Counter(s)
            if Hash_t == Hash_s:
                return True
            else:
                return False

