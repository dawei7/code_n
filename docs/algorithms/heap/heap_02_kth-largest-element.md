# K-th Largest Element

| | |
|---|---|
| **ID** | `heap_02` |
| **Category** | heap |
| **Complexity (required)** | $O(N log K)$ |
| **Difficulty** | 4/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) |

## Problem statement

Given an unsorted integer array `nums` and an integer `k`, return the `k`-th largest element in the array.
Note that it is the `k`-th largest element in the sorted order, not the `k`-th distinct element.
While sorting the array takes $O(N \log N)$, you must use a Priority Queue (Heap) to achieve $O(N log K)$ time complexity.

**Input:** An unsorted array of integers, and an integer K.
**Output:** The integer representing the K-th largest element.

## When to use it

- This is one of the most frequently asked fundamental interview questions.
- Use this specific $O(N log K)$ Min-Heap approach when dealing with a **Streaming Data** problem where N is practically infinite and you cannot hold the entire array in memory.

## Approach

A naive heap approach throws all N elements into a Max-Heap in $O(N)$ time (`heap_01`), and then pops the max element K times, taking $O(K log N)$. This is fast, but it requires allocating memory for all N elements simultaneously.

**The Min-Heap Strategy ($O(N log K)$):**
If we only want the K-th largest element, we don't care about anything smaller than that!
We can maintain a **Min-Heap** of strictly size K. This heap will act as a "VIP Club" that only holds the top K largest elements we've seen so far.
Because it is a Min-Heap, the *smallest* element in this VIP club is always sitting at the top (`heap[0]`).

1. Iterate through the array.
2. Push each element into the Min-Heap.
3. If the size of the heap exceeds K, we instantly `pop()`! The Min-Heap guarantees that we just kicked out the smallest element currently in the VIP club.
4. When the loop finishes, the heap contains exactly the K largest elements from the entire array.
5. The element sitting at the top of the Min-Heap (`heap[0]`) is the smallest of those K largest elements... which is exactly the **K-th largest element overall**!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for heap_02: Kth Largest Element.

Maintain a min-heap of size k. For each element, push it onto
the heap and pop the smallest if the heap is over k. At the end
the heap contains the k largest elements; the smallest of those
(the heap top) is the kth largest. O(n log k).
"""


def solve(data, n, k):
    import heapq
    if k <= 0 or k > n:
        return -1
    heap = []
    for value in data:
        if len(heap) < k:
            heapq.heappush(heap, value)
        elif value > heap[0]:
            heapq.heapreplace(heap, value)
    return heap[0]
```

</details>

## Walk-through

`nums = [3, 2, 1, 5, 6, 4]`, `k = 2`.

1. **Push 3:** `min_heap = [3]`. (Size 1 \le 2).
2. **Push 2:** `min_heap = [2, 3]`. (Size 2 \le 2).
3. **Push 1:** `min_heap = [1, 3, 2]`. (Size 3 > 2).
   - Pop! The smallest element `1` is kicked out. `min_heap = [2, 3]`.
4. **Push 5:** `min_heap = [2, 3, 5]`. (Size 3 > 2).
   - Pop! The smallest element `2` is kicked out. `min_heap = [3, 5]`.
5. **Push 6:** `min_heap = [3, 5, 6]`. (Size 3 > 2).
   - Pop! The smallest element `3` is kicked out. `min_heap = [5, 6]`.
6. **Push 4:** `min_heap = [4, 6, 5]`. (Size 3 > 2).
   - Pop! The smallest element `4` is kicked out. `min_heap = [5, 6]`.

Loop finishes! The heap is `[5, 6]`. The 2nd largest element overall is at the top of the Min-Heap: `5`! ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N log K)$ | $O(K)$ |
| **Average** | $O(N log K)$ | $O(K)$ |
| **Worst** | $O(N log K)$ | $O(K)$ |

We iterate through N elements. For each element, we push and possibly pop from a heap of max size K. Heap operations on size K take $O(log K)$. Total time is exactly $O(N log K)$.
Space complexity is strictly $O(K)$ to store the VIP elements. This makes it perfect for massive data streams where N is billions but K is just 100.

## Variants & optimizations

- **Quickselect ($O(N)$ Average):** The absolute fastest algorithm in practice if all data is available in memory. It uses the partition logic from Quick Sort. If you randomly pick a pivot and partition the array, you know exactly how many elements are larger than the pivot. If there are exactly K-1 larger elements, the pivot IS the K-th largest! It takes $O(N)$ average time, but degrades to $O(N^2)$ worst case.
- **Max-Heap ($O(N + K log N)$):** As discussed, `build_max_heap` takes $O(N)$, and K pops take $O(K log N)$. If K is very small, this is actually mathematically faster than the $O(N log K)$ Min-Heap approach! However, it uses $O(N)$ space.

## Real-world applications

- **Twitter Trending Topics:** A streaming aggregator identifying the top K most active hashtags out of millions of live tweets.
- **Stock Market:** Finding the 10 most heavily traded stocks in real-time.

## Related algorithms in cOde(n)

- **[heap_03 - Top K Frequent Elements](heap_03_top-k-frequent-elements.md)** — A direct extension of this VIP club pattern applied to frequency maps.
- **[sort_04 - Quick Sort](../sorting/sort_04_quick-sort.md)** — The foundation of the $O(N)$ Quickselect alternative.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
