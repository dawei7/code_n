import itertools
import urllib.request


def solve() -> int:
    """Decrypt message with 3-character lowercase key and find the sum of ASCII values.
    
    Time Complexity: O(26^3 * L)
    Space Complexity: O(L)
    """
    url = "https://projecteuler.net/resources/documents/0059_cipher.txt"
    with urllib.request.urlopen(url, timeout=5) as resp:
        text = resp.read().decode("utf-8")
    cipher = [int(x) for x in text.strip().split(",")]

    alphabet = range(ord('a'), ord('z') + 1)
    
    for key in itertools.product(alphabet, repeat=3):
        plain = [b ^ key[i % 3] for i, b in enumerate(cipher)]
        decoded = "".join(chr(c) for c in plain)
        if " the " in decoded and " of " in decoded and " and " in decoded:
            return sum(plain)

    return -1
