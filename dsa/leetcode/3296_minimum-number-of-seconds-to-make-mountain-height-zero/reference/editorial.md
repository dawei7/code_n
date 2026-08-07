### Approach: Binary Answer

#### Intuition

According to the problem description, if the mountain's height can be reduced to $0$ within $t$ seconds, then it can also be reduced within any time greater than $t$ seconds. Therefore, the answer is monotonic with respect to time, which allows us to apply binary search.

During each step of the binary search, suppose the current guess for the time is $\textit{mid}$. We need to determine whether all workers together can reduce the mountain's height to $H = \textit{mountainHeight}$ within $\textit{mid}$ seconds.

For the $i$-th worker, the time required to reduce the mountain's height by $k$ units is

$$
\textit{workerTimes}[i] \cdot (1 + 2 + \cdots + k)
==================================================

\textit{workerTimes}[i] \cdot \frac{k(k+1)}{2}
$$

Thus, within $\textit{mid}$ seconds, the maximum height that the $i$-th worker can reduce is the largest positive integer $k$ satisfying

$\textit{workerTimes}[i] \cdot \frac{k(k+1)}{2} \le \textit{mid}$

Let

$\textit{work} = \left\lfloor \frac{\textit{mid}}{\textit{workerTimes}[i]} \right\rfloor$

where $\lfloor \cdot \rfloor$ denotes the floor function. Then we must have

$\frac{k(k+1)}{2} \le \textit{work}$

Solving this inequality using the quadratic formula gives

$$
k = \left\lfloor
\frac{-1 + \sqrt{1 + 8 \cdot \textit{work}}}{2}
\right\rfloor
$$

We compute this value for every worker and sum the resulting $k$ values. If the total is greater than or equal to $H$, then the mountain can be reduced within $\textit{mid}$ seconds, and we attempt to find a smaller feasible time. Otherwise, we need to increase the allowed time.

The lower bound of the binary search is $1$, and the upper bound is

$\max(\textit{workerTimes}) \cdot \frac{H(H + 1)}{2}$

which represents the time required for the slowest worker to complete all the work alone.

#### Implementation

```python
class Solution:
    def minNumberOfSeconds(
        self, mountainHeight: int, workerTimes: List[int]
    ) -> int:
        maxWorkerTimes = max(workerTimes)
        l, r, ans = (
            1,
            maxWorkerTimes * mountainHeight * (mountainHeight + 1) // 2,
            0,
        )
        eps = 1e-7

        while l <= r:
            mid = (l + r) // 2
            cnt = 0
            for t in workerTimes:
                work = mid // t
                # find the largest k such that 1+2+...+k <= work
                k = int((-1 + ((1 + work * 8) ** 0.5)) / 2 + eps)
                cnt += k
            if cnt >= mountainHeight:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans
```

#### Complexity Analysis

Let $n$ be the length of the array $\textit{workerTimes}$, $M$ be the maximum value in $\textit{workerTimes}$, and $H = \textit{mountainHeight}$.

- Time complexity: $O(n \log(MH^2))$.

  Binary search requires $O(\log(MH^2))$ iterations. In each iteration, we traverse all workers, which takes $O(n)$ time.

- Space complexity: $O(1)$.

---