class StringEncodeAndDecode():
    def __init__(self, strs, encoded_string):
        self.strs = strs
        self.encoded_string = encoded_string

    def string_encode(self):
        res = ""
        for i in self.strs:
            res += i + "#"
        return res
    
    def string_decode(self):
        decoded_strs = []
        s = ""
        for i in self.encoded_string:
            if i == "#":
                decoded_strs.append(s)
                s = ""

            else:
                s += i
        return decoded_strs

