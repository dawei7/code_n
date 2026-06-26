# KMP String Matching

| | |
|---|---|
| **ID** | `string_03` |
| **Category** | strings |
| **Complexity (required)** | $O(N + M)$ |
| **Difficulty** | 8/10 |
| **Interview relevance** | 7/10 |
| **Wikipedia** | [Knuth-Morris-Pratt algorithm](https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm) |

## Problem statement

Given two strings: a `text` of length `N` and a `pattern` of length `M`.
Find all starting indices in `text` where `pattern` exists as a contiguous substring.

**Input:** Two strings `text` and `pattern`.
**Output:** A list of integers representing the starting indices of matches.

**Example:**
`text = "ABABDABACDABABCABAB"`, `pattern = "ABABCABAB"`
Output: `[10]`.

## When to use it

- When performing string searching where $O(N \times M)$ naive time is too slow, and you need guaranteed linear $O(N + M)$ time.
- It is the canonical solution for the string matching problem.

## Approach

In naive search (`string_04`), if we mismatch at character 5, we shift the pattern right by just 1 space and start the comparison all over again from the beginning.
The **Knuth-Morris-Pratt (KMP)** algorithm realizes that *we already know* what the previous 4 characters were! We shouldn't throw that information away.

KMP uses an auxiliary array called the **LPS (Longest Proper Prefix which is also Suffix)** array.
For the pattern `"ABABCABAB"`, the LPS array tells us: "If a mismatch occurs at index `i`, what is the length of the longest prefix of the pattern that correctly matches the suffix of the chunk we just evaluated?"
This tells us exactly how far back we need to backtrack our pattern pointer `j`, without ever moving our text pointer `i` backwards!

**Step 1: Compute the LPS array for the `pattern` in $O(M)$ time.**
For each index, track the length of the longest proper prefix that matches the suffix ending at that index.

**Step 2: Search the `text` in $O(N)$ time.**
Use two pointers: `i` for `text`, `j` for `pattern`.
- If `text[i] == pattern[j]`, increment both.
- If `j == M`, we found a match! Record the starting index. Set `j = lps[j-1]` to continue searching for overlapping matches.
- If `text[i] != pattern[j]`:
  - If `j > 0`, we don't start over! We backtrack `j` to `lps[j-1]`.
  - If `j == 0`, we simply increment `i` (we are at the start of the pattern and no prefix matched).

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for string_03: KMP String Matching.

Knuth-Morris-Pratt: build a failure function over the pattern,
then scan the text without ever restarting.
"""


def solve(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0:
        return 0
    if m > n:
        return -1

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
            return i - m + 1
    return -1
```

</details>

## Walk-through

Let's build the LPS for `pattern = "AAAC"`. `M = 4`.
- `lps[0] = 0`.
- `i=1` ('A'): `pat[1] == pat[0]`. `length = 1`. `lps[1] = 1`.
- `i=2` ('A'): `pat[2] == pat[1]`. `length = 2`. `lps[2] = 2`.
- `i=3` ('C'): `pat[3] != pat[2]`. Backtrack: `length = lps[1] = 1`.
- `i=3` ('C'): `pat[3] != pat[1]`. Backtrack: `length = lps[0] = 0`.
- `i=3` ('C'): `pat[3] != pat[0]`. Length is 0. `lps[3] = 0`. `i += 1`.
LPS = `[0, 1, 2, 0]`.

`text = "AAAAC"`. `i=0, j=0`.
- `i=0,1,2`: Match 'A', 'A', 'A'. `j=3`.
- `i=3`: `text[3]` ('A') != `pat[3]` ('C'). Mismatch!
  - `j` backtracks to `lps[j-1] = lps[2] = 2`.
  - Notice `i` is STILL 3. We didn't backtrack the text!
- `i=3`: `text[3]` ('A') == `pat[2]` ('A'). Match! `i=4, j=3`.
- `i=4`: `text[4]` ('C') == `pat[3]` ('C'). Match! `i=5, j=4`.
- `j == 4`. Match found at index `i - j = 5 - 4 = 1`.

Output: `[1]`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N + M)$ | $O(M)$ |
| **Average** | $O(N + M)$ | $O(M)$ |
| **Worst** | $O(N + M)$ | $O(M)$ |

Computing the LPS array takes $O(M)$ time.
The search loop iterates through the text array of size N. Although the inner `if/else` can backtrack `j` in a `while`-like manner, `i` never decreases, and `j` is bounded by `i`. Amortized analysis proves the search loop executes at most 2N operations. Thus, time complexity is strictly $O(N + M)$.
Space complexity is $O(M)$ to store the LPS array.

## Variants & optimizations

- **Aho-Corasick Algorithm:** If you need to search for *multiple* patterns simultaneously (e.g., a dictionary of bad words) against a single text, running KMP K times takes $O(K \cdot (N+M)$). Aho-Corasick builds an automaton (Trie with LPS-like failure links) to search for ALL patterns simultaneously in $O(N + M + \text{Matches})$ time!

## Real-world applications

- **Text Editors:** The `Ctrl+F` or "Find" functionality in IDEs and text editors relies heavily on KMP or similar linear-time string searching algorithms to prevent freezing on massive log files.

## Related algorithms in cOde(n)

- **[string_04 - Naive Pattern Search](string_04_naive-pattern-search.md)** — The brute force $O(N \times M)$ approach.
- **[string_06 - Rabin-Karp](string_06_rabin-karp.md)** — An alternative $O(N+M)$ search using rolling hashes instead of an LPS array.
- **[string_07 - Z-Algorithm](string_07_z-algorithm.md)** — Another linear time pattern matching algorithm using a different prefix array concept.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
