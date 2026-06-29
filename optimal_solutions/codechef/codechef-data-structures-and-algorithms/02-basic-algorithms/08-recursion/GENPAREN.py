


def solve():
    def generate(n):
        result = []

        def solve(open_count, close_count, current):
            # Base case: valid combination formed
            if len(current) == 2 * n:
                result.append(current)
                return

            # Try adding '(' if possible
            if open_count < n:
                solve(open_count + 1, close_count, current + '(')

            # Try adding ')' if it keeps the string valid
            if close_count < open_count:
                solve(open_count, close_count + 1, current + ')')

        solve(0, 0, "")
        return result


if __name__ == "__main__":
    solve()
