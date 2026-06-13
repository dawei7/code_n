"""String algorithms - anagram checks, palindromes, pattern matching.

Three classic O(n)-ish string problems. They share a ``str``
input shape, distinct from the list-based 1D challenges, but
the spec framework handles them with the same ``setup_fn`` /
``verify_fn`` pattern.
"""

from __future__ import annotations

import random
from typing import Any, Optional

from challenges.spec import AlgorithmSpec, Sample
from code_n.counter import ComplexityClass


# === string_01: Anagram Check ======================================


STRING_01_SOURCE = '''
def solve(s, t):
    """Return True iff s and t are anagrams of each other.

    An anagram uses exactly the same letters the same number of
    times; case is significant and whitespace is treated as a
    character.
    """
    return sorted(s) == sorted(t)
'''


def _setup_anagram(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    # Build a random lowercase string of length n. Half the time
    # we shuffle it (anagram, True); the other half we mutate one
    # character (not an anagram, False). For n=4 this still
    # produces deterministic and interesting cases.
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s = "".join(rng.choice(alphabet) for _ in range(max(1, n)))
    is_anagram = rng.random() < 0.5
    if is_anagram:
        chars = list(s)
        rng.shuffle(chars)
        t = "".join(chars)
    else:
        # Change one character at a random position. Use a letter
        # that's definitely not the current one to make the test
        # robust.
        t_list = list(s)
        idx = rng.randint(0, len(t_list) - 1)
        new_char = rng.choice(alphabet)
        while new_char == t_list[idx]:
            new_char = rng.choice(alphabet)
        t_list[idx] = new_char
        t = "".join(t_list)
    challenge._is_anagram = is_anagram
    return {"s": s, "t": t}


def _verify_anagram(challenge, result: Any) -> bool:
    if not isinstance(result, bool):
        return False
    return result == challenge._is_anagram


# === string_02: Longest Palindromic Substring ======================
#
# IMPORTANT tiebreak: when two palindromes share the longest
# length, return the leftmost (lowest starting index). Both
# STRING_02_SOURCE and _verify_longest_palindrome implement the
# same leftmost rule.


STRING_02_SOURCE = '''
def solve(s):
    """Return the longest palindromic substring of s.

    Tiebreak: the leftmost substring wins.
    """
    n = len(s)
    if n == 0:
        return ""
    # Expand-around-center, expanding both odd- and even-length
    # centers, tracking the best (longest, leftmost) match.
    best_lo, best_hi = 0, 0  # inclusive indices into s

    def expand(lo, hi):
        while lo >= 0 and hi < n and s[lo] == s[hi]:
            lo -= 1
            hi += 1
        return lo + 1, hi - 1  # last matching pair

    for c in range(n):
        # Odd-length: center is s[c]
        lo, hi = expand(c, c)
        if hi - lo > best_hi - best_lo:
            best_lo, best_hi = lo, hi
        # Even-length: center is between s[c-1] and s[c]
        if c > 0:
            lo, hi = expand(c - 1, c)
            if hi - lo > best_hi - best_lo:
                best_lo, best_hi = lo, hi

    return s[best_lo:best_hi + 1]
'''


def _setup_longest_palindrome(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    # Build a string of length n with at least one palindrome.
    # We always include "aa" (even length 2) or a single char
    # so the answer is at least length 1.
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s = "".join(rng.choice(alphabet) for _ in range(max(1, n)))
    challenge._s = s
    return {"s": s}


def _verify_longest_palindrome(challenge, result: Any) -> bool:
    if not isinstance(result, str):
        return False
    s = challenge._s
    expected = STRING_02_SOURCE_DICT["solve"](s)
    return result == expected


# Compile the source once so the verifier can call the canonical
# solve without re-parsing the source string. The dict name is
# referenced by _verify_longest_palindrome.
_STRING_02_NS: dict[str, Any] = {"__name__": "spec.string_02"}
exec(STRING_02_SOURCE, _STRING_02_NS)
STRING_02_SOURCE_DICT = _STRING_02_NS


# === string_03: KMP String Matching ================================
#
# Knuth-Morris-Pratt. The player implements the failure-function
# (a.k.a. prefix-function) and uses it to scan the text in O(n+m).
# Returns the first index where pattern occurs in text, or -1.


STRING_03_SOURCE = '''
def solve(text, pattern):
    """Find the first index of pattern in text, or -1 if absent.

    Knuth-Morris-Pratt. Build the longest-proper-prefix-which-is-
    suffix table (the failure function) over the pattern, then
    walk the text keeping a running match length; on a mismatch,
    fall back to the failure function instead of restarting.
    """
    n, m = len(text), len(pattern)
    if m == 0:
        return 0  # empty pattern matches at position 0
    if m > n:
        return -1

    # Failure function: pi[i] = length of the longest proper prefix
    # of pattern[0..i] that is also a suffix of pattern[0..i].
    pi = [0] * m
    k = 0
    for i in range(1, m):
        while k > 0 and pattern[k] != pattern[i]:
            k = pi[k - 1]
        if pattern[k] == pattern[i]:
            k += 1
        pi[i] = k

    # Scan text.
    k = 0
    for i in range(n):
        while k > 0 and pattern[k] != text[i]:
            k = pi[k - 1]
        if pattern[k] == text[i]:
            k += 1
        if k == m:
            return i - m + 1
    return -1
'''


def _setup_kmp(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    alphabet = "abcdefghij"
    # Build a text of length max(n, 1).
    text_len = max(1, n)
    text = "".join(rng.choice(alphabet) for _ in range(text_len))
    # Decide whether the pattern will match or not.
    will_match = rng.random() < 0.5
    if will_match and text_len >= 1:
        # Take a random substring of text (length 1..min(3, text_len)).
        plen = rng.randint(1, min(3, text_len))
        start = rng.randint(0, text_len - plen)
        pattern = text[start:start + plen]
    else:
        # Build a pattern that's definitely not in text.
        pattern = "z" * rng.randint(1, 3)
    challenge._pattern = pattern
    challenge._text = text
    return {"text": text, "pattern": pattern}


def _verify_kmp(challenge, result: Any) -> bool:
    if not isinstance(result, int):
        return False
    text = challenge._text
    pattern = challenge._pattern
    # Re-run KMP to compute the expected answer.
    n, m = len(text), len(pattern)
    if m == 0:
        return result == 0
    if m > n:
        return result == -1
    pi = [0] * m
    k = 0
    for i in range(1, m):
        while k > 0 and pattern[k] != pattern[i]:
            k = pi[k - 1]
        if pattern[k] == pattern[i]:
            k += 1
        pi[i] = k
    k = 0
    for i in range(n):
        while k > 0 and pattern[k] != text[i]:
            k = pi[k - 1]
        if pattern[k] == text[i]:
            k += 1
        if k == m:
            return result == i - m + 1
    return result == -1


# === Spec list =====================================================


SPECS: list[AlgorithmSpec] = [
    AlgorithmSpec(
        id="string_01",
        name="Anagram Check",
        category="strings",
        difficulty=1,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Return True iff the two input strings are anagrams of each other.\n"
            "Two strings are anagrams if they contain exactly the same\n"
            "characters the same number of times (case-sensitive).\n"
            "Requirement: O(n) where n is the length of the strings.\n"
            "Source: https://www.geeksforgeeks.org/check-whether-two-strings-are-anagram-of-each-other/"
        ),
        source_url="https://www.geeksforgeeks.org/check-whether-two-strings-are-anagram-of-each-other/",
        params=["s", "t"],
        inputs={
            "s": "first string.",
            "t": "second string.",
        },
        returns="True iff s and t are anagrams.",
        source=STRING_01_SOURCE,
        setup_fn=_setup_anagram,
        verify_fn=_verify_anagram,
        samples=[
            Sample("s = 'listen', t = 'silent'", "True"),
            Sample("s = 'hello', t = 'world'", "False"),
            Sample("s = 'anagram', t = 'nagaram'", "True"),
        ],
        hint="Sort both strings and compare, or count character frequencies.",
        parents=["intro_01"],
        children=["string_02"],
    ),
    AlgorithmSpec(
        id="string_02",
        name="Longest Palindromic Substring",
        category="strings",
        difficulty=5,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Find the longest palindromic substring of the input string.\n"
            "A palindrome reads the same forwards and backwards.\n"
            "Tiebreak: if multiple substrings share the longest length,\n"
            "return the leftmost (lowest starting index).\n"
            "Requirement: O(n^2) — expand-around-center.\n"
            "Source: https://www.geeksforgeeks.org/longest-palindromic-substring/"
        ),
        source_url="https://www.geeksforgeeks.org/longest-palindromic-substring/",
        params=["s"],
        inputs={
            "s": "string to search.",
        },
        returns="the longest palindromic substring (leftmost on tie).",
        source=STRING_02_SOURCE,
        setup_fn=_setup_longest_palindrome,
        verify_fn=_verify_longest_palindrome,
        samples=[
            Sample("s = 'babad'", "'bab' or 'aba' (leftmost: 'bab')"),
            Sample("s = 'cbbd'", "'bb'"),
            Sample("s = 'a'", "'a'"),
        ],
        hint="Expand around every center (both odd and even). Track the longest match.",
        parents=["string_01"],
        children=["string_03"],
    ),
    AlgorithmSpec(
        id="string_03",
        name="KMP String Matching",
        category="strings",
        difficulty=7,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Find the first index where pattern occurs in text, or -1 if not found.\n"
            "Uses the Knuth-Morris-Pratt algorithm (prefix-function table).\n"
            "Requirement: O(n + m) — never restarts the match from scratch.\n"
            "Source: https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/"
        ),
        source_url="https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/",
        params=["text", "pattern"],
        inputs={
            "text": "the string to search in.",
            "pattern": "the string to search for.",
        },
        returns="the first index of pattern in text, or -1 if pattern does not occur.",
        source=STRING_03_SOURCE,
        setup_fn=_setup_kmp,
        verify_fn=_verify_kmp,
        samples=[
            Sample("text = 'hello', pattern = 'll'", "2"),
            Sample("text = 'aaaa', pattern = 'aa'", "0"),
            Sample("text = 'abcde', pattern = 'xyz'", "-1"),
        ],
        hint="Build the failure function over the pattern, then walk the text without ever restarting.",
        parents=["string_02"],
        children=[],
    ),
]


# === string_04: Naive Pattern Search ==========================
#
# The simplest O(n·m) substring search — slide the pattern
# across the text and check every position. Kept around
# because it's the easiest pattern matcher to write; the
# KMP spec (string_03) is the linear-time alternative.


STRING_04_SOURCE = '''
def solve(text, pattern):
    """Naive substring search. First index of pattern in text, or -1."""
    n, m = len(text), len(pattern)
    if m == 0:
        return 0
    if m > n:
        return -1
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            return i
    return -1
'''


def _setup_naive(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    alphabet = "abcdefgh"
    text_len = max(1, n)
    text = "".join(rng.choice(alphabet) for _ in range(text_len))
    # Half the time embed a real pattern (1..3 chars), half the
    # time use one that's not in the text.
    will_match = rng.random() < 0.5
    if will_match and text_len >= 1:
        plen = rng.randint(1, min(3, text_len))
        start = rng.randint(0, text_len - plen)
        pattern = text[start:start + plen]
    else:
        pattern = "z" * rng.randint(1, 3)
    challenge._text = text
    challenge._pattern = pattern
    return {"text": text, "pattern": pattern}


def _verify_naive(challenge, result: Any) -> bool:
    if not isinstance(result, int):
        return False
    text, pattern = challenge._text, challenge._pattern
    n, m = len(text), len(pattern)
    if m == 0:
        return result == 0
    if m > n:
        return result == -1
    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            return result == i
    return result == -1


# === string_05: Longest Common Substring =====================
#
# DP over two strings: longest contiguous substring shared
# by both. Returns the substring itself (leftmost on tie)
# AND its length is the canonical answer. The spec asks for
# the length only — a single int is the simplest return.


STRING_05_SOURCE = '''
def solve(s, t):
    """Length of the longest common substring of s and t."""
    m, n = len(s), len(t)
    if m == 0 or n == 0:
        return 0
    # dp[i][j] = length of the longest common suffix of s[:i] and t[:j].
    # We only need the previous row.
    prev = [0] * (n + 1)
    best = 0
    for i in range(1, m + 1):
        cur = [0] * (n + 1)
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                cur[j] = prev[j - 1] + 1
                if cur[j] > best:
                    best = cur[j]
        prev = cur
    return best
'''


def _setup_lcsubstr(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    alphabet = "abcdef"
    len1 = max(1, min(n, 12))
    len2 = max(1, min(n, 12))
    s = "".join(rng.choice(alphabet) for _ in range(len1))
    t = "".join(rng.choice(alphabet) for _ in range(len2))
    # Pre-compute expected.
    m, n_words = len(s), len(t)
    prev = [0] * (n_words + 1)
    best = 0
    for i in range(1, m + 1):
        cur = [0] * (n_words + 1)
        for j in range(1, n_words + 1):
            if s[i - 1] == t[j - 1]:
                cur[j] = prev[j - 1] + 1
                if cur[j] > best:
                    best = cur[j]
        prev = cur
    challenge._expected = best
    return {"s": s, "t": t}


def _verify_lcsubstr(challenge, result: Any) -> bool:
    if not isinstance(result, int):
        return False
    return result == challenge._expected


# Append the new string specs to SPECS.
SPECS.extend([
    AlgorithmSpec(
        id="string_04",
        name="Naive Pattern Search",
        category="strings",
        difficulty=3,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Find the first index where pattern occurs in text using\n"
            "the naive O(n*m) sliding-window approach. Returns -1\n"
            "if the pattern is not present.\n"
            "Use KMP (string_03) for the linear-time alternative.\n"
            "Source: https://www.geeksforgeeks.org/naive-algorithm-for-pattern-searching/"
        ),
        source_url="https://www.geeksforgeeks.org/naive-algorithm-for-pattern-searching/",
        params=["text", "pattern"],
        inputs={
            "text": "the string to search in.",
            "pattern": "the string to search for.",
        },
        returns="the first index of pattern in text, or -1 if not found.",
        source=STRING_04_SOURCE,
        setup_fn=_setup_naive,
        verify_fn=_verify_naive,
        samples=[
            Sample("text = 'hello', pattern = 'll'", "2"),
            Sample("text = 'aaaa', pattern = 'aa'", "0"),
            Sample("text = 'abcde', pattern = 'xyz'", "-1"),
        ],
        hint="Slide the pattern over the text. Compare character-by-character at every position.",
        parents=["string_03"],
        children=[],
    ),
    AlgorithmSpec(
        id="string_05",
        name="Longest Common Substring",
        category="strings",
        difficulty=5,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Find the length of the longest contiguous substring that\n"
            "appears in both input strings. Distinct from the longest\n"
            "common SUBSEQUENCE (dp_04), which need not be contiguous.\n"
            "Requirement: O(m * n) DP over a 2-row table.\n"
            "Source: https://www.geeksforgeeks.org/longest-common-substring-dp-29/"
        ),
        source_url="https://www.geeksforgeeks.org/longest-common-substring-dp-29/",
        params=["s", "t"],
        inputs={
            "s": "first string.",
            "t": "second string.",
        },
        returns="the length of the longest contiguous substring shared by s and t.",
        source=STRING_05_SOURCE,
        setup_fn=_setup_lcsubstr,
        verify_fn=_verify_lcsubstr,
        samples=[
            Sample("s = 'abcdxyz', t = 'xyzabcd'", "4 ('abcd' or 'xyz')"),
            Sample("s = 'GeeksforGeeks', t = 'GeeksQuiz'", "5 ('Geeks')"),
            Sample("s = 'abc', t = 'def'", "0"),
        ],
        hint="dp[i][j] = length of the longest common suffix of s[:i] and t[:j]. Take the max over all i, j.",
        parents=["string_03"],
        children=[],
    ),
])


# === string_06: Rabin-Karp ======================================
#
# Rolling-hash substring search. We use a simple base+mod hash;
# for the test sizes (text/pattern up to ~16 chars) collisions
# are vanishingly unlikely.


STRING_06_SOURCE = '''
def solve(text, pattern):
    """Rabin-Karp substring search via rolling hash.

    Returns the first index of pattern in text, or -1.
    """
    n, m = len(text), len(pattern)
    if m == 0:
        return 0
    if m > n:
        return -1
    BASE = 256
    MOD = (1 << 61) - 1  # Mersenne-ish prime for fewer collisions
    # Hash of pattern and the first window of text.
    p_hash = 0
    t_hash = 0
    h = 1
    for i in range(m):
        p_hash = (p_hash * BASE + ord(pattern[i])) % MOD
        t_hash = (t_hash * BASE + ord(text[i])) % MOD
        if i < m - 1:
            h = (h * BASE) % MOD
    # Slide the window.
    for i in range(n - m + 1):
        if p_hash == t_hash:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            t_hash = ((t_hash - ord(text[i]) * h) * BASE + ord(text[i + m])) % MOD
            if t_hash < 0:
                t_hash += MOD
    return -1
'''


def _setup_rabin_karp(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    alphabet = "abcdefghij"
    text_len = max(1, n)
    text = "".join(rng.choice(alphabet) for _ in range(text_len))
    will_match = rng.random() < 0.5
    if will_match and text_len >= 1:
        plen = rng.randint(1, min(3, text_len))
        start = rng.randint(0, text_len - plen)
        pattern = text[start:start + plen]
    else:
        pattern = "z" * rng.randint(1, 3)
    challenge._text = text
    challenge._pattern = pattern
    return {"text": text, "pattern": pattern}


def _verify_rabin_karp(challenge, result: Any) -> bool:
    if not isinstance(result, int):
        return False
    text, pattern = challenge._text, challenge._pattern
    n, m = len(text), len(pattern)
    if m == 0:
        return result == 0
    if m > n:
        return result == -1
    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            return result == i
    return result == -1


# === string_07: Z-Algorithm =====================================
#
# Linear-time pattern matching using the Z-array. Z[i] is the
# longest prefix of s that matches s[i:]. To find pattern in
# text, concatenate pattern + '$' + text and find positions
# where Z[i] == len(pattern).


STRING_07_SOURCE = '''
def solve(text, pattern):
    """Z-algorithm pattern search. First index of pattern in text, or -1."""
    n, m = len(text), len(pattern)
    if m == 0:
        return 0
    if m > n:
        return -1
    # Build Z-array over pattern + '$' + text.
    s = pattern + "$" + text
    z = [0] * len(s)
    l = 0
    r = 0
    for i in range(1, len(s)):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < len(s) and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l = i
            r = i + z[i]
    # Pattern matches wherever z[i] == m, in the suffix starting
    # at index m + 1 of s (i.e. position i - m - 1 in text).
    offset = m + 1
    for i in range(offset, len(s)):
        if z[i] == m:
            return i - offset
    return -1
'''


def _setup_z_algo(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    alphabet = "abcdefgh"
    text_len = max(1, n)
    text = "".join(rng.choice(alphabet) for _ in range(text_len))
    will_match = rng.random() < 0.5
    if will_match and text_len >= 1:
        plen = rng.randint(1, min(3, text_len))
        start = rng.randint(0, text_len - plen)
        pattern = text[start:start + plen]
    else:
        # Use a separator character not in alphabet to avoid edge cases.
        pattern = "z" * rng.randint(1, 3)
    challenge._text = text
    challenge._pattern = pattern
    return {"text": text, "pattern": pattern}


def _verify_z_algo(challenge, result: Any) -> bool:
    if not isinstance(result, int):
        return False
    text, pattern = challenge._text, challenge._pattern
    n, m = len(text), len(pattern)
    if m == 0:
        return result == 0
    if m > n:
        return result == -1
    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            return result == i
    return result == -1


# === string_08: Smallest Window Containing All Chars ============
#
# Given a string s and a pattern p, find the smallest substring
# of s that contains every character of p (with multiplicity).
# The pattern uses distinct characters only so the test stays
# simple (each char in p appears exactly once).


STRING_08_SOURCE = '''
def solve(s, p):
    """Smallest substring of s containing every char of p at least once.

    Pattern p uses distinct characters. Returns the smallest
    such substring, or "" if no such substring exists.
    """
    n = len(s)
    if not p or not s:
        return ""
    need = set(p)
    have = set()
    best = ""
    left = 0
    for right in range(n):
        if s[right] in need:
            have.add(s[right])
        # Shrink from the left while we still have everything.
        while have >= need and left <= right:
            window = s[left:right + 1]
            if not best or len(window) < len(best):
                best = window
            if s[left] in need:
                # Removing s[left] might drop coverage.
                pass
            left += 1
            # Re-evaluate coverage after the shift.
            have = set()
            for k in range(left, right + 1):
                if s[k] in need:
                    have.add(s[k])
            if not (have >= need):
                break
    return best
'''


def _setup_smallest_window(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    s_len = max(2, min(n, 16))
    alphabet = "abcde"
    s = "".join(rng.choice(alphabet) for _ in range(s_len))
    # Pattern: a non-empty subset of alphabet (distinct chars).
    p = list(set(rng.choice(alphabet) for _ in range(rng.randint(1, 3))))
    rng.shuffle(p)
    p = "".join(p)
    challenge._s = s
    challenge._p = p
    return {"s": s, "p": p}


def _verify_smallest_window(challenge, result: Any) -> bool:
    if not isinstance(result, str):
        return False
    s, p = challenge._s, challenge._p
    if not p or not s:
        return result == ""
    # Brute-force: try every substring.
    expected = ""
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            window = s[i:j]
            if all(c in window for c in p):
                if not expected or len(window) < len(expected):
                    expected = window
                break  # inner loop: smallest window starting at i
    return result == expected


SPECS.extend([
    AlgorithmSpec(
        id="string_06",
        name="Rabin-Karp",
        category="strings",
        difficulty=6,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Find the first index where pattern occurs in text using\n"
            "the Rabin-Karp rolling-hash algorithm. Uses a base-256\n"
            "polynomial hash mod a large prime; on a hash match we\n"
            "verify by direct comparison to avoid false positives.\n"
            "Requirement: O(n + m) average; worst-case O(n*m) on\n"
            "spurious hash collisions (vanishingly rare in practice).\n"
            "Source: https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/"
        ),
        source_url="https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/",
        params=["text", "pattern"],
        inputs={
            "text": "the string to search in.",
            "pattern": "the string to search for.",
        },
        returns="the first index of pattern in text, or -1 if not found.",
        source=STRING_06_SOURCE,
        setup_fn=_setup_rabin_karp,
        verify_fn=_verify_rabin_karp,
        samples=[
            Sample("text = 'hello', pattern = 'll'", "2"),
            Sample("text = 'aaaa', pattern = 'aa'", "0"),
            Sample("text = 'abcde', pattern = 'xyz'", "-1"),
        ],
        hint="Hash the pattern and the first window of text. Slide: drop text[i], add text[i+m].",
        parents=["string_04"],
        children=[],
    ),
    AlgorithmSpec(
        id="string_07",
        name="Z-Algorithm",
        category="strings",
        difficulty=7,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Find the first index where pattern occurs in text using\n"
            "the Z-algorithm. Builds the Z-array over (pattern + '$' + text)\n"
            "in linear time, then scans for positions where Z[i] == len(pattern).\n"
            "Requirement: O(n + m) — strictly linear.\n"
            "Source: https://www.geeksforgeeks.org/z-algorithm-linear-time-pattern-searching-algorithm/"
        ),
        source_url="https://www.geeksforgeeks.org/z-algorithm-linear-time-pattern-searching-algorithm/",
        params=["text", "pattern"],
        inputs={
            "text": "the string to search in.",
            "pattern": "the string to search for.",
        },
        returns="the first index of pattern in text, or -1 if not found.",
        source=STRING_07_SOURCE,
        setup_fn=_setup_z_algo,
        verify_fn=_verify_z_algo,
        samples=[
            Sample("text = 'hello', pattern = 'll'", "2"),
            Sample("text = 'aaaa', pattern = 'aa'", "0"),
            Sample("text = 'abcde', pattern = 'xyz'", "-1"),
        ],
        hint="Z[i] = longest prefix of s matching s[i:]. Compute in O(n); match where Z[i] == m.",
        parents=["string_04"],
        children=[],
    ),
    AlgorithmSpec(
        id="string_08",
        name="Smallest Window",
        category="strings",
        difficulty=7,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Given a string s and a pattern p (with distinct chars),\n"
            "find the smallest substring of s that contains every\n"
            "character of p at least once. Returns the smallest such\n"
            "substring, or \"\" if no such substring exists.\n"
            "Requirement: O(n) sliding window.\n"
            "Source: https://www.geeksforgeeks.org/smallest-window-contains-characters-string/"
        ),
        source_url="https://www.geeksforgeeks.org/smallest-window-contains-characters-string/",
        params=["s", "p"],
        inputs={
            "s": "the string to search in.",
            "p": "the pattern (distinct characters).",
        },
        returns="the smallest substring of s containing all of p, or '' if none.",
        source=STRING_08_SOURCE,
        setup_fn=_setup_smallest_window,
        verify_fn=_verify_smallest_window,
        samples=[
            Sample("s = 'timetopractice', p = 'toc'", "'toprac' (smallest window containing t, o, c)"),
            Sample("s = 'zoomlazapop', p = 'oza'", "'oza'"),
            Sample("s = 'abc', p = 'xyz'", "'' (no window contains all of p)"),
        ],
        hint="Sliding window: expand right to cover all pattern chars, then shrink from the left as long as coverage is maintained.",
        parents=["string_04"],
        children=[],
    ),
])


# === string_09: Run-Length Encoding =============================
#
# Encode a string by collapsing consecutive identical chars
# into <char><count> pairs. Empty input -> empty output.


STRING_09_SOURCE = '''
def solve(s):
    """Run-length encode s as <char><count> pairs."""
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
'''


def _setup_rle(challenge, n, seed):
    rng = random.Random(seed)
    s_len = max(0, min(n, 12))
    s = ""
    while len(s) < s_len:
        run = rng.randint(1, 3)
        c = rng.choice("abcde")
        s += c * run
    s = s[:s_len]
    ns: dict[str, Any] = {"__name__": "spec.string_09"}
    exec(STRING_09_SOURCE, ns)
    challenge._expected = ns["solve"](s)
    return {"s": s}


def _verify_rle(challenge, result):
    if not isinstance(result, str):
        return False
    return result == challenge._expected


# === string_10: Word Break (segmentation) =======================
#
# Same as dp_15 but in the strings category: given a string
# and a dictionary, return True iff the string can be
# segmented into a sequence of dictionary words.


STRING_10_SOURCE = '''
def solve(s, word_dict):
    """True iff s can be segmented into dictionary words."""
    n = len(s)
    word_set = set(word_dict)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[n]
'''


def _setup_word_break_str(challenge, n, seed):
    rng = random.Random(seed)
    s_len = max(2, min(n, 12))
    word_dict = ["a", "ab", "abc", "b", "bc", "cd", "abcde", "de", "f", "fg"]
    s = "".join(rng.choice(word_dict) for _ in range(max(1, s_len // 2)))
    challenge._s = s
    return {"s": s, "word_dict": word_dict}


def _verify_word_break_str(challenge, result):
    if not isinstance(result, bool):
        return False
    return isinstance(result, bool)


SPECS.extend([
    AlgorithmSpec(
        id="string_09",
        name="Run-Length Encoding",
        category="strings",
        difficulty=2,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Encode a string by collapsing consecutive identical\n"
            "characters into <char><count> pairs. For example,\n"
            "'aaabbc' becomes 'a3b2c1' and '' becomes ''.\n"
            "The input contains only lowercase letters (no digits\n"
            "in the alphabet so there's no ambiguity).\n"
            "Requirement: O(n).\n"
            "Source: https://www.geeksforgeeks.org/run-length-encoding/"
        ),
        source_url="https://www.geeksforgeeks.org/run-length-encoding/",
        params=["s"],
        inputs={"s": "the input string (lowercase letters)."},
        returns="the run-length encoded string.",
        source=STRING_09_SOURCE,
        setup_fn=_setup_rle,
        verify_fn=_verify_rle,
        samples=[
            Sample("s = 'aaabbc'", "'a3b2c1'"),
            Sample("s = 'abcd'", "'a1b1c1d1'"),
            Sample("s = ''", "''"),
        ],
        hint="Walk the string, counting consecutive equal chars. Emit <char><count> at each transition.",
        parents=["string_01"],
        children=[],
    ),
    AlgorithmSpec(
        id="string_10",
        name="Word Break (Strings)",
        category="strings",
        difficulty=4,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Given a string s and a dictionary of words, return True\n"
            "iff s can be segmented into a sequence of one or more\n"
            "dictionary words. The setup builds s by concatenating\n"
            "random dictionary words, so the answer is always True.\n"
            "This is the strings-category variant of dp_15.\n"
            "Requirement: O(n * L).\n"
            "Source: https://www.geeksforgeeks.org/word-break-problem-dp-32/"
        ),
        source_url="https://www.geeksforgeeks.org/word-break-problem-dp-32/",
        params=["s", "word_dict"],
        inputs={
            "s": "the string to segment.",
            "word_dict": "list of unique words in the dictionary.",
        },
        returns="True iff s can be segmented into dictionary words.",
        source=STRING_10_SOURCE,
        setup_fn=_setup_word_break_str,
        verify_fn=_verify_word_break_str,
        samples=[
            Sample("s = 'leetcode', word_dict = ['leet', 'code']", "True"),
            Sample("s = 'catsandog', word_dict = ['cats', 'dog', 'sand', 'and', 'cat']", "False"),
        ],
        hint="dp[i] = True if some dp[j] is True AND s[j:i] is in word_dict.",
        parents=["string_04"],
        children=["string_11"],
    ),
])


# === string_11: Longest Common Substring ===

STRING_11_SOURCE = '''
def solve(s1, s2, n1, n2):
    """Length of the longest common substring of s1 and s2.

    dp[i][j] = length of the longest common suffix of s1[..i]
    and s2[..j]. dp[i][j] = dp[i-1][j-1] + 1 if s1[i-1] == s2[j-1]
    else 0. The answer is the maximum dp value.
    """
    if n1 == 0 or n2 == 0:
        return 0
    best = 0
    dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > best:
                    best = dp[i][j]
            else:
                dp[i][j] = 0
    return best
'''


def _setup_lc_substring(challenge, n, seed):
    rng = random.Random(seed)
    n1 = max(1, min(n, 6))
    n2 = max(1, min(n - n1 + 1, 6))
    n1 = min(n1, 6)
    n2 = min(n2, 6)
    s1 = "".join(rng.choice("abc") for _ in range(n1))
    s2 = "".join(rng.choice("abc") for _ in range(n2))
    challenge._s1 = s1
    challenge._s2 = s2
    return {"s1": s1, "s2": s2, "n1": len(s1), "n2": len(s2)}


def _verify_lc_substring(challenge, result):
    if not isinstance(result, int):
        return False
    s1, s2 = challenge._s1, challenge._s2
    # Brute force: check every substring.
    best = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            k = 0
            while i + k < len(s1) and j + k < len(s2) and s1[i + k] == s2[j + k]:
                k += 1
            if k > best:
                best = k
    return result == best


# === string_12: String to Integer (atoi) ===
#
# Trim leading whitespace, handle optional +/- sign, then read
# digits until a non-digit. Clamp to the int32 range [-2^31, 2^31-1].
# Return 0 if the string is empty / no digits / overflow before sign.


STRING_12_SOURCE = '''
def solve(s, n):
    """Implement atoi: parse s as a 32-bit signed integer."""
    if n == 0:
        return 0
    i = 0
    # Skip leading whitespace.
    while i < n and s[i] == " ":
        i += 1
    if i == n:
        return 0
    sign = 1
    if s[i] == "+":
        i += 1
    elif s[i] == "-":
        sign = -1
        i += 1
    result = 0
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    while i < n and s[i].isdigit():
        digit = int(s[i])
        new_result = result * 10 + digit
        if sign == 1 and new_result > INT_MAX:
            return INT_MAX
        if sign == -1 and -new_result < INT_MIN:
            return INT_MIN
        result = new_result
        i += 1
    return sign * result
'''


def _setup_atoi(challenge, n, seed):
    rng = random.Random(seed)
    # Generate a string with whitespace, optional sign, and digits.
    n_chars = max(1, min(n, 8))
    digits = [str(rng.randint(0, 9)) for _ in range(n_chars)]
    s_list = []
    for _ in range(rng.randint(0, 3)):
        s_list.append(" ")
    if rng.random() < 0.5:
        s_list.append(rng.choice("+-"))
    s_list.extend(digits)
    # Sometimes add a non-digit suffix.
    if rng.random() < 0.5:
        s_list.append(rng.choice("abc"))
    s = "".join(s_list)
    challenge._s = s
    return {"s": s, "n": len(s)}


def _verify_atoi(challenge, result):
    if not isinstance(result, int):
        return False
    s = challenge._s
    i = 0
    while i < len(s) and s[i] == " ":
        i += 1
    if i == len(s):
        return result == 0
    sign = 1
    if s[i] == "+":
        i += 1
    elif s[i] == "-":
        sign = -1
        i += 1
    value = 0
    while i < len(s) and s[i].isdigit():
        value = value * 10 + int(s[i])
        i += 1
    value = sign * value
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    if value > INT_MAX:
        value = INT_MAX
    if value < INT_MIN:
        value = INT_MIN
    return result == value


SPECS.extend([
    AlgorithmSpec(
        id="string_11",
        name="Longest Common Substring",
        category="strings",
        difficulty=4,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Length of the longest common substring (consecutive, not\n"
            "subsequence) of s1 and s2. Standard DP: dp[i][j] = length\n"
            "of the common suffix of s1[..i] and s2[..j]. The answer\n"
            "is the max over the table.\n"
            "Source: https://www.geeksforgeeks.org/longest-common-substring-dp-29/"
        ),
        source_url="https://www.geeksforgeeks.org/longest-common-substring-dp-29/",
        params=["s1", "s2", "n1", "n2"],
        inputs={
            "s1": "first string (capped at 6 in the setup).",
            "s2": "second string (capped at 6 in the setup).",
            "n1": "length of s1.",
            "n2": "length of s2.",
        },
        returns="the length of the longest common substring.",
        source=STRING_11_SOURCE,
        setup_fn=_setup_lc_substring,
        verify_fn=_verify_lc_substring,
        samples=[
            Sample('s1 = "abcdxyz", s2 = "xyzabcd", n1 = 7, n2 = 7', "4 (abcd or xyzd)"),
            Sample('s1 = "geeks", s2 = "geekfor", n1 = 5, n2 = 7', "4 (geek)"),
        ],
        hint="dp[i][j] = dp[i-1][j-1] + 1 if chars match, else 0. Track the max.",
        parents=["string_10"],
        children=["string_12"],
    ),
    AlgorithmSpec(
        id="string_12",
        name="String to Integer (atoi)",
        category="strings",
        difficulty=3,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Parse a string as a 32-bit signed integer. Skip leading\n"
            "whitespace, handle an optional +/- sign, read digits\n"
            "until a non-digit. Clamp to the int32 range.\n"
            "Source: https://www.geeksforgeeks.org/write-your-own-atoi/"
        ),
        source_url="https://www.geeksforgeeks.org/write-your-own-atoi/",
        params=["s", "n"],
        inputs={
            "s": "the string to parse.",
            "n": "length of s.",
        },
        returns="the parsed integer (clamped to int32 range, or 0 if invalid).",
        source=STRING_12_SOURCE,
        setup_fn=_setup_atoi,
        verify_fn=_verify_atoi,
        samples=[
            Sample("s = ' -42', n = 4", "-42"),
            Sample("s = '4193 with words', n = 15", "4193"),
            Sample("s = 'words and 987', n = 13", "0"),
        ],
        hint="Skip whitespace, optional sign, read digits, clamp to int32 range.",
        parents=["string_11"],
        children=["string_13"],
    ),
])


# === string_13: Z-Algorithm ===

STRING_13_SOURCE = '''
def solve(s, n, pattern, m):
    """Return the list of starting indices in s where pattern occurs.

    Build the Z-array of pattern + '$' + s, then walk it.
    Z[i] is the longest prefix of the combined string that
    starts at position i. Z[i] >= m iff pattern occurs at
    position i - m - 1 in s.
    """
    if m == 0 or n == 0:
        return []
    combined = pattern + "$" + s
    L = len(combined)
    z = [0] * L
    left = 0
    right = 0
    for i in range(1, L):
        if i < right:
            z[i] = min(right - i, z[i - left])
        while i + z[i] < L and combined[z[i]] == combined[i + z[i]]:
            z[i] += 1
        if i + z[i] > right:
            left = i
            right = i + z[i]
    out = []
    for i in range(m + 1, L):
        if z[i] == m:
            out.append(i - m - 1)
    return out
'''


def _setup_z_algo(challenge, n, seed):
    rng = random.Random(seed)
    n_chars = max(2, min(n, 10))
    s = "".join(rng.choice("abc") for _ in range(n_chars))
    m = rng.randint(1, 3)
    pattern = "".join(rng.choice("abc") for _ in range(m))
    challenge._s = s
    challenge._pattern = pattern
    return {"s": s, "n": len(s), "pattern": pattern, "m": m}


def _verify_z_algo(challenge, result):
    if not isinstance(result, list):
        return False
    s = challenge._s
    pattern = challenge._pattern
    expected = []
    for i in range(len(s) - len(pattern) + 1):
        if s[i:i + len(pattern)] == pattern:
            expected.append(i)
    return result == expected


SPECS.extend([
    AlgorithmSpec(
        id="string_13",
        name="Z-Algorithm (Pattern Search)",
        category="strings",
        difficulty=5,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Find every position in s where pattern occurs, using the\n"
            "Z-algorithm. Build the Z-array of pattern + '$' + s;\n"
            "Z[i] is the longest prefix of the combined string that\n"
            "starts at position i. Z[i] == |pattern| in the s region\n"
            "iff pattern matches there. O(n + m) total.\n"
            "Source: https://www.geeksforgeeks.org/z-algorithm-linear-time-pattern-searching-algorithm/"
        ),
        source_url="https://www.geeksforgeeks.org/z-algorithm-linear-time-pattern-searching-algorithm/",
        params=["s", "n", "pattern", "m"],
        inputs={
            "s": "string to search in.",
            "n": "length of s.",
            "pattern": "the pattern.",
            "m": "length of pattern.",
        },
        returns="a sorted list of starting indices where pattern occurs.",
        source=STRING_13_SOURCE,
        setup_fn=_setup_z_algo,
        verify_fn=_verify_z_algo,
        samples=[
            Sample("s = 'aabxaayaab', n = 10, pattern = 'aab', m = 3", "[0, 6]"),
            Sample("s = 'aaaa', n = 4, pattern = 'aa', m = 2", "[0, 1, 2]"),
        ],
        hint="Build Z-array of pattern + '$' + s. Z[i] >= m in s-region means match.",
        parents=["string_12"],
        children=[],
    ),
])
