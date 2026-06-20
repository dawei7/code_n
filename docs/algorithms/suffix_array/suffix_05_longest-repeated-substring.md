# Longest Repeated Substring

| | |
|---|---|
| **ID** | `suffix_05` |
| **Category** | suffix_array |
| **Complexity (required)** | $O(N \log N)$ Time, $O(N)$ Space |
| **Difficulty** | 4/10 |
| **Interview relevance** | 5/10 |
| **GeeksForGeeks Equivalent** | [Longest Repeating Substring](https://www.geeksforgeeks.org/longest-repeating-substring-using-suffix-automaton/) |

## Problem statement

Given a string `s`, find the longest substring that appears at least twice in the string.
The two occurrences may overlap.
If no such substring exists, return `""`.

**Input:** A string `s`.
**Output:** A string representing the longest repeated substring.

## When to use it

- To find the largest recurring block of data in a file.
- The most satisfying, absolute simplest problem to solve once the LCP Array is built.

## Approach

**1. The "Adjacent Sorting" Insight:**
If you have a massive list of completely random words, and you want to find the two words that share the longest matching prefix, doing this naively requires checking every word against every other word ($O(N^2)$).
But if you sort the list alphabetically, words with matching prefixes are mathematically forced to sit directly next to each other!
To find the longest common prefix among the entire dataset, you only ever need to compare adjacent neighbors!

**2. The LCP Array Solution:**
A Suffix Array is literally a sorted list of every possible suffix (substring) of the text.
Therefore, the two suffixes in the text that share the longest prefix MUST be sitting right next to each other in the Suffix Array.
What data structure stores the length of the matching prefix between adjacent elements in the Suffix Array? The **LCP Array**!
Therefore, the Longest Repeated Substring in the entire text is simply the **MAXIMUM VALUE** inside the LCP Array!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for suffix_05: Longest Repeated Substring.

Find the length of the longest substring of s
"""


def solve(s, n):
    """Length of the longest repeated substring."""
    if n == 0:
        return 0
    # Build the suffix array naively.
    sa = sorted(range(n), key=lambda i: s[i:])
    # Build the LCP array.
    rank = [0] * n
    for i, idx in enumerate(sa):
        rank[idx] = i
    lcp = [0] * n
    h = 0
    for i in range(n):
        if rank[i] > 0:
            j = sa[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[rank[i]] = h
            if h > 0:
                h -= 1
    # Return the max LCP (lcp[0] is 0, so the max is over i >= 1).
    return max(lcp)
```

</details>

## Walk-through

`s = "banana"`, N = 6.

1. Build Suffix Array: `[5, 3, 1, 0, 4, 2]`
   - `0: "a"`
   - `1: "ana"`
   - `2: "anana"`
   - `3: "banana"`
   - `4: "na"`
   - `5: "nana"`
2. Build LCP Array: `[0, 1, 3, 0, 0, 2]`.
   - The value at index 2 is `3` (comparing `"anana"` with `"ana"`).
   - The value at index 5 is `2` (comparing `"nana"` with `"na"`).
3. Scan LCP Array for maximum value.
   - Max value is `3` at `lcp_arr[2]`.
   - `max_len = 3`.
   - The suffix that generated this is `suffix_arr[2]`, which is index `1` in the original string!
4. Return substring from index 1 with length 3: `s[1 : 1+3]`.

Output: `"ana"`. ✓ (It appears twice: b**ana**na and ban**ana**).

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N \log N)$ | $O(N)$ |
| **Average** | $O(N \log N)$ | $O(N)$ |
| **Worst** | $O(N \log N)$ | $O(N)$ |

Building the Suffix Array takes $O(N \log N)$.
Building the LCP Array takes $O(N)$.
Finding the maximum value in the LCP array takes $O(N)$.
Time complexity is bounded by the sorting of the Suffix Array: $O(N \log N)$.
Space complexity is $O(N)$ for the arrays.

## Variants & optimizations

- **Dynamic Programming ($O(N^2)$):** If you don't know the Suffix Array algorithm, you can solve this in $O(N^2)$ time using the exact same 2D DP matrix as Longest Common Substring (`string_05`), but passing `s` and `s` as both arguments, and restricting it with `i != j`!
- **Rabin-Karp Binary Search ($O(N \log N)$ Time, $O(1)$ Space):** A stunningly clever alternative! You Binary Search the *length* of the answer! You guess the answer is length K = N/2. You use a Rolling Hash to hash every window of length K. If you see a duplicate hash, it means a repeated substring of length K exists! You update your Binary Search to try a larger K. If no duplicate hashes exist, you try a smaller K. It requires no Suffix Array and takes almost no space!

## Real-world applications

- **Lossless Audio Compression (FLAC):** Finding massive, exact repeating waveforms (like a consistent drum beat) across an audio file to encode them a single time.

## Related algorithms in cOde(n)

- **[suffix_03 - LCP Array](suffix_03_lcp-array-kasai-s-algorithm.md)** — The engine that makes this $O(1)$ search possible.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
