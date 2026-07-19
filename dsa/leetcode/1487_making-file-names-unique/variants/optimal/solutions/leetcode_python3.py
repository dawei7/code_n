from typing import List


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        next_suffix = {}
        assigned = []

        for name in names:
            if name not in next_suffix:
                next_suffix[name] = 1
                assigned.append(name)
                continue

            suffix = next_suffix[name]
            candidate = f"{name}({suffix})"

            while candidate in next_suffix:
                suffix += 1
                candidate = f"{name}({suffix})"

            next_suffix[name] = suffix + 1
            next_suffix[candidate] = 1
            assigned.append(candidate)

        return assigned
