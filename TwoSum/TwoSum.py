class TwoSum():
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def two_sum_brute_force(self):
        for i in range(len(self.nums)):
            for j in range(i+1, len(self.nums)):
                if (self.nums[i]+self.nums[j]) == self.target:
                    return [i,j]
                
    def two_sum_hashing(self):
        h = {}

        for i in range(len(self.nums)):
            if self.target - self.nums[i] in h:
                return [h[self.target-self.nums[i]], i]
            else:
                h[self.nums[i]] = i
            
