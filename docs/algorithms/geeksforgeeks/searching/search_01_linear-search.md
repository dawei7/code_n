# Linear Search

| | |
|---|---|
| **ID** | `search_01` |
| **Category** | searching |
| **Complexity (required)** | $O(N)$ Time, $O(1)$ Space |
| **Difficulty** | 1/10 |
| **Interview relevance** | 1/10 |
| **Wikipedia** | [Linear search](https://en.wikipedia.org/wiki/Linear_search) |

## Problem statement

Given an array `arr` of `N` elements and a `target` value.
Find the index of the `target` in the array. If the `target` is not present, return `-1`.

**Input:** An array `arr` and a `target` value.
**Output:** An integer representing the index of the target.

## When to use it

- When the array is completely unsorted and no other data structures (like Hash Maps) are available or allowed.
- As a baseline brute-force solution to prove why a more complex algorithm (like Binary Search) is necessary.

## Approach

**1. The "Check Everything" Philosophy:**
If you lose your keys in a messy room, you have to physically check every single spot until you find them.
Because the array is completely unsorted, there is no mathematical shortcut to guess where the `target` might be.
The element could be at the very first index, or the very last index.
Therefore, we must iterate through the entire array from index `0` to index `N-1`.

**2. The Exit Condition:**
At each step, we compare `arr[i]` with the `target`.
If they match, we immediately return the index `i`.
If the loop finishes checking every single element and we never returned, we know for a fact the element does not exist. We return `-1`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for search_01: Linear Search.

Walk the array until the target is found or the end is reached.
O(n) time.
"""


def solve(data, target):
    for index in range(len(data)):
        if data[index] == target:
            return index
    return -1
```

</details>

## Walk-through

`arr = [10, 50, 30, 70, 80, 60, 20, 90, 40]`, `target = 20`.

1. `i = 0`: `arr[0] = 10`. `10 == 20`? False.
2. `i = 1`: `arr[1] = 50`. `50 == 20`? False.
3. `i = 2`: `arr[2] = 30`. `30 == 20`? False.
4. `i = 3`: `arr[3] = 70`. `70 == 20`? False.
5. `i = 4`: `arr[4] = 80`. `80 == 20`? False.
6. `i = 5`: `arr[5] = 60`. `60 == 20`? False.
7. `i = 6`: `arr[6] = 20`. `20 == 20`? TRUE!
   - Return `6`.

Result: `6`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(1)$ |
| **Average** | $O(N)$ | $O(1)$ |
| **Worst** | $O(N)$ | $O(1)$ |

The best-case scenario is that the target is the very first element in the array, returning immediately in $O(1)$ time.
The worst-case scenario is that the target is the very last element, or doesn't exist at all, forcing us to check all N elements in $O(N)$ time.
Space complexity is $O(1)$ because we only use a single integer variable `i` for the loop counter.

## Variants & optimizations

- **Transposition Optimization:** If you expect certain elements to be searched for multiple times (like a caching system), when you find the `target` at index `i`, you swap it with the element at `i-1` before returning! Over many searches, frequently accessed elements will naturally "bubble up" to the front of the array, turning their future search times closer to $O(1)$.
- **Move-to-Front Optimization:** Similar to Transposition, but instead of swapping with `i-1`, you instantly swap the found `target` all the way to index `0`!

## Real-world applications

- **Linked List Searching:** Linear search is the ONLY way to search through a Linked List, because Linked Lists do not support random access indexing, rendering algorithms like Binary Search impossible.

## Related algorithms in cOde(n)

- **[search_02 - Binary Search](search_02_binary-search.md)** — The $O(\log N)$ alternative that completely obsoletes Linear Search, but strictly requires the array to be sorted first.
- **[hash_01 - Two Sum](../hashing/hash_01_two-sum.md)** — Uses a Hash Map to reduce a nested $O(N^2)$ double linear search down to $O(N)$.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
