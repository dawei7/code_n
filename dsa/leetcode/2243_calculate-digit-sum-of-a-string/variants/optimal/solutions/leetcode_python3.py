class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            groups = []
            for start in range(0, len(s), k):
                groups.append(str(sum(int(digit) for digit in s[start : start + k])))
            s = "".join(groups)
        return s
