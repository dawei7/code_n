class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = list(range(26))

        def find(letter: int) -> int:
            while parent[letter] != letter:
                parent[letter] = parent[parent[letter]]
                letter = parent[letter]
            return letter

        for first, second in zip(s1, s2):
            first_root = find(ord(first) - ord("a"))
            second_root = find(ord(second) - ord("a"))
            if first_root < second_root:
                parent[second_root] = first_root
            else:
                parent[first_root] = second_root

        return "".join(
            chr(find(ord(character) - ord("a")) + ord("a"))
            for character in baseStr
        )
