


def solve():
    def is_interleave(s1, s2, s3):
        # Base case: if all strings are empty, return True
        if not s1 and not s2 and not s3:
            return True

        # If s3 is empty but either s1 or s2 is not, return False
        if not s3:
            return False

        # Recursive cases:
        if s1 and s1[0] == s3[0]:
            if is_interleave(s1[1:], s2, s3[1:]):
                return True

        if s2 and s2[0] == s3[0]:
            if is_interleave(s1, s2[1:], s3[1:]):
                return True

        return False


    s1 = input()
    s2 = input()
    s3 = input()
    print(is_interleave(s1, s2, s3))  # Output: True


if __name__ == "__main__":
    solve()
