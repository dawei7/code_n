from typing import List


class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def representations(digits: str) -> List[str]:
            if len(digits) == 1:
                return [digits]
            if digits[0] == "0" and digits[-1] == "0":
                return []
            if digits[0] == "0":
                return ["0." + digits[1:]]
            if digits[-1] == "0":
                return [digits]
            return [digits] + [
                digits[:index] + "." + digits[index:]
                for index in range(1, len(digits))
            ]

        digits = s[1:-1]
        coordinates = []
        for split in range(1, len(digits)):
            for left in representations(digits[:split]):
                for right in representations(digits[split:]):
                    coordinates.append(f"({left}, {right})")
        return coordinates
