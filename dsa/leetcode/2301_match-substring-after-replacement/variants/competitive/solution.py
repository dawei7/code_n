from typing import List


class Solution:
    def matchReplacement(
        self,
        s: str,
        sub: str,
        mappings: List[List[str]],
    ) -> bool:
        allowed = {(old, new) for old, new in mappings}
        width = len(sub)

        for start in range(len(s) - width + 1):
            for offset, old in enumerate(sub):
                new = s[start + offset]
                if old != new and (old, new) not in allowed:
                    break
            else:
                return True

        return False
