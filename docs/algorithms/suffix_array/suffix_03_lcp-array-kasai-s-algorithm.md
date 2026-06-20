# LCP Array (Kasai's Algorithm)

| | |
|---|---|
| **ID** | `suffix_03` |
| **Category** | suffix_array |
| **Complexity (required)** | $O(N)$ Time, $O(N)$ Space |
| **Difficulty** | 8/10 |
| **Interview relevance** | 3/10 |
| **GeeksForGeeks Equivalent** | [Kasai’s Algorithm for Construction of LCP array from Suffix Array](https://www.geeksforgeeks.org/%C2%AD%C2%ADkasais-algorithm-for-construction-of-lcp-array-from-suffix-array/) |

## Problem statement

Given a string `s` of length N and its pre-computed Suffix Array `suffix_arr`, construct its **Longest Common Prefix (LCP) Array**.
The LCP Array is an array of size N where `lcp[i]` stores the length of the longest common prefix between the i-th suffix and the (i-1)-th suffix in the sorted Suffix Array.
You must generate this array in mathematically guaranteed $O(N)$ linear time.

**Input:** A string `s` and an integer array `suffix_arr`.
**Output:** An integer array `lcp`.

## When to use it

- A Suffix Array alone is just a sorted list. It is the combination of the Suffix Array **AND** the LCP Array that allows you to magically solve some of the hardest string problems in computer science (Longest Repeated Substring, Count Distinct Substrings) in $O(N)$ time!

## Approach

**1. The Naive $O(N^2)$ Comparison:**
If we iterate through the Suffix Array and compare `suffix_arr[i]` with `suffix_arr[i-1]` character by character, it takes $O(N)$ time per comparison. Over N elements, that's $O(N^2)$. This is too slow.

**2. Kasai's Magical Insight:**
Instead of computing the LCP array in the sorted order of the Suffix Array, what if we compute it in the **original order** of the string?
Let's find the LCP of the longest suffix first (`s[0...]`), then the second longest (`s[1...]`), then `s[2...]`.

Suppose the suffix `s[i...]` is at position `rank` in the Suffix Array. Its neighbor above it is `rank - 1`. Let's say their LCP is K.
For example, the neighbor is `"banana"` and our suffix is `"banjo"`. K = 3 (`"ban"`).
Now, let's move to the next suffix in the original string: `s[i+1...]`. This physically chops off the first character!
Our new suffix is `"anjo"`. The neighbor mathematically shrinks to `"anana"`.
Because the first character was chopped off BOTH strings, the remaining matching prefix MUST be exactly K - 1! (e.g., `"an"`).
Therefore, we ALREADY KNOW the LCP of our new suffix with its neighbor is **at least** K - 1!
We do not need to compare the first K - 1 characters! We just resume our character comparison starting from index K - 1!

**3. The Rank Array:**
To process suffixes in their original string order, but easily find their "neighbors" in the sorted Suffix Array, we need a reverse lookup map. We build an $O(N)$ `rank` array where `rank[i]` tells us the sorted index of the suffix starting at string index `i`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for suffix_03: LCP Array (Kasai's Algorithm).

Given a string s, return its suffix array sa and
"""


def solve(s, n):
    """Return (suffix_array, lcp_array) of s.

    Build the suffix array naively (sort suffixes), then run
    Kasai's algorithm to build the LCP array in O(n).
    """
    if n == 0:
        return [], []
    # Build the suffix array naively.
    sa = sorted(range(n), key=lambda i: s[i:])
    # Inverse SA: rank[i] = position of suffix i in sa.
    rank = [0] * n
    for i, idx in enumerate(sa):
        rank[idx] = i
    # Kasai's algorithm.
    lcp = [0] * n
    h = 0
    for i in range(n):
        if rank[i] > 0:
            # j is the previous suffix in the suffix array.
            j = sa[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[rank[i]] = h
            if h > 0:
                h -= 1
        # If rank[i] == 0 (it's the smallest suffix), lcp[0] = 0
        # (already initialized).
    return sa, lcp
```

</details>

## Walk-through

`s = "banana"`, `suffix_arr = [5, 3, 1, 0, 4, 2]`.
*Sorted Suffixes:*
`0: "a" (idx 5)`
`1: "ana" (idx 3)`
`2: "anana" (idx 1)`
`3: "banana" (idx 0)`
`4: "na" (idx 4)`
`5: "nana" (idx 2)`

1. **Build `rank` array:**
   `rank[5]=0, rank[3]=1, rank[1]=2, rank[0]=3, rank[4]=4, rank[2]=5`.
2. **`i = 0` (suffix `"banana"`):**
   - `rank[0] = 3`. Neighbor is `rank 2` (suffix `"anana"` at `idx 1`).
   - Compare `"banana"` with `"anana"`. `b != a`. `k = 0`.
   - `lcp[3] = 0`.
3. **`i = 1` (suffix `"anana"`):**
   - `rank[1] = 2`. Neighbor is `rank 1` (suffix `"ana"` at `idx 3`).
   - Compare `"anana"` with `"ana"`. Match 3 chars! `k = 3`.
   - `lcp[2] = 3`.
   - **Kasai Shrink:** Next step, `k` becomes 3 - 1 = 2. We are guaranteed to skip 2 comparisons!
4. **`i = 2` (suffix `"nana"`):**
   - `rank[2] = 5`. Neighbor is `rank 4` (suffix `"na"` at `idx 4`).
   - We instantly skip the first `k=2` chars!
   - We only check `s[2 + 2]` with `s[4 + 2]`. `s[4]` is `'n'`, `s[6]` is out of bounds. Mismatch!
   - `k = 2`. `lcp[5] = 2`.
   - **Kasai Shrink:** Next step, `k` becomes 2 - 1 = 1.

LCP Array is completely built in linear time: `[0, 1, 3, 0, 0, 2]`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(N)$ |
| **Average** | $O(N)$ | $O(N)$ |
| **Worst** | $O(N)$ | $O(N)$ |

Building the Rank Array takes $O(N)$ time.
In the main loop, we execute a `while` loop that increments `k`.
Although `k` can theoretically be incremented up to N times, notice that `k` is only ever decremented by exactly 1 at the end of each iteration.
Since `k` can never exceed N, and it is decreased at most N times, the total number of times `k` is incremented across the ENTIRE algorithm is mathematically bounded to 2N.
Therefore, the inner `while` loop executes at most 2N times globally. Total time complexity is strictly $O(N)$.
Space complexity is $O(N)$ to hold the `rank` array and the `lcp` array.

## Variants & optimizations

- **Direct Computation in Suffix Array Generation:** Highly advanced, state-of-the-art Suffix Array generation algorithms (like DC3) can actually compute the LCP Array directly during the sorting process, avoiding the need for a separate Kasai pass.

## Real-world applications

- **Bioinformatics / Shortest Unique Substring:** Finding the shortest DNA sequence that uniquely identifies a specific virus strain by finding the minimum length substring that has an LCP of 0 with its sorted neighbors.

## Related algorithms in cOde(n)

- **[suffix_05 - Longest Repeated Substring](suffix_05_longest-repeated-substring.md)** — A complex problem completely trivialized by the LCP array (it's simply the maximum value in the LCP array!).
- **[suffix_04 - Count Distinct Substrings](suffix_04_count-distinct-substrings.md)** — Another problem trivialized by the LCP array (N(N+1)/2 - \sum LCP[i]).

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
