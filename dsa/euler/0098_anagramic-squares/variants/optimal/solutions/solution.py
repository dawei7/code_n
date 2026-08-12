from collections import defaultdict
import math
import urllib.request


def solve() -> int:
    """Find largest square formed by any member of a square anagram pair in words.txt.
    
    Time Complexity: O(W^2 + S)
    Space Complexity: O(W + S)
    """
    url = "https://projecteuler.net/resources/documents/0098_words.txt"
    with urllib.request.urlopen(url, timeout=5) as resp:
        text = resp.read().decode("utf-8")

    words = [w.strip('"') for w in text.strip().split(",") if w.strip('"')]

    # Group words by anagram key
    anagram_groups = defaultdict(list)
    for w in words:
        anagram_groups["".join(sorted(w))].append(w)

    valid_pairs = []
    for group in anagram_groups.values():
        if len(group) >= 2:
            for i in range(len(group)):
                for j in range(i + 1, len(group)):
                    valid_pairs.append((group[i], group[j]))

    # Precompute squares by length
    max_len = max(len(p[0]) for p in valid_pairs)
    squares_by_len = defaultdict(list)
    n = 1
    while True:
        sq = n * n
        s_sq = str(sq)
        L = len(s_sq)
        if L > max_len:
            break
        if L >= 2:
            squares_by_len[L].append(s_sq)
        n += 1

    max_square = 0

    for w1, w2 in valid_pairs:
        L = len(w1)
        for s1 in squares_by_len[L]:
            # Check 1-to-1 mapping condition
            char_to_digit = {}
            digit_to_char = {}
            valid_map = True
            for ch, d in zip(w1, s1):
                if ch in char_to_digit and char_to_digit[ch] != d:
                    valid_map = False
                    break
                if d in digit_to_char and digit_to_char[d] != ch:
                    valid_map = False
                    break
                char_to_digit[ch] = d
                digit_to_char[d] = ch

            if not valid_map:
                continue

            # Apply mapping to w2
            s2_chars = [char_to_digit[ch] for ch in w2]
            if s2_chars[0] == '0':
                continue  # No leading zeroes

            s2 = "".join(s2_chars)
            sq2 = int(s2)
            root2 = math.isqrt(sq2)
            if root2 * root2 == sq2:
                max_square = max(max_square, int(s1), sq2)

    return max_square
