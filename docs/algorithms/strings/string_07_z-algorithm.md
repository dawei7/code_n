# Z Algorithm

| | |
|---|---|
| **ID** | `string_07` |
| **Category** | strings |
| **Complexity (required)** | $O(N)$ Time, $O(N)$ Space |
| **Difficulty** | 8/10 |
| **Interview relevance** | 2/10 |
| **GeeksForGeeks Equivalent** | [Z algorithm (Linear time pattern searching Algorithm)](https://www.geeksforgeeks.org/z-algorithm-linear-time-pattern-searching-algorithm/) |

## Problem statement

Given a string `S` of length N.
Construct the Z-Array.
The Z-array is an array of length N where the i-th element stores the length of the longest substring starting from `S[i]` which is also a prefix of the string `S`.
You must build this array in linear $O(N)$ time.

**Input:** A string `S`.
**Output:** An integer array representing the Z-Array.

## When to use it

- To perform String Matching in $O(N+M)$ time.
- The conceptually simpler alternative to the dreaded KMP Algorithm. While KMP tracks the "longest proper prefix that is also a suffix", the Z-Algorithm just directly measures "how much of the prefix matches starting right here?".

## Approach

**1. The Z-Array Definition:**
For string `S = "aabzaa"`.
- `Z[0] = 6` (The prefix matches itself completely).
- `Z[1] = 1` (`"abzaa"` matches `"a"`).
- `Z[2] = 0` (`"bzaa"` doesn't match `"a"`).
- `Z[3] = 0` (`"zaa"` doesn't match `"a"`).
- `Z[4] = 2` (`"aa"` perfectly matches the prefix `"aa"`).
- `Z[5] = 1` (`"a"` matches `"a"`).

**2. The Z-Box (The Sliding Window of Known Matches):**
If we compute the array naively (comparing character by character starting at every index i), it takes $O(N^2)$ time.
To get $O(N)$, we must avoid redundant comparisons.
We maintain a "Z-Box" defined by a Left bound `L` and a Right bound `R`. This box represents the right-most substring we've found so far that perfectly matches the prefix.
Inside this box, `S[L...R]` perfectly matches `S[0...(R-L)]`.

**3. The Three Cases:**
As we iterate i from 1 to N-1:
- **Case 1 (Outside the Box):** `i > R`. We are in unknown territory! We have no cached information. We manually compare `S[i]` with `S[0]`, `S[i+1]` with `S[1]`, etc., until a mismatch occurs. We then update our box: `L = i` and `R = i + matches - 1`.
- **Case 2 (Inside the Box, Safe):** `i <= R`. Because `S[L...R]` perfectly matches the prefix, the characters starting at `i` are identical to the characters starting at index `k = i - L`. We can just look up `Z[k]`!
  If `Z[k]` is strictly less than the remaining space in our box (`R - i + 1`), then we KNOW the match will end before escaping the box! We instantly set `Z[i] = Z[k]` in $O(1)$ time! No comparisons needed!
- **Case 3 (Inside the Box, Touching the Edge):** `i <= R`, but `Z[k] >= R - i + 1`. Our cached value says the match goes exactly up to the edge of our known box (or beyond). We can safely set `Z[i] = R - i + 1` to skip all the comparisons inside the box! But we must manually check the characters *outside* the box to see how much further the match actually goes. After checking, we update `L` and `R`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for string_07: Z-Algorithm.

Linear-time pattern matching.
"""


def solve(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0:
        return 0
    if m > n:
        return -1
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
    offset = m + 1
    for i in range(offset, len(s)):
        if z[i] == m:
            return i - offset
    return -1
```

</details>

## Walk-through

`S = "aabcaabxaaaz"`.

1. `i = 1`: `S[1] = 'a'`. Outside box. Compare `S[1]` to `S[0]` ('a' == 'a'). `S[2] != S[1]`.
   - `Z[1] = 1`. Box is `L=1, R=1`.
2. `i = 2`: `S[2] = 'b'`. Outside box (`i > R`). Mismatch immediately.
   - `Z[2] = 0`. Box unchanged.
3. `i = 3`: `S[3] = 'c'`. Mismatch immediately. `Z[3] = 0`.
4. `i = 4`: `S[4] = 'a'`. Outside box. Compare `S[4]` to `S[0]` ('a'=='a'), `S[5]` to `S[1]` ('a'=='a'), `S[6]` to `S[2]` ('b'=='b'), `S[7]` to `S[3]` ('x'!='c').
   - `Z[4] = 3`. Box is now `L=4, R=6` (`"aab"`).
5. `i = 5`: `S[5] = 'a'`. Inside box (`5 <= 6`)!
   - Corresponding index k = 5 - 4 = 1.
   - `Z[1]` is `1`.
   - Remaining space in box is R - i + 1 = 6 - 5 + 1 = 2.
   - `1 < 2`! (Case 2: Safe!).
   - Instantly set `Z[5] = 1`. No comparisons! ✓
6. `i = 6`: `S[6] = 'b'`. Inside box!
   - k = 6 - 4 = 2.
   - `Z[2]` is `0`.
   - `0 < 1`. (Case 2: Safe!).
   - Instantly set `Z[6] = 0`. ✓
7. `i = 7`: `S[7] = 'x'`. Outside box...

Final Array: `[0, 1, 0, 0, 3, 1, 0, 0, 2, 1, 1, 0]`.

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(N)$ |
| **Average** | $O(N)$ | $O(N)$ |
| **Worst** | $O(N)$ | $O(N)$ |

Although there is a `while` loop inside the `for` loop, look closely at what the `while` loop does: it ONLY increments `right` when a successful character match is found.
Once `right` is incremented, it NEVER goes backwards! It can only traverse the string from `0` to `N`.
Therefore, across the entire outer `for` loop, the inner `while` loop executes a maximum total of N times.
Time complexity is strictly $O(N)$.
Space complexity is $O(N)$ to hold the integer Z-Array.

## Variants & optimizations

- **String Matching (`string_13`):** To use this for pattern matching (like searching for `"dog"` in `"the dog ran"`), you simply concatenate them with a special separator character: `"dogthe dog ran"`. You compute the Z-Array. Any index where `Z[i] == len("dog")` is a perfect pattern match in the text!

## Real-world applications

- **Bioinformatics:** Rapidly mapping massive DNA short-reads to a reference genome sequence. The Z-algorithm's logic is fundamentally easier to parallelize on GPUs than KMP.

## Related algorithms in cOde(n)

- **[string_03 - KMP Pattern Matching](string_03_kmp-string-matching.md)** — The famous, but slightly harder to understand, alternative $O(N)$ string matching algorithm.
- **[string_02 - Longest Palindromic Substring](string_02_longest-palindromic-substring.md)** — Manacher's Algorithm for palindromes uses the exact same "Sliding Box" caching logic (Cases 1, 2, and 3) to achieve O(N)$ time!

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
