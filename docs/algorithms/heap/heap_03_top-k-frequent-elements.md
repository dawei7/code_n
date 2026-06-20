# Top K Frequent Elements

| | |
|---|---|
| **ID** | `heap_03` |
| **Category** | heap |
| **Complexity (required)** | $O(N log K)$ or $O(N)$ |
| **Difficulty** | 5/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) |

## Problem statement

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.
Your algorithm's time complexity must be strictly better than $O(N \log N)$.

**Input:** An array of integers `nums`, and an integer `k`.
**Output:** A list of `k` integers representing the most frequent elements.

## When to use it

- Another massively popular FAANG interview question.
- Tests your ability to chain a Hash Map frequency counter directly into a Priority Queue or Bucket Sort algorithm.

## Approach

**Approach 1: The Min-Heap VIP Club ($O(N log K)$)**
This is exactly the same logic as `heap_02`!
1. Iterate over the array and count frequencies using a Hash Map (`O(N)`).
2. Iterate over the distinct `(frequency, number)` pairs in the map.
3. Push them into a Min-Heap of size K. We configure the heap to sort by `frequency`!
4. If the heap size exceeds K, pop the element with the smallest frequency.
5. Extract the K elements remaining in the heap.

**Approach 2: Bucket Sort ($O(N)$)**
Since the absolute maximum frequency any number could possibly have is exactly N (if the array is entirely the same number), we can use a bounded array as buckets!
1. Build the Hash Map of frequencies (`O(N)`).
2. Create an array of empty lists (buckets) of size N + 1.
3. For every `(frequency, number)` in the map, append the `number` to the list at `bucket[frequency]`.
4. Iterate backwards from the maximum bucket index N down to 1. Gather numbers until you have exactly K elements!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for heap_03: Top K Frequent Elements.

Count occurrences with a hash map, then push (count, value) into
a max-heap. Pop the top k. The output is sorted in DESCENDING
order of frequency; ties broken by value in DESCENDING order so
the verify can do a plain equality check.
"""


def solve(data, n, k):
    import heapq
    if k <= 0 or n == 0:
        return []
    counts = {}
    for value in data:
        counts[value] = counts.get(value, 0) + 1
    # Max-heap via (-count, -value). Inverting both ensures ties
    # are broken by DESCENDING value (the smaller -v comes first).
    heap = [(-c, -v) for v, c in counts.items()]
    heapq.heapify(heap)
    out = []
    for _ in range(min(k, len(heap))):
        neg_c, neg_v = heapq.heappop(heap)
        out.append(-neg_v)
    return out
```

</details>

## Walk-through

`nums = [1, 1, 1, 2, 2, 3]`, `k = 2`.

**Bucket Sort Execution:**
1. `freq_map`: `{1: 3, 2: 2, 3: 1}`.
2. `buckets` initialization: `[[], [], [], [], [], [], []]` (size 7).
3. Populate:
   - Num 1 has freq 3: `buckets[3].append(1)`.
   - Num 2 has freq 2: `buckets[2].append(2)`.
   - Num 3 has freq 1: `buckets[1].append(3)`.
   - `buckets = [[], [3], [2], [1], [], [], []]`.
4. Iterate Backwards:
   - `i = 6`: empty.
   - `i = 5`: empty.
   - `i = 4`: empty.
   - `i = 3`: Contains `[1]`. `result = [1]`. Length is 1 \neq 2.
   - `i = 2`: Contains `[2]`. `result = [1, 2]`. Length is 2 == K. Return!

Final output: `[1, 2]`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ Bucket Sort | $O(N)$ |
| **Average** | $O(N)$ Bucket Sort | $O(N)$ |
| **Worst** | $O(N log K)$ Heap | $O(N)$ |

The Heap approach is bounded by $O(N log K)$ if all elements are distinct and K is close to N.
The Bucket Sort approach completely avoids logarithmic operations, iterating exactly bounded arrays taking strictly $O(N)$ time!
Both algorithms take $O(N)$ space (the heap approach for the hash map, the bucket sort for the nested lists).

## Variants & optimizations

- **Trie / Suffix Tree:** If the elements were massive strings instead of integers, calculating the Hash Map might become the bottleneck due to heavy string hashing. A Trie can be used to count string occurrences natively.
- **MapReduce:** In Big Data (e.g. counting words across petabytes of text logs), this algorithm is split into parallel "Map" workers that produce local frequencies, and "Reduce" workers that merge them and keep a rolling Top-K heap.

## Real-world applications

- **E-commerce:** Generating the "Top 10 Best Selling Items this Hour" widget on a high-traffic homepage.
- **Cybersecurity:** Detecting DDoS attacks by finding the IP addresses with the highest request frequencies in the firewall logs.

## Related algorithms in cOde(n)

- **[heap_02 - Kth Largest Element](heap_02_kth-largest-element.md)** — The foundation of the Min-Heap size K trick.
- **[sort_06 - Radix/Bucket Sort](../sorting/sort_06_radix-sort.md)** — The theory underlying the $O(N)$ array-index-as-frequency optimization.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
