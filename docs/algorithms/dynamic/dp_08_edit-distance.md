# Edit Distance (Levenshtein)

| | |
|---|---|
| **ID** | `dp_08` |
| **Category** | dynamic |
| **Complexity (required)** | O(n²) |
| **Difficulty** | 5/10 |
| **Interview relevance** | 9/10 |
| **Wikipedia** | [Edit distance](https://en.wikipedia.org/wiki/Edit_distance) |

## Problem statement

Given two strings `s` and `t`, find the minimum number of
**single-character edits** (insertions, deletions, or
substitutions) needed to transform `s` into `t`. This is the
**Levenshtein distance**.

**Input:** two strings `s`, `t`.
**Output:** the minimum edit count.

**Example:**

| s | t | Distance | One transformation |
|---|---|---:|---|
| "" | "abc" | 3 | insert × 3 |
| "abc" | "abc" | 0 | (identical) |
| "kitten" | "sitting" | 3 | k→s, e→i, +g |
| "sunday" | "saturday" | 3 | +a, +t, n→r |
| "intention" | "execution" | 5 | i→e, n→x, e→c, +u, n→n (wait, 5) |

## When to use it

- The canonical **2D-string DP** problem and one of the most
  asked at FAANG-tier interviews. The recurrence is small
  (three operations) but the state space (s-prefix × t-prefix)
  is 2D and easy to fumble.
- Foundation for **spell-checkers**, **fuzzy search**,
  **DNA-sequence alignment** (with a weighted version of
  the same recurrence), and **autocorrect** in text editors.

## Approach

Let `dp[i][j]` = the edit distance between the first `i`
characters of `s` and the first `j` characters of `t`.

**Recurrence:** consider the last characters `s[i-1]` and
`t[j-1]`:
- If they match, `dp[i][j] = dp[i-1][j-1]`. No edit needed.
- Otherwise, take the **minimum** of three operations:
  - **Substitute** `s[i-1]` with `t[j-1]`: `1 + dp[i-1][j-1]`
  - **Delete** `s[i-1]`: `1 + dp[i-1][j]`
  - **Insert** `t[j-1]`: `1 + dp[i][j-1]`

**Base case:** `dp[0][j] = j` (insert j chars) and
`dp[i][0] = i` (delete i chars). The empty string is `j`
insertions away from any string of length `j`.

**Answer:** `dp[len(s)][len(t)]`.

**Space optimization:** the recurrence only uses the previous
row and the current row, so 2D → 2×(n+1) → with a small tweak
even 1×(n+1) (use a `prev_row` variable). cOde(n)'s engine
expects O(n²) time and accepts either 2D or optimized memory.

## Algorithm (pseudocode)

```
edit_distance(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i from 0 to m: dp[i][0] = i
    for j from 0 to n: dp[0][j] = j
    for i from 1 to m:
        for j from 1 to n:
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j-1],   # substitute
                    dp[i-1][j],     # delete
                    dp[i][j-1],     # insert
                )
    return dp[m][n]
```

## Walk-through

`s = "cat"`, `t = "cars"`. Answer: 1 (insert `s`).

```
        ""   c   a   r   s
  ""  [  0,  1,  2,  3,  4 ]
   c  [  1,  0,  1,  2,  3 ]
   a  [  2,  1,  0,  1,  2 ]
   t  [  3,  2,  1,  1,  1 ]
```

Walk through filling `dp[1][1]` = edit("c", "c"):
`s[0] = t[0] = "c"`, so `dp[1][1] = dp[0][0] = 0`.

`dp[1][2]` = edit("c", "ca"): `c ≠ a`. Candidates:
- Substitute: `1 + dp[0][1] = 1 + 1 = 2`
- Delete `c`: `1 + dp[0][2] = 1 + 2 = 3`
- Insert `a`: `1 + dp[1][1] = 1 + 0 = 1`
- `dp[1][2] = 1`.

`dp[3][4]` = edit("cat", "cars") = 1. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | O(m·n) | O(min(m, n)) with rolling |
| **Average** | O(m·n) | O(min(m, n)) with rolling |
| **Worst** | O(m·n) | O(min(m, n)) with rolling |

For the 2D table, space is O(m·n). The rolling-row version
reduces to O(n) (or O(min(m, n)) whichever is smaller).

## Variants & optimizations

- **Damerau-Levenshtein** — also count transpositions of
  adjacent characters as 1 edit. Useful for spell-check
  (where "teh" ↔ "the" is 1 transposition, not 2 substitutions).
- **Weighted edit distance** — different costs for each
  operation. DNA alignment uses this (substitution matrix
  BLOSUM / PAM).
- **Hirschberg's algorithm** — O(m·n) time, O(min(m, n))
  space, AND reconstructs the actual sequence of edits. Uses
  divide-and-conquer + the rolling-row trick.
- **Myers' bit-parallel algorithm** — O((m·n)/w) where w is
  the word size, with w=64 effectively O(m·n/64). The
  standard for production diff tools.

## Real-world applications

- **Spell-checkers and autocorrect** — suggestions are the
  words in the dictionary with the lowest edit distance to
  the user's input.
- **Plagiarism detection** — high edit distance between two
  documents suggests they were independently produced.
- **DNA sequence alignment** — the weighted version, with
  substitution matrices tuned for evolution.
- **fzf, ripgrep, ag** — fuzzy finders use edit distance (or
  related measures) to rank matches.
- **git diff** — at its core, the edit distance problem.

## Related algorithms in cOde(n)

- **[dp_04 — Longest Common Subsequence](dp_04_longest-common-subsequence.md)** —
  related 2D string DP, but maximization instead of
  minimization. (d=5/10, r=9/10)
- **[dp_20 — Shortest Common Supersequence (Length)](dp_20_shortest-common-supersequence.md)** —
  builds directly on the LCS table. (d=5/10, r=9/10)
- **[dp_14 — Palindromic Partitioning](dp_14_palindromic-partitioning.md)** —
  another 2D string DP. (d=5/10, r=9/10)

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-
programming reference sites. For the canonical encyclopedia
entry, follow the Wikipedia link at the top of the page.
Source repository: <https://github.com/dawei7/code_n>.*
