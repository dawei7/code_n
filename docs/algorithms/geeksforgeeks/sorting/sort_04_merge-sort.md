# Merge Sort

| | |
|---|---|
| **ID** | `sort_04` |
| **Category** | sorting |
| **Complexity (required)** | $O(n log n)$ |
| **Difficulty** | 5/10 |
| **Interview relevance** | 9/10 |
| **Wikipedia** | [Merge sort](https://en.wikipedia.org/wiki/Merge_sort) |

## Problem statement

Given an array of integers `arr`, sort the array in ascending order using the Merge Sort algorithm.

**Input:** An unsorted array of integers `arr`.
**Output:** The array sorted in strictly ascending order.

**Example:**
| Input `arr` | Output |
|---|---|
| `[38, 27, 43, 3, 9, 82, 10]` | `[3, 9, 10, 27, 38, 43, 82]` |

## When to use it

- When you need a guaranteed $O(n log n)$ sorting algorithm that is **stable** (it preserves the relative order of equal elements).
- When sorting massive datasets that do not fit into RAM. Merge Sort is the foundation of **External Sorting**, allowing chunks of data to be read from a hard drive, sorted, and cleanly merged back to disk.
- When sorting Linked Lists. Because Merge Sort traverses sequentially and doesn't require random access (like Heap Sort or Quick Sort), it sorts Linked Lists optimally in $O(n log n)$ time and strictly $O(1)$ auxiliary space!

## Approach

Merge Sort is the textbook example of a **Divide and Conquer** algorithm.

1. **Divide:** Cut the array in half recursively until every sub-array has exactly 1 element. An array of length 1 is mathematically already sorted!
2. **Conquer (Merge):** Take two adjacent sorted sub-arrays and merge them into a single, larger sorted array. We do this by maintaining two pointers at the start of both sub-arrays, repeatedly picking the smaller of the two elements and placing it into a temporary array.
3. Repeat the merge process up the recursive tree until the entire array is stitched back together.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for sort_04: Merge Sort.

Divide the array in half, sort each half recursively, then merge
the two sorted halves. O(n log n) time, O(n) extra space.
"""


def solve(data, n):
    def merge_sort(items):
        if len(items) <= 1:
            return items
        mid = len(items) // 2
        left = merge_sort(items[:mid])
        right = merge_sort(items[mid:])
        return _merge(left, right)

    def _merge(left, right):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    sorted_items = merge_sort(data)
    # Copy back into the player's list so the in-place contract
    # is satisfied. Each `data[i] = value` counts as one write
    # in the AST op count.
    for i, value in enumerate(sorted_items):
        data[i] = value
    return data
```

</details>

## Walk-through

Let `arr = [38, 27, 43, 3]`.

**1. Divide Phase (Recursion going down)**
- `[38, 27, 43, 3]` is split into `[38, 27]` and `[43, 3]`.
- `[38, 27]` is split into `[38]` and `[27]`.
- `[43, 3]` is split into `[43]` and `[3]`.

**2. Conquer Phase (Merging coming up)**
- Merge `[38]` and `[27]`. Compare 38 and 27. 27 is smaller. Array becomes `[27, 38]`.
- Merge `[43]` and `[3]`. Compare 43 and 3. 3 is smaller. Array becomes `[3, 43]`.
- Merge `[27, 38]` and `[3, 43]`:
  - Pointers at `27` and `3`. `3` is smaller. Push `3`.
  - Pointers at `27` and `43`. `27` is smaller. Push `27`.
  - Pointers at `38` and `43`. `38` is smaller. Push `38`.
  - Left array empty. Push remaining right element `43`.
- Final array: `[3, 27, 38, 43]`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(n log n)$ | $O(n)$ |
| **Average** | $O(n log n)$ | $O(n)$ |
| **Worst** | $O(n log n)$ | $O(n)$ |

The array is repeatedly halved, resulting in a recursion tree of depth `log n`. At each level of the tree, merging the arrays requires touching all `n` elements exactly once ($O(n)$). Thus, the time complexity is strictly `O(n) * O(log n) = O(n log n)`. 
Unlike Quicksort or Heapsort, Merge Sort requires allocating a temporary array during the merge phase to hold the sorted elements. This results in an $O(n)$ auxiliary space complexity. 

## Variants & optimizations

- **Bottom-Up Merge Sort:** Instead of recursive division, treat the array as `n` sub-arrays of size 1. Loop through the array, merging pairs into size 2, then size 4, then size 8, etc. This eliminates the recursion call stack overhead entirely.
- **In-Place Merge Sort:** A highly complex variant that manages to merge arrays in $O(1)$ space, usually by leveraging block-swapping (like the *WikiSort* algorithm). The constant time overhead is massive, making it impractical.

## Real-world applications

- **External Sorting / Databases:** When a Postgres database needs to `ORDER BY` a table that is 500GB in size, it cannot fit it into 16GB of RAM. It streams chunks into RAM, sorts them, writes them as "runs" to the disk, and then sequentially reads and *merges* the runs together back onto the disk.
- **Timsort Backbone:** The standard sort for Python and Java is essentially an optimized bottom-up Merge Sort!

## Related algorithms in cOde(n)

- **[sort_05 - Quick Sort](sort_05_quick-sort.md)** — The other famous $O(n log n)$ divide-and-conquer algorithm.
- **[sort_13 - Timsort](sort_13_tim-sort-simplified.md)** — The modern production algorithm heavily derived from Merge Sort.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
