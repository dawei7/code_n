# Randomized Quicksort

| | |
|---|---|
| **ID** | `randomized_01` |
| **Category** | randomized |
| **Complexity (required)** | $O(N \log N)$ Expected |
| **Difficulty** | 4/10 |
| **Interview relevance** | 8/10 |
| **Wikipedia** | [Quicksort (Randomized)](https://en.wikipedia.org/wiki/Quicksort#Randomized_quicksort) |

## Problem statement

Sort an array of N elements using the Quicksort algorithm, but explicitly guarantee an expected time complexity of $O(N \log N)$ regardless of the initial ordering of the input array.

**Input:** An unsorted array of integers.
**Output:** The same array, sorted in-place.

## When to use it

- You want the fastest practical in-place sorting algorithm and need to defend against adversarial inputs that would cause standard Quicksort to degrade to $O(N^2)$.
- Often explicitly requested in interviews to test understanding of algorithmic worst-case scenarios.

## Approach

Standard Quicksort works by picking a "pivot" (often the last element or first element), partitioning the array so smaller elements are on the left and larger on the right, and recursing.
The fatal flaw of standard Quicksort is that if the input is *already sorted* (or reverse sorted), picking the last element as the pivot results in partitions of size 0 and N-1. The recursion depth becomes N, yielding $O(N^2)$ time!

To fix this, we introduce **Las Vegas Randomization**.
Before we partition a segment `[low...high]`, we randomly select an index `r` between `low` and `high`.
We swap the element at `r` with the element at `high`.
Then, we proceed with the exact standard partitioning logic, using `high` as the pivot!

Because the pivot is chosen uniformly at random, the probability of consistently picking the absolute worst pivot at every step of recursion becomes astronomically low. The *expected* partition sizes are balanced, guaranteeing $O(N \log N)$ expected time, independent of the input permutation!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for randomized_01: Randomized Quicksort.

Quicksort with a random pivot. Each partition picks a random
index in [lo, hi], swaps it to the end, then Lomuto-partitions.
Expected O(n log n); with adversarial input, expected
O(n log n) - the random pivot breaks the bad case.
"""


def solve(data, n):
    import random
    work = list(data)

    def partition(lo, hi):
        pivot_idx = random.randint(lo, hi)
        work[pivot_idx], work[hi] = work[hi], work[pivot_idx]
        pivot = work[hi]
        i = lo
        for j in range(lo, hi):
            if work[j] <= pivot:
                work[i], work[j] = work[j], work[i]
                i += 1
        work[i], work[hi] = work[hi], work[i]
        return i

    def sort(lo, hi):
        if lo < hi:
            p = partition(lo, hi)
            sort(lo, p - 1)
            sort(p + 1, hi)

    if n > 1:
        sort(0, n - 1)
    return work
```

</details>

## Walk-through

`arr = [1, 2, 3, 4, 5]` (Already sorted - worst case for standard Quicksort!)
`low = 0, high = 4`.

**Standard Quicksort:**
- Pivot is `arr[4] = 5`.
- Partitions into `[1, 2, 3, 4]` and `[]`.
- Next pivot is `arr[3] = 4`. Partitions into `[1, 2, 3]` and `[]`.
- $O(N^2)$ degradation!

**Randomized Quicksort:**
- `random.randint(0, 4)` rolls `2`.
- Swap `arr[2]` with `arr[4]`. Array is now `[1, 2, 5, 4, 3]`.
- Pivot is `arr[4] = 3`.
- `partition` groups `<3` to the left, `>3` to the right.
- Array becomes `[1, 2, 3, 4, 5]`. Pivot `3` ends up at index `2`.
- Partitions perfectly into `[1, 2]` and `[4, 5]`!
- Recursion depth is log N.

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N \log N)$ | $O(\log N)$ |
| **Average** | $O(N \log N)$ Expected | $O(\log N)$ |
| **Worst** | $O(N^2)$ (Mathematically possible, practically zero) | $O(N)$ |

The theoretical worst case is still $O(N^2)$ if the random number generator miraculously rolls the worst possible pivot at every single step, but the probability of this is 1 / N!, which is practically 0. The expected time is proven to be $O(N \log N)$.
Space complexity is $O(\log N)$ expected for the recursive call stack.

## Variants & optimizations

- **Median-of-Three:** Instead of calling a random number generator (which is slow in system libraries), pick three elements (first, middle, last) and use their median as the pivot. This deterministically defeats the "already sorted" worst-case while avoiding random overhead.
- **IntroSort:** The algorithm used in C++ `std::sort`. It begins with Randomized Quicksort, but if the recursion depth exceeds 2 log N, it abruptly switches to HeapSort to absolutely guarantee $O(N \log N)$ worst-case time!

## Real-world applications

- **System Libraries:** General-purpose sorting functions in dynamically typed languages where the input distribution is unknown and must be protected against malicious adversarial inputs (e.g., DDOS attacks targeting sort routines).

## Related algorithms in cOde(n)

- **[sorting_03 - Quicksort](../sorting/sorting_03_quicksort.md)** — The deterministic precursor.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
