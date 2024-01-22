class Solution:
    def two_sum(self, input: list[int], target: int) -> list | None:
        num_map = {}
        for idx, i in enumerate(input):
            result = target - i
            print(num_map, idx)
            if result in num_map:
                return [num_map[result], idx]
            else:
                num_map[result] = idx
        return None


nums = [2, 7, 11, 15]
target = 9


two_sum = Solution()
print(two_sum.two_sum(nums, target))
