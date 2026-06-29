


def solve():
    def generate(n):
        s = []

        def backtrack():
            # Base case
            if len(s) == n:
                print("".join(s))
                return

            # Always try adding '0'
            s.append('0')
            backtrack()
            s.pop()

            # Try adding '1' only if previous character is not '1'
            if not s or s[-1] == '0':
                s.append('1')
                backtrack()
                s.pop()

        backtrack()


if __name__ == "__main__":
    solve()
