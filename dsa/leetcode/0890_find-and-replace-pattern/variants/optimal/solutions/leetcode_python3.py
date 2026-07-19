from typing import List


class Solution:
    def findAndReplacePattern(
        self, words: List[str], pattern: str
    ) -> List[str]:
        def signature(text: str) -> tuple[int, ...]:
            identifiers = {}
            return tuple(
                identifiers.setdefault(character, len(identifiers))
                for character in text
            )

        target = signature(pattern)
        return [word for word in words if signature(word) == target]
