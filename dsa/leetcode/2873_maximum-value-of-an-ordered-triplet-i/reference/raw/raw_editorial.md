[TOC]

## Solution

--- 

### Approach 1: Brute-force enumeration

#### Intuition

Enumerate all triples $(i, j, k)$ satisfying $i < j < k$, and return the maximum value of all triples with values greater than or equal to $0$.

#### Implementation


```python
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    res = max(res, (nums[i] - nums[j]) * nums[k])
        return res
```


#### Complexity Analysis

Let $n$ be the length of the array $\textit{nums}$.

- Time complexity: $O(n^3)$.

Since we need to enumerate all triplets, we need a triple loop to traverse the entire array.

- Space complexity: $O(1)$.

Only a few additional variables are needed.

---

### Approach 2: Greedy

#### Intuition

When $j$ and $k$ of the triplet $(i, j, k)$ are fixed, it can be known from the value formula $(\textit{nums}[i] - \textit{nums}[j]) \times \textit{nums}[k]$ that $(\textit{nums}[i] - \textit{nums}[j]) \times \textit{nums}[k]$ is maximized when $\textit{nums}[i]$ takes the maximum value in the interval $[0, j)$. Use two nested loops to enumerate $k$ and $j$ respectively, while using $m$ to maintain the maximum value of $[0, j)$. Return the maximum value of all $(m - \textit{nums}[j]) \times \textit{nums}[k]$ (if all values are negative, return $0$).

#### Implementation


```python
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for k in range(2, n):
            maxPrefix = nums[0]
            for j in range(1, k):
                res = max(res, (maxPrefix - nums[j]) * nums[k])
                maxPrefix = max(maxPrefix, nums[j])
        return res
```


#### Complexity Analysis

Let $n$ be the length of the array $\textit{nums}$.

- Time complexity: $O(n^2)$.

Since we used a variable to maintain the maximum value of $\textit{nums}[i]$, we saved one layer of loop.

- Space complexity: $O(1)$.

Only a few additional variables are needed.

---

### Approach 3: Greedy + Prefix Suffix Array

#### Intuition

Let the length of the array $\textit{nums}$ be $n$. According to the value formula $(\textit{nums}[i] - \textit{nums}[j]) \times \textit{nums}[k]$, it can be known that when $j$ is fixed, the maximum value of the triplet is achieved when $\textit{nums}[i]$ and $\textit{nums}[k]$ respectively take the maximum values from $[0, j)$ and $[j + 1, n)$. We use $\textit{leftMax}[j]$ and $\textit{rightMax}[j]$ to maintain the maximum value of the prefix $[0, j)$ and the maximum value of the suffix $[j + 1, n)$, respectively. We then enumerate $j$ in order, calculate the value $(\textit{leftMax}[j] - \textit{nums}[j]) \times \textit{rightMax}[j]$, and return the maximum value (if all values are negative, return $0$).

#### Implementation


```python
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        leftMax = [0] * n
        rightMax = [0] * n
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], nums[i - 1])
            rightMax[n - 1 - i] = max(rightMax[n - i], nums[n - i])
        res = 0
        for j in range(1, n - 1):
            res = max(res, (leftMax[j] - nums[j]) * rightMax[j])
        return res
```


#### Complexity Analysis

Let $n$ be the length of the array $\textit{nums}$.

- Time complexity: $O(n)$.

  The algorithm traverses the array twice: once to compute both the prefix maximums (`leftMax`) and suffix maximums (`rightMax`), and once to compute the result. Each traversal takes $O(n)$ time, so the overall time complexity remains $O(n)$.

- Space complexity: $O(n)$.

  Two additional arrays of size $n$ are used to store the prefix and suffix maximum values. Therefore, the space complexity is $O(n)$.

### Approach 4: Greedy

#### Intuition

Similar to approach 3, if we fix $k$, then the value of the triplet is maximized when $\textit{nums}[i] - \textit{nums}[j]$ takes the maximum value. We can use $\textit{imax}$ to maintain the maximum value of $\textit{nums}[i]$ and $\textit{dmax}$ to maintain the maximum value of $\textit{nums}[i] - \textit{nums}[j]$. During the enumeration of $k$, update $\textit{dmax}$ and $\textit{imax}$.

#### Implementation


```python
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        res, imax, dmax = 0, 0, 0
        for k in range(n):
            res = max(res, dmax * nums[k])
            dmax = max(dmax, imax - nums[k])
            imax = max(imax, nums[k])
        return res
```


#### Complexity Analysis

Let $n$ be the length of the array $\textit{nums}$.

- Time complexity: $O(n)$.

We perform a single traversal of the array, maintaining the maximum value seen so far and the best difference.

- Space complexity: $O(1)$.

We only need two variables to maintain the maximum and maximum difference values.

---