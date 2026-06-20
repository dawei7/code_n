# Rabin-Karp Algorithm

| | |
|---|---|
| **ID** | `string_06` |
| **Category** | strings |
| **Complexity (required)** | $O(N + M)$ Time, $O(1)$ Space |
| **Difficulty** | 7/10 |
| **Interview relevance** | 4/10 |
| **Wikipedia** | [Rabin-Karp algorithm](https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm) |

## Problem statement

Given a `text` string of length N and a `pattern` string of length M.
Find all starting indices where the `pattern` exists as a contiguous substring within the `text`.
You must solve this in average $O(N + M)$ time using string hashing.

**Input:** Two strings `text` and `pattern`.
**Output:** An array of integers representing the starting indices of matches.

## When to use it

- When performing string matching (like KMP), but you specifically need to match MULTIPLE different patterns simultaneously! (KMP requires pre-computing an LPS array for every single pattern. Rabin-Karp just computes a single integer hash for each pattern!).
- To detect plagiarism across massive documents by hashing sequences of words.

## Approach

**1. The Flaw of Naive Matching:**
If `text = "AAAAAAAAAB"` and `pattern = "AAAB"`, the naive approach checks `"AAAB"` against index 0, fails on the last letter, shifts by 1, checks `"AAAB"` against index 1, fails on the last letter... This results in $O(N \times M)$ comparisons! Comparing strings character-by-character is expensive.

**2. The Hashing Insight:**
Comparing integers is lightning fast $O(1)$. What if we convert the `pattern` into an integer (a Hash)?
We also convert the first window of the `text` (length M) into an integer Hash.
If the hashes MATCH, we confidently check the strings character-by-character to ensure it's not a hash collision.
If the hashes DO NOT match, the strings mathematically cannot be identical! We instantly shift the window!

**3. The Rolling Hash (The Magic Trick):**
Wait, if we calculate a new Hash for every single window in the text, hashing a string of length M takes $O(M)$ time. N windows x $O(M)$ hashing = $O(N \times M)$ time! This defeats the entire purpose!
We must use a **Rolling Hash**.
Imagine the string is a base-256 number. `"ABC"` -> A \cdot 256^2 + B \cdot 256^1 + C \cdot 256^0.
If we shift our window from `"ABC"` to `"BCD"`, we don't recalculate from scratch!
We just take the old hash, subtract the value of `"A"` (the letter falling out of the window), multiply the whole thing by 256 to shift everything left, and add `"D"` (the new letter entering the window)!
This takes exactly $O(1)$ constant time!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for string_06: Rabin-Karp.

Rolling-hash substring search.
"""


def solve(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0:
        return 0
    if m > n:
        return -1
    BASE = 256
    MOD = (1 << 61) - 1
    p_hash = 0
    t_hash = 0
    h = 1
    for i in range(m):
        p_hash = (p_hash * BASE + ord(pattern[i])) % MOD
        t_hash = (t_hash * BASE + ord(text[i])) % MOD
        if i < m - 1:
            h = (h * BASE) % MOD
    for i in range(n - m + 1):
        if p_hash == t_hash:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            t_hash = ((t_hash - ord(text[i]) * h) * BASE + ord(text[i + m])) % MOD
            if t_hash < 0:
                t_hash += MOD
    return -1
```

</details>

## Walk-through

`text = "ABABDABACDABABC"`, `pattern = "ABABC"`. M = 5.
`d = 10` (for simpler math walkthrough), `q = 13`.
`h = 10^4 % 13 = 3`.

1. **Initial Hashes:**
   - Hash of `"ABABC"` is computed. `p_hash = 8`.
   - Hash of first window `"ABABD"` is computed. `t_hash = 2`.
2. **Window 0 (`"ABABD"`):**
   - `t_hash (2) != p_hash (8)`. Mismatch!
   - Roll hash: Subtract `"A"`, shift left `* 10`, add `"B"`. New `t_hash` is computed in $O(1)$.
3. **Window 1 (`"BABDA"`):**
   - Hashes don't match. Roll hash.
...
10. **Window 10 (`"ABABC"`):**
    - `t_hash (8) == p_hash (8)`! Hashes match!
    - Enter safety check: compare `"ABABC"` to `"ABABC"` character by character.
    - Perfect match! Append index `10` to results.
11. End of loop. Return `[10]`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N + M)$ | $O(1)$ |
| **Average** | $O(N + M)$ | $O(1)$ |
| **Worst** | $O(N \times M)$ | $O(1)$ |

The initial hash calculation takes $O(M)$ time.
Sliding the window takes $O(N)$ steps. Each step takes $O(1)$ time to roll the hash.
If the hashes match, we do an $O(M)$ verification.
Because our prime modulo q is large, hash collisions are extremely rare. The average time complexity is cleanly $O(N + M)$.
**WORST CASE:** If we have a terrible hash function (or malicious data `text="AAAAAAAAA", pattern="AAAA"`), every single window will produce a hash collision! We will have to run the $O(M)$ string verification at every single step, degrading the algorithm to $O(N \times M)$!
Space complexity is strictly $O(1)$ constant time.

## Variants & optimizations

- **Multiple Pattern Search:** If searching for K different patterns of length M, you compute all K hashes and put them in a Hash Set. As you roll the text hash, you simply check if `t_hash in pattern_hashes_set`! This searches for thousands of patterns simultaneously in the exact same $O(N)$ time!

## Real-world applications

- **Anti-Plagiarism Software:** Turnitin and Moss use Rabin-Karp to break student papers into chunks of 50 characters, hashing them, and comparing them against a massive database of millions of hashes to detect verbatim copying.

## Related algorithms in cOde(n)

- **[string_03 - KMP Pattern Matching](string_03_kmp-string-matching.md)** — The mathematically superior alternative that mathematically guarantees $O(N+M)$ worst-case time by completely avoiding hashing and collisions.
- **[hashing_01 - Two Sum](../hashing/hash_01_two-sum.md)** — The foundational concept of mapping complex data (or expected targets) to integers for $O(1)$ lookups.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
