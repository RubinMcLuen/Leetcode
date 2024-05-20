class ProductExceptSelf:
    def __init__(self, nums):
        self.nums = nums

    def product_except_self_brute_force(self):
        res = []
        for i in range(len(self.nums)):
            prod = 1
            for j in range(len(self.nums)):
                if j != i:
                    prod *= self.nums[j]
            res.append(prod)

        return res
    
    def product_except_self_division(self):
        prod = 1
        for n in self.nums:
            prod *= n

        res = [prod] * len(self.nums)
        for i in range(len(res)):
            if self.nums[i] == 0:
                res[i] = 0
            else:
                res[i] = res[i] / self.nums[i]

        return res
    
    def product_except_self_prefix_suffix(self):
        res = [0] * len(self.nums)
        pre = 1
        post = 1

        for i in range(len(self.nums)):
            res[i] = pre
            pre *= self.nums[i]

        for i in range(len(self.nums)-1, -1, -1):
            res[i] *= post
            post *= self.nums[i]

        return res
        