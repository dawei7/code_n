# Z Algorithm Pattern Search

| | |
|---|---|
| **ID** | `string_13` |
| **Category** | strings |
| **Complexity (required)** | $O(N + M)$ Time, $O(N + M)$ Space |
| **Difficulty** | 7/10 |
| **Interview relevance** | 2/10 |
| **GeeksForGeeks Equivalent** | [Z algorithm (Linear time pattern searching Algorithm)](https://www.geeksforgeeks.org/z-algorithm-linear-time-pattern-searching-algorithm/) |

## Problem statement

Given a `text` string of length N and a `pattern` string of length M.
Find all starting indices where the `pattern` exists as a contiguous substring within the `text`.
You must solve this in mathematically guaranteed $O(N + M)$ time using the Z-Algorithm.

**Input:** Two strings `text` and `pattern`.
**Output:** An array of integers representing the starting indices of matches.

## When to use it

- When performing pattern matching and you want the easiest mathematically guaranteed $O(N+M)$ algorithm to implement from scratch (compared to the nightmare of implementing KMP's LPS array).

## Approach

**1. The Magic Concatenation:**
The Z-Algorithm computes an array where `Z[i]` is the length of the longest substring starting at `S[i]` that perfectly matches the prefix of `S`.
If our goal is to find `pattern` inside `text`, what if we violently force the `pattern` to BE the prefix of `S`?
We create a new concatenated string: `S = pattern + "" + text`.
(The `""` is a special sentinel character that MUST NOT exist anywhere in the pattern or text).

**2. The Sentinel Wall:**
Why the `""`?
If we didn't have it, a match in the text might accidentally "spill over" and match parts of the text *past* the pattern. By placing `""` exactly after the pattern, we guarantee that the maximum possible Z-value anywhere in the string is exactly M (the length of the pattern). The `""` physically blocks the match from ever going further.

**3. Executing the Search:**
1. Concatenate `S = pattern + "" + text`.
2. Run the standard $O(K)$ Z-Algorithm on `S` (where K = N + M + 1).
3. Iterate through the resulting Z-Array. If you find an index `i` where `Z[i] == M` (the length of the pattern), it means you found a perfect match!
4. Calculate the original index in the `text`: `text_index = i - M - 1`. Add it to your results!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for string_13: Z-Algorithm (Pattern Search).

Build the Z-array of pattern + '$' + s, then collect
positions where Z[i] == |pattern| in the s region.
"""


def solve(s, n, pattern, m):
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
```

</details>

## Walk-through

`text = "aabzaa"`, `pattern = "aa"`. M = 2.
`S = "aaaabzaa"`.

1. Run Z-Algorithm on `S`:
   - `Z[0] = 9` (Length of entire string).
   - `Z[1] = 1` (`"aaabzaa"` matches `"a"`).
   - `Z[2] = 0` (`"aabzaa"` matches nothing).
   - `Z[3] = 2` (`"aabzaa"` matches `"aa"` perfectly! Blocked by `b` vs ``).
   - `Z[4] = 1` (`"abzaa"` matches `"a"`).
   - `Z[5] = 0` (`"bzaa"` matches nothing).
   - `Z[6] = 0` (`"zaa"` matches nothing).
   - `Z[7] = 2` (`"aa"` matches `"aa"` perfectly!).
   - `Z[8] = 1` (`"a"` matches `"a"`).
   Z-Array: `[9, 1, 0, 2, 1, 0, 0, 2, 1]`.
2. Scan Z-Array from index M+1 = 3:
   - `Z[3] == 2` (M). Match! Original index = 3 - 2 - 1 = 0. `matches = [0]`.
   - `Z[4] == 1`.
   - `Z[5] == 0`.
   - `Z[6] == 0`.
   - `Z[7] == 2` (M). Match! Original index = 7 - 2 - 1 = 4. `matches = [0, 4]`.
   - `Z[8] == 1`.
3. Return `[0, 4]`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N + M)$ | $O(N + M)$ |
| **Average** | $O(N + M)$ | $O(N + M)$ |
| **Worst** | $O(N + M)$ | $O(N + M)$ |

Building the concatenated string takes $O(N + M)$ time.
Running the Z-Algorithm takes strictly linear time proportional to the length of the string: $O(N + M)$.
Scanning the resulting array takes $O(N)$ time.
Total time complexity is mathematically guaranteed $O(N + M)$ regardless of malicious inputs, unlike Rabin-Karp.
Space complexity is $O(N + M)$ to hold the physically concatenated string and the resulting Z-Array. (KMP is slightly better because its auxiliary array is only size M).

## Variants & optimizations

- **Rolling Z-Box ($O(M)$ Space):** You don't actually need to physically concatenate the string and build a massive Z-Array of size N+M. You can compute the Z-Array for the pattern `Z_pat` first. Then, you conceptually slide the Z-box across the `text`, looking up values from `Z_pat` when inside the box, and doing manual comparisons when outside. This drops the space complexity to strictly $O(M)$!

## Real-world applications

- **DNA Subsequence Matching:** Finding all occurrences of a specific genome sequence (the pattern) within a massive chromosome file (the text).

## Related algorithms in cOde(n)

- **[string_07 - Z Algorithm](string_07_z-algorithm.md)** — The engine that powers this search algorithm.
- **[string_03 - KMP Pattern Matching](string_03_kmp-string-matching.md)** — The other O(N+M)$ search algorithm that relies on the "Longest Proper Prefix which is also Suffix" array instead of direct matching.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
