


def solve():
    def findLargestOddSubstring(num):
        # Traverse from the end to find the last odd digit
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 != 0:  # Check if digit is odd
                return num[:i + 1]
        return "-1"


if __name__ == "__main__":
    solve()
