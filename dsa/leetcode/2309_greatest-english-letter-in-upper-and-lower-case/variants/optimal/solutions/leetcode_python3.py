class Solution:
    def greatestLetter(self, s: str) -> str:
        characters = set(s)
        for uppercase in reversed("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            if uppercase in characters and uppercase.lower() in characters:
                return uppercase
        return ""
