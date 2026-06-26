# Bucket Sort

| | |
|---|---|
| **ID** | `sort_09` |
| **Category** | sorting |
| **Complexity (required)** | $O(N)$ Time, $O(N + K)$ Space |
| **Difficulty** | 4/10 |
| **Interview relevance** | 3/10 |
| **Wikipedia** | [Bucket sort](https://en.wikipedia.org/wiki/Bucket_sort) |

## Problem statement

Given an array of N floating-point numbers `arr`, where every element is uniformly distributed over a known range (e.g. `[0.0, 1.0)`).
Sort the array in strictly linear $O(N)$ average time.

**Input:** An unsorted array of floats `arr`.
**Output:** A sorted array.

## When to use it

- When the input data is known to be **uniformly distributed** (evenly spread out) across a specific range.
- The absolute best algorithm for sorting floating-point decimals between `0.0` and `1.0` where Radix and Counting sort fail because the values aren't integers.

## Approach

**1. The Pigeonhole Analogy:**
If you have 100 students with grades uniformly ranging from 0 to 100, and you want to sort them, you don't throw them all into a giant room and compare them.
You create 10 empty buckets: Bucket 1 for grades 0-9, Bucket 2 for 10-19... Bucket 10 for 90-100.
You throw the students into their respective buckets in $O(1)$ time. Because the grades are perfectly uniform, each bucket receives roughly 10 students.
You then sort each small bucket individually. Finally, you concatenate the buckets in order!

**2. The Bucket Hashing Function:**
How do we know which bucket a float belongs to?
If we create exactly N empty buckets, and the data is uniformly distributed between `0.0` and `1.0`, we multiply the value by N to get the index!
`bucket_index = int(N * arr[i])`
Example: N=10. If the value is `0.23`, it goes into bucket `int(10 * 0.23) = 2`.

**3. The Internal Sort:**
After distributing all elements into the buckets, some buckets might have 2 or 3 elements due to slight randomness.
We iterate through all N buckets, and run a standard sorting algorithm (usually **Insertion Sort**) on each bucket.
Because the buckets are incredibly small (average size ~= 1), Insertion Sort executes essentially in $O(1)$ time per bucket!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for sort_09: Bucket Sort.

Auto-generated from challenges/algorithms/sorting.py:SPECS.
O(n) time.
"""


def solve(data, n):
    if n == 0:
        return data
    min_val = min(data)
    max_val = max(data)
    span = max_val - min_val
    if span == 0:
        return data
    bucket_count = min(n, 10)
    bucket_size = span / bucket_count
    buckets = [[] for _ in range(bucket_count)]
    for value in data:
        idx = int((value - min_val) / bucket_size)
        if idx == bucket_count:
            # Float rounding: the max value can land one bucket too far.
            idx -= 1
        buckets[idx].append(value)
    for bucket in buckets:
        bucket.sort()
    index = 0
    for bucket in buckets:
        for value in bucket:
            data[index] = value
            index += 1
    return data
```

</details>

## Walk-through

`arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12]`. `N = 8`.

1. Create 8 empty buckets.
2. Distribute:
   - `0.78 * 8 = 6.24`. Bucket 6.
   - `0.17 * 8 = 1.36`. Bucket 1.
   - `0.39 * 8 = 3.12`. Bucket 3.
   - `0.26 * 8 = 2.08`. Bucket 2.
   - `0.72 * 8 = 5.76`. Bucket 5.
   - `0.94 * 8 = 7.52`. Bucket 7.
   - `0.21 * 8 = 1.68`. Bucket 1.
   - `0.12 * 8 = 0.96`. Bucket 0.
3. Buckets:
   - `B0 = [0.12]`
   - `B1 = [0.17, 0.21]` (Sorting applies! Stays `0.17, 0.21`).
   - `B2 = [0.26]`
   - `B3 = [0.39]`
   - `B4 = []`
   - `B5 = [0.72]`
   - `B6 = [0.78]`
   - `B7 = [0.94]`
4. Concatenate:
   - `[0.12, 0.17, 0.21, 0.26, 0.39, 0.72, 0.78, 0.94]`.

Result is perfectly sorted! ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(N)$ |
| **Average** | $O(N)$ | $O(N)$ |
| **Worst** | $O(N^2)$ | $O(N)$ |

Distributing N elements takes $O(N)$ time.
Concatenating N buckets takes $O(N)$ time.
The time to sort the buckets depends heavily on the data distribution. Because the data is uniform, each bucket has average length N/N = 1. Sorting an array of length 1 is $O(1)$. Total sort time is N x $O(1)$ = $O(N)$.
Therefore, the average time complexity is $O(N)$.
**WORST CASE:** If the data is terribly clumped (e.g. all 10,000 floats are clustered exactly around `0.51`), EVERY single element goes into the exact same bucket! The algorithm devolves into running an $O(N^2)$ Insertion Sort on the entire array!
Space complexity is $O(N)$ to hold the 2D array of buckets.

## Variants & optimizations

- **Generalized Range Buckets:** If the data isn't `[0.0, 1.0)` but instead ranges from `MIN` to `MAX`, the bucket hash formula is modified to: `index = floor((arr[i] - MIN) / (MAX - MIN) * (bucket_count - 1))`.
- **Top K Frequent Elements (`hash_07`):** Bucket Sort is wildly popular as an implicit Hash Map reversal! If you have the frequencies of elements, you can use the frequencies as Bucket Indices. The highest non-empty bucket instantly gives you the most frequent element in $O(N)$ time!

## Real-world applications

- **Sensor Data Analytics:** Sorting temperature, humidity, or telemetry data streams which naturally follow uniform bounds throughout the day, avoiding the $O(N \log N)$ overhead of Quicksort.

## Related algorithms in cOde(n)

- **[sort_03 - Insertion Sort](sort_03_insertion-sort.md)** — The optimal algorithm for sorting the tiny sub-arrays inside the buckets.
- **[sort_07 - Counting Sort](sort_07_counting-sort.md)** — Conceptually identical to Bucket Sort, but every Bucket is mathematically guaranteed to hold exactly one distinct Integer value.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
