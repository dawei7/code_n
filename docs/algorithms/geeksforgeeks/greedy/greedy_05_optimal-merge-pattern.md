# Optimal Merge Pattern

| | |
|---|---|
| **ID** | `greedy_05` |
| **Category** | greedy |
| **Complexity (required)** | $O(N \log N)$ Time, $O(N)$ Space |
| **Difficulty** | 4/10 |
| **Interview relevance** | 7/10 |
| **LeetCode Equivalent** | [Minimum Cost to Connect Sticks](https://leetcode.com/problems/minimum-cost-to-connect-sticks/) |

## Problem statement

Given `N` files (or sticks, or ropes) of different sizes. You need to merge them into a single massive file.
Merging two files of size `A` and `B` incurs a computational cost of exactly `A + B`. The new merged file has a size of `A + B` and is added back to the pool of files.
Find the absolute minimum total cost required to merge all `N` files into one.

**Input:** An integer array `sizes` representing the sizes of `N` files.
**Output:** An integer representing the minimum total merge cost.

## When to use it

- Any problem asking for the "minimum cost to connect ropes/sticks/files".
- Very closely related to Huffman Coding logic.

## Approach

**1. The Cost Accumulation Insight:**
If we merge files A and B, their cost `A+B` is paid.
Later, we merge the result with C. The cost is `(A+B) + C`.
Notice that `A` and `B` were added to the total cost TWICE! `C` was added ONCE.
This means files that are merged early on will have their sizes repeatedly added to the total cost over and over again in subsequent merges.
**Greedy Choice:** To minimize the total sum, we must merge the **absolute smallest** files first, so that their tiny sizes are the ones getting repeatedly added! The largest files should be saved for the very end, so their massive sizes are only added to the total cost once.

**2. The Priority Queue (Min-Heap):**
We need a data structure that constantly gives us the 2 smallest elements, even as we create new merged elements and throw them back into the pool.
A Min-Heap is perfect for this!

**3. The Algorithm:**
1. Push all file sizes into a Min-Heap.
2. While there is more than 1 file in the heap:
   - Pop the two smallest files: `file1` and `file2`.
   - Calculate their merge cost: `cost = file1 + file2`.
   - Add this `cost` to our `total_cost` accumulator.
   - Push the new merged file `cost` back into the Min-Heap!
3. When exactly 1 file remains in the heap, we are done!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for greedy_05: Optimal Merge Pattern.

Auto-generated from challenges/algorithms/greedy.py:SPECS.
O(n log n) time.
"""


def solve(sizes, n):
    import heapq
    if n <= 1:
        return 0
    heap = list(sizes)
    heapq.heapify(heap)
    total = 0
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        merged = a + b
        total += merged
        heapq.heappush(heap, merged)
    return total
```

</details>

## Walk-through

`sizes = [4, 3, 2, 6]`.
`heap = [2, 3, 4, 6]`.
`total = 0`.

1. Pop `2`, `3`.
   `current_cost = 2 + 3 = 5`.
   `total = 0 + 5 = 5`.
   Push `5`. `heap = [4, 5, 6]`.
2. Pop `4`, `5`.
   `current_cost = 4 + 5 = 9`.
   `total = 5 + 9 = 14`.
   Push `9`. `heap = [6, 9]`.
3. Pop `6`, `9`.
   `current_cost = 6 + 9 = 15`.
   `total = 14 + 15 = 29`.
   Push `15`. `heap = [15]`.
4. Heap length is 1. Terminate.

Result `29`. ✓
*(If we merged them linearly `4+3=7`, `7+2=9`, `9+6=15`, total cost would be `7+9+15=31`. By using the optimal pattern, we saved 2 computational cycles!)*

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N \log N)$ | $O(N)$ |
| **Average** | $O(N \log N)$ | $O(N)$ |
| **Worst** | $O(N \log N)$ | $O(N)$ |

Building the initial heap takes $O(N)$ using `heapify`.
The `while` loop runs exactly N-1 times. In each iteration, we perform two `heappop`s and one `heappush`. Priority Queue operations take $O(\log N)$.
Total time complexity is strictly $O(N \log N)$.
Space complexity is $O(N)$ to store the elements in the heap. (If modifying the input array in-place, it is still logically $O(N)$ but technically $O(1)$ auxiliary space).

## Variants & optimizations

- **K-way Merge:** What if you can merge exactly K files at a time for a cost of their sum? The logic is identical, but you pop K elements at a time. *Edge case:* If you do this, you might end up with a final merge of < K elements, which is sub-optimal! You must pad the initial heap with dummy `0`-size files until (N - 1) \pmod{K - 1} == 0.

## Real-world applications

- **Database Query Planners:** When a SQL query performs a massively parallel `SORT` operation on billions of rows that cannot fit in RAM, the database splits it into thousands of small sorted chunks on the hard drive. To merge them back together, the query planner uses Optimal Merge Pattern to minimize expensive disk I/O reads.
- **Rope Splicing Algorithms:** Calculating the minimum kinetic energy required to splice fragments of carbon fiber cables in materials science.

## Related algorithms in cOde(n)

- **[greedy_03 - Huffman Coding](greedy_03_huffman-coding.md)** — The exact same logic! Huffman builds a tree where edge weights are accumulated from the bottom up by merging the two lowest frequencies.
- **[sort_04 - Merge Sort](../sorting/sort_04_merge-sort.md)** — Relies on merging sorted arrays, though Merge Sort is a top-down divide-and-conquer approach, not a greedy bottom-up approach.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
