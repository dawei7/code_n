# Palindromic Partitioning (Min Cuts)

| | |
|---|---|
| **ID** | `dp_24` |
| **Category** | dynamic |
| **Complexity (required)** | O(n²) |
| **Difficulty** | 6/10 |
| **Interview relevance** | 9/10 |
| **Wikipedia** | [Palindrome](https://en.wikipedia.org/wiki/Palindrome) (problem variant) |

## Problem statement

Given a string `s`, partition it into substrings such that
**every substring is a palindrome**. Minimize the number of
cuts.

**Input:** a string `s`.
**Output:** the minimum number of cuts to partition `s` into
palindromes.

**Example:**

| s | Min cuts | Partitioning |
|---|---:|---|
| `"aab"` | 1 | `"aa" | "b"` |
| `"a"` | 0 | `"a"` |
| `"ab"` | 1 | `"a" | "b"` |
| `"abcba"` | 0 | `"abcba"` (already a palindrome) |
| `"ababbbabbababa"` | 3 | (one of many) |

## When to use it

- The classic 2D-string DP for **partitioning a string into
  palindromes**. Tests whether you can chain together the
  "is palindrome" sub-problem and the "min cuts" optimization.
- Foundation for **batch text processing** (find palindromic
  runs), **DNA palindromes**, and **combinatorial generation**
  (count all palindromic partitions of a string).

## Approach

Two-stage DP:

**Stage 1: precompute palindrome substrings.** Build a 2D
boolean table `is_pal[i][j]` = is `s[i..j]` a palindrome?
- `is_pal[i][i] = True` (single char).
- `is_pal[i][j] = (s[i] == s[j]) and (j - i < 2 or is_pal[i+1][j-1])`.
- Iterate `j - i` increasing.

**Stage 2: min cuts.** `dp[i]` = min cuts for `s[0..i-1]`
(length `i`).
- `dp[0] = 0`.
- For each `i` from `1` to `n`:
  - If `s[0..i-1]` is itself a palindrome: `dp[i] = 0`.
  - Otherwise, try every `j < i` such that `s[j..i-1]` is a
    palindrome. `dp[i] = min(dp[j] + 1)` over all such `j`.

**Answer:** `dp[n]`.

**Space optimization (Stage 1):** `is_pal[i][j]` only depends
on `is_pal[i+1][j-1]`, so iterate `j - i` increasing and you
get the inner-cell-first behavior for free.

## Algorithm (pseudocode)

```
min_cut(s):
    n = len(s)
    if n <= 1: return 0

    # Stage 1: palindrome table
    is_pal = [[False] * n for _ in range(n)]
    for i in range(n): is_pal[i][i] = True
    for length in 2..n:
        for i in 0..n-length:
            j = i + length - 1
            if s[i] == s[j] and (length == 2 or is_pal[i+1][j-1]):
                is_pal[i][j] = True

    # Stage 2: min cuts
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if is_pal[0][i-1]:
            dp[i] = 0
        else:
            dp[i] = min(dp[j] + 1 for j in range(i) if is_pal[j][i-1])
    return dp[n]
```

## Walk-through

`s = "aab"`. Expected: 1.

**Stage 1:**
- `is_pal[0][0] = T`, `is_pal[1][1] = T`, `is_pal[2][2] = T`.
- Length 2: (0,1) "aa": same, length 2, `is_pal[0][1] = T`. (1,2) "ab": different, F.
- Length 3: (0,2) "aab": `a != b`, F.

`is_pal`:
```
       0  1  2
  0  [ T  T  F ]
  1  [ .  T  F ]
  2  [ .  .  T ]
```

**Stage 2:**
- `dp[0] = 0`.
- `i=1`: `s[0..0] = "a"` is palindrome (is_pal[0][0]=T). `dp[1] = 0`.
- `i=2`: `s[0..1] = "aa"` is palindrome (is_pal[0][1]=T). `dp[2] = 0`.
- `i=3`: `s[0..2] = "aab"` not palindrome (is_pal[0][2]=F). Try j=0,1,2:
  - j=0: is_pal[0][2] = F. Skip.
  - j=1: is_pal[1][2] = F. Skip.
  - j=2: is_pal[2][2] = T. `dp[2] + 1 = 0 + 1 = 1`. `dp[3] = 1`.

Answer: `dp[3] = 1`. ✓ (partition: "aa" | "b".)

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | O(n²) | O(n²) |
| **Average** | O(n²) | O(n²) |
| **Worst** | O(n²) | O(n²) |

Both stages are O(n²). Space for the palindrome table is
O(n²). Can be reduced to O(n) by computing `is_pal[i][j]`
on the fly inside Stage 2.

## Variants & optimizations

- **Count all palindromic partitions** — backtracking from
  the cuts; exponential in the worst case.
- **Min cuts for K different palindromes** — generalize
  to a different cut objective.
- **Print the actual partition** — store the `j` that
  achieved the min, walk back to reconstruct.
- **O(n) space variant** — compute palindromes on the fly
  using expand-around-center; drop the 2D table.
- **Manacher's algorithm** — preprocess palindromes in
  O(n) (instead of O(n²)); useful when many queries need
  palindromic info.

## Real-world applications

- **Text processing** — find natural breakpoint in a
  palindromic document.
- **Bioinformatics** — locate palindromic subsequences in
  DNA for restriction-enzyme sites.
- **Music / palindromic lyrics** — find the best
  palindromic segmentation of a phrase.
- **Code formatting** — break a long string into palindromic
  visual chunks.
- **Compression** — palindromes are good candidates for
  back-references in LZ-style compression.

## Related algorithms in cOde(n)

- **[dp_14 — Palindromic Partitioning](dp_14_palindromic-partitioning.md)** —
  counts all partitions, doesn't minimize. (d=5/10, r=9/10)
- **[dp_19 — Longest Palindromic Subsequence](dp_19_longest-palindromic-subsequence.md)** —
  longest single palindrome, not a partition. (d=5/10, r=9/10)
- **[string_02 — Longest Palindromic Substring](string_02_longest-palindromic-substring.md)** —
  the contiguous variant (no gaps). (d=5/10, r=7/10)

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-
programming reference sites. For the canonical encyclopedia
entry, follow the Wikipedia link at the top of the page.
Source repository: <https://github.com/dawei7/code_n>.*
