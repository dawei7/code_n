## General

Let $N_i$ and $C_i$ be the sums of `nums[0:i]` and `cost[0:i]`, respectively. Define $dp[i]$ as the minimum transformed cost for partitioning the suffix beginning at $i$, with its first subarray numbered $1$. If that first suffix subarray ends just before $j$, it contributes

$$
(N_j + k)(C_j - C_i).
$$

The remaining suffix begins at $j$. Its subarrays are numbered from $1$ inside $dp[j]$, but placing the new first subarray before them increases every one of those numbers by $1$. That shift adds $k$ times the total remaining `cost`, namely $k(C_n-C_j)$. Therefore,

$$
dp[i] = \min_{i < j \le n}
\left((N_j+k)(C_j-C_i)+dp[j]+k(C_n-C_j)\right),
$$

with $dp[n]=0$. Every division has a unique first boundary $j$, and the recurrence combines its exact first-subarray cost with an optimal division of the remainder, so it considers every valid division and no invalid one.

Expanding a candidate cancels the two $kC_j$ terms:

$$
dp[i] = \min_{i < j \le n}
\left(-(N_j+k)C_i + dp[j] + N_jC_j + kC_n\right).
$$

For each possible $j$, this is a line evaluated at $x=C_i$, with slope $-(N_j+k)$ and intercept $dp[j]+N_jC_j+kC_n$. Process $i$ from right to left. Since every `nums` value is positive, newly inserted slopes are strictly increasing; since every `cost` value is positive, query coordinates strictly decrease. A deque can consequently maintain the lower convex hull: remove a newest line when its intersection order makes it permanently redundant, and remove the oldest line when the next line is no worse at the current query.

Intersection comparisons use integer cross multiplication, avoiding floating-point precision loss. Prefix sums are also updated backward as scalars: begin with both total sums, subtract index $i$, query $dp[i]$, and insert its line. The deque then contains exactly the still-useful transitions for future, smaller indices.

## Complexity detail

Let $n$ be the common array length. Each of the $n+1$ lines is appended once and can be removed from either end at most once. All hull maintenance is therefore amortized $O(1)$ per index, for $O(n)$ total time. The deque can retain $O(n)$ lines in the worst case, while all other state is scalar, giving $O(n)$ auxiliary space.

Reading both length-$n$ arrays already requires $\Omega(n)$ time. The algorithm matches that lower bound and is asymptotically time-optimal. The benchmark varies $n$ and contrasts the hull with the same correct suffix recurrence evaluated by testing every possible next boundary, which requires $\Theta(n^2)$ transitions.

## Alternatives and edge cases

- **Quadratic suffix dynamic programming:** Evaluate the displayed recurrence directly over every pair $i<j$ for a clear $O(n^2)$ solution, but it repeats comparisons that the convex hull eliminates.
- **Dynamic programming by subarray count:** Tracking both an endpoint and the number of parts introduces an unnecessary dimension; the suffix shift identity absorbs the order change without preserving that count.
- **Floating-point intersections:** Storing division results can misorder nearly equal crossings for large prefix products; cross multiplication keeps every comparison exact.
- **Arbitrary-slope hull:** A Li Chao tree handles nonmonotone inputs but adds logarithmic overhead; positivity guarantees monotone slopes and queries here.
- **Single element:** Only one subarray exists, and the recurrence queries the terminal line directly.
- **Large values:** Prefix products and the final answer can exceed 32-bit range, so fixed-width implementations need 64-bit integers.
- **No division:** The boundary $j=n$ is always a candidate, so using one subarray is naturally included.
- **Division at every position:** Successive choices with $j=i+1$ remain available when many short subarrays are optimal.
- **Input positivity:** Strictly positive values are what make both slope and query orders monotone; the hull argument would require modification if zeros or negatives were allowed.
