# Tim Sort (Simplified)

| | |
|---|---|
| **ID** | `sort_13` |
| **Category** | sorting |
| **Complexity (required)** | $O(N \log N)$ Time, $O(N)$ Space |
| **Difficulty** | 7/10 |
| **Interview relevance** | 6/10 |
| **Wikipedia** | [Timsort](https://en.wikipedia.org/wiki/Timsort) |

## Problem statement

Given an array of integers `arr`, sort the array in ascending order.
You must use a hybrid algorithm that guarantees $O(N \log N)$ worst-case performance, but is hyper-optimized to achieve $O(N)$ time if the data is already partially sorted.

**Input:** An unsorted array of integers `arr`.
**Output:** A sorted array.

## When to use it

- When you type `arr.sort()` in Python or `Arrays.sort()` in Java. This IS the algorithm executing under the hood!
- To demonstrate deep systems-level knowledge of how purely academic algorithms (Merge Sort / Insertion Sort) are blended together for real-world hardware.

## Approach

**1. The Reality of Real-World Data:**
Merge Sort is mathematically brilliant, dividing arrays down to size 1 and merging them up. But recursively splitting an array down to size 1 causes massive Call Stack overhead.
Furthermore, real-world data is rarely 100% random. It usually contains long "runs" of data that are already perfectly sorted! Merge Sort blindly tears these sorted runs apart down to size 1, completely destroying existing order.

**2. The Tim Sort Hybrid Strategy:**
Invented by Tim Peters in 2002 for Python, Tim Sort is a beautiful marriage of **Insertion Sort** and **Merge Sort**.
Insertion Sort is incredibly fast on small arrays (size \le 32), and theoretically $O(N)$ on arrays that are already mostly sorted!
Merge Sort is perfectly stable and guarantees $O(N \log N)$ for massively huge arrays.
So, we just break the massive array into fixed blocks of size 32 (called "Runs"). We sort each 32-element run individually using Insertion Sort. Then, we use the Merge Sort `merge()` function to seamlessly stitch the sorted blocks together!

**3. The Algorithm Steps:**
1. Pick a `RUN` size (typically 32 or 64).
2. Iterate through the array in chunks of `RUN`.
3. Call `insertion_sort` on each chunk.
4. Start a `size` variable at `RUN`.
5. Iterate through the array, taking two adjacent chunks of `size` and merging them into a chunk of `size * 2`.
6. Double the `size` and repeat the merging phase until `size > N`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for sort_13: Tim Sort (Simplified).

Identify natural runs, extend to minrun, merge pairwise.
"""


def solve(data, n):
    if n <= 1:
        return data
    work = list(data)
    RUN = max(1, min(32, n // 4))
    runs = []
    i = 0
    while i < n:
        j = i + 1
        while j < n and work[j] >= work[j - 1]:
            j += 1
        runs.append((i, j))
        if j - i < RUN:
            end = min(i + RUN, n)
            sub = work[i:end]
            sub.sort()
            work[i:end] = sub
            j = end
            runs[-1] = (runs[-1][0], j)  # update with extended end
        i = j
    while len(runs) > 1:
        new_runs = []
        for k in range(0, len(runs), 2):
            if k + 1 < len(runs):
                lo1, hi1 = runs[k]
                lo2, hi2 = runs[k + 1]
                merged = []
                a, b = lo1, lo2
                while a < hi1 and b < hi2:
                    if work[a] <= work[b]:
                        merged.append(work[a])
                        a += 1
                    else:
                        merged.append(work[b])
                        b += 1
                merged.extend(work[a:hi1])
                merged.extend(work[b:hi2])
                work[lo1:hi2] = merged
                new_runs.append((lo1, hi2))
            else:
                new_runs.append(runs[k])
        runs = new_runs
    return work
```

</details>

## Walk-through

`arr = [5, 21, 7, 23, 19, 11, 3, 17]`. `N = 8`.
Let's artificially set `MIN_MERGE = 4` for this example.

**Phase 1: Insertion Sort Runs**
- Chunk 1: `[5, 21, 7, 23]` (Indices 0 to 3).
  - Insertion Sort perfectly sorts to `[5, 7, 21, 23]`.
- Chunk 2: `[19, 11, 3, 17]` (Indices 4 to 7).
  - Insertion Sort perfectly sorts to `[3, 11, 17, 19]`.
Array is now two sorted blocks: `[5, 7, 21, 23 | 3, 11, 17, 19]`.

**Phase 2: Merging**
- `size = 4`.
- `left = 0`, `mid = 3`, `right = 7`.
- Merge `[5, 7, 21, 23]` with `[3, 11, 17, 19]`.
  - Compares pointers and interleaves correctly.
Array is perfectly sorted: `[3, 5, 7, 11, 17, 19, 21, 23]`. ✓
- `size = 8`. `size < N` is False. Loop terminates!

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(N)$ |
| **Average** | $O(N \log N)$ | $O(N)$ |
| **Worst** | $O(N \log N)$ | $O(N)$ |

The array is divided into N/32 blocks. Insertion sort sorts each block in constant $O(32^2)$ ~= $O(1)$ time. Over N/32 blocks, this initial phase takes $O(N)$ time.
The merging phase doubles the block size at each step, requiring exactly log_2(N/32) passes. Each pass touches every element, taking $O(N)$.
Total worst-case time is $O(N \log N)$.
However, if the array is entirely sorted, Phase 1 executes in exactly $O(N)$ time, and the advanced merging logic detects no merges are necessary, exiting instantly in $O(N)$ Best-Case Time!
Space complexity is $O(N)$ because the `merge` subroutine strictly requires creating temporary left/right arrays.

## Variants & optimizations

- **Natural Runs (The True Tim Sort):** The Python implementation does not blindly cut blocks of size 32. It scans the array sequentially to find "Natural Runs" (sequences that are already sorted). If a Natural Run is smaller than 32, it runs Insertion Sort to pad it up to 32. If a Natural Run is 1000 elements long, it leaves it completely intact and just merges it as a massive block later!
- **Galloping Mode (`search_07`):** During the `merge` subroutine, if Tim Sort notices that the pointer on the `left_arr` is winning 7 times in a row, it mathematically assumes the `left_arr` is vastly smaller. It switches from $O(1)$ linear pointer increments to an $O(\log N)$ Exponential Search to instantly find the insertion boundary, saving thousands of comparisons!

## Real-world applications

- **Python, Java, Android, V8 Engine:** It is the undisputed king of stable sorting. If a language promises an incredibly fast, stable sort for Objects, it uses Tim Sort.

## Related algorithms in cOde(n)

- **[sort_03 - Insertion Sort](sort_03_insertion-sort.md)** — The engine for the small runs.
- **[sort_04 - Merge Sort](sort_04_merge-sort.md)** — The engine for combining the runs.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
