[TOC]

## Solution

--- 

### Approach: Tuple Representation + Counting

#### Intuition

In this problem, we need to count all equivalent dominoes, where dominoes are represented by pairs. The definition of "equivalent" is that, under the condition of allowing the flip of two pairs, their elements correspond and are equal one by one.

So we might as well directly convert each binary pair into the specified format, that is, the first dimension must not be greater than the second dimension. Two pairs are equivalent if they contain the same two numbers, regardless of order.

Noticing that the elements in the pairs are all not greater than $9$, we can concatenate each binary pair into a two-digit positive integer, i.e., $(x, y) \to 10x + y$. In this way, there is no need to use a hash table to count the number of elements, but we can directly use an array of length $100$.

#### Implementation


```python
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        num = [0] * 100
        ret = 0
        for x, y in dominoes:
            val = x * 10 + y if x <= y else y * 10 + x
            ret += num[val]
            num[val] += 1
        return ret
```


#### Complexity Analysis

Let $n$ be the number of dominoes.

- Time complexity: $O(n)$

We only need to traverse the array once.

- Space complexity: $O(1)$

We only need constant space to store a few variables.