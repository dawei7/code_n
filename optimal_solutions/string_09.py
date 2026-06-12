"""Optimal solution for string_09: Run-Length Encoding.

Walk the string, counting consecutive equal chars.
"""


def solve(s):
    if not s:
        return ""
    out = []
    cur = s[0]
    count = 1
    for c in s[1:]:
        if c == cur:
            count += 1
        else:
            out.append(cur + str(count))
            cur = c
            count = 1
    out.append(cur + str(count))
    return "".join(out)
