### Approach 1: Hash Table

#### Intuition

Use a hash table to count the numbers that appear twice in $\textit{nums}$, and return the result.

#### Implementation


```python
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = []
        count = {}
        for x in nums:
            count[x] = count.get(x, 0) + 1
            if count[x] == 2:
                res.append(x)
        return res
```


#### Complexity Analysis

- Time complexity: $O(n)$.

- Space complexity: $O(n)$.

### Approach 2: Bitwise Operations

#### Intuition

We XOR all the numbers in $\textit{nums}$ with all the numbers from $0$ to $n - 1$.
The result is the XOR of the two extra numbers, denoted as $y$.

The lowest differing bit between these two numbers can be found using `lowBit = y & -y`.

Using this bit, we divide all the numbers in $\textit{nums}$ and the numbers from $0$ to $n - 1$ into two groups, then compute the XOR of each group. The results are the two missing numbers.

#### Implementation


```python
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums) - 2
        y = 0
        for x in nums:
            y ^= x
        for i in range(n):
            y ^= i
        lowBit = y & -y
        x1 = x2 = 0
        for x in nums:
            if x & lowBit:
                x1 ^= x
            else:
                x2 ^= x
        for i in range(n):
            if i & lowBit:
                x1 ^= i
            else:
                x2 ^= i
        return [x1, x2]
```


#### Complexity Analysis

- Time complexity: $O(n)$.

- Space complexity: $O(1)$.

### Approach 3: Mathematics

#### Intuition

Let the two extra numbers be $x_1$ and $x_2$.
Let $\textit{sum}$ and $\textit{squaredSum}$ denote the sum and the squared sum of elements in $\textit{nums}$, respectively.
The sum and squared sum of integers from $0$ to $n - 1$ are $\frac{n(n - 1)}{2}$ and $\frac{n(n - 1)(2n - 1)}{6}$, respectively.

Define:
$$
\textit{sum}_2 = \textit{sum} - \frac{n(n - 1)}{2}, \quad
\textit{squaredSum}_2 = \textit{squaredSum} - \frac{n(n - 1)(2n - 1)}{6}
$$

Then:
$$
\begin{cases}
x_1 + x_2 = \textit{sum}_2 \
x_1^2 + x_2^2 = \textit{squaredSum}_2
\end{cases}
$$

Solving gives:
$$
\begin{cases}
x_1 = \frac{\textit{sum}_2 - \sqrt{2 \times \textit{squaredSum}_2 - \textit{sum}_2^2}}{2} \
x_2 = \frac{\textit{sum}_2 + \sqrt{2 \times \textit{squaredSum}_2 - \textit{sum}_2^2}}{2}
\end{cases}
$$

#### Implementation


```python
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums) - 2
        sum_ = sum(nums)
        squared_sum = sum(x * x for x in nums)
        sum2 = sum_ - n * (n - 1) // 2
        squared_sum2 = squared_sum - n * (n - 1) * (2 * n - 1) // 6
        x1 = (sum2 - math.sqrt(2 * squared_sum2 - sum2 * sum2)) / 2
        x2 = (sum2 + math.sqrt(2 * squared_sum2 - sum2 * sum2)) / 2
        return [int(x1), int(x2)]
```


#### Complexity Analysis

- Time complexity: $O(n)$.

- Space complexity: $O(1)$.

---