[TOC]

## Solution

---

### Approach 1: Recursive Dynamic Programming (Top Down)

#### Intuition

Due to the large length of `s`, checking every subsequence is not a feasible option. Instead, we should find some property that simplifies the construction of an ideal subsequence.

Consider building an ideal string as a subsequence of `s` by checking each letter from left to right. To keep track of what letters could be appended to some ideal string, we only need to access the last letter of the current ideal string.

For example, the same set of letters can be appended to the two strings "acdba" and "abbca" because both strings end with the letter "a". Any characters before the last letter won't affect future letter choices.

Therefore, we can maintain the longest possible subsequence of `s` created from the first `i` letters of `s`. Among all of these subsequences, we only need to track the last letter `c` of any ideal subsequence.

This motivates a dynamic programming (DP) approach. We can define $\text{dp}[i][c]$ as the longest ideal subsequence ending with the letter `c` when considering only the first `i` letters in the input string `s`.

Since we need to perform difference calculations between characters, we will represent `c` as an integer from $0$ to $25$ that corresponds to each letter of the alphabet.

There are two types of transitions when calculating $\text{dp}[i][c]$:

1. Do not include $s_i$ in an ideal subsequence. The length of the current longest subsequence stays the same, so $\text{dp}[i][c] = dp[i - 1][c]$
2. Include $s_i$ in an ideal subsequence. Let $c = s_i-{'a'}$. This subsequence becomes one letter longer, so $\text{dp}[i][c] = max(dp[i - 1][p]) + 1$ for all characters `p` such that $|c-p| \leq K$. This simulates adding a new character to the longest previous subsequences that allow appending `c`.

For the base case of $i = 0$ (the first letter), if `c` matches the first letter, then we can create an ideal sequence of length $1$. Otherwise, $c \neq s_0$, so it's impossible to create a non-empty ideal sequence with the first letter. We set $\text{dp}[0][c]$ to $0$ to indicate an empty sequence.

To retrieve the answer, we should consider the longest subsequences that consider all $N$ letters and all $26$ possible ending letters. These quantities are stored in the row $dp[N - 1][c]$. We calculate the possible ideal substring lengths for each `c` value, and the maximum is the result.

#### Algorithm

1. Initialize a `dp` table with $N$ rows and $26$ columns, and set the default values to $-1$.
2. Create the `dfs` method that passes `i`, `c`, `dp`, `s`, and `k` as parameters. Note that `dp` and `s` should be passed by reference. Steps 3-7 describe the implementation of the `dfs` method.
3. If $\text{dp}[i][c]$ is not equal to $-1$, return the memoized value stored in $\text{dp}[i][c]$.
4. Otherwise, set $\text{dp}[i][c]$ to $1$ if $c = (s[i] - 'a')$, and $0$ otherwise.
5. If the current state is not a base case ($i > 0$), check the option of not including $s_i$ in this ideal subsequence.
6. If $c = (s[i] - 'a')$, check all transistions to previous letters $p$ such that $|c - p| \leq k$.
7. Return $\text{dp}[i][c]$ to end the recursive call.
8. Find the maximum of `dp[N-1][c]` for all `c` from $0$ to $25$, and return this value as the answer.

#### Implementation

```python
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        N = len(s)

        # Initialize all dp values to -1 to indicate non-visited states
        dp = [[-1] * 26 for _ in range(N)]

        def dfs(i: int, c: int, dp: list, s: str, k: int) -> int:
            # Memoized value
            if dp[i][c] != -1:
                return dp[i][c]

            # State is not visited yet
            dp[i][c] = 0
            match = c == (ord(s[i]) - ord('a'))
            if match:
                dp[i][c] = 1

            # Non base case handling
            if i > 0:
                dp[i][c] = dfs(i - 1, c, dp, s, k)
                if match:
                    for p in range(26):
                        if abs(c - p) <= k:
                            dp[i][c] = max(dp[i][c], dfs(i - 1, p, dp, s, k) + 1)
            return dp[i][c]

        # Find the maximum dp[N-1][c] and return the result
        res = 0
        for c in range(26):
            res = max(res, dfs(N - 1, c, dp, s, k))
        return res
```

#### Complexity Analysis

Let $N$ be the length of `s` and $L$ be the number of letters in the English alphabet, which is $26$.

* Time complexity: $O(NL)$.

    In the main function, we check each possible ending letter of some subsequence, calling `dfs()` $L$ times. The `dfs()` function recursively calls itself, and the total number of `dfs()` calls that run prior to memoizing is bounded by $N \cdot L$, so this step takes $O(NL + L)$, which is essentially $O(NL)$.

    The loop inside the `dfs()` function makes up to $26$ iterations. This loop is executed only if  `match` is true, which is the case if `c` corresponds to the same ASCII value as the character $s[i]$. There is only one instance of `c` that fits this description for each distinct `i`, so this loop is executed at most once for each character in `s`. In other words, $L$ transitions are executed only for $N$ total states. Over the course of the whole search process, this loop executes up to $O(NL)$ times.

    Therefore, the total time complexity is $O(NL + NL)$, or $O(2NL)$, which we can simplify to $O(NL)$. Note that $L$ is $26$, which is a constant, so we could simplify the time complexity to $O(N)$.

* Space complexity: $O(NL)$.

    The additional space complexity is $O(NL)$, since the two-dimensional `dp` grid needs to be initialized for memoization. $L$ is $26$, which is a constant, so we could simplify the time complexity to $O(N)$.

---

### Approach 2: Iterative Dynamic Programming (Bottom Up, Space Optimized)

#### Intuition

Please read the above approach first, as this approach builds off of the previous approach. Top-down dynamic programming requires overhead for the call stack; let's use bottom-up dynamic programming to develop a more efficient solution.

If we examine the above approach, we can observe that $\text{dp}[i]$ depends only on the previous row $dp[i - 1]$ in the DP grid. When we transition to DP states ending at index $i$, we only need to check DP states ending at $i-1$.

By implementing this approach iteratively, we can store `dp` as an array that tracks only the previous row of DP values. We no longer need to memoize all DP states, so we can reduce the additional space complexity by a factor of $N$.

We can use two nested `for` loops to iterate through the `dp` values in order. The outer loop iterates over the current index `i` of `s`, and the inner loop iterates over every choice `prev.` Variable `prev` indicates the previous last letter of the subsequence. `curr`, which corresponds to the character $s[i]$, is used to check if appending $s[i]$ is valid.

#### Algorithm

1. Initialize the `dp` array of length $26$ with all $0$'s.
2. Iterate through each letter in input string `s` and repeat steps 3-6 $N$ times where $N$ is the length of `s`.
3. Initialize a variable `curr` to the ASCII representation of $s_i$, and a variable `best` to `0`.
4. Iterate through the possible candidates for the previous ending letter of some ideal subsequence, which are the letters in the alphabet that are at most $K$ apart from $s_i$. Use `best` to track the maximum $\text{dp}[prev]$.
5. Set $\text{dp}[curr] = best + 1$ to simulate appending letter $curr = s_i-{'a'}$ to an ideal subsequence.
6. Update the result to the maximum between `res` and $\text{dp}[curr]$.
7. Return the result.

#### Implementation

```python
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        N = len(s)
        dp = [0] * 26

        res = 0
        # Updating dp with the i-th character
        for i in range(N):
            curr = ord(s[i]) - ord('a')
            best = 0
            for prev in range(max(0, curr - k), min(26, curr + k + 1)):
                    best = max(best, dp[prev])

            # Append s[i] to the previous longest ideal subsequence
            dp[curr] =  best + 1
            res = max(res, dp[curr])

        return res
```

#### Complexity Analysis

Let $N$ be the length of `s` and $L$ be the number of letters in the English alphabet, which is $26$.

* Time complexity: $O(NL)$.

    The outer loop iterates through the characters in `s`, so it runs $N$ times. The inner loop iterates up to $L$ times for each character in `s`. Therefore, the time complexity is $O(NL)$. Note that $L$ is $26$, which is a constant, so we could simplify the time complexity to $O(N)$.

* Space complexity: $O(L)$

    We use a DP array of size $L$. $L$ is $26$, which is a constant, so we could simplify the time complexity to $O(1)$.