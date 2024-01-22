class Solution:
    def contains_duplicate(self, nums: list[int]) -> bool:
        as_set = set(nums)
        return True if len(as_set) != len(nums) else False


if __name__ == "__main__":
    solution_instance = Solution()

    # Test case 1: Contains duplicate
    nums1 = [1, 2, 3, 1]
    result1 = solution_instance.contains_duplicate(nums1)
    print(f"Test case 1: {result1}")  # Output should be True

    # Test case 2: No duplicates
    nums2 = [4, 5, 6, 7]
    result2 = solution_instance.contains_duplicate(nums2)
    print(f"Test case 2: {result2}")  # Output should be False
