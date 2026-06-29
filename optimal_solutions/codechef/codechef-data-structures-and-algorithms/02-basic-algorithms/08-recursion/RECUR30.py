import sys

# Increase the recursion limit


def solve():
    sys.setrecursionlimit(10**6)

    def flatten_string(s: str) -> str:
        def helper(index):
            result = []
            while index < len(s):
                if s[index] == '(':
                    sub_result, index = helper(index + 1)
                    result.extend(sub_result)
                elif s[index] == ')':
                    return result, index
                else:
                    result.append(s[index])
                index += 1
            return result, index

        flattened_string, _ = helper(0)
        return ''.join(flattened_string)

    # Input string
    s = input()
    print(flatten_string(s))


if __name__ == "__main__":
    solve()
