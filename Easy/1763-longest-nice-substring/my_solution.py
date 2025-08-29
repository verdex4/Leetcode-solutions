class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        self.longest = ""
        self.recursive_search(s)
        return self.longest
    
    def recursive_search(self, s: str) -> None:
        if len(s) <= 1:
            return

        all_letters = set(s)
        single_letters = set()
        for l in all_letters:
            if l.islower() and not l.upper() in all_letters:
                single_letters.add(l)
            if l.isupper() and not l.lower() in all_letters:
                single_letters.add(l)
        
        if len(single_letters) == len(s):
            return
        if len(single_letters) == 0 and len(s) > len(self.longest):
            self.longest = s

        for i, l in enumerate(s):
            if l in single_letters:
                self.recursive_search(s[:i])
                self.recursive_search(s[i+1:])
                return
