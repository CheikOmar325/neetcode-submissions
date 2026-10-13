from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #parse the string, store of every element in it
        #once stored, we check the second string and validate
        #that every element in that string
        if len(s) != len(t):
            return False
        else:
             s_hash = Counter(s)
             t_hash = Counter(t)
             if s_hash == t_hash:
                return True
             else:
                 return False

       

       

        