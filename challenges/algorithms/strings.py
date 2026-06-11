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
