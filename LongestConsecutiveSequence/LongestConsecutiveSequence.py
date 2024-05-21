class LongestConsecutiveSequence:
    def __init__(self, nums):
        self.nums = nums

    def longest_consecutive_sequence_hash_set(self):
        hs = set(self.nums)
        longest = 0

        for n in hs:
            if (n-1) not in hs:
                length = 1
                while (n + length) in hs:
                    length += 1

                longest = max(length, longest)

        return longest
