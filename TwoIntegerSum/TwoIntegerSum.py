class TwoIntegerSum:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def two_integer_sum_two_pointers(self):
        l = 0
        r = len(self.nums) - 1

        while l < r:
            sum = self.nums[l] + self.nums[r]
            if sum == self.target:
                return [l + 1, r + 1]
            if sum > self.target:
                r -= 1
            else:
                l += 1

