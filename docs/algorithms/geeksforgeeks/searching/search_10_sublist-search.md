# Sublist Search

| | |
|---|---|
| **ID** | `search_10` |
| **Category** | searching |
| **Complexity (required)** | $O(N \times M)$ Time, $O(1)$ Space |
| **Difficulty** | 3/10 |
| **Interview relevance** | 4/10 |
| **GeeksForGeeks Equivalent** | [Sublist Search (Search a linked list in another list)](https://www.geeksforgeeks.org/sublist-search-search-a-linked-list-in-another-list/) |

## Problem statement

Given two Singly Linked Lists: a target `sublist`, and a main `list`.
Find whether the `sublist` is present entirely and contiguously within the main `list`.
If it exists, return `True` (or the starting node of the match). Otherwise, return `False`.

**Input:** Two head nodes `sublist` and `list`.
**Output:** A boolean.

## When to use it

- When performing string matching (like finding a substring in a text), but the data structure is a Linked List instead of a String Array.
- A classic test of multi-pointer manipulation without losing track of the original starting positions.

## Approach

**1. The Sliding Window Analogy:**
Imagine taking a transparent physical ruler (the `sublist`) and sliding it slowly across a long piece of paper (the `list`).
You place the ruler at the very beginning. You check if EVERY inch of the ruler perfectly matches the paper underneath it.
If even one inch mismatches, you pick up the ruler, shift it forward by exactly 1 position on the paper, and try matching the entire ruler again from scratch!

**2. The Pointer Strategy:**
We need three active pointers:
- `first`: Points to the node in the main list where we are currently attempting to start a match.
- `main_ptr`: Points to the specific node in the main list we are currently checking *during* a match attempt.
- `sub_ptr`: Points to the specific node in the sublist we are currently checking.

**3. The Matching Loop:**
1. Initialize `first = list.head`.
2. Enter an outer loop while `first` is not null.
3. Reset `main_ptr = first` and `sub_ptr = sublist.head`.
4. Enter an inner loop while both `main_ptr` and `sub_ptr` are not null.
   - If `main_ptr.val == sub_ptr.val`, they match! Move BOTH pointers forward.
   - If they don't match, instantly break the inner loop!
5. After the inner loop breaks, check why it broke. If `sub_ptr == null`, it means we successfully matched every single node in the sublist! Return `True`.
6. If not, the match failed. Move `first` forward by 1 node, and try again!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for search_10: Sublist Search.

Find the first index where ``sub`` appears as a contiguous run
in ``data``, or -1 if it never does. Sliding window of length
m scanned across an n-length list. O(n * m) worst case.
"""


def solve(data, sub, n, m):
    if m == 0:
        return 0
    if m > n:
        return -1
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if data[i + j] != sub[j]:
                match = False
                break
        if match:
            return i
    return -1
```

</details>

## Walk-through

`sublist = 1 -> 2 -> 3`.
`main_list = 5 -> 1 -> 2 -> 4 -> 1 -> 2 -> 3 -> 9`.

1. `first = 5`.
   - `main_ptr = 5`, `sub_ptr = 1`.
   - `5 != 1`. Inner loop breaks.
2. `first = 1` (second node).
   - `main_ptr = 1`, `sub_ptr = 1`. Match!
   - `main_ptr = 2`, `sub_ptr = 2`. Match!
   - `main_ptr = 4`, `sub_ptr = 3`. `4 != 3`. Mismatch! Inner loop breaks.
3. `first = 2`. Mismatch on first node (`2 != 1`).
4. `first = 4`. Mismatch (`4 != 1`).
5. `first = 1` (fifth node).
   - `main_ptr = 1`, `sub_ptr = 1`. Match!
   - `main_ptr = 2`, `sub_ptr = 2`. Match!
   - `main_ptr = 3`, `sub_ptr = 3`. Match!
   - Both advance. `sub_ptr` becomes `None`!
   - Inner loop condition fails (`sub_ptr is not None` is False). Break inner loop.
6. Check `sub_ptr is None`? TRUE!
Return `True`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(M)$ | $O(1)$ |
| **Average** | $O(N \times M)$ | $O(1)$ |
| **Worst** | $O(N \times M)$ | $O(1)$ |

Let N be the length of the main list, and M be the length of the sublist.
In the worst-case scenario (e.g., `main = a-a-a-a-a-a-b`, `sub = a-a-b`), the inner loop will successfully match almost all M characters before failing at the very last node, and it will do this N times. The total time complexity is $O(N \times M)$.
Space complexity is strictly $O(1)$ because we only instantiate three node pointers, regardless of list size.

## Variants & optimizations

- **KMP Algorithm (`string_06`):** The $O(N \times M)$ worst-case time is identical to brute-force substring matching. If you convert the linked lists to arrays, you can use the Knuth-Morris-Pratt algorithm to pre-compute a "Longest Prefix Suffix" (LPS) array, reducing the time complexity to a strictly linear $O(N + M)$ by skipping redundant pointer resets!

## Real-world applications

- **DNA Sequence Analysis:** Scanning a massive genome sequence (stored as a Linked List to allow rapid $O(1)$ mutations/insertions without memory reallocation) to find the existence of a specific short viral RNA sub-chain.

## Related algorithms in cOde(n)

- **[string_06 - KMP Pattern Matching](../strings/string_06_kmp-pattern-matching.md)** — The mathematically optimized $O(N+M)$ version of this exact problem applied to strings/arrays.
- **[linked_list_07 - Intersection of Two Lists](../linked_list/ll_07_intersection-two-lists.md)** — Another multi-pointer linked list traversal algorithm, but checking for physical memory intersections rather than value subsets.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
