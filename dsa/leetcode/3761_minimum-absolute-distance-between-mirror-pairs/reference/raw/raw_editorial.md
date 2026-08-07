### Approach: One-time Traversal

#### Intuition

We traverse the array from left to right and maintain a hash table $\textit{prev}$. Here, $\textit{prev}[v]$ represents the most recent index $j$ such that $\textit{reverse}(\textit{nums}[j]) = v$.

For the current position $i$, let the current value be $x = \textit{nums}[i]$:

- If $x$ exists in $\textit{prev}$, it means there is an index $j$ such that $\textit{reverse}(\textit{nums}[j]) = x$. Thus, $(j, i)$ forms a mirror pair, and we can update the answer with $i - j$.
- Then, we compute $\textit{reverse}(x)$ and set $\textit{prev}[\textit{reverse}(x)] = i$, indicating that the current index can form a pair with future elements whose value equals $\textit{reverse}(x)$.

For each key, we always keep the most recent index. This is because when the right endpoint is fixed later, a closer left endpoint results in a smaller distance, allowing us to obtain the minimum possible value.

#### Implementation


```python
class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        prev = dict()
        ans = inf
        for i, num in enumerate(nums):
            if num in prev:
                ans = min(ans, i - prev[num])
            prev[int(str(num)[::-1])] = i
        return -1 if ans == inf else ans
```


#### Complexity Analysis

Let $n$ be the length of the array $\textit{nums}$, and $C$ be the range of values in the array.

- Time complexity: $O(n \log C)$.
  
  We traverse the array once, and each hash table operation takes $O(1)$ on average. Reversing a number takes $O(\log C)$ time.

- Space complexity: $O(n)$.
  
  In the worst case, the hash table stores up to $n$ key-value pairs.

---