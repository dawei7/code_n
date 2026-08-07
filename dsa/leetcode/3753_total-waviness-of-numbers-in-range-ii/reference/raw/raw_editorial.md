### Approach 1: Digit Dynamic Programming

#### Intuition

This problem involves digit counting, making it a good candidate for digit DP. We first compute the total waviness of all numbers in the range $[0, x]$, and then use the prefix-sum idea to obtain the answer. Let $\textit{solve}(x)$ denote the total waviness of all numbers in the range $[0, x]$. Then:

$$
\textit{ans} = \textit{solve}(\textit{num}_2) - \textit{solve}(\textit{num}_1 - 1)
$$

To implement $\textit{solve}(x)$, we use digit DP with memoized DFS (top-down DP). The core idea is to process the digits from left to right, keep track of the previous two significant digits, and use $\textit{isLimit}$ and $\textit{isLeading}$ to handle the upper bound and leading zeros.

During the DFS, we maintain the following state information:
- $\textit{pos}$: The index of the digit currently being processed, ranging from $0$ to $n - 1$.
- $\textit{prev}$: The digit at position $\textit{pos} - 2$. If it does not exist, its value is $-1$.
- $\textit{curr}$: The digit at position $\textit{pos} - 1$. If it does not exist (i.e., we are still in the leading-zero stage), its value is $-1$.
- $\textit{isLimit}$: Indicates whether the digits chosen so far exactly match the prefix of the upper bound. If it is $\text{true}$, the current digit cannot exceed $\textit{num}_{\textit{pos}}$; otherwise, any digit from $0$ to $9$ can be chosen.
- $\textit{isLeading}$: Indicates whether we are still skipping leading zeros. Initially, it is set to $\text{true}$.

The DFS returns two values:
- $\textit{cnt}$: The number of valid numbers that can be formed from the current state.
- $\textit{sum}$: The total waviness of all valid numbers that can be formed from the current state.

We use two three-dimensional arrays for memoization:
- $\textit{memo\_cnt}[\textit{pos}][\textit{prev}][\textit{curr}]$ stores the number of valid numbers reachable from the current state.
- $\textit{memo\_sum}[\textit{pos}][\textit{prev}][\textit{curr}]$ stores the total waviness of all valid numbers reachable from the current state.
- Both arrays are initialized to $-1$ to indicate that a state has not yet been computed. The arrays are indexed by digit values in $[0, 9]$, so states where $\textit{prev}$ or $\textit{curr}$ is $-1$ (meaning no digit has been placed yet) cannot be indexed and are simply recomputed on every call rather than cached.

For each position, we enumerate the digit placed at position $\textit{pos}$:
- Determine the range of digits that can be chosen. If $\textit{isLimit}$ is true, the current digit can range from $0$ to $\textit{num}_{\textit{pos}}$; otherwise, it can range from $0$ to $9$. Let the upper bound be $\textit{up}$.
- Enumerate every possible digit $\textit{digit}$ in $[0, \textit{up}]$.
- Update the leading-zero flag: $\textit{newLeading}$.
  - $\textit{newPrev} = \textit{curr}$
  - $\textit{newCurr} = \textit{digit}$, unless we are still in the leading-zero stage.
- Recursively call $\text{dfs}(\textit{pos}+1, \textit{newPrev}, \textit{newCurr}, \textit{isLimit} \land (\textit{digit} = \textit{up}), \textit{newLeading})$ to obtain $(\textit{subCnt}, \textit{subSum})$.

- Compute the waviness contribution of the current digit. This is the key insight: when $\textit{curr}$ is confirmed as a peak or valley, every number in the subtree rooted at this DFS call gains exactly one extra waviness point. So instead of tracking each number individually, we add $\textit{subCnt}$ (the count of those numbers) directly to $\textit{sum}$.
  - A contribution is possible only when three valid non-leading digits exist (i.e., $\textit{prev} \ge 0$ and $\textit{curr} \ge 0$).
  - If $\textit{prev} < \textit{curr} \land \textit{curr} > \textit{digit}$ or $\textit{prev} > \textit{curr} \land \textit{curr} < \textit{digit},$ then $\textit{curr}$ forms a peak or valley, and we add $\textit{subCnt}$ to $\textit{sum}$.
- Accumulate the results of all substates.
The recursion terminates when:
- $\textit{pos} = n$, meaning all digits have been processed. In this case, we return $(1, 0)$ because exactly one valid number has been formed and no additional waviness is generated.

The DFS starts from:

$$\text{dfs}(0,-1,-1,\text{true},\text{true})$$

As a small optimization, if $\textit{num} < 100$, no number contains three digits, so the answer is immediately $0$.

Finally, $\textit{solve}(\textit{num})$ returns the $\textit{sum}$ component of the DFS result, which represents the total waviness of all numbers in $[0,\textit{num}]$.

#### Implementation


```python
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        #  calculate the sum of fluctuation values of all numbers in the range [0, num]
        def solve(num: int) -> int:
            # if the fluctuation value of numbers less than 3 is 0
            if num < 100:
                return 0
            s = str(num)
            n = len(s)

            # memoized search uses two independent arrays
            # memo_cnt[pos][x][y]: the number of valid filling schemes where the current digit is at position pos, and the previous two digits are x and y
            memo_cnt = [[[-1] * 10 for _ in range(10)] for _ in range(16)]
            # memo_sum[pos][x][y]: the fluctuation value when the current position is pos, and the two left digits are x and y
            memo_sum = [[[-1] * 10 for _ in range(10)] for _ in range(16)]

            from functools import lru_cache

            @lru_cache(None)
            def dfs(
                pos: int, prev: int, curr: int, isLimit: bool, isLeading: bool
            ):
                # end position
                if pos == n:
                    return 1, 0

                # calculate the number of filling schemes and fluctuation value under current conditions
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
                    # only calculate the fluctuation value when there are no leading zeros
                    if not newLeading and prev >= 0 and curr >= 0:
                        # when the digit is a peak or a valley, update the current fluctuation value
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

Let $D$ denote the base, which is $10$ in this problem.

- Time complexity: $O(D^3 \log \textit{num}_2)$.
  
  The memoized DFS contains $O(D^2 \log \textit{num}_2)$ states, and each state enumerates $O(D)$ possible digits. Therefore, the total time complexity is $O(D^3 \log \textit{num}_2)$.

- Space complexity: $O(D^2 \log \textit{num}_2)$.
  
  The memoization table contains $O(D^2 \log \textit{num}_2)$ states, and the recursion depth is $O(\log \textit{num}_2)$.

---

### Approach 2: Bottom-Up Dynamic Programming

#### Intuition

The same idea can also be implemented using bottom-up dynamic programming. The state definition and transition logic are identical to those used in Approach 1. Instead of using recursive DFS with memoization, we iteratively build the DP states from left to right while maintaining the same information about the previous two digits, the tight constraint, and the leading-zero state.

Therefore, the underlying principle remains the same, and only the implementation style differs.

#### Implementation


```python
class Solution:
    def solve(self, num: int) -> int:
        # if the number has fewer than 3 digits, the fluctuation value is 0
        if num < 100:
            return 0
        s = str(num)
        n = len(s)

        # digit 10 represents the invalid state when there is a leading zero
        curr_states = [
            (10, 10, 1, 1, 1, 0)
        ]  # (prev, curr, tight, lead, cnt, sum)

        for pos in range(n):
            limit = int(s[pos])
            cnt = [
                [[[0] * 11 for _ in range(11)] for _ in range(2)]
                for _ in range(2)
            ]
            sum_arr = [
                [[[0] * 11 for _ in range(11)] for _ in range(2)]
                for _ in range(2)
            ]

            for prev, curr, tight, lead, c, s_val in curr_states:
                max_digit = limit if tight else 9
                for digit in range(max_digit + 1):
                    new_lead = 1 if (lead and digit == 0) else 0
                    new_prev = curr
                    new_curr = 10 if new_lead else digit
                    new_tight = 1 if (tight and digit == max_digit) else 0

                    add = 0
                    # calculate fluctuation only when there are three significant digits (both prev and curr are valid and not leading zeros)
                    if not new_lead and prev != 10 and curr != 10:
                        if (prev < curr and curr > digit) or (
                            prev > curr and curr < digit
                        ):
                            add = c

                    cnt[new_tight][new_lead][new_prev][new_curr] += c
                    sum_arr[new_tight][new_lead][new_prev][new_curr] += (
                        s_val + add
                    )

            # collect legal states
            next_states = []
            for tight in range(2):
                for lead in range(2):
                    for prev in range(11):
                        for cur in range(11):
                            c = cnt[tight][lead][prev][cur]
                            if c != 0:
                                next_states.append(
                                    (
                                        prev,
                                        cur,
                                        tight,
                                        lead,
                                        c,
                                        sum_arr[tight][lead][prev][cur],
                                    )
                                )
            curr_states = next_states

        # sum of fluctuation values of all valid states
        ans = 0
        for _, _, _, _, _, s_val in curr_states:
            ans += s_val
        return ans

    def totalWaviness(self, num1: int, num2: int) -> int:
        return self.solve(num2) - self.solve(num1 - 1)
```


#### Complexity Analysis

Let $D$ denote the base, which is $10$ in this problem.

- Time complexity: $O(D^3 \log \textit{num}_2)$.
  
  There are $O(D^2 \log \textit{num}_2)$ states, and each state considers $O(D)$ possible transitions.

- Space complexity: $O(D^2)$.
  
  At any step, the number of active DP states is bounded by $O(D^2)$, so the total space complexity is $O(D^2)$.

---