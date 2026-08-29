## General

Jobs cannot be reordered. Once the schedule is divided into days, each day receives a nonempty contiguous block of the original array, and the day contributes the maximum difficulty inside that block. The problem is therefore to choose exactly `d - 1` cut positions so that the sum of the resulting block maxima is as small as possible.

Trying every set of cuts repeats the same suffix or prefix scheduling questions many times. The checked-in solution stores those repeated answers in a two-dimensional bottom-up dynamic-programming table.

**Give every table cell one precise meaning**

Let `f[i][j]` mean the minimum total difficulty for scheduling the first `i` jobs, which are indices zero through `i - 1`, in exactly `j` nonempty days.

The word “exactly” is essential. A schedule using fewer days is not interchangeable with one using `j` days, and an empty day is forbidden. The final requested state is consequently `f[n][d]`, where `n = len(jobDifficulty)`.

The table starts filled with infinity. Infinity represents an impossible or not-yet-reached state and behaves conveniently under minimization. The sole zero-work base case is `f[0][0] = 0`: scheduling zero jobs in zero days has total difficulty zero. States such as `f[i][0]` for positive `i` remain impossible because jobs cannot be completed in no days. Likewise, `f[0][j]` for positive `j` remains impossible because every day must contain a job.

**Choose the final day and reuse an earlier answer**

Suppose the first `i` jobs are scheduled in `j` days. Let `k - 1` be the first job assigned to the final day. Then:

- The first `k - 1` jobs must occupy exactly `j - 1` days, whose best known cost is `f[k - 1][j - 1]`.
- The final day contains indices `k - 1` through `i - 1`.
- That final day contributes the maximum difficulty among those jobs.

This produces the candidate

$$
f[k - 1][j - 1] + \max(\texttt{jobDifficulty}[k - 1 \ldots i - 1]).
$$

Every valid `j`-day schedule of the first `i` jobs has one unique first position `k - 1` on its final day, so considering every `k` considers every possible final cut. Taking the minimum candidate therefore loses no valid schedule.

**Maintain the block maximum while moving the cut**

For fixed `i` and `j`, the inner loop moves `k` backward from `i` to one. Initially, the final day contains only job `i - 1`. Each step to the left adds job `k - 1` to that same final-day block. The assignment `mx = max(mx, jobDifficulty[k - 1])` updates the block maximum in constant time.

Without `mx`, recomputing a maximum by scanning the whole final block for every candidate cut would add another factor of $n$. Incremental maintenance is what keeps the transition at $O(n)$ per state.

The code lets `k` continue to one even when there are too few earlier jobs to fill `j - 1` days. Those candidates refer to table entries that are still infinity. Adding a finite `mx` to infinity remains infinity, so such impossible splits cannot win the minimum. A tighter loop could skip them, but the broader loop is still correct.

**Fill states only after their dependencies exist**

The outer loop increases `i` from one through `n`. Every transition for `f[i][j]` reads `f[k - 1][j - 1]`, whose job count `k - 1` is strictly smaller than `i`. Those rows have already been processed. The day loop covers `j` from one through `min(d, i)` because `i` jobs cannot fill more than `i` nonempty days.

To see the recurrence on a small prefix, consider jobs `[6, 5, 4]` and two days. For `f[3][2]`, the final day can start at job index two, giving the best one-day cost for `[6, 5]` plus four, or it can start at index one, giving the best one-day cost for `[6]` plus the maximum of `[5, 4]`. The algorithm evaluates both cuts and keeps the smaller total. The same reasoning applies to every prefix and number of days.

The table is reliable by induction over `i`. The base `f[0][0]` is exact. Assume all smaller-prefix states hold their true minimum. For `f[i][j]`, each examined cut combines an optimal schedule for its smaller prefix with the forced maximum cost of its chosen final block, so every candidate is a valid schedule cost when its prefix is feasible. Conversely, every valid schedule has one final cut included in the scan, and the stored prefix cost is no worse than that schedule’s prefix. The minimum of the candidates is therefore exactly the optimum.

If `n < d`, no schedule can give at least one job to every day. The state `f[n][d]` is never made finite, and the final expression returns `-1`. Otherwise, the requested cell contains the minimum and is returned directly.

## Complexity detail

Let $n$ be the number of jobs and $d$ the required number of days.

There are at most $n d$ relevant pairs `(i, j)`. For each pair, the `k` loop considers at most $n$ possible starting positions for the final day, and updating `mx` is constant time. The total time complexity is $O(dn^2)$. Some impossible cuts are still scanned, but they do not increase this asymptotic bound.

The exact checked-in source allocates `f` with `n + 1` rows and `d + 1` columns. Its auxiliary space is therefore $O(nd)$, not generally $O(n)$. Because the problem constrains $d$ to a small constant upper bound, one may simplify $O(nd)$ to $O(n)$ only when deliberately treating that bound as a fixed constant. When both input parameters are reported symbolically, $O(nd)$ is the faithful bound for this implementation.

The scalar variables `n`, `mx`, `i`, `j`, and `k` use constant extra space. No recursion stack is used. A rolling-array version can reduce the DP storage to $O(n)$ because transitions for one day count need only the preceding day count, but the checked-in solution retains the full table for direct indexing and clarity.

## Alternatives and edge cases

- **One-dimensional bottom-up DP:** Keep only the previous and current day layers. It preserves the $O(dn^2)$ time bound and reduces symbolic auxiliary space from $O(nd)$ to $O(n)$.
- **Top-down memoization:** Define a state by the next job index and remaining days, try every possible end of the current day, and cache results. It expresses the same recurrence naturally but adds recursion overhead and must carefully leave enough jobs for later days.
- **Monotonic-stack optimization:** The editorial derives an advanced $O(nd)$-time and $O(n)$-space method by exploiting how only changing block maxima affect transitions. It is asymptotically faster, but it is substantially harder to derive and is not the algorithm implemented by this Optimal branch.
- **Enumerating every cut set:** This directly represents the definition but examines a combinatorial number of schedules and repeats identical prefix computations.
- **Recomputing every block maximum:** Scanning the final block anew inside the `k` loop would make the straightforward DP slower. Maintaining `mx` incrementally avoids that extra factor.
- **More days than jobs:** A nonempty assignment for every day is impossible, so the answer is `-1`. Infinity propagation leaves `f[n][d]` unreachable.
- **Exactly one day:** Every job belongs to the same block, and the answer is the maximum difficulty in the entire array.
- **One job per day:** When `d == n`, every block has length one, so the answer is the sum of all job difficulties.
- **Zero-difficulty jobs:** Initializing `mx` to zero is valid because the stated job difficulties are nonnegative. Blocks containing only zeros correctly contribute zero.
- **Order preservation:** Sorting the difficulties would change which contiguous day partitions are possible and is never allowed. The DP uses prefixes specifically to preserve dependency order.
- **Inclusive final block:** For a chosen `k`, the last day starts at index `k - 1` and ends at `i - 1`. Off-by-one changes here would either omit a job or assign it twice.
- **Impossible predecessor states:** The broad `k` loop may read infinity from a prefix that cannot fill `j - 1` days. Such a candidate remains infinity and cannot corrupt a feasible minimum.
