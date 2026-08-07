class Solution:
    def residuePrefixes(self, s: str) -> int:
        distinct = set()
        residues = 0

        for length, character in enumerate(s, start=1):
            distinct.add(character)
            if len(distinct) == length % 3:
                residues += 1

        return residues
