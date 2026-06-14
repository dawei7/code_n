# Longest Palindromic Subsequence

| | |
|---|---|
| **ID** | `dp_19` |
| **Category** | dynamic |
| **Complexity (required)** | O(n²) |
| **Difficulty** | 5/10 |
| **Interview relevance** | 9/10 |
| **Wikipedia** | [Longest palindromic subsequence](https://en.wikipedia.org/wiki/Longest_palindromic_subsequence) |

## Problem statement

Given a string `s`, find the length of the longest
**palindromic subsequence**. A subsequence keeps the order
of elements but doesn't have to be contiguous.

**Input:** a string `s`.
**Output:** the length of the longest palindromic subsequence.

**Example:**

| s | LPS | Length |
|---|---|---:|
| `"bbbab"` | `"bbbb"` | 4 |
| `"cbbd"` | `"bb"` | 2 |
| `"a"` | `"a"` | 1 |
| `""` | `""` | 0 |
| `"racecar"` | `"racecar"` | 7 |
| `"abcda"` | `"a"` or `"d"` | 1 |

## When to use it

- The standard 2D-string DP. Reduction to **LCS** is the
  elegant insight: `LPS(s) = LCS(s, reverse(s))`.
- Foundation for the harder **Longest Palindromic
  Substring** (`string_02`), which requires contiguity.

## Approach

Two equivalent approaches.

### Approach A: 2D DP on `s`

Let `dp[i][j]` = the length of the longest palindromic
subsequence in the substring `s[i..j]` (inclusive).

**Recurrence:**
- If `s[i] == s[j]`: `dp[i][j] = dp[i+1][j-1] + 2`
  (extend the inner palindrome by 2).
  - Edge case: if `i == j`, the single character is a
    palindrome of length 1, so `dp[i][i] = 1`.
  - If `i+1 > j-1` (adjacent or same), the "inner" is
    empty, so the contribution is 2.
- Otherwise: `dp[i][j] = max(dp[i+1][j], dp[i][j-1])` (skip
  one of the two ends).

**Base case:** `dp[i][i] = 1` (single character).

**Answer:** `dp[0][n-1]`.

**Iteration order:** `j - i` increasing (longest substrings
last) so the inner sub-problems are computed first.

### Approach B: Reduce to LCS

The longest palindromic subsequence of `s` is the **longest
common subsequence** of `s` and `reverse(s)`. Same O(n²)
complexity; reuse the existing `dp_04` implementation.

## Algorithm (pseudocode)

```
lps(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for length in 2..n:
        for i in 0..n-length:
            j = i + length - 1
            if s[i] == s[j]:
                inner = dp[i+1][j-1] if i+1 <= j-1 else 0
                dp[i][j] = inner + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1]
```

## Walk-through

`s = "bbbab"`. Expected: 4.

`dp` is 5x5.

Initialize diagonal: `dp[i][i] = 1`.

**Length 2:** compare adjacent pairs.
- (0,1) "bb": `s[0]=s[1]=b`, inner is 0, so `dp[0][1] = 2`.
- (1,2) "bb": same, `dp[1][2] = 2`.
- (2,3) "ba": `s[2]=b, s[3]=a`, mismatch, `dp[2][3] = max(dp[3][3], dp[2][2]) = max(1, 1) = 1`.
- (3,4) "ab": mismatch, `dp[3][4] = max(dp[4][4], dp[3][3]) = 1`.

**Length 3:**
- (0,2) "bbb": `s[0]=s[2]=b`, inner `dp[1][1] = 1`, so `dp[0][2] = 1 + 2 = 3`.
- (1,3) "bba": `s[1]=b, s[3]=a`, mismatch, `dp[1][3] = max(dp[2][3], dp[1][2]) = max(1, 2) = 2`.
- (2,4) "bab": `s[2]=s[4]=b`, inner `dp[3][3] = 1`, so `dp[2][4] = 1 + 2 = 3`.

**Length 4:**
- (0,3) "bbba": `s[0]=b, s[3]=a`, mismatch, `dp[0][3] = max(dp[1][3], dp[0][2]) = max(2, 3) = 3`.
- (1,4) "bbab": `s[1]=b, s[4]=b`, inner `dp[2][3] = 1`, so `dp[1][4] = 1 + 2 = 3`.

**Length 5:**
- (0,4) "bbbab": `s[0]=b, s[4]=b`, inner `dp[1][3] = 2`, so `dp[0][4] = 2 + 2 = 4`.

`dp[0][4] = 4`. ✓ (LPS is "bbbb".)

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | O(n²) | O(n²) |
| **Average** | O(n²) | O(n²) |
| **Worst** | O(n²) | O(n²) |

Standard 2D DP. The LCS-reduction approach has the same
complexity but reuses an existing implementation.

## Variants & optimizations

- **Reconstruct the palindrome** — walk back from
  `dp[0][n-1]`, picking matches greedily. O(n) extra space.
- **Longest Palindromic Substring** (`string_02`) — must be
  contiguous. Use Manacher's algorithm for O(n) time, or
  expand-around-center for O(n²) time and O(1) space.
- **Count distinct palindromic subsequences** — modify the
  DP to count instead of maximize.
- **Minimum insertions to make a palindrome** — same DP,
  answer is `n - dp[0][n-1]`.
- **Minimum deletions to make a palindrome** — same.

## Real-world applications

- **DNA palindromes** — many restriction enzymes recognize
  palindromic DNA sequences. Finding the longest palindromic
  subsequence helps locate these.
- **Music / palindrome poems** — finding the longest
  palindromic pattern in a text.
- **Data compression** — palindromic patterns can be
  referenced with offset + length, reducing size.
- **Code analysis** — finding palindromes in source code
  for refactoring opportunities.
- **Cryptography** — palindromic ciphers and the
  Scytale cipher rely on palindromic patterns.

## Related algorithms in cOde(n)

- **[dp_04 — Longest Common Subsequence](dp_04_lcs.md)** —
  the equivalence `LPS(s) = LCS(s, reverse(s))`. (d=5/10, r=9/10)
- **[string_02 — Longest Palindromic Substring](string_02_longest-palindromic-substring.md)** —
  the contiguous variant. (d=5/10, r=7/10)
- **[dp_14 — Palindromic Partitioning](dp_14_palindromic-partitioning.md)** —
  partitioning the string into palindromes. (d=5/10, r=9/10)
- **[dp_24 — Palindromic Partitioning (Min Cuts)](dp_24_palindromic-partitioning-min-cuts.md)** —
  same, but minimize the number of cuts. (d=6/10, r=9/10)

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-
programming reference sites. For the canonical encyclopedia
entry, follow the Wikipedia link at the top of the page.
Source repository: <https://github.com/dawei7/code_n>.*
