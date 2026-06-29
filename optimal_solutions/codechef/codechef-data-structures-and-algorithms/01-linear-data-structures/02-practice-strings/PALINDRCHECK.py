


def solve():
    def reverseWords(s: str) -> str:
        chars = list(s)
        n = len(chars)

        # Step 1: Reverse the entire string
        chars.reverse()

        # Step 2: Reverse each word
        start = 0
        for i in range(n + 1):
            if i == n or chars[i] == ' ':
                left, right = start, i - 1
                while left < right:
                    chars[left], chars[right] = chars[right], chars[left]
                    left += 1
                    right -= 1
                start = i + 1

        # Step 3: Remove extra spaces in-place
        idx = 0
        i = 0
        while i < n:
            # skip spaces
            while i < n and chars[i] == ' ':
                i += 1
            if i >= n:
                break

            # copy word
            while i < n and chars[i] != ' ':
                chars[idx] = chars[i]
                idx += 1
                i += 1

            # skip spaces after word
            while i < n and chars[i] == ' ':
                i += 1

            # add space if another word exists
            if i < n:
                chars[idx] = ' '
                idx += 1

        return ''.join(chars[:idx])


if __name__ == "__main__":
    solve()
