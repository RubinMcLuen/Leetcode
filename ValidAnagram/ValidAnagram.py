class ValidAnagram:
    def __init__(self, s, t):
        self.s = s
        self.t = t

    def valid_anagram_brute_force(self):
        count_s = {}
        count_t = {}
        for i in self.s:
            if i not in count_s:
                count_s[i] = 1
            else:
                count_s[i] = count_s[i] + 1

        for i in self.t:
            if i not in count_t:
                count_t[i] = 1
            else:
                count_t[i] = count_t[i] + 1

        for i in count_s:
            if i not in count_t or count_s[i] != count_t[i]:
                return False
            
        return True
            

    def valid_anagram_sorting(self):
        s_sorted = sorted(list(self.s))
        t_sorted = sorted(list(self.t))
        return s_sorted == t_sorted
    
