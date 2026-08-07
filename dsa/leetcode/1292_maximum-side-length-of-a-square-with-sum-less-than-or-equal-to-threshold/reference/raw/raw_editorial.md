### Prerequisites

This problem requires knowledge of **two-dimensional prefix sums**, which are an extension of one-dimensional prefix sums.

Let the size of the two-dimensional array `A` be `m × n`, with row indices in the range `[1, m]` and column indices in the range `[1, n]`.

The array `P` is the prefix sum array of `A`, where each element `P[i][j]` is defined as follows:

* If both `i` and `j` are greater than `0`, then `P[i][j]` represents the sum of all elements in the rectangular region of `A` with the top-left corner at `(1, 1)` and the bottom-right corner at `(i, j)`.

* If either `i` or `j` is equal to `0`, then `P[i][j] = 0`.

The prefix sum array `P` allows us to compute the sum of elements in any rectangular submatrix in $O(1)$ time. Specifically, if the top-left corner of the rectangle is `(x1, y1)` and the bottom-right corner is `(x2, y2)`, then the sum of elements in this region is:

```
sum = A[x1..x2][y1..y2]
    = P[x2][y2] - P[x1 - 1][y2] - P[x2][y1 - 1] + P[x1 - 1][y1 - 1]
```

The correctness of this formula follows from the **inclusion-exclusion principle**. For example, when the size of `A` is `8 × 5`, and the rectangular region to be summed has its top-left corner at `(3, 2)` and bottom-right corner at `(5, 5)`, the sum of this region is computed as `P[5][5] - P[2][5] - P[5][1] + P[2][1]`.

![1292-1](images/1.png)


How can we obtain the array `P`? To compute the array `P`, we process the elements in **row-major order**. When computing `P[i][j]`, the first `i - 1` rows of `P` and the first `j - 1` elements of the `i`-th row have already been computed.

Considering the `1 × 1` rectangle ending at `(i, j)`, we can write:

```
A[i][j] = P[i][j] - P[i - 1][j] - P[i][j - 1] + P[i - 1][j - 1]
```

Since `A[i][j]`, `P[i - 1][j]`, `P[i][j - 1]`, and `P[i - 1][j - 1]` are all known at this point, we can rearrange the equation to obtain:

```
P[i][j] = P[i - 1][j] + P[i][j - 1] - P[i - 1][j - 1] + A[i][j]
```

Each value of `P[i][j]` is computed in $O(1)$ time. Therefore, the entire prefix sum array `P` can be constructed in $O(MN)$ time. After this preprocessing step, the sum of any rectangular region can be queried in constant time.

**Notes:**

In most programming languages, array indices start from `0` instead of `1`. This needs to be handled carefully during implementation.

### Approach 1: Binary Search

#### Intuition

We first compute the prefix sum array `P` for the matrix `mat`, and then attempt to enumerate square submatrices to compute their sums.

If the size of `mat` is `m × n`, the top-left corner of a square can be any valid position in the matrix, and the maximum possible side length of a square is `min(m, n)`. A brute-force enumeration of all squares would therefore require three nested loops, resulting in a time complexity of $O(MN × \min(M, N))$. Since the prefix sum array allows us to compute the sum of any square in $O(1)$ time, this is the total complexity of the naive approach.

This approach passes all test cases in C++, but it is too slow in Python. Therefore, optimization is necessary.

Because all elements in `mat` are **non-negative integers**, an important monotonicity property holds:
If there exists a square with side length `c` whose sum does not exceed the threshold, then there must also exist valid squares of side lengths `1, 2, ..., c - 1`. This is because any smaller square can be chosen inside the larger valid square.

As a result, we can apply **binary search** to find the maximum feasible side length `c`. The search range is `[1, min(m, n)]`. For a given candidate side length `c'`, we enumerate all squares of that size and check whether at least one of them satisfies the threshold condition.

#### Implementation


```python
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        P = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                P[i][j] = (
                    P[i - 1][j]
                    + P[i][j - 1]
                    - P[i - 1][j - 1]
                    + mat[i - 1][j - 1]
                )

        def getRect(x1, y1, x2, y2):
            return P[x2][y2] - P[x1 - 1][y2] - P[x2][y1 - 1] + P[x1 - 1][y1 - 1]

        l, r, ans = 1, min(m, n), 0
        while l <= r:
            mid = (l + r) // 2
            find = any(
                getRect(i, j, i + mid - 1, j + mid - 1) <= threshold
                for i in range(1, m - mid + 2)
                for j in range(1, n - mid + 2)
            )
            if find:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
```


#### Complexity Analysis

- Time complexity: $O(MN * \log\min(M, N))$.
  
    Binary search performs $O(\log \min(M, N))$ iterations. In each iteration, all squares of a fixed side length are enumerated, which takes $O(MN)$ time.

- Space complexity: $O(MN)$.

### Approach 2: Enumeration + Optimization

#### Intuition

In Approach 1, binary search reduces the time complexity from $O(MN × \min(M, N))$ to $O(MN × \log \min(M, N))$. We now consider whether it is possible to optimize the enumeration directly.

The naive enumeration consists of three nested loops:

1. The first two loops enumerate the top-left corner `(i, j)` of the square.
2. The third loop enumerates the side length `c`.

The first two loops already iterate over all valid positions and offer little room for optimization. The third loop, however, can be optimized using two observations:

* Since all elements in `mat` are non-negative, once the sum of a square with side length `c` exceeds the threshold, any larger square with the same top-left corner will also exceed the threshold. Therefore, we can stop increasing `c` immediately.

* If we have already found a valid square with side length `c'`, then for any subsequent top-left corner `(i, j)`, there is no need to check side lengths less than or equal to `c'`. We can start directly from `c' + 1`.

Applying these two optimizations leads to the following implementation.

#### Implementation


```python
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        P = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                P[i][j] = (
                    P[i - 1][j]
                    + P[i][j - 1]
                    - P[i - 1][j - 1]
                    + mat[i - 1][j - 1]
                )

        def getRect(x1, y1, x2, y2):
            return P[x2][y2] - P[x1 - 1][y2] - P[x2][y1 - 1] + P[x1 - 1][y1 - 1]

        r, ans = min(m, n), 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for c in range(ans + 1, r + 1):
                    if (
                        i + c - 1 <= m
                        and j + c - 1 <= n
                        and getRect(i, j, i + c - 1, j + c - 1) <= threshold
                    ):
                        ans += 1
                    else:
                        break
        return ans
```


#### Complexity Analysis

To analyze the time complexity, we categorize iterations of the third loop into two types:

* **Successful enumeration:**
  The square with side length `c` satisfies the threshold condition. Each successful enumeration increases `ans`. Since the maximum possible side length is `min(m, n)`, the total number of successful enumerations is at most `min(m, n)`.

* **Failed enumeration:**
  The square with side length `c` exceeds the threshold. In this case, the loop breaks immediately. For each top-left corner `(i, j)`, there can be at most one failed enumeration.

Since there are `MN` possible top-left corners, the total number of failed enumerations is at most `MN`.

Combining both cases, the total number of iterations of the innermost loop is bounded by:

$$
O(\min(M, N) + MN) = O(MN)
$$

- Time complexity: $O(MN)$.
  
  Although this result may seem surprising, the amortized analysis shows that the total work is linear in the size of the matrix.

- Space complexity: $O(MN)$.

  The prefix sum array dominates the space usage.
    
---