# Count Inversions

| | |
|---|---|
| **ID** | `dc_08` |
| **Category** | divide_conquer |
| **Complexity (required)** | $O(N \log N)$ Time, $O(N)$ Space |
| **Difficulty** | 6/10 |
| **Interview relevance** | 7/10 |
| **GeeksForGeeks Equivalent** | [Count Inversions in an array](https://www.geeksforgeeks.org/inversion-count-in-array-using-merge-sort/) |

## Problem statement

Given an array of integers, find the Inversion Count in the array.
Two elements `a[i]` and `a[j]` form an inversion if `a[i] > a[j]` and `i < j`.
In simpler terms, it measures how far (or close) the array is from being fully sorted. If the array is already sorted, the inversion count is 0. If the array is sorted in reverse order, the inversion count is the maximum possible.

**Input:** An integer array `arr`.
**Output:** An integer representing the total number of inversions.

## When to use it

- To test your deep understanding of **Merge Sort**.
- When you need to quantify the "unsortedness" or calculate the Kendall rank correlation coefficient of a dataset.

## Approach

**1. The Flaw of $O(N^2)$ Checks:**
The naive approach is to use two nested `for` loops. For every element `i`, check all elements `j` to its right. If `arr[i] > arr[j]`, increment a counter. This takes $O(N^2)$ time.

**2. Piggybacking on Merge Sort:**
An inversion occurs when a larger element appears *before* a smaller element.
What algorithm is explicitly designed to find elements out of order and physically swap them until they are in order? Merge Sort!
We can use a standard Merge Sort, and simply add a counter inside the `merge` function!

**3. The Magic Counting Step:**
During the `merge` step, we have a `left_half` array and a `right_half` array. Both halves are internally sorted.
We use two pointers, `i` for `left_half` and `j` for `right_half`.
- If `left_half[i] <= right_half[j]`: They are in the correct order. No inversion!
- If `left_half[i] > right_half[j]`: We found an inversion! Wait, we didn't just find ONE inversion... we found a massive batch of them!
  Because `left_half` is strictly sorted, if `left_half[i]` is strictly greater than `right_half[j]`, then EVERY SINGLE ELEMENT to the right of `i` in the `left_half` MUST ALSO be greater than `right_half[j]`!
  Therefore, we instantly found `len(left_half) - i` inversions! We add this directly to our total counter.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dc_08: Count Inversions.

Count the number of inversions in an array of n
"""


def solve(arr, n):
    """Count inversions via merge sort."""
    if n <= 1:
        return 0
    work = list(arr)

    def sort_count(lo, hi):
        if lo >= hi:
            return 0
        mid = (lo + hi) // 2
        count = sort_count(lo, mid) + sort_count(mid + 1, hi)
        left = work[lo:mid + 1]
        right = work[mid + 1:hi + 1]
        i = j = 0
        k = lo
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                work[k] = left[i]
                i += 1
            else:
                work[k] = right[j]
                count += len(left) - i
                j += 1
            k += 1
        while i < len(left):
            work[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            work[k] = right[j]
            j += 1
            k += 1
        return count

    return sort_count(0, n - 1)
```

</details>

## Walk-through

`arr = [2, 4, 1, 3]`.

1. Split into `[2, 4]` and `[1, 3]`.
2. **Left Half `[2, 4]`:**
   - Split to `[2]` and `[4]`.
   - Merge `[2]` and `[4]`:
     - `2 <= 4`. Add 2.
     - Add 4. `split_inv = 0`. Returns `[2, 4]`, inv=0.
3. **Right Half `[1, 3]`:**
   - Split to `[1]` and `[3]`.
   - Merge `[1]` and `[3]`:
     - `1 <= 3`. Add 1.
     - Add 3. `split_inv = 0`. Returns `[1, 3]`, inv=0.
4. **Global Merge `[2, 4]` and `[1, 3]`:**
   - `i=0` (val 2), `j=0` (val 1).
   - `2 > 1`! INVERSION!
   - `split_inv += (len(left) - i)` -> `split_inv += (2 - 0)` -> `2` inversions found! (Both 2 and 4 are > 1).
   - Add 1. `j` becomes 1.
   - `i=0` (val 2), `j=1` (val 3).
   - `2 <= 3`. Add 2. `i` becomes 1.
   - `i=1` (val 4), `j=1` (val 3).
   - `4 > 3`! INVERSION!
   - `split_inv += (len(left) - i)` -> `split_inv += (2 - 1)` -> `1` inversion found! (4 > 3).
   - Add 3. `j` becomes 2.
   - `j` exhausted. Add remaining `[4]`.
   - Total `split_inv = 3`.

Result `total_inversions = 0 + 0 + 3 = 3`. ✓
*(The 3 inversions are (2,1), (4,1), (4,3))*.

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N \log N)$ | $O(N)$ |
| **Average** | $O(N \log N)$ | $O(N)$ |
| **Worst** | $O(N \log N)$ | $O(N)$ |

Because we are literally just executing a standard Merge Sort, the time complexity is strictly bounded to $O(N \log N)$ in all cases.
Space complexity is $O(N)$ because the merge arrays create temporary copies at each level.

## Variants & optimizations

- **Fenwick Tree / Binary Indexed Tree (BIT):** You can also solve this iteratively using a Fenwick Tree in $O(N \log N)$ time. You iterate through the array from right to left. For each element, you query the Fenwick tree to see how many elements you've *already processed* that are strictly smaller than the current element. Then you insert the current element into the Fenwick tree. This is extremely elegant and requires $O(\text{Max\_Value})$ space or coordinate compression.
- **Reverse Pairs (LeetCode 493):** A harder variant where an inversion is defined as `nums[i] > 2 * nums[j]`. You can STILL use Merge Sort! You just have to do a quick $O(N)$ counting loop *before* you execute the standard merge pointer logic.

## Real-world applications

- **Collaborative Filtering / Recommendation Systems:** Calculating the Kendall tau distance between two users' ranked preference lists. If User A ranks 5 movies, and User B ranks them differently, the number of inversions directly quantifies how dissimilar their tastes are!

## Related algorithms in cOde(n)

- **[sort_01 - Merge Sort](../sorting/sort_01_merge-sort.md)** — The pure sorting algorithm without the internal counters.
- **[fenwick_01 - Binary Indexed Tree](../fenwick/fenwick_01_binary-indexed-tree.md)** — The alternative data structure capable of solving inversion counting.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
