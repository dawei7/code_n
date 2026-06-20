# Find Median from Data Stream

| | |
|---|---|
| **ID** | `heap_04` |
| **Category** | heap |
| **Complexity (required)** | $O(\log N)$ insert, $O(1)$ query |
| **Difficulty** | 7/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) |

## Problem statement

Design a data structure that supports the following operations:
1. `addNum(int num)`: Adds an integer `num` from a data stream to the data structure.
2. `findMedian()`: Returns the median of all elements so far. The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

You must handle an endless stream of incoming integers, maintaining the ability to return the exact median in $O(1)$ time and inserting new numbers in $O(\log N)$ time.

**Input:** A stream of numbers calling `addNum`, interspersed with `findMedian` queries.
**Output:** Float values representing the current median.

## When to use it

- A textbook system-design/data-structure interview question.
- Whenever you need dynamic access to the exact middle of a shifting dataset without sorting the whole array ($O(N \log N)$) or maintaining a balanced BST (complex to implement).

## Approach

**The Two-Heap Pattern:**
Imagine the sorted version of our data stream. We want to draw a line perfectly down the middle.
All numbers on the left half of the line are \le the median. All numbers on the right half are \ge the median.
If we know the absolute **largest** number in the left half, and the absolute **smallest** number in the right half, we instantly know the median!

We can maintain this exact state using two Priority Queues:
1. **Max-Heap (`lo`):** Stores the smaller half of the numbers. The root is the *largest* of the small numbers.
2. **Min-Heap (`hi`):** Stores the larger half of the numbers. The root is the *smallest* of the large numbers.

**The Balancing Act:**
To maintain the median, we must enforce two strict rules:
1. **Value Integrity:** EVERY number in the `lo` Max-Heap must be \le EVERY number in the `hi` Min-Heap.
2. **Size Balance:** The sizes of the two heaps can differ by at most 1. We will arbitrarily decide that if the total count is odd, the `lo` Max-Heap gets to hold the extra element.

**Insertion Logic:**
1. Always push the new number into the `lo` Max-Heap first.
2. But wait! The number we just pushed might actually belong in the `hi` half (it might be larger than the minimum element in `hi`). To fix this, we unconditionally `pop` the largest element from `lo` and `push` it into `hi`!
3. Now, `lo` and `hi` have perfect value integrity. But what about size balance?
4. If `hi` suddenly has more elements than `lo`, we `pop` the smallest element from `hi` and `push` it back into `lo`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for heap_04: Median in a Stream.

Two heaps: a max-heap of the smaller half, a min-heap of the
larger half. After each insert, rebalance so the two heaps are
within 1 of each other; the median is the top of the larger
heap (odd length) or the average of the two tops (even).
"""


def solve(data, n):
    import heapq
    if n == 0:
        return []
    small = []  # max-heap (inverted)
    large = []  # min-heap
    out = []
    for value in data:
        # Insert into the appropriate heap.
        if not small or value <= -small[0]:
            heapq.heappush(small, -value)
        else:
            heapq.heappush(large, value)
        # Rebalance.
        if len(small) > len(large) + 1:
            heapq.heappush(large, -heapq.heappop(small))
        elif len(large) > len(small):
            heapq.heappush(small, -heapq.heappop(large))
        # Compute the median.
        if len(small) > len(large):
            out.append(-small[0])
        else:
            out.append((-small[0] + large[0]) / 2)
    return out
```

</details>

## Walk-through

Stream: `1, 2, 3`

1. **`addNum(1)`:**
   - Push `-1` to `lo`. `lo = [-1]`.
   - Pop `lo` -> `1`. Push `1` to `hi`. `hi = [1]`.
   - Size check: `len(lo)=0 < len(hi)=1`.
   - Pop `hi` -> `1`. Push `-1` to `lo`. `lo = [-1]`, `hi = []`.
   - `findMedian()`: Sizes unequal. Median is `-(-1) = 1.0`. ✓

2. **`addNum(2)`:**
   - Push `-2` to `lo`. `lo = [-2, -1]`.
   - Pop `lo` (largest is `-1`, which is `1`). Push `1` to `hi`. `hi = [1]`. `lo = [-2]`.
   - Size check: `len(lo)=1 == len(hi)=1`. No action.
   - `findMedian()`: Sizes equal. Average of `2` and `1` = `1.5`. ✓

3. **`addNum(3)`:**
   - Push `-3` to `lo`. `lo = [-3, -2]`.
   - Pop `lo` (`2`). Push `2` to `hi`. `hi = [1, 2]`. `lo = [-3]`.
   - Size check: `len(lo)=1 < len(hi)=2`.
   - Pop `hi` (`1`). Push `-1` to `lo`. `lo = [-1, -3]`, `hi = [2]`.
   - `findMedian()`: Sizes unequal. Median is `-(-1) = 2.0`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(\log N)$ | $O(N)$ |
| **Average** | $O(\log N)$ | $O(N)$ |
| **Worst** | $O(\log N)$ | $O(N)$ |

Every `addNum` call triggers 2 or 3 heap operations. `heappush` and `heappop` take exactly $O(\log N)$ time.
Every `findMedian` call just reads `heap[0]`, taking exactly $O(1)$ time.
Space complexity is $O(N)$ because the heaps permanently store all the elements in the stream.

## Variants & optimizations

- **Order Statistic Tree:** If you use a Fenwick Tree with Binary Lifting (`fenwick_07`), you can find *any* arbitrary percentile (K-th element) in $O(log M)$ time, where M is the maximum value. The Two-Heap approach is strictly for finding the exactly 50th percentile (Median), but it does not require bounding the input values!
- **Count Array (If input values are small):** If you are guaranteed the stream only contains integers from 0 \dots 100, you don't need heaps! Just maintain an array of 101 counters $O(1)$, and a `total_count` variable. Finding the median takes $O(100)$ = $O(1)$ by looping through the array until the cumulative count reaches `total_count // 2`.

## Real-world applications

- **Network Monitoring:** Calculating the median ping response time dynamically to establish a baseline for alerts without recalculating historical logs.

## Related algorithms in cOde(n)

- **[heap_05 - Sliding Window Maximum](heap_05_sliding-window-maximum.md)** — Another streaming algorithm, but handles removing expired elements from the working set.
- **[fenwick_07 - K-th Smallest / Order Statistic](../fenwick/fenwick_07_k-th-smallest-order-statistic-bit.md)** — The algebraic alternative that allows querying arbitrary percentiles.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
