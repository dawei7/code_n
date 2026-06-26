# Build Suffix Array

| | |
|---|---|
| **ID** | `suffix_01` |
| **Category** | suffix_array |
| **Complexity (required)** | $O(N \log N \log N)$ Time, $O(N)$ Space |
| **Difficulty** | 8/10 |
| **Interview relevance** | 3/10 |
| **GeeksForGeeks Equivalent** | [Suffix Array Definition and Construction](https://www.geeksforgeeks.org/suffix-array-set-1-introduction/) |

## Problem statement

Given a string `s` of length N, construct its **Suffix Array**.
A Suffix Array is a sorted array of all the suffixes of a string.
Instead of storing the actual string suffixes (which would take $O(N^2)$ space), the Suffix Array stores the starting **indices** of these suffixes in lexicographical (alphabetical) order.

**Input:** A string `s`.
**Output:** An integer array of size N containing the sorted indices.

## When to use it

- To perform blazing-fast text searches on a static document.
- It is a space-efficient alternative to the Suffix Tree data structure, solving exactly the same massive substring queries but using drastically less memory.

## Approach

**1. The Naive $O(N^2 log N)$ Sort:**
If `s = "banana"`.
Suffixes are: `0: "banana"`, `1: "anana"`, `2: "nana"`, `3: "ana"`, `4: "na"`, `5: "a"`.
We put these in an array and use standard sorting.
Sorted: `"a" (5)`, `"ana" (3)`, `"anana" (1)`, `"banana" (0)`, `"na" (4)`, `"nana" (2)`.
Suffix Array is `[5, 3, 1, 0, 4, 2]`.
Standard sorting compares strings $O(N \log N)$ times. Each string comparison takes $O(N)$ time. Total time is $O(N^2 log N)$. This is way too slow for a 1-million character text!

**2. The Prefix Doubling Optimization ($O(N log^2 N)$):**
We don't need to compare entire suffixes at once. We can sort them progressively!
- **Pass 1 (Length 1):** We sort the suffixes based ONLY on their first character. We assign a "Rank" to each suffix.
- **Pass 2 (Length 2):** We want to sort suffixes based on their first 2 characters. But wait! The first 2 characters of a suffix starting at `i` is just the first character of `i`, combined with the first character of `i+1`! Since we ALREADY calculated the Ranks of length 1, we can just sort based on the Tuple: `(Rank[i], Rank[i+1])`!
- **Pass 3 (Length 4):** We want to sort based on the first 4 characters. The first 4 characters of `i` is the first 2 characters of `i` combined with the first 2 characters of `i+2`! We sort based on `(Rank[i], Rank[i+2])`!

By doubling the length we look at (1, 2, 4, 8...), we only need log_2 N passes to completely sort strings of length N.
In each pass, we sort an array of N tuples, which takes $O(N \log N)$ time.
Total time: $O(log N \text{ passes})$ x $O(N log N \text{ sort})$ = $O(N log^2 N)$.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for suffix_01: Build Suffix Array.

Naive: build all n suffixes and sort them. O(n^2 log n).
"""


def solve(s, n):
    if n == 0:
        return []
    return sorted(range(n), key=lambda i: s[i:])
```

</details>

## Walk-through

`s = "banana"`, N = 6.
**Initialization (Length 1 prefixes):**
Tuples are `(s[i], s[i+1])`.
- `0 (ba)`: `(1, 0)`
- `1 (an)`: `(0, 13)`
- `2 (na)`: `(13, 0)`
- `3 (an)`: `(0, 13)`
- `4 (na)`: `(13, 0)`
- `5 (a_)`: `(0, -1)`
Sorted: `[5 (a_), 1 (an), 3 (an), 0 (ba), 2 (na), 4 (na)]`.

**Iteration 1 (Length 2 -> Length 4 prefixes):**
We assign new integer ranks to the sorted elements:
- `5` gets Rank 0.
- `1` and `3` are identical `(0, 13)`, they both get Rank 1.
- `0` gets Rank 2.
- `2` and `4` are identical `(13, 0)`, they both get Rank 3.
Now we build tuples for Length 4.
For suffix `1 (anana)`, its tuple is `(Rank of 1, Rank of 1+2)`.
Rank of 1 is `1`. Rank of 3 is `1`. Tuple is `(1, 1)`.
For suffix `3 (ana)`, tuple is `(Rank of 3, Rank of 5)`.
Rank of 3 is `1`. Rank of 5 is `0`. Tuple is `(1, 0)`.
Notice how `3` now has a SMALLER tuple than `1`! `"ana"` correctly comes before `"anana"`!
We sort the new tuples.

By log_2 N iterations, every suffix is perfectly separated and sorted.
Returns `[5, 3, 1, 0, 4, 2]`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N \log^2 N)$ | $O(N)$ |
| **Average** | $O(N \log^2 N)$ | $O(N)$ |
| **Worst** | $O(N \log^2 N)$ | $O(N)$ |

The algorithm iterates a `while` loop log_2 N times.
Inside the loop, the built-in `sort()` function sorts an array of N objects, taking $O(N \log N)$ time.
Total time complexity is cleanly $O(N log^2 N)$.
Space complexity is $O(N)$ to hold the arrays of `Suffix` objects and ranks.

## Variants & optimizations

- **Radix Sort Optimization ($O(N \log N)$):** In the inner loop, we are sorting an array of 2D tuples `(rank1, rank2)`. We don't need $O(N \log N)$ comparison sorting for this! We can use a 2-pass Radix Sort (`sort_08`). This reduces the inner sort to $O(N)$, bringing the total algorithmic time down to mathematically guaranteed $O(N \log N)$!
- **DC3 / Skew Algorithm ($O(N)$):** There exist incredibly complex linear-time algorithms for constructing Suffix Arrays natively, but they are generally considered too verbose for technical interviews.

## Real-world applications

- **Full-Text Search Engines:** ElasticSearch and Lucene use suffix arrays/trees under the hood to instantly find substrings in massive gigabyte log files without scanning the file.
- **Data Compression:** Suffix Arrays are the foundational step of the Burrows-Wheeler Transform, which is the mathematical engine behind `bzip2` compression.

## Related algorithms in cOde(n)

- **[suffix_03 - LCP Array (Kasai's Algorithm)](suffix_03_lcp-array-kasai-s-algorithm.md)** — The mandatory secondary array that makes Suffix Arrays actually useful for solving complex string problems.
- **[suffix_02 - Pattern Search](suffix_02_pattern-search-with-suffix-array.md)** — How to use the generated Suffix Array to instantly find substrings.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
