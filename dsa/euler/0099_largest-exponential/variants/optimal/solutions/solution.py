import math
import urllib.request


def solve() -> int:
    """Find 1-indexed line number in base_exp.txt with the largest numerical value b^e using logarithms.
    
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    url = "https://projecteuler.net/resources/documents/0099_base_exp.txt"
    with urllib.request.urlopen(url, timeout=5) as resp:
        text = resp.read().decode("utf-8")

    lines = [line.strip().split(",") for line in text.strip().splitlines() if line.strip()]

    max_val = 0.0
    best_line = 0

    for idx, (base_s, exp_s) in enumerate(lines, 1):
        b, e = int(base_s), int(exp_s)
        val = e * math.log(b)
        if val > max_val:
            max_val = val
            best_line = idx

    return best_line
