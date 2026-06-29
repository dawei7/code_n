import sys


def solve():
    def repeatedStringMatch(A, B):
        # Start with one repetition
        repeated_A = A
        count = 1

        # Repeat A until length is sufficient (at least len(B))
        while len(repeated_A) < len(B):
            repeated_A += A
            count += 1

        # Check if B is in the repeated string
        if B in repeated_A:
            return count

        # Check with one extra repetition
        repeated_A += A
        count += 1

        if B in repeated_A:
            return count

        return -1


if __name__ == "__main__":
    solve()
