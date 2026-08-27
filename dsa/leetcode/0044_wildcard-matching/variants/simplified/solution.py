class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p_clean = []
        for ch in p:
            if ch == "*" and p_clean and p_clean[-1] == "*":
                continue
            p_clean.append(ch)
        p = "".join(p_clean)

        s_idx, p_idx = 0, 0
        star_idx = -1
        s_match = 0
        n, m = len(s), len(p)

        while s_idx < n:
            if p_idx < m and (p[p_idx] == "?" or p[p_idx] == s[s_idx]):
                s_idx += 1
                p_idx += 1
            elif p_idx < m and p[p_idx] == "*":
                star_idx = p_idx
                s_match = s_idx
                p_idx += 1
            elif star_idx != -1:
                p_idx = star_idx + 1
                s_match += 1
                s_idx = s_match
            else:
                return False

        while p_idx < m and p[p_idx] == "*":
            p_idx += 1

        return p_idx == m
