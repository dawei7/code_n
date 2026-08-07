### Approach: Parity of Enumeration Elements

#### Intuition

According to the definition of a valid subsequence, we can observe that all elements at odd indices in the subsequence must have the same parity, and all elements at even indices must also have the same parity. Therefore, there are a total of four possible parity patterns for the subsequence:

1. All elements are even.
2. All elements are odd.
3. Elements at odd indices are odd, and elements at even indices are even.
4. Elements at odd indices are even, and elements at even indices are odd.

We can enumerate these four possibilities. For each one, we traverse the entire `nums` array and calculate the maximum length of a subsequence that fits the chosen pattern. While traversing, if the current number satisfies the required parity based on its position in the subsequence, we greedily increase the length by 1.
Finally, we return the maximum subsequence length across all possibilities.

#### Implementation


```python
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        res = 0
        for pattern in [[0, 0], [0, 1], [1, 0], [1, 1]]:
            cnt = 0
            for num in nums:
                if num % 2 == pattern[cnt % 2]:
                    cnt += 1
            res = max(res, cnt)
        return res
```


#### Time complexity

Let $n$ be the length of the array $\textit{nums}$.

- Time complexity: $O(n)$.
  
  We only need to traverse the array once.

- Space complexity: $O(1)$.