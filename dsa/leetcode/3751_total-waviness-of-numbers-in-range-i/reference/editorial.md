### Approach 1: Enumeration

#### Intuition

Since the constraints satisfy $1 \le \textit{num}_1 \le \textit{num}_2 \le 10^5$, we can directly enumerate every number in the range $[\textit{num}_1, \textit{num}_2]$ and compute its fluctuation value. The answer is the sum of the fluctuation values of all numbers in this range.

To calculate the fluctuation value of a number $x$, we first convert it into its string representation. We then traverse the string and count the number of peaks and valleys, which gives us the fluctuation value of the number.

#### Implementation

```python
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def waviness(n: int) -> int:
            s = str(n)
            return sum(
                (a < b > c) or (a > b < c) for a, b, c in zip(s, s[1:], s[2:])
            )

        return sum(waviness(n) for n in range(num1, num2 + 1))
```

#### Complexity Analysis

Let $\textit{num}_2$ be the larger given number.

- Time complexity: $O(\textit{num}_2 \cdot \log \textit{num}_2)$.

  We need to traverse all numbers in the interval $[\textit{num}_1, \textit{num}_2]$. In the worst case, the interval contains $O(\textit{num}_2)$ numbers. Calculating the fluctuation value of each number requires traversing its digits, which takes $O(\log \textit{num}_2)$ time. Therefore, the overall time complexity is $O(\textit{num}_2 \cdot \log \textit{num}_2)$.

- Space complexity: $O(\log \textit{num}_2)$.

  The string representation of a number contains $O(\log \textit{num}_2)$ digits.

---

### Approach 2: Digit Dynamic Programming

#### Intuition

This is a digit-counting problem, making it a natural fit for digit DP.

Instead of directly computing the answer over the interval $[\textit{num}_1, \textit{num}_2]$, we first calculate the total fluctuation value of all numbers in the range $[0, x]$. Let $\textit{solve}(x)$ denote this value. Using the prefix-sum idea, the answer can then be computed as

$\textit{ans} = \textit{solve}(\textit{num}_2) - \textit{solve}(\textit{num}_1 - 1)$

To implement $\textit{solve}(x)$, we use a memoized digit DP (top-down DFS). The digits are processed from left to right while tracking the previous two valid digits. We also use the standard digit-DP flags $\textit{isLimit}$ and $\textit{isLeading}$ to handle upper-bound constraints and leading zeros.

During the DFS, we maintain the following state information:

- $\textit{pos}$: the index of the digit currently being processed, ranging from $0$ to $n - 1$.
- $\textit{prev}$: the digit at position $\textit{pos} - 2$. If it does not exist, its value is $-1$.
- $\textit{curr}$: the digit at position $\textit{pos} - 1$. If it does not exist, its value is $-1$.
- $\textit{isLimit}$: whether the current prefix is equal to the prefix of the upper bound.
- $\textit{isLeading}$: whether we are still in the leading-zero phase.

Each DFS call returns two values:

- $\textit{cnt}$: the number of valid numbers that can be formed from the current state.
- $\textit{sum}$: the total fluctuation value contributed by those numbers.

For memoization, we use two three-dimensional arrays:

- $\textit{memoCnt}[\textit{pos}][\textit{prev}][\textit{curr}]$, which stores the number of valid numbers.
- $\textit{memoSum}[\textit{pos}][\textit{prev}][\textit{curr}]$, which stores the total fluctuation value.

Both arrays are initialized to $-1$ to indicate that a state has not yet been computed.

For simplicity, states where $\textit{prev} = -1$ or $\textit{curr} = -1$ are not memoized.

For each position, we enumerate all possible digits:

1. Determine the upper bound of the current digit.
  - If $\textit{isLimit}$ is true, the digit range is $[0, \textit{num}_{\textit{pos}}]$.
  - Otherwise, the digit range is `[0, 9]`.

2. Enumerate each candidate digit $\textit{digit}$.
3. Update the leading-zero state:

$$
\textit{isLeading}
\land
(\textit{digit} = 0).
$$

4. Update the previous two digits:
  - $\textit{newPrev} = \textit{curr}$
  - $\textit{newCurr} = \textit{digit}$ if we are no longer in the leading-zero phase; otherwise $-1$.
5. Recursively compute

$\text{dfs}(\textit{pos} + 1, \textit{newPrev}, \textit{newCurr}, \dots).$

6. Calculate the fluctuation contribution of the current digit.

A fluctuation can only be formed when three valid digits already exist. In that case, we check whether $(\textit{prev}, \textit{curr}, \textit{digit})$ forms a peak or a valley:

$\textit{prev} < \textit{curr} > \textit{digit}$

or

$\textit{prev} > \textit{curr} < \textit{digit}.$

If either condition holds, every number represented by the current subtree gains one additional fluctuation point, so we add $\textit{subCnt}$ to the current sum.

Finally, we accumulate the contributions from all child states and return $(\textit{cnt}, \textit{sum})$.

**Recursive Boundary:**

When $\textit{pos} = n$, all digits have been processed, so we return $(1, 0)$, indicating one valid number and no additional fluctuation contribution.

**Recursive Entry:**

The DFS starts from

$\text{dfs}(0, -1, -1, \text{true}, \text{true}).$

**Pruning**

If $\textit{num} < 100$, no three-digit sequence exists, so a peak or valley can never occur. Therefore, we can directly return $0$.

The value returned by $\textit{solve}(\textit{num})$ is the $\textit{sum}$ component of the DFS result, which represents the total fluctuation value of all numbers in the range $[0, \textit{num}]$.

#### Implementation

```python
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        #  calculate the sum of the volatility values of all numbers in the range [0, num]
        def solve(num: int) -> int:
            # if the number is less than 3, the fluctuation value is 0
            if num < 100:
                return 0
            s = str(num)
            n = len(s)

            # memoized search uses two independent arrays
            # memo_cnt[pos][x][y]: the number of valid filling schemes where the current position is pos, and the previous two positions are x, y
            memo_cnt = [[[-1] * 10 for _ in range(10)] for _ in range(16)]
            # memo_sum[pos][x][y]: the fluctuation value when the current position is pos and the two left digits are x and y
            memo_sum = [[[-1] * 10 for _ in range(10)] for _ in range(16)]

            from functools import lru_cache

            @lru_cache(None)
            def dfs(
                pos: int, prev: int, curr: int, isLimit: bool, isLeading: bool
            ):
                # end position
                if pos == n:
                    return 1, 0

                # calculate the number of filling schemes and the fluctuation value under current conditions
                cnt = 0
                waviness = 0
                up = int(s[pos]) if isLimit else 9
                for digit in range(up + 1):
                    newLeading = isLeading and (digit == 0)
                    # the previous number is updated to curr
                    newPrev = curr
                    # the current number is updated to digit
                    newCurr = -1 if newLeading else digit
                    subCnt, subSum = dfs(
                        pos + 1,
                        newPrev,
                        newCurr,
                        isLimit and (digit == up),
                        newLeading,
                    )
                    # only calculate the volatility value when there are no leading zeros
                    if not newLeading and prev >= 0 and curr >= 0:
                        # when the value is a peak or a trough, update the current fluctuation value
                        if (prev < curr and curr > digit) or (
                            prev > curr and curr < digit
                        ):
                            waviness += subCnt

                    cnt += subCnt
                    waviness += subSum

                return cnt, waviness

            _, totalSum = dfs(0, -1, -1, True, True)
            return totalSum

        return solve(num2) - solve(num1 - 1)
```

#### Complexity Analysis

Let $D$ denote the base, which is $10$ in this problem, and let $\textit{num}_2$ be the larger given number.

- Time complexity: $O(D^3 \log \textit{num}_2)$.

  The digit DP contains $O(D^2 \log \textit{num}_2)$ states. For each state, we enumerate up to $D$ digits. Therefore, the total time complexity is $O(D^3 \log \textit{num}_2)$.

- Space complexity: $O(D^2 \log \textit{num}_2)$.

  The memoization table contains $O(D^2 \log \textit{num}_2)$ states, and the recursion depth is $O(\log \textit{num}_2)$.

---