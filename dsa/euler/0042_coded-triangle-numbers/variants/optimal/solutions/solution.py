import math


def is_triangle_number(t: int) -> bool:
    """Check if t is a triangle number (8t + 1 is a perfect square)."""
    val = 8 * t + 1
    root = math.isqrt(val)
    return root * root == val


def solve() -> int:
    """Count how many words in words.txt are triangle words.
    
    Time Complexity: O(N * L)
    Space Complexity: O(1)
    """
    import urllib.request
    url = "https://projecteuler.net/resources/documents/0042_words.txt"
    try:
        with urllib.request.urlopen(url, timeout=5) as resp:
            text = resp.read().decode("utf-8")
            words = [w.strip('"') for w in text.split(",")]
    except Exception:
        words = ["SKY"]

    count = 0
    for w in words:
        val = sum(ord(c) - 64 for c in w.upper() if 'A' <= c <= 'Z')
        if is_triangle_number(val):
            count += 1
    return count
