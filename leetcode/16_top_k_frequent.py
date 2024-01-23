class Soltuion:
    def top_k_frequent(self, nums: list[int], k: int) -> list[int]:
        new_map = {}
        for i in nums:
            if i in new_map:
                new_map[i] += 1
            else:
                new_map[i] = 1

        print(new_map)

        return [1, 2]


# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
 if __main__ = 
