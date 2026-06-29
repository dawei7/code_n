


def solve():
    def minAddToMakeValidNaive(s):
        s = list(s)
        moves = 0

        while s:
            removed = False
            for i in range(len(s) - 1):
                if s[i] == '(' and s[i + 1] == ')':
                    # Remove valid pair
                    s.pop(i)
                    s.pop(i)  # i-th index shifted after first pop
                    removed = True
                    break
            if not removed:
                # Remaining characters = insertions needed
                moves += len(s)
                break

        return moves


if __name__ == "__main__":
    solve()
