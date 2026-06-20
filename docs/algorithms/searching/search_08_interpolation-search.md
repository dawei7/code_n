# Interpolation Search

| | |
|---|---|
| **ID** | `search_08` |
| **Category** | searching |
| **Complexity (required)** | $O(\log(\log N)$) Time, $O(1)$ Space |
| **Difficulty** | 4/10 |
| **Interview relevance** | 2/10 |
| **Wikipedia** | [Interpolation search](https://en.wikipedia.org/wiki/Interpolation_search) |

## Problem statement

Given a sorted array `arr` and a `target` value.
Find the index of the `target` in the array. If the `target` is not present, return `-1`.
Optimize the search for scenarios where the elements are uniformly distributed (e.g., `10, 20, 30, 40, 50`).

**Input:** A sorted array `arr` and a `target` value.
**Output:** An integer representing the index.

## When to use it

- When searching through a physical phone book.
- When the data is massive and strictly uniformly distributed. If the data is clumped or exponential (e.g. `1, 2, 4, 100, 10000`), this algorithm degrades severely.

## Approach

**1. The Phone Book Analogy:**
If you want to find "Zebra" in a dictionary, do you open it exactly in the middle? (Binary Search).
NO! You know that "Z" is at the very end of the alphabet, so you instinctively open the dictionary 95% of the way to the back!
If you want to find "Apple", you open it 5% of the way to the front.
Interpolation Search mimics human intuition. It guesses the probable location of the target based on its value relative to the min and max values of the array.

**2. The Interpolation Formula:**
In standard Binary Search, the midpoint is always:
mid = left + \frac{1}{2} \cdot (right - left)

In Interpolation Search, we replace the fixed \frac{1}{2} fraction with a dynamic ratio!
Ratio = \frac{\text{target} - arr[left]}{arr[right] - arr[left]}
If the array goes from 0 to 100, and the target is 80, the ratio is \frac{80-0}{100-0} = 0.8.
We then multiply this ratio by the index range to find our exact "Probe" position:
probe = left + \lfloor Ratio \cdot (right - left) \rfloor

**3. The Elimination Logic:**
Exactly like Binary Search!
- If `arr[probe] == target`: Return `probe`.
- If `arr[probe] < target`: `left = probe + 1`.
- If `arr[probe] > target`: `right = probe - 1`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for search_08: Interpolation Search.

Auto-generated from challenges/algorithms/searching.py:SPECS.
O(n) time.
"""


def solve(data, target, n):
    low, high = 0, n - 1
    while low <= high and data[low] <= target <= data[high]:
        if data[high] == data[low]:
            if data[low] == target:
                return low
            return -1
        # Probe position estimated from the target's value.
        pos = low + (target - data[low]) * (high - low) // (data[high] - data[low])
        if pos < low or pos > high:
            return -1
        value = data[pos]
        if value == target:
            return pos
        if value < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1
```

</details>

## Walk-through

`arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]`. `target = 80`. Length 10.

1. `left = 0` (val 10), `right = 9` (val 100).
   - Ratio = \frac{80 - 10}{100 - 10} = \frac{70}{90} = 0.777.
   - probe = 0 + \lfloor 0.777 x 9 \rfloor = \lfloor 7.0 \rfloor = 7.
   - Check `arr[7]`: It is `80`!
   - `80 == 80`! Match found!

Result: `7`. ✓
*(Binary Search would have taken 3 iterations to find it: mid=4, mid=7. Interpolation Search found it instantly in exactly 1 iteration by correctly guessing its mathematical location!)*

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(1)$ |
| **Average** | $O(\log(\log N)$) | $O(1)$ |
| **Worst** | $O(N)$ | $O(1)$ |

If the data is perfectly uniformly distributed, the probe lands incredibly close to the target every time, shrinking the search space exponentially faster than Binary Search. The average time complexity is $O(log(log N)$).
For a 4-billion element array (N = 2^{32}), Binary Search takes 32 operations. Interpolation Search takes ~= log_2(32) = 5 operations!
However, if the data is exponential (e.g. `[1, 2, 4, 8, 16, 1000]`) and the target is `15`, the probe calculation will repeatedly guess index 0, forcing the algorithm to creep forward exactly 1 index at a time, degrading completely into an $O(N)$ Linear Search!
Space complexity is $O(1)$.

## Variants & optimizations

- **Robust Interpolation Search:** A hybrid algorithm that uses the Interpolation formula to guess the probe, but then forces the search window to shrink by at least a guaranteed chunk size C (similar to Jump Search). If the data is clumpy, it gracefully falls back to $O(\log N)$ instead of degrading to $O(N)$.

## Real-world applications

- **Database Primary Keys:** Since Auto-Incrementing Primary Keys in SQL databases (`1, 2, 3...`) form a perfectly uniform arithmetic progression, Interpolation Search allows the database engine to jump instantly to the exact disk block containing the required row in $O(1)$ time, skipping the B-Tree traversal entirely!

## Related algorithms in cOde(n)

- **[search_02 - Binary Search](search_02_binary-search.md)** — The mathematically safer, universally applicable search algorithm that doesn't care about data distribution.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
