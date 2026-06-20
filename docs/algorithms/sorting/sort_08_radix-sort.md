# Radix Sort

| | |
|---|---|
| **ID** | `sort_08` |
| **Category** | sorting |
| **Complexity (required)** | $O(D \times (N + K)$) Time, $O(N + K)$ Space |
| **Difficulty** | 5/10 |
| **Interview relevance** | 4/10 |
| **Wikipedia** | [Radix sort](https://en.wikipedia.org/wiki/Radix_sort) |

## Problem statement

Given an array of integers `arr`, sort the array in ascending order.
You must sort the array in linear $O(N)$ time, breaking the $O(N \log N)$ mathematical barrier of comparison-based sorting algorithms.

**Input:** An unsorted array of integers `arr`.
**Output:** A sorted array.

## When to use it

- When sorting integers, strings, or fixed-length sequences where the maximum number of digits/characters (D) is relatively small.
- To completely bypass the $O(N \log N)$ limit of algorithms like Merge Sort and Quick Sort.

## Approach

**1. The Flaw of Counting Sort (`sort_07`):**
Counting Sort achieves $O(N)$ time, but it requires allocating an array of size equal to the MAXIMUM value in the array. If you have just two elements `[1, 999999999]`, Counting Sort crashes the memory by trying to allocate an array of size 1 Billion!

**2. The Digit-by-Digit Strategy (Radix):**
Instead of sorting the entire number at once, what if we sort the numbers *one digit at a time*?
First, we sort all the numbers purely based on their 1s place (Least Significant Digit).
Then, we sort them based on their 10s place.
Then the 100s place... up to the maximum number of digits!
After the final pass, the array is magically completely sorted!

**3. The Stable Sort Requirement:**
For this magic trick to work, the underlying digit-sorting algorithm MUST be a "Stable Sort".
(If two numbers have the same 10s digit, e.g., 52 and 58, the sorting algorithm MUST preserve their relative order from the previous 1s place pass. If it scrambles them, the algorithm fails).
We use **Counting Sort** as the underlying subroutine! But because we are only sorting a single base-10 digit at a time, the Counting Sort array only ever needs to be size `10`! Memory crash avoided!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for sort_08: Radix Sort.

Auto-generated from challenges/algorithms/sorting.py:SPECS.
O(n) time.
"""


def solve(data, n):
    if n == 0:
        return data
    max_val = max(data)
    exp = 1
    while max_val // exp > 0:
        # Counting sort on the current digit.
        counts = [0] * 10
        for value in data:
            counts[(value // exp) % 10] += 1
        # Turn counts into a stable-position table.
        for i in range(1, 10):
            counts[i] += counts[i - 1]
        # Walk the input right-to-left so the sort stays stable.
        output = [0] * n
        for i in range(n - 1, -1, -1):
            digit = (data[i] // exp) % 10
            counts[digit] -= 1
            output[counts[digit]] = data[i]
        # Copy the per-digit sorted output back into data.
        for i in range(n):
            data[i] = output[i]
        exp *= 10
    return data
```

</details>

## Walk-through

`arr = [170, 45, 75, 90, 802, 24, 2, 66]`.
Maximum value is `802` (3 digits). We will do 3 passes (`exp=1`, `exp=10`, `exp=100`).

1. **`exp = 1` (1s place):**
   - Extract digits: `0, 5, 5, 0, 2, 4, 2, 6`.
   - Counting sort places them:
   - `[170, 90, 802, 2, 24, 45, 75, 66]`.
2. **`exp = 10` (10s place):**
   - Extract digits: `7, 9, 0, 0, 2, 4, 7, 6`.
   - Counting sort strictly maintains relative stability! (e.g. `802` stays before `2` because they both have a 10s digit of `0`).
   - `[802, 2, 24, 45, 66, 170, 75, 90]`.
3. **`exp = 100` (100s place):**
   - Extract digits: `8, 0, 0, 0, 0, 1, 0, 0`.
   - Counting sort applies.
   - `[2, 24, 45, 66, 75, 90, 170, 802]`.

Array is sorted! ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(D \times (N + K)$) | $O(N + K)$ |
| **Average** | $O(D \times (N + K)$) | $O(N + K)$ |
| **Worst** | $O(D \times (N + K)$) | $O(N + K)$ |

Let N be the number of elements. Let K be the base of the number system (10 for decimal digits). Let D be the maximum number of digits.
Counting Sort takes $O(N + K)$ time.
Radix Sort calls Counting Sort exactly D times.
Therefore, the time complexity is strictly $O(D x (N + K)$).
If D is a small constant (e.g. 64-bit integers have max 20 decimal digits), the time complexity drops perfectly to $O(N)$ linear time!
Space complexity is $O(N + K)$ to hold the `output` array and the base-10 `count` array.

## Variants & optimizations

- **Base 256 (Bitwise Radix):** Instead of using base-10 digits, modern systems optimize Radix Sort by using Base-256 (a single 8-bit byte). By using bitwise shifts `(arr[i] >> (pass * 8)) & 0xFF` instead of modulo arithmetic `(arr[i] // exp) % 10`, the CPU executes the algorithm orders of magnitude faster. A 32-bit integer is sorted in exactly 4 passes!
- **MSD Radix Sort (Most Significant Digit):** The version written above is LSD (Least Significant Digit). MSD Radix Sort starts from the highest digit and recursively divides the array into "buckets", which is highly optimal for sorting alphabetical strings!

## Real-world applications

- **String/Suffix Array Sorting:** Radix sort is the fastest algorithm in the world for sorting arrays of fixed-length Strings (like IP addresses, UUIDs, or DNA sequences), treating each character as a "digit".

## Related algorithms in cOde(n)

- **[sort_07 - Counting Sort](sort_07_counting-sort.md)** — The engine that powers the digit-by-digit sorting passes.
- **[sort_09 - Bucket Sort](sort_09_bucket-sort.md)** — Another non-comparison integer sorting algorithm that distributes items into uniform ranges.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
