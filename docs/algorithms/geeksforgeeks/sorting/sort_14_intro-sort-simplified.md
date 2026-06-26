# Intro Sort (Introspective Sort)

| | |
|---|---|
| **ID** | `sort_14` |
| **Category** | sorting |
| **Complexity (required)** | $O(N \log N)$ Time, $O(\log N)$ Space |
| **Difficulty** | 7/10 |
| **Interview relevance** | 5/10 |
| **Wikipedia** | [Introsort](https://en.wikipedia.org/wiki/Introsort) |

## Problem statement

Given an array of integers `arr`, sort the array in ascending order.
You must use a hybrid algorithm that guarantees the incredible average-case speed of Quicksort, but physically prevents Quicksort from ever degrading into its mathematical $O(N^2)$ worst-case.

**Input:** An unsorted array of integers `arr`.
**Output:** A sorted array.

## When to use it

- When you type `std::sort()` in C++. This IS the algorithm executing under the hood!
- When you absolutely need an in-place sort with $O(\log N)$ space, meaning Merge Sort and Tim Sort (which require $O(N)$ auxiliary memory arrays) are disqualified.

## Approach

**1. The Fatal Flaw of Quicksort (`sort_05`):**
Quicksort is mathematically the fastest comparison-based sort in the world on average. But if the array is already sorted (or reversed) and you pick a bad pivot, the recursion tree becomes incredibly unbalanced. The recursion goes N levels deep, taking $O(N^2)$ time and risking a Stack Overflow memory crash!

**2. The Introspection Strategy (Self-Awareness):**
Invented by David Musser in 1997, Intro Sort literally "introspects" (looks at its own behavior) while it runs.
We start by running standard Quicksort. But we pass a `depth_limit` parameter into the recursive function!
The optimal depth for a perfectly balanced Quicksort tree is 2 x log_2(N).
Every time Quicksort recurses, we subtract 1 from the depth limit.

**3. The Emergency Bailout (Heap Sort):**
If `depth_limit` hits `0`, Intro Sort mathematically realizes: *"Wait! I've recursed too deep! The pivot selection is failing, and I'm heading towards $O(N^2)$ territory!"*
Instead of continuing to recurse, it instantly ABORTS Quicksort for that specific sub-array!
It immediately calls **Heap Sort (`sort_06`)** on that specific sub-array!
Why Heap Sort? Because Heap Sort is strictly $O(N \log N)$ worst-case, requires zero extra memory, and doesn't use recursion (saving the call stack)!

**4. The Small Array Optimization (Insertion Sort):**
Just like Tim Sort, when the sub-array size becomes very small (e.g., < 16 elements), the overhead of recursion or building Heaps isn't worth it. Intro Sort switches to **Insertion Sort (`sort_03`)** to finish the tiny chunks in blisteringly fast $O(1)$ time.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for sort_14: Intro Sort (Simplified).

Quicksort with depth limit; fall back to heapsort.
"""


def solve(data, n):
    if n <= 1:
        return data
    import math
    work = list(data)
    depth_limit = 2 * int(math.log2(n)) if n > 1 else 0

    def sift_down(lo, hi, root):
        while True:
            child = 2 * (root - lo) + 1 + lo
            if child >= hi:
                break
            if child + 1 < hi and work[child + 1] > work[child]:
                child += 1
            if work[child] > work[root]:
                work[root], work[child] = work[child], work[root]
                root = child
            else:
                break

    def heap_sort(lo, hi):
        for start in range((hi - lo) // 2 - 1 + lo, lo - 1, -1):
            sift_down(lo, hi, start)
        for end in range(hi - 1, lo, -1):
            work[lo], work[end] = work[end], work[lo]
            sift_down(lo, end, lo)

    def partition(lo, hi):
        pivot = work[hi - 1]
        i = lo
        for j in range(lo, hi - 1):
            if work[j] <= pivot:
                work[i], work[j] = work[j], work[i]
                i += 1
        work[i], work[hi - 1] = work[hi - 1], work[i]
        return i

    def intro_sort(lo, hi, depth):
        if hi - lo <= 1:
            return
        if depth == 0:
            heap_sort(lo, hi)
            return
        p = partition(lo, hi)
        intro_sort(lo, p, depth - 1)
        intro_sort(p + 1, hi, depth - 1)

    intro_sort(0, n, depth_limit)
    return work
```

</details>

## Walk-through

Let's imagine a pathological array designed specifically to break Quicksort: `arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]`. `N = 10`.
1. `max_depth = 2 * int(log2(10)) = 2 * 3 = 6`.
2. **`intro_sort_helper` (Depth 6):**
   - Quicksort partition picks `1`. Array stays reversed.
   - Recurse on left `[10, 9, 8, 7, 6, 5, 4, 3, 2]`. Size 9.
3. **`intro_sort_helper` (Depth 5):**
   - Quicksort partition picks `2`.
   - Recurse on left `[10...3]`. Size 8.
   ... *(This keeps happening, and Quicksort is failing terribly)* ...
4. **`intro_sort_helper` (Depth 0):**
   - `depth_limit == 0`!
   - Intro Sort detects the $O(N^2)$ failure in real-time!
   - It instantly aborts Quicksort. It calls `heap_sort` on the remaining sub-array!
   - Heap Sort executes in strictly $O(N \log N)$ time with no recursion!
5. All recursions finish. Array is perfectly sorted! ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N \log N)$ | $O(\log N)$ |
| **Average** | $O(N \log N)$ | $O(\log N)$ |
| **Worst** | $O(N \log N)$ | $O(\log N)$ |

Intro Sort achieves the holy grail of sorting:
It runs Quicksort 99% of the time, inheriting Quicksort's incredibly low constant factors and unmatched hardware cache locality (making it practically faster than anything else).
But its worst-case time complexity is completely guaranteed to be $O(N \log N)$ because the Heap Sort bailout strictly prevents the $O(N^2)$ tree from ever forming!
Space complexity is $O(\log N)$ because the depth limit prevents the recursive Call Stack from ever exceeding 2 log_2 N frames. Heap Sort runs strictly in $O(1)$ space.

## Variants & optimizations

- **Median-of-Three Pivot:** Intro Sort implementations often optimize the Quicksort `partition` phase by taking the Left, Right, and Middle elements, and using their median as the pivot, massively reducing the chances of ever hitting the `depth_limit` emergency bailout in the first place!

## Real-world applications

- **C++ Standard Template Library (STL):** The C++ `std::sort` was completely rewritten to use Intro Sort because it strictly required $O(N \log N)$ worst-case time but developers refused to accept the memory allocation overhead of Merge Sort.
- **.NET Framework:** Microsoft's `Array.Sort` uses Intro Sort for primitive types.

## Related algorithms in cOde(n)

- **[sort_05 - Quick Sort](sort_05_quick-sort.md)** — The primary engine.
- **[sort_06 - Heap Sort](sort_06_heap-sort.md)** — The emergency bailout engine.
- **[sort_03 - Insertion Sort](sort_03_insertion-sort.md)** — The small-array cleanup engine.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
