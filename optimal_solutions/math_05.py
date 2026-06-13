"""Optimal solution for math_05: Big Integer Add (Strings).

Add two non-negative integers given as digit strings.
"""


def solve(a, b):
    if not a:
        return b
    if not b:
        return a
    a_rev = a[::-1]
    b_rev = b[::-1]
    n = max(len(a_rev), len(b_rev))
    carry = 0
    out = []
    for i in range(n):
        da = int(a_rev[i]) if i < len(a_rev) else 0
        db = int(b_rev[i]) if i < len(b_rev) else 0
        s = da + db + carry
        out.append(str(s % 10))
        carry = s // 10
    if carry:
        out.append(str(carry))
    return "".join(reversed(out))
