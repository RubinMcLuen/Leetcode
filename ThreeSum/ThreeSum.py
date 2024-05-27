class ThreeSum:
    def __init__(self, nums):
        self.nums = nums

    def three_sum_two_pointers(self):
        res = []
        self.nums = sorted(self.nums)
        n = len(self.nums)
        
        for i in range(n - 2):
            if i > 0 and self.nums[i] == self.nums[i - 1]:
                continue
            
            l, r = i + 1, n - 1
            while l < r:
                sum = self.nums[i] + self.nums[l] + self.nums[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    res.append([self.nums[i], self.nums[l], self.nums[r]])
                    l += 1
                    r -= 1
                    while l < r and self.nums[l] == self.nums[l - 1]:
                        l += 1
                    while l < r and self.nums[r] == self.nums[r + 1]:
                        r -= 1

        return res
