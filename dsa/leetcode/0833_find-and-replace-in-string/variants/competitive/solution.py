from typing import List


class Solution:
    def findReplaceString(
        self,
        s: str,
        indices: List[int],
        sources: List[str],
        targets: List[str],
    ) -> str:
        replacements = {}
        for index, source, target in zip(indices, sources, targets):
            if s.startswith(source, index):
                replacements[index] = (source, target)

        pieces = []
        cursor = 0
        while cursor < len(s):
            replacement = replacements.get(cursor)
            if replacement is None:
                pieces.append(s[cursor])
                cursor += 1
                continue

            source, target = replacement
            pieces.append(target)
            cursor += len(source)

        return "".join(pieces)
