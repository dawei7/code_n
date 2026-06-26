# Ternary Search

| | |
|---|---|
| **ID** | `search_05` |
| **Category** | searching |
| **Complexity (required)** | $O(\log_3 N)$ Time, $O(1)$ Space |
| **Difficulty** | 4/10 |
| **Interview relevance** | 2/10 |
| **Wikipedia** | [Ternary search](https://en.wikipedia.org/wiki/Ternary_search) |

## Problem statement

Given a sorted array `arr` and a `target` value.
Find the index of the `target` in the array. If the `target` is not present, return `-1`.
Unlike Binary Search which splits the array into 2 halves, you must split the array into 3 sections.

**Input:** A sorted array `arr` and a `target` value.
**Output:** An integer representing the index.

## When to use it

- To search for a specific value in a sorted array (though it is practically inferior to Binary Search).
- **Primary Use Case:** Finding the exact maximum or minimum value of a Unimodal Mathematical Function f(x) (a continuous curve that strictly increases to a peak and then strictly decreases, like a parabola).

## Approach

**1. The Three Sections:**
Binary search uses one `mid` pointer to split the array into two halves.
Ternary search uses TWO mid pointers (`mid1` and `mid2`) to split the array into three perfectly equal thirds.
- `mid1 = left + (right - left) / 3`
- `mid2 = right - (right - left) / 3`

**2. The Elimination Logic (Array Search):**
We compare the `target` against both `mid1` and `mid2`.
- If `target == arr[mid1]`, return `mid1`.
- If `target == arr[mid2]`, return `mid2`.
- If `target < arr[mid1]`: The target MUST be in the First Third. `right = mid1 - 1`.
- If `target > arr[mid2]`: The target MUST be in the Last Third. `left = mid2 + 1`.
- Otherwise, the target MUST be trapped in the Middle Third! `left = mid1 + 1` and `right = mid2 - 1`.

**3. The Elimination Logic (Unimodal Peak Finding):**
If evaluating a parabola f(x) to find its highest peak:
- If f(\text{mid1}) < f(\text{mid2}): The peak MUST be to the right of `mid1`. We discard the entire First Third! `left = mid1`.
- If f(\text{mid1}) > f(\text{mid2}): The peak MUST be to the left of `mid2`. We discard the entire Last Third! `right = mid2`.
We repeat this until `left` and `right` converge on the exact peak!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for search_05: Ternary Search.

Auto-generated from challenges/algorithms/searching.py:SPECS.
O(log n) time.
"""


def solve(data, target, n):
    low, high = 0, n - 1
    while low <= high:
        third = (high - low) // 3
        mid1 = low + third
        mid2 = high - third
        if data[mid1] == target:
            return mid1
        if data[mid2] == target:
            return mid2
        if target < data[mid1]:
            high = mid1 - 1
        elif target > data[mid2]:
            low = mid2 + 1
        else:
            low = mid1 + 1
            high = mid2 - 1
    return -1
```

</details>

## Walk-through

`arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, `target = 7`.

1. `left = 0`, `right = 9`.
   - `mid1 = 0 + 9//3 = 3`. `arr[3] = 4`.
   - `mid2 = 9 - 9//3 = 6`. `arr[6] = 7`.
   - `arr[mid2] == 7`! Match found!
   - Return `mid2 = 6`.

Result: `6`. ✓

*What if `target = 5`?*
1. `left=0`, `right=9`, `mid1=3 (val=4)`, `mid2=6 (val=7)`.
   - `5` is not 4 or 7.
   - `5 < 4`? False.
   - `5 > 7`? False.
   - It's in the middle! `left = 4`, `right = 5`.
2. `left=4`, `right=5`.
   - `mid1 = 4 + 1//3 = 4`. `arr[4] = 5`.
   - `arr[mid1] == 5`! Match found.
   - Return `mid1 = 4`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(1)$ |
| **Average** | $O(\log_3 N)$ | $O(1)$ |
| **Worst** | $O(\log_3 N)$ | $O(1)$ |

The search space is reduced by a factor of 3 at each step. Thus, the time complexity is $O(log_3 N)$.
**Wait, isn't log_3 N smaller than log_2 N? Shouldn't Ternary Search be faster than Binary Search?**
NO! While Ternary Search requires fewer *iterations*, it requires doing TWO comparisons per iteration instead of just one!
Mathematically, the number of comparisons for Binary Search is ~= 1 x log_2 N.
The number of comparisons for Ternary Search is ~= 2 x log_3 N.
By the change-of-base formula, 2 log_3 N = 2 \frac{log_2 N}{log_2 3} ~= 1.26 log_2 N.
Therefore, Ternary Search makes 26% MORE comparisons than Binary Search! It is strictly inferior for standard array searching.
Space complexity is $O(1)$.

## Variants & optimizations

- **Golden-Section Search:** An optimization over Ternary Search for finding Unimodal peaks. Instead of calculating two new midpoints every single iteration, the Golden-Section ratio (\phi ~= 1.618) is used so that one of the previous midpoints can be perfectly reused in the next iteration, reducing function evaluations by 50%!

## Real-world applications

- **Machine Learning (Hyperparameter Tuning):** Finding the optimal learning rate that minimizes the Loss Function curve. If the loss function is known to be convex (unimodal), Ternary Search can perfectly locate the mathematical minimum without using computationally expensive Calculus derivatives (Gradient Descent).

## Related algorithms in cOde(n)

- **[search_02 - Binary Search](search_02_binary-search.md)** — The standard, practically superior $O(log_2 N)$ search algorithm.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
