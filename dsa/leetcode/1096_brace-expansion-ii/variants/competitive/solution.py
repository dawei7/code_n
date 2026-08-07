from typing import List


class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        index = 0

        def parse_union() -> set[str]:
            nonlocal index
            result = parse_concatenation()
            while index < len(expression) and expression[index] == ",":
                index += 1
                result |= parse_concatenation()
            return result

        def parse_concatenation() -> set[str]:
            nonlocal index
            result = {""}
            while index < len(expression) and expression[index] not in ",}":
                if expression[index] == "{":
                    index += 1
                    factor = parse_union()
                    index += 1
                else:
                    factor = {expression[index]}
                    index += 1
                result = {prefix + suffix for prefix in result for suffix in factor}
            return result

        return sorted(parse_union())
