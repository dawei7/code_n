### Approach 1: Sorting + Enumeration

#### Intuition

We first sort the array. Then, for each pair of adjacent elements $\textit{nums}[i]$ and $\textit{nums}[i + 1]$, every integer in the range $[\textit{nums}[i] + 1, \textit{nums}[i + 1])$ is missing from the array. We simply enumerate all such values and add them to the answer.

#### Implementation

```python
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        for x, y in pairwise(nums):
            ans.extend(range(x + 1, y))
        return ans
```

#### Complexity Analysis

Let $n$ be the length of the array $\textit{nums}$, and let $D$ be the difference between the maximum and minimum elements in $\textit{nums}$.

- Time complexity: $O(n \log n + D)$.

  Sorting the array takes $O(n \log n)$ time. After sorting, enumerating all missing values between adjacent elements takes $O(D)$ time in the worst case. Therefore, the overall time complexity is $O(n \log n + D)$.

- Space complexity: $O(1)$.

  Only a few extra variables are used. The returned array is not included in the space complexity.

---

### Approach 2: Hash Set + Enumeration

#### Intuition

We can store all elements of the array in a hash set. Then, enumerate every integer between the minimum and maximum values in the array. If a value does not exist in the hash set, it is a missing element and should be added to the answer.

#### Implementation

```python
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        st = set(nums)
        mn = min(nums)
        mx = max(nums)
        return [x for x in range(mn + 1, mx) if x not in st]
```

#### Complexity Analysis

Let $n$ be the length of the array $\textit{nums}$, and let $D$ be the difference between the maximum and minimum elements in $\textit{nums}$.

- Time complexity: $O(D + n)$.

  Building the hash set and finding the minimum and maximum elements each require traversing the array, which takes $O(n)$ time overall. Enumerating every integer between the minimum and maximum values takes $O(D)$ time. Therefore, the total time complexity is $O(n + D)$.

- Space complexity: $O(n)$.

  The hash set stores all elements of the array, requiring $O(n)$ extra space.

---