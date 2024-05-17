class ContainsDuplicate:
    def __init__(self, nums):
        self.nums = nums

    def contains_duplicate_brute_force(self):
        # Brute force approach: Check each pair of elements
        n = len(self.nums)
        for i in range(n):
            for j in range(i + 1, n):
                if self.nums[i] == self.nums[j]:
                    return True
        return False

    def contains_duplicate_sorting(self):
        # Sorting approach: Sort the array and check consecutive elements
        sorted_nums = sorted(self.nums)
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i - 1]:
                return True
        return False

    def contains_duplicate_hashing(self):
        # Hashing approach: Use a set to track seen elements
        seen = set()
        for num in self.nums:
            if num in seen:
                return True
            seen.add(num)
        return False
