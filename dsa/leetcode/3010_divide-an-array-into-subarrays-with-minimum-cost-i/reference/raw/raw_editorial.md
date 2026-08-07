### Approach 1: Sorting

#### Intuition

The **cost** of an array is its **first element**. We need to divide the given array $\textit{nums}$ into **3 continuous and non-overlapping** subarrays and return the **minimum** possible sum of the costs of these 3 subarrays.

According to the problem statement, the **cost** of the first subarray is fixed as $\textit{nums}[0]$. Once the starting positions of the second and third subarrays are determined, the entire division of the array is uniquely defined. We can choose two indices $(i, j)$ as the starting positions of the second and third subarrays, respectively, such that $1 \le i < j \le n - 1$, where $n$ is the length of the array $\textit{nums}$. In this case, the **cost** of the second subarray is $\textit{nums}[i]$, and the **cost** of the third subarray is $\textit{nums}[j]$.

To minimize the total **cost**, we need to select the two smallest values among the elements in the range $[1, n - 1]$. This can be achieved by sorting the subarray $\textit{nums}[1 \cdots n - 1]$ in ascending order and taking the first two elements.

#### Implementation


```python
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        nums[1:] = sorted(nums[1:])
        return sum(nums[:3])
```


#### Complexity Analysis

Let $n$ denote the length of the given array $\textit{nums}$.

- Time complexity: $O(n \log n)$.
  
  Sorting requires $O(n \log n)$ time.

- Space complexity: $O(\log n)$.
  
  Sorting requires $O(\log n)$ stack space.

---

### Approach 2: Maintaining The Minimum And Second Minimum Values

#### Intuition

As discussed in Approach 1, we need to find the two smallest elements whose indices lie in the range $[1, n - 1]$. Instead of sorting, we can maintain the minimum value $\textit{first}$ and the second minimum value $\textit{second}$ while traversing the array. After the traversal, the minimum total cost is simply $\textit{nums}[0] + \textit{first} + \textit{second}$.

#### Implementation


```python
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        return nums[0] + sum(nsmallest(2, nums[1:]))
```


#### Complexity Analysis

Let $n$ be the length of the array $\textit{nums}$.

- Time complexity: $O(n)$.

- Space complexity: $O(1)$.

---