class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        self.longest = ""
        self.recursive_search(s)
        return self.longest
    
    def recursive_search(self, s: str) -> None:
        if len(s) <= 1:
            return

        unique_chars = set(s)
        bad_chars = set()
        for char in unique_chars:
            opposite = char.upper() if char.islower() else char.lower()
            if opposite not in unique_chars:
                bad_chars.add(char)
      
        if not bad_chars:
            if len(s) > len(self.longest):
                self.longest = s

        partitions = []
        start = 0
        for i, char in enumerate(s):
            if char in bad_chars:
                if start < i:
                    partitions.append(s[start:i])
                start = i + 1
        if start < len(s) and start:
            partitions.append(s[start:])
        
        for part in partitions:
            self.recursive_search(part)
