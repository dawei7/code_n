# Longest Common Subsequence (LCS)

| | |
|---|---|
| **ID** | `dp_04` |
| **Category** | dynamic |
| **Complexity (required)** | $O(n²)$ |
| **Difficulty** | 5/10 |
| **Interview relevance** | 9/10 |
| **Wikipedia** | [Longest common subsequence problem](https://en.wikipedia.org/wiki/Longest_common_subsequence_problem) |

## Problem statement

Given two sequences `s` and `t`, find the length of the
**longest subsequence** common to both. A subsequence keeps
the relative order of elements but doesn't have to be
contiguous.

**Input:** two sequences (typically strings, but works on
arrays of any comparable type).
**Output:** the length of the LCS.

**Example:**

| s | t | LCS | Length |
|---|---|---|---:|
| `"abcde"` | `"ace"` | `"ace"` | 3 |
| `"AGGTAB"` | `"GXTXAYB"` | `"GTAB"` | 4 |
| `"abc"` | `"def"` | `""` | 0 |
| `"abc"` | `"abc"` | `"abc"` | 3 |
| `""` | `"anything"` | `""` | 0 |

## When to use it

- The most-asked **2D string DP** (along with edit distance).
  Recurrence is simpler than edit distance: it's a
  max-and-skip rather than a min-and-three-choices.
- Foundation for **diff tools** (the LCS of two lines is the
  common block), **version control** (`git diff`), **plagiarism
  detection**, and **bioinformatics** (DNA alignment — though
  weighted LCS is the production version).

## Approach

Let `dp[i][j]` = the length of the LCS of the first `i`
characters of `s` and the first `j` characters of `t`.

**Recurrence:** consider the last characters `s[i-1]` and
`t[j-1]`:
- If they match (`s[i-1] == t[j-1]`), extend the LCS by 1:
  `dp[i][j] = 1 + dp[i-1][j-1]`.
- Otherwise, take the better of skipping one of them:
  `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`.

**Base case:** `dp[0][j] = dp[i][0] = 0` (one of the sequences
is empty, so the LCS is empty).

**Answer:** `dp[len(s)][len(t)]`.

**Reconstruction:** to get the actual LCS, walk back from
`dp[m][n]`: if `s[i-1] == t[j-1]`, that's part of the LCS,
go diagonally; otherwise go to the larger of the two
neighbors.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dp_04: Longest Common Subsequence.

DP table: dp[i][j] = LCS length of seq_a[:i] and seq_b[:j]. O(n*m)
time, O(n*m) space.
"""


def solve(seq_a, seq_b):
    m, n = len(seq_a), len(seq_b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq_a[i - 1] == seq_b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]
```

</details>

## Walk-through

`s = "AGGTAB"`, `t = "GXTXAYB"`. Answer: 4 (`"GTAB"`).

```
         ""  G  X  T  X  A  Y  B
   ""  [  0, 0, 0, 0, 0, 0, 0, 0 ]
    A  [  0, 0, 0, 0, 0, 1, 1, 1 ]
    G  [  0, 1, 1, 1, 1, 1, 1, 1 ]
    G  [  0, 1, 1, 1, 1, 1, 1, 1 ]
    T  [  0, 1, 1, 2, 2, 2, 2, 2 ]
    A  [  0, 1, 1, 2, 2, 3, 3, 3 ]
    B  [  0, 1, 1, 2, 2, 3, 3, 4 ]
```

`dp[6][7] = 4`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(m·n)$ | $O(m·n)$ — 2D table; $O(min(m,n)$) with rolling |
| **Average** | $O(m·n)$ | $O(m·n)$ |
| **Worst** | $O(m·n)$ | $O(m·n)$ |

Standard DP. The rolling-row version (keep only the previous
row) drops space to $O(n)$, but loses the ability to reconstruct
the LCS without re-running.

## Variants & optimizations

- **Hunt-Szymanski algorithm** — $O((r + n)$ log n) where `r` is
  the number of matching pairs. Faster when the sequences are
  very similar (most characters match).
- **Bit-parallel LCS** — $O(n · ⌈m/w⌉)$ where w is the word size.
  Excellent for short s and long t.
- **Diff with line-level granularity** — git, diff, and
  similar tools work on lines, not characters, and use a
  similar DP (the "patience diff" variant is even faster in
  practice).
- **Multiple LCS** — there can be many LCSs of the same
  length. To count them: `count[i][j] = 0` if `s[i-1] != t[j-1]`,
  else `count[i][j] = count[i-1][j-1] + count[i-1][j] + count[i][j-1] - count[i-1][j-1]` (with care to avoid double-counting).

## Real-world applications

- **Version control** — `git diff` and `git merge` find LCS to
  identify unchanged regions.
- **Bioinformatics** — DNA and protein sequence alignment
  (the weighted version).
- **Plagiarism detection** — high LCS between two essays is
  suspicious.
- **Screen diff tools** — the Vim `diff` command uses an
  LCS-based algorithm.
- **fuzzy string matching** — high LCS ratio is one signal of
  similarity.

## Related algorithms in cOde(n)

- **[dp_08 — Edit Distance](dp_08_edit-distance.md)** —
  minimization version of the same 2D-table structure.
  (d=5/10, r=9/10)
- **[dp_20 — Shortest Common Supersequence (Length)](dp_20_shortest-common-supersequence.md)** —
  build the SCS using the LCS table. (d=5/10, r=9/10)
- **[dp_19 — Longest Palindromic Subsequence](dp_19_longest-palindromic-subsequence.md)** —
  LCS of a string with its reverse. (d=5/10, r=9/10)

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-
programming reference sites. For the canonical encyclopedia
entry, follow the Wikipedia link at the top of the page.
Source repository: <https://github.com/dawei7/code_n>.*
