### Approach: Hash Table + Sorting

#### Intuition

We enumerate all subarrays of length $k$, using a hash table $\textit{cnt}$ to count the occurrences of each number within the subarray. For each key-value pair $(\textit{key}, \textit{value})$ in the hash table—where $\textit{key}$ represents a number and $\textit{value}$ represents its occurrence count—we store them in an array and sort this array primarily in descending order by $\textit{value}$, and secondarily in descending order by $\textit{key}$.

After sorting, the first $x$ tuples correspond to the $x$ most frequent elements and their counts. By summing their products, we obtain the answer for this subarray.

#### Implementation


```python
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = list()
        for i in range(n - k + 1):
            cnt = Counter(nums[i : i + k])
            freq = sorted(cnt.items(), key=lambda item: (-item[1], -item[0]))
            xsum = sum(key * value for key, value in freq[:x])
            ans.append(xsum)
        return ans
```


#### Complexity Analysis

- Time complexity: $O(n \times k \log k)$.
  
  The time to enumerate all subarrays of length $k$ is $O(n)$, and each subarray takes $O(k \log k)$ time for sorting and computing the answer.

- Space complexity: $O(k)$.
  
  This is the space required for hash table and arrays.

---