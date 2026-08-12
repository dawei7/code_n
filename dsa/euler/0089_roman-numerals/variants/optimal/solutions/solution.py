import re
import urllib.request


def solve() -> int:
    """Find number of characters saved by simplifying Roman numerals in roman.txt using regex replacements.
    
    Time Complexity: O(N * L)
    Space Complexity: O(N * L)
    """
    url = "https://projecteuler.net/resources/documents/0089_roman.txt"
    with urllib.request.urlopen(url, timeout=5) as resp:
        text = resp.read().decode("utf-8")

    lines = [line.strip() for line in text.strip().splitlines() if line.strip()]

    pattern = re.compile(r"VIIII|IIII|LXXXX|XXXX|DCCCC|CCCC")
    
    original_len = sum(len(line) for line in lines)
    minimal_len = sum(len(pattern.sub("XX", line)) for line in lines)

    return original_len - minimal_len
