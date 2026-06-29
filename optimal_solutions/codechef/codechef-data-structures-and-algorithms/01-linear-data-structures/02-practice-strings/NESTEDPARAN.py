


def solve():
    def maxNestingDepth(s):
        max_depth = 0
        current_depth = 0

        for ch in s:
            if ch == '(':
                current_depth += 1
                if current_depth > max_depth:
                    max_depth = current_depth
            elif ch == ')':
                current_depth -= 1
        return max_depth


if __name__ == "__main__":
    solve()
