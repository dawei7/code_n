class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        left_length = len(str1)
        right_length = len(str2)
        lcs = [[0] * (right_length + 1) for _ in range(left_length + 1)]

        for left in range(1, left_length + 1):
            for right in range(1, right_length + 1):
                if str1[left - 1] == str2[right - 1]:
                    lcs[left][right] = lcs[left - 1][right - 1] + 1
                else:
                    lcs[left][right] = max(lcs[left - 1][right], lcs[left][right - 1])

        reversed_result = []
        left = left_length
        right = right_length
        while left and right:
            if str1[left - 1] == str2[right - 1]:
                reversed_result.append(str1[left - 1])
                left -= 1
                right -= 1
            elif lcs[left - 1][right] > lcs[left][right - 1]:
                reversed_result.append(str1[left - 1])
                left -= 1
            else:
                reversed_result.append(str2[right - 1])
                right -= 1

        reversed_result.extend(reversed(str1[:left]))
        reversed_result.extend(reversed(str2[:right]))
        return "".join(reversed(reversed_result))
