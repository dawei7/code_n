# Pattern Search with Suffix Array

| | |
|---|---|
| **ID** | `suffix_02` |
| **Category** | suffix_array |
| **Complexity (required)** | $O(M \log N)$ Time, $O(1)$ Space |
| **Difficulty** | 5/10 |
| **Interview relevance** | 4/10 |
| **GeeksForGeeks Equivalent** | [Pattern Searching using Suffix Array](https://www.geeksforgeeks.org/pattern-searching-using-suffix-array/) |

## Problem statement

Given a large `text` string of length N, its pre-computed Suffix Array `suffix_arr`, and a `pattern` string of length M.
Find whether the `pattern` exists as a contiguous substring within the `text`.
You must leverage the Suffix Array to achieve a search time of $O(M log N)$, avoiding the $O(N)$ scan of algorithms like KMP or Rabin-Karp.

**Input:** A string `text`, its Suffix Array, and a string `pattern`.
**Output:** A boolean indicating if the pattern exists.

## When to use it

- When you have a massive, static document (like the entire text of a book) and you need to query it thousands of times for different patterns. (An $O(N)$ KMP scan per query would be too slow).

## Approach

**1. The Alphabetical Guarantee:**
What is a Suffix Array? It is a list of ALL possible suffixes of the text, perfectly sorted in alphabetical order.
If `pattern` exists anywhere inside the `text`, it mathematically MUST be the *prefix* of at least one suffix!
For example, if `text = "banana"` and `pattern = "nan"`. `"nan"` is literally the prefix of the suffix `"nana"`.
Therefore, searching for a pattern is mathematically identical to searching for a string that *starts with* the pattern inside a perfectly alphabetically sorted array!

**2. Standard Binary Search:**
How do you find a string in a sorted array? You use **Binary Search (`search_02`)**!
The array size is N. Binary search takes $O(\log N)$ steps.
At each step, we look at `suffix_arr[mid]`. This points to a specific suffix in the text.
We compare our `pattern` against the characters of the text starting at that index.
Because string comparison takes $O(M)$ time, the total search time is exactly $O(M log N)$!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for suffix_02: Pattern Search with Suffix Array.

Build SA, then binary-search for the range of suffixes
that start with pattern.
"""


def solve(s, n, pattern, m):
    if m == 0 or n == 0:
        return []
    sa = sorted(range(n), key=lambda i: s[i:])
    out = []
    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi) // 2
        if s[sa[mid]:] < pattern:
            lo = mid + 1
        else:
            hi = mid
    lower = lo
    hi = n
    while lo < hi:
        mid = (lo + hi) // 2
        if s[sa[mid]:].startswith(pattern):
            lo = mid + 1
        elif s[sa[mid]:] < pattern:
            lo = mid + 1
        else:
            hi = mid
    upper = lo
    for i in range(lower, upper):
        out.append(sa[i])
    return sorted(out)
```

</details>

## Walk-through

`text = "banana"`, `suffix_arr = [5, 3, 1, 0, 4, 2]`.
`pattern = "nan"`. M = 3.

*Suffixes in array order:*
0: `[5]` "a"
1: `[3]` "ana"
2: `[1]` "anana"
3: `[0]` "banana"
4: `[4]` "na"
5: `[2]` "nana"

1. `left = 0`, `right = 5`. `mid = 2`.
   - `suffix_arr[2]` is index `1`.
   - Suffix starting at index `1` is `"anana"`.
   - Extract length 3: `"ana"`.
   - Compare `"nan"` with `"ana"`. `"nan" > "ana"` alphabetically.
   - `left = mid + 1 = 3`.
2. `left = 3`, `right = 5`. `mid = 4`.
   - `suffix_arr[4]` is index `4`.
   - Suffix starting at index `4` is `"na"`.
   - Extract length 3: `"na"`.
   - Compare `"nan"` with `"na"`. `"nan" > "na"` alphabetically.
   - `left = mid + 1 = 5`.
3. `left = 5`, `right = 5`. `mid = 5`.
   - `suffix_arr[5]` is index `2`.
   - Suffix starting at index `2` is `"nana"`.
   - Extract length 3: `"nan"`.
   - Compare `"nan"` with `"nan"`. MATCH!

Return `True`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(M)$ | $O(1)$ |
| **Average** | $O(M \log N)$ | $O(1)$ |
| **Worst** | $O(M \log N)$ | $O(1)$ |

The binary search cuts the search space in half at each step, requiring exactly log_2 N iterations.
At each iteration, we compare two strings of maximum length M. A string comparison takes $O(M)$ time in the worst case (where the strings are almost perfectly identical until the last character).
Total time complexity is strictly $O(M log N)$.
Space complexity is $O(1)$ constant auxiliary space (excluding the pre-computed Suffix Array itself).

## Variants & optimizations

- **LCP-Accelerated Binary Search ($O(M + log N)$):** If you also pre-compute the Longest Common Prefix (LCP) Array, you can optimize the Binary Search! During binary search, if you know you matched K characters with the Left bound, and K characters with the Right bound, any Suffix in between mathematically MUST also match those K characters! You can safely skip the first K characters during your string comparison, dropping the time complexity to an insane $O(M + log N)$!

## Real-world applications

- **Bioinformatics / Genome Databases:** Genomes are massive strings (3 billion characters) that never change. They are pre-processed into Suffix Arrays overnight. When scientists query a short RNA pattern, the database executes this exact $O(M log N)$ search to return the chromosome locations instantly.

## Related algorithms in cOde(n)

- **[search_02 - Binary Search](../searching/search_02_binary-search.md)** — The engine that powers this lookup.
- **[suffix_01 - Build Suffix Array](suffix_01_build-suffix-array.md)** — How the index array is generated in the first place.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
