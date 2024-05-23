class ValidPalindrome:
    def __init__(self, s):
        self.s = s

    def valid_palindrome_two_pointers(self):
        l = 0
        r = len(self.s) - 1

        while l < r:
            while not self.alphaNum(self.s[l]) and l < r:
                l += 1

            while not self.alphaNum(self.s[r]) and r > l:
                r -= 1

            if self.s[l].lower() != self.s[r].lower():
                return False
            l += 1
            r -= 1
        return True
            


    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))