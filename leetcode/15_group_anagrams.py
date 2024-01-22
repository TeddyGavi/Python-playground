from collections import defaultdict


class Solution:
    def group_anagrams(self, strs: list[str]):
        sorted_key_map = defaultdict(list)
        print(sorted_key_map)

        for word in strs:
            sorted_word = "".join(sorted(word))
            sorted_key_map[sorted_word].append(word)

        return sorted_key_map.values()


# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"
# first sort each word, use that as the key, go through the words and sort them,
# if the key is the same as the key thats in the dict, then add that word to the array of that key
# return the values as an array of arrays
#
group_anagrams = Solution()
print(group_anagrams.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
