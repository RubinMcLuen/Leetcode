class TopKElementsInList:
    def __init__(self, nums, k):
        self.nums = nums
        self.k = k

    def top_k_elements_in_list_bucket_sort(self):
        counts = {}
        freq = [[] for i in range(len(self.nums) + 1)]

        for i in range(len(self.nums)):
            if self.nums[i] in counts:
                counts[self.nums[i]] += 1
            else:
                counts[self.nums[i]] = 1

        for num, count in counts.items():
            freq[count].append(num)

        res = []
        for i in freq[::-1]:
            if i:
                for j in i:
                    res.append(j)
                    self.k -= 1
                    if self.k == 0:
                        return res
        
