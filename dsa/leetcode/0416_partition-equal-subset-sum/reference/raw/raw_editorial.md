[TOC]

## Video Solution
---

<div>
    <div class="video-container">
        <iframe src="https://player.vimeo.com/video/487088932?texttrack=en" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>
    </div>
</div>

<div>&nbsp;
</div>

## Solution Article
---

### Overview ####

The problem is similar to the classic _Knapsack_ problem. The basic idea is to understand that to partition an array into two subsets of equal sum say $$\text{subSetSum}$$,  the $$\text{totalSum}$$ of given array must be twice the $$\text{subSetSum}$$

$$\text{totalSum} = \text{subSetSum} * 2$$

This could also be written as,
$$\text{subSetSum} = \text{totalSum}/2$$

_Example_
Assume $$\text{totalSum}$$ of an array is $$20$$ and if we want to partition it into 2 subsets of equal sum, then the $$\text{subSetSum}$$ must be $$(20/2) = 10$$.

Now, the problem to find the subset with a sum equals a given target. Here target is $$\text{subSetSum}$$.

It must be noted that the total sum of an array must be _even_, only then we can divide it into 2 equal subsets. For instance, we cannot have an equal $$\text{subSetSum}$$ for an array with total sum as $$21$$.

**Note:**

>Finding a subset with a sum equal to a given target is different than [Subarray sum equals k](https://leetcode.com/problems/subarray-sum-equals-k/). Subarray is a contiguous sequence of array elements, whereas the subset could consist of any array elements regardless of the sequence. But each array element must belong to exactly one subset.

Let's discuss different algorithms to find the subset with a given sum.

---

### Approach 1: Brute Force

**Intuition**

We have to find a subset in an array where the sum must be equal to $$\text{subSetSum}$$ that we calculated above. The brute force approach would be to generate all the possible subsets of an array and return true if we find a subset with the required sum.

**Algorithm**

Assume, there is an array $$\text{nums}$$ of size $$n$$ and we have to find if there exists a subset with total $$\text{sum} = \text{subSetSum}$$.
For a given array element $$x$$, there could be either of 2 possibilities:

- Case 1) $$x$$ is included in subset sum. $$\text{subSetSum} = \text{subSetSum} - x$$

- Case 2) $$x$$ is not included in subset sum, so we must take previous sum without $$x$$. $$\text{subSetSum} = \text{subSetSum}$$

We can use _depth first search_ and recursively calculate the $$\text{subSetSum}$$ for each case and check if either of them is true. This can be formulated as

```java
isSum (subSetSum, n) = isSum(subSetSum- nums[n], n-1) ||  isSum(subSetSum, n-1)
```

_Base Cases_

- If $$\text{subSetSum}$$ is $$0$$, return _true_ ( Since we found a subset with sum subSetSum )
- If $$\text{subSetSum}$$ is less than $$0$$, return _false_


```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def dfs(nums: List[int], n: int, subset_sum: int) -> bool:
            # Base cases
            if subset_sum == 0:
                return True
            if n == 0 or subset_sum < 0:
                return False
            result = (dfs(nums, n - 1, subset_sum - nums[n - 1])
                    or dfs(nums, n - 1, subset_sum))
            return result

        # find sum of array elements
        total_sum = sum(nums)

        # if total_sum is odd, it cannot be partitioned into equal sum subsets
        if total_sum % 2 != 0:
            return False

        subset_sum = total_sum // 2
        n = len(nums)
        return dfs(nums, n - 1, subset_sum)
```


**Complexity Analysis**

- Time Complexity : $$\mathcal{O}(2^{n})$$, where $$n$$ is equal to number of array elements.
The recursive solution takes the form of a binary tree where there are 2 possibilities for every array element and the maximum depth of the tree could be $$n$$.  The time complexity is exponential, hence this approach is exhaustive and results in _Time Limit Exceeded (TLE)_.

- Space Complexity: $$\mathcal{O}(N)$$ This space will be used to store the recursion stack. We can’t have more than $$n$$ recursive calls on the call stack at any time.

---

### Approach 2: Top Down Dynamic Programming - Memoization

**Intuition**

In the above approach, we observe that the same subproblem is computed and solved multiple times.

Example :

![img](images/subset_sum_rec_tree.png)

In the above recursion tree, we could see that   $$\text{isSum}( 3,[6] )$$  is computed twice and the result is always the same. Since the same subproblem is computed again and again, the problem has _Overlapping Subproblem_ property and can be solved using _Dynamic Programming_.

**Algorithm**

 We could have stored the results of our computation for the first time and used it later.
 This technique of computing once and returning the stored value is called memoization.
We use a two dimensional array $$\text{memo}$$ and follow the following steps for each recursive call :
- Check if subSetSum for a given $$n$$ exists in $$\text{memo}$$ to see if we can avoid computing the answer and return the result stored in memo.
- Save the results of any calculations to $$\text{memo}$$.


```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @lru_cache(maxsize=None)
        def dfs(nums: Tuple[int], n: int, subset_sum: int) -> bool:
            # Base cases
            if subset_sum == 0:
                return True
            if n == 0 or subset_sum < 0:
                return False
            result = (dfs(nums, n - 1, subset_sum - nums[n - 1])
                    or dfs(nums, n - 1, subset_sum))
            return result

        # find sum of array elements
        total_sum = sum(nums)

        # if total_sum is odd, it cannot be partitioned into equal sum subsets
        if total_sum % 2 != 0:
            return False

        subset_sum = total_sum // 2
        n = len(nums)
        return dfs(tuple(nums), n - 1, subset_sum)
```


**Complexity Analysis**

Let $$n$$ be the number of array elements and $$m$$ be the $$\text{subSetSum}$$.

- Time Complexity : $$\mathcal{O}(m \cdot n)$$.

    - In the worst case where there is no overlapping calculation, the maximum number of entries in the `memo` would be $$m \cdot n$$. For each entry, overall we could consider that it takes constant time, _i.e._ each invocation of `dfs()` at most emits one entry in the `memo`.

    - The overall computation is proportional to the number of entries in `memo`. Hence, the overall time complexity is $$\mathcal{O}(m \cdot n)$$.

- Space Complexity: $$\mathcal{O}(m \cdot n)$$. We are using a 2 dimensional array $$\text{memo}$$ of size $$(m \cdot n)$$ and $$\mathcal{O}(n)$$ space to store the recursive call stack. This gives us the space complexity as $$\mathcal{O}(n)$$ + $$\mathcal{O}(m \cdot n)$$ = $$\mathcal{O}(m \cdot n)$$

---

### Approach 3: Bottom Up Dynamic Programming

**Intuition**

This is another approach to solving the Dynamic Programming problems. We use the iterative approach and store the result of subproblems in bottom-up fashion also known as Tabulation.

**Algorithm**

We maintain a 2D array ,
$$\text{dp}[n][\text{subSetSum}]$$
For an array element $$i$$ and sum $$j$$ in array $$\text{nums}$$,

$$\text{dp}[i][j] =
\text{true}$$ if the sum $$j$$ can be formed by array elements in subset $$\text{nums[0]} .. \text{nums[i]}$$,otherwise $$\text{dp}[i][j] = \text{false}$$

$$\text{dp}[i][j]$$ is $$\text{true}$$ it satisfies one of the following conditions :

- Case 1) sum $$j$$ can be formed without including $$i^{th}$$ element,

$$\text{if } \text{dp}[i-1][j] ==   \text{true}$$

- Case 2) sum $$j$$ can be formed including $$i^{th}$$ element,

$$\text{if } \text{dp}[i-1][j - \text{nums}[i]] == \text{true}$$



![Slide 1](images/slideshow_416_LIS_slide_1.png)

![Slide 2](images/slideshow_416_LIS_slide_2.png)

![Slide 3](images/slideshow_416_LIS_slide_3.png)

![Slide 4](images/slideshow_416_LIS_slide_4.png)

![Slide 5](images/slideshow_416_LIS_slide_5.png)

![Slide 6](images/slideshow_416_LIS_slide_6.png)

![Slide 7](images/slideshow_416_LIS_slide_7.png)

![Slide 8](images/slideshow_416_LIS_slide_8.png)

![Slide 9](images/slideshow_416_LIS_slide_9.png)

![Slide 10](images/slideshow_416_LIS_slide_10.png)




```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # find sum of array elements
        total_sum = sum(nums)

        # if total_sum is odd, it cannot be partitioned into equal sum subsets
        if total_sum % 2 != 0:
            return False
        subset_sum = total_sum // 2
        n = len(nums)

        # construct a dp table of size (n+1) x (subset_sum + 1)
        dp = [[False] * (subset_sum + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            curr = nums[i - 1]
            for j in range(subset_sum + 1):
                if j < curr:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - curr]
        return dp[n][subset_sum]
```


**Complexity Analysis**

- Time Complexity : $$\mathcal{O}(m \cdot n)$$, where $$m$$ is the $$\text{subSetSum}$$, and $$n$$ is the number of array elements. We iteratively fill the array of size $$m \cdot n$$.

- Space Complexity : $$\mathcal{O}(m \cdot n)$$ , where $$n$$ is the number of array elements and $$m$$ is the $$\text{subSetSum}$$. We are using a 2 dimensional array $$\text{dp}$$ of size $$m \cdot n$$

---

### Approach 4: Optimised Dynamic Programming - Using 1D Array

**Intuition**

We could further optimize _Approach 3_. We must understand that for any array element $$i$$, we need results of the previous iteration (i-1) only. Hence, we could achieve the same using a one-dimensional array as well.


```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # find sum of array elements
        total_sum = sum(nums)

        # if total_sum is odd, it cannot be partitioned into equal sum subsets
        if total_sum % 2 != 0:
            return False
        subset_sum = total_sum // 2

        # construct a dp table of size (subset_sum + 1)
        dp = [False] * (subset_sum + 1)
        dp[0] = True
        for curr in nums:
            for j in range(subset_sum, curr - 1, -1):
                dp[j] = dp[j] or dp[j - curr]

        return dp[subset_sum]
```


**Complexity Analysis**

- Time Complexity : $$\mathcal{O}(m \cdot n)$$, where $$m$$ is the $$\text{subSetSum}$$, and $$n$$ is the number of array elements. The time complexity is the same as _Approach 3_.

- Space Complexity: $$\mathcal{O}(m)$$, As we use an array of size $$m$$ to store the result of subproblems.

**Note:**

The overall performance of _Approach 2_ is better than all the approaches discussed above. This is because we terminate our search as soon as we find a subset with the required sum. Hence, it performs better in most cases except for the worst case.