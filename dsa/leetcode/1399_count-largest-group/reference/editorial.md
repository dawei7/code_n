
## Solution

---

### Approach: Hash Map

#### Intuition

For each integer $i$ in the interval $[1, n]$, we can calculate its digit sum $s_i$. We establish a hash mapping from the digit sum to the original number. For each number $i$, we increment the value corresponding to the key $s_i$ by one. We then find the maximum value $m$ in the set of values and traverse the hash table to count the number of occurrences of $m$.

#### Implementation

```python
class Solution:
    def countLargestGroup(self, n: int) -> int:
        hashMap = collections.Counter()
        for i in range(1, n + 1):
            key = sum([int(x) for x in str(i)])
            hashMap[key] += 1
        maxValue = max(hashMap.values())
        count = sum(1 for v in hashMap.values() if v == maxValue)
        return count
```

#### Complexity Analysis

- Time complexity: $O(n \log n)$.

The time complexity for calculating the sum of digits of $x$ is $O(\log_{10} x) = O(\log x)$, so the total time required is $O(n \log n)$. Selecting the maximum element and traversing the hash table both take $O(n)$ time; therefore, the overall time complexity is $O(n \log n) +$\mathcal{O}(n)$= O(n \log n)$.

- Space complexity: $O(\log n)$.

Using a hash map as auxiliary space, the number of digits of $n$ is $O(\log_{10} n) = O(\log n)$, and each digit is in the range `[0, 9]`, so the hash map can contain at most $O(10 \log n) = O(\log n)$ keys, and the asymptotic space complexity is $O(\log n)$.