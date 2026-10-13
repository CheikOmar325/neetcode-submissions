class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result= {} #mapping the charCount to list of Anagrams
        #key = sorted string value
        #we iterate through the list and if a word has the same key value, it is added to the group, until we reach the end of the strs

        for i in range (len(strs)):
            key = "".join(sorted(strs[i]))

            if key not in result:
                result[key] = []

            result[key].append(strs[i])
        return list(result.values())

        

        
        