## Solution
---
### Approach 1: Sort

**Intuition and Algorithm**

Create an array of the squares of each element, and sort them.

```python
class Solution(object):
    def sortedSquares(self, A):
        return sorted(x*x for x in A)
```

**Complexity Analysis**

* Time Complexity:  $O(N \log N)$, where $N$ is the length of `A`.

* Space complexity : $\mathcal{O}(N)$ or $\mathcal{O}(\log{N})$

  - The space complexity of the sorting algorithm depends on the implementation of each program language.

  - For instance, the `list.sort()` function in Python is implemented with the [Timsort](https://en.wikipedia.org/wiki/Timsort) algorithm whose space complexity is $\mathcal{O}(N)$.

  - In Java, the [Arrays.sort()](https://docs.oracle.com/javase/8/docs/api/java/util/Arrays.html#sort-byte:A-) is implemented as a variant of quicksort algorithm whose space complexity is $\mathcal{O}(\log{N})$. However, if the array is highly structured (has few sorted subarrays), then [linear space](https://github.com/openjdk/jdk/blob/jdk-14-ga/src/java.base/share/classes/java/util/DualPivotQuicksort.java#L733) may be used instead.

---
### Approach 2: Two Pointer

**Intuition**

Since the array `A` is sorted, loosely speaking it has some negative elements with squares in decreasing order, then some non-negative elements with squares in increasing order.

For example, with `[-3, -2, -1, 4, 5, 6]`, we have the negative part `[-3, -2, -1]` with squares `[9, 4, 1]`, and the positive part `[4, 5, 6]` with squares `[16, 25, 36]`.  Our strategy is to iterate over the negative part in reverse, and the positive part in the forward direction.

**Algorithm**

We can use two pointers to read the positive and negative parts of the array - one pointer `j` in the positive direction, and another `i` in the negative direction.

Now that we are reading two increasing arrays (the squares of the elements), we can merge these arrays together using a two-pointer technique.

```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            result[i] = square * square
        return result
```

**Complexity Analysis**

* Time Complexity:  $O(N)$, where $N$ is the length of `A`.

* Space Complexity: $O(N)$ if you take output into account and $O(1)$ otherwise.
<br />
<br />