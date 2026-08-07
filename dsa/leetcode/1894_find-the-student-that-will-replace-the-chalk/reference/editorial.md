[TOC]

## Solution

---

### Approach 1: Prefix Sum

#### Intuition

In this problem, we have an array `chalk` of `n` elements representing the number of chalks used by each student, and an integer `k` indicating the total number of chalks available. The brute force approach would involve repeatedly subtracting the number of chalks from `k` until it reaches zero, cycling through the array if necessary. Given that `k` can be as large as 1,000,000,000, this approach is impractical.

To optimize, observe that the total number of chalks used in one complete cycle through the array is given by `sum`, the sum of all elements in `chalk`. If `k` is less than `sum`, we will reach zero within the first cycle. If `k` is greater than `sum`, after the first cycle, `k` will be reduced to $k - sum$, and after subsequent cycles, it will be reduced further. This process continues until `k` becomes less than `sum`, which is equivalent to computing `k % sum`.
> This is because `k` reduced by multiples of `sum` will eventually be less than `sum`, and this final value is equivalent to `k % sum`.

We then need to find the first index in the `chalk` array where the remaining `k % sum` becomes negative. We do this by maintaining a running prefix sum of `chalk` elements and iterating through the array to find the index where the prefix sum exceeds `k % sum`.

#### Algorithm

1. Initialize an integer variable `sum` to 0.
2. Iterate over the chalk array from 0 to $\text{chalk.size}() - 1$:
- Add the value at the current index `i` to `sum`.
- If at any point `sum` exceeds `k`, exit the loop.
3. Calculate `k` as `k % sum`, representing the remaining chalk after full rounds.
4. Iterate over the chalk array again from `0` to $\text{chalk.size}() - 1$:
- If `k` is less than the value at the current index `i`, return `i` as the index of the student who will run out of chalk.
- Otherwise, subtract the value at $\text{chalk}[i]$ from `k`.
5. If no student is found within the loop, return `0` (though this should not be reached given the problem constraints).

!?!../Documents/1894/slideshow.json:960,540!?!

#### Implementation

```python
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        # Find the sum of all elements.
        sum_chalk = 0
        for i in range(len(chalk)):
            sum_chalk += chalk[i]
            if sum_chalk > k:
                break
        # Find modulo of k with sum.
        k = k % sum_chalk
        for i in range(len(chalk)):
            if k < chalk[i]:
                return i
            k -= chalk[i]
        return 0
```

#### Complexity Analysis

Let $n$ be the size of the `chalk` array.

- Time complexity: $O(n)$

    We iterate through the `chalk` array exactly twice. Apart from this, all operations are performed in constant time. Therefore, the total time complexity is given by $O(n)$.

- Space complexity: $O(1)$

    No additional space is used proportional to the array size `n`. Therefore, the space complexity is given by $O(1)$.

---

### Approach 2: Binary Search

#### Intuition

Instead of iterating through the array to find the first index, we can use binary search. Binary search is ideal here because it quickly narrows down the search space in a sorted array.

We start by defining a predicate function that checks if the prefix sum at a given index is greater than the `k modulo sum`. This function returns `true` for indices where the prefix sum exceeds the target and `false` otherwise. Since the array is sorted based on the prefix sums, `true` indicates indices with no chalk left, while `false` indicates indices with some chalk remaining.

Using binary search, we locate the smallest index where the predicate returns `true`.
- If the predicate returns `true`, it means there might be smaller indices with `true` values, so we adjust the upper bound of the search space to the current index.
- If the predicate returns `false`, it means all `true` values are beyond the current index, so we adjust the lower bound of the search space to the current index.

#### Algorithm

Main Function - `chalkReplacer(chalk, k)`:

1. Create an array `prefixSum` of length `n`to store prefix sums.
2. Initialize $\text{prefixSum}[0]$ with $\text{chalk}[0]$.
3. Iterate through the chalk array from index `1` to `n-1` and update $\text{prefixSum}[i]$ as the sum of `prefixSum[i-1]` and $\text{chalk}[i]$.
4. Calculate `sum` as `prefixSum[n-1]`, representing the total chalk needed for one full round.
5. Calculate `remainingChalk` as `k % sum`.
6. Call the helper function `binarySearch(prefixSum, remainingChalk)` to find the student who will run out of chalk and return the result of binarySearch.

Helper Function - `binarySearch(arr, remainingChalk)`

1. Set `low` to 0 and `high` to arr.length - 1.
2. While `low` is less than `high`:
- Calculate mid as the average of `low` and `high`.
- If $\text{arr}[mid]$ is less than or equal to `remainingChalk`, update $low to mid + 1$.
- Otherwise, update `high` to `mid`.
3. Return `high` as the index of the student who will run out of chalk.

#### Implementation

```python
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)

        prefix_sum = [0] * n
        prefix_sum[0] = chalk[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + chalk[i]

        sum_chalk = prefix_sum[n - 1]
        remaining_chalk = k % sum_chalk

        return self.__binary_search(prefix_sum, remaining_chalk)

    def __binary_search(self, arr, tar):
        low = 0
        high = len(arr) - 1

        while low < high:
            mid = low + (high - low) // 2

            if arr[mid] <= tar:
                low = mid + 1
            else:
                high = mid

        return high
```

#### Complexity Analysis

Let $n$ be the size of the `chalk` array.

- Time complexity: $O(n)$

    We iterate through the `chalk` array once. Apart from this, the binary search operation takes $O(log n)$ time. Therefore, the total time complexity is given by $O(n)$.

- Space complexity: $O(n)$

    We initialize an array `prefixSum` of size `n` to store the prefix sums of the `chalk` array. Apart from this, no additional space is used. Therefore, the space complexity is given by $O(n)$.

---