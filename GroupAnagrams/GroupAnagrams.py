import ValidAnagram

class GroupAnagrams:
    def __init__(self, strs):
        self.strs = strs

    def group_anagrams_brute_force(self):
        for i in range(len(self.strs)):
            