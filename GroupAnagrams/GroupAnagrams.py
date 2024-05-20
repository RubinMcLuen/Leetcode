from collections import defaultdict


class GroupAnagrams:
    def __init__(self, strs):
        self.strs = strs

    def group_anagrams_sorting(self):
        res = defaultdict(list)

        for s in self.strs:
            t = str(sorted(s))
            if t in res:
                res[t] = res[t] + [s]

            else:
                res[t] = [s]

        return list(res.values())
    
    def group_anagrams_hash_map(self):
        res = defaultdict(list)

        for s in self.strs:

            chars = [0] * 26
            for c in s:
                chars[ord(c) - ord("a")] += 1

            res[tuple(chars)].append(s)

        return list(res.values())

