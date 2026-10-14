class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        #we put the elements in a dictionary, tracking the number of occurences of that said element as the key
        
        # from that we iterate through the resulting dictionary to find the k most frequent elements, of course the dictionary will be sorted by keys
        ordered = sorted(freq, key=freq.get, reverse=True)
        return ordered[:k]