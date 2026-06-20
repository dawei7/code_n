# Build Max Heap (Heapify)

| | |
|---|---|
| **ID** | `heap_01` |
| **Category** | heap |
| **Complexity (required)** | $O(N)$ |
| **Difficulty** | 5/10 |
| **Interview relevance** | 6/10 |
| **Wikipedia** | [Binary heap](https://en.wikipedia.org/wiki/Binary_heap#Building_a_heap) |

## Problem statement

Given an unsorted array of N integers, rearrange the elements in-place so that they satisfy the **Max-Heap property**: For every node i, the value of node i is greater than or equal to the values of its children.
You must build this heap in strictly $O(N)$ time, not $O(N \log N)$.

**Input:** An unsorted array of integers.
**Output:** The same array mutated in-place into a valid Max-Heap.

## When to use it

- As the fundamental first step of the Heap Sort algorithm.
- When you need a Priority Queue but are handed the entire batch of data upfront instead of a stream. Building a heap in $O(N)$ is mathematically faster than inserting N elements into an empty heap one by one ($O(N \log N)$).

## Approach

A Binary Heap is typically visualized as a complete binary tree, but it is stored perfectly efficiently in a flat array!
If a node is at index `i` (0-indexed):
- Its Left Child is at `2*i + 1`.
- Its Right Child is at `2*i + 2`.
- Its Parent is at `(i - 1) // 2`.

**The `sift_down` Operation:**
If you have a node that is smaller than its children, it violates the Max-Heap property. You fix this by "sifting" it down: swap it with its *largest* child, and repeat this recursively until it is larger than both children or it hits the bottom (becomes a leaf).

**The $O(N)$ Build Strategy (Floyd's Algorithm):**
A naive way to build a heap is to call `sift_up` for every element from left to right. This takes $O(N \log N)$.
To achieve $O(N)$, we must work **bottom-up**, calling `sift_down`!
1. The bottom half of the array represents the leaf nodes of the tree. Leaves have no children, so they trivially satisfy the heap property already! (We can skip them).
2. The last non-leaf node is at index `N // 2 - 1`.
3. We loop backwards from this index down to `0`.
4. For each node, we call `sift_down`. Because we are going backwards, we mathematically guarantee that the subtrees below the current node are already perfect Max-Heaps! The `sift_down` operation effortlessly merges them.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for heap_01: Build Max Heap.

Treat the input as a 0-indexed binary heap and sift-down from
the last non-leaf to the root. Bottom-up heapify is O(n) - faster
than the O(n log n) naive "insert" approach.
"""


def solve(data, n):
    # Sift down ``start`` in [0, n).
    def sift_down(start, end):
        root = start
        while True:
            child = 2 * root + 1
            if child >= end:
                break
            if child + 1 < end and data[child + 1] > data[child]:
                child += 1
            if data[child] > data[root]:
                data[root], data[child] = data[child], data[root]
                root = child
            else:
                break
    # Build the max-heap.
    for start in range(n // 2 - 1, -1, -1):
        sift_down(start, n)
    return data
```

</details>

## Walk-through

`arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]`
N = 11. Last non-leaf node is `11 // 2 - 1 = 4`.
*(Leaves: `13, 10, 9, 8, 15, 17` are ignored).*

1. **i = 4 (value 6):** Children are at 9 (value 15) and 10 (value 17). Largest child is 17. Swap 6 and 17!
   - `arr = [1, 3, 5, 4, 17, 13, 10, 9, 8, 15, 6]`.
2. **i = 3 (value 4):** Children at 7 (value 9) and 8 (value 8). Largest is 9. Swap 4 and 9!
   - `arr = [1, 3, 5, 9, 17, 13, 10, 4, 8, 15, 6]`.
3. **i = 2 (value 5):** Children at 5 (value 13) and 6 (value 10). Largest is 13. Swap 5 and 13!
   - `arr = [1, 3, 13, 9, 17, 5, 10, 4, 8, 15, 6]`.
4. **i = 1 (value 3):** Children at 3 (value 9) and 4 (value 17). Largest is 17. Swap 3 and 17!
   - `arr = [1, 17, 13, 9, 3, 5, 10, 4, 8, 15, 6]`.
   - Node 3 sifted down to index 4. Its new children are 15 and 6. Swap 3 and 15!
   - `arr = [1, 17, 13, 9, 15, 5, 10, 4, 8, 3, 6]`.
5. **i = 0 (value 1):** Children at 1 (value 17) and 2 (value 13). Swap 1 and 17!
   - `arr = [17, 1, 13, 9, 15, 5, 10, 4, 8, 3, 6]`.
   - Node 1 cascades down the tree exactly like Node 3 did.
   - Swap 1 with 15. Then Swap 1 with 6.
   - Final `arr = [17, 15, 13, 9, 6, 5, 10, 4, 8, 3, 1]`.

The maximum element (17) is now perfectly seated at `arr[0]`! ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(1)$ |
| **Average** | $O(N)$ | $O(1)$ |
| **Worst** | $O(N)$ | $O(1)$ |

Why is building a heap $O(N)$ when sifting down takes $O(\log N)$?
Most nodes in a tree are at the bottom! Half of the nodes are leaves (height 0, sift distance 0). A quarter of the nodes are at height 1 (sift distance 1). Only the single root node has to travel the full log N distance.
The mathematical sum of the series \sum \frac{h}{2^h} converges to exactly $O(N)$!
Space complexity is $O(1)$ auxiliary space if done iteratively (the recursive pseudocode above uses $O(\log N)$ call stack space, easily converted to a `while` loop).

## Variants & optimizations

- **Heap Sort ($O(N \log N)$):** Once the Max-Heap is built, swap `arr[0]` (the maximum element) with the last element of the array. Then call `sift_down(0)` on the reduced array size. Repeat until the array size is 1. The array is now perfectly sorted in ascending order!

## Real-world applications

- **OS Task Schedulers:** Maintaining a queue of processes where the process with the highest priority is always executed next.

## Related algorithms in cOde(n)

- **[heap_02 - K-th Largest Element](heap_02_kth-largest-element.md)** — Uses exactly this Max-Heap build to quickly extract the top elements.
- **[sort_04 - Quick Sort](../sorting/sort_04_quick-sort.md)** — Heap Sort provides a guaranteed $O(N \log N)$ worst-case time, unlike Quick Sort which degrades to $O(N^2)$, but Quick Sort is generally faster due to CPU cache locality.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
