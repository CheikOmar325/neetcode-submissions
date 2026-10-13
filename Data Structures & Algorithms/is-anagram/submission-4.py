class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #first we checked the length of both strings, if they differ = false

        #if not, we create a HashMap with Counter of both strings
        #the hashmap counts the numer of occurence of each element of a given string
        #from that, we can the then check if both the elements and their number of occurences are the same across both hashmaps
        if len(s) != len(t):
            return False
        else:
            Hash_t = Counter(t)
            Hash_s = Counter(s)
            if Hash_t == Hash_s:
                return True
            else:
                return False

