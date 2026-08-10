## General

**Turn four indices into one middle pair**

The required inequalities are

$$
i < j < k < l
\quad\text{and}\quad
\texttt{nums[i]} < \texttt{nums[k]} < \texttt{nums[j]} < \texttt{nums[l]}.
$$

Trying every choice of four indices would take $O(n^4)$ time. The useful observation is that once the two middle indices $j$ and $k$ are fixed, the remaining decisions become independent. The middle values must first form an inversion: `nums[j] > nums[k]`. If they do, a valid left index is any $i<j$ whose value is smaller than `nums[k]`, and a valid right index is any $l>k$ whose value is larger than `nums[j]`.

For a fixed valid middle pair, let $L(j,k)$ count indices $i<j$ with `nums[i] < nums[k]`, and let $R(j,k)$ count indices $l>k$ with `nums[l] > nums[j]`. Every one of the $L(j,k)$ left choices can be combined with every one of the $R(j,k)$ right choices. Their product therefore counts exactly

$$
L(j,k)\cdot R(j,k)
$$

quadruplets having that particular middle pair. Different pairs $(j,k)$ cannot count the same quadruplet because a quadruplet has only one second index and one third index. The final answer is the sum of these products over all $j<k$ with `nums[j] > nums[k]`.

**What the table `f` stores**

The solution calls the right-choice table `f`. For each fixed $j$, it first computes `cnt` as the number of positions after $j$ whose values are greater than `nums[j]`. At this moment the count includes all possible right-side positions after $j$.

It then moves $k$ from left to right, starting at $j+1$. If `nums[j] > nums[k]`, the current pair is a usable inversion, and `f[j][k]` receives `cnt`. Why does `cnt` now mean the number of valid $l>k$, rather than merely $l>j$? Whenever an earlier scanned position has value greater than `nums[j]`, the `else` branch subtracts one from `cnt`. Thus, by the time the scan reaches a particular $k$, every greater value at an index strictly between $j$ and $k$ has already been removed.

There is no subtraction when `nums[j] > nums[k]` because that position is not greater than `nums[j]` and was never part of `cnt`. Consequently, when an inversion is found, `f[j][k]` equals $R(j,k)$. The loop does not need to fill entries for non-inversions. Those entries stay zero, and such a pair cannot be the middle of a valid quadruplet anyway.

**What the table `g` stores**

The second table, `g`, is symmetric but is built in the opposite direction. For a fixed $k$, `cnt` initially counts all positions before $k$ whose values are smaller than `nums[k]`. The code then moves $j$ from $k-1$ down toward index $1$.

Whenever `nums[j] < nums[k]`, position $j$ cannot be the large middle value. It was, however, included among the smaller positions counted by `cnt`, so the code subtracts it before continuing farther left. Therefore, once the reverse scan reaches an inversion with `nums[j] > nums[k]`, all smaller positions strictly between $j$ and $k$ have already been removed. The current $j$ is not smaller than `nums[k]`, so it was not counted. What remains is precisely the number of smaller positions strictly before $j$, meaning `g[j][k]` equals $L(j,k)$.

The fact that `nums` is a permutation is useful here. Values are distinct, so every comparison is strictly smaller or strictly greater; there is no equality case to handle.

**Why multiplying and summing is correct**

Consider any valid quadruplet $(i,j,k,l)$. Its middle pair satisfies `nums[j] > nums[k]`. During preprocessing, $i$ contributes to `g[j][k]` because it is before $j$ and has a value smaller than `nums[k]`. Similarly, $l$ contributes to `f[j][k]` because it is after $k$ and has a value larger than `nums[j]`. The product for this pair therefore includes the choice $(i,l)$ and counts the quadruplet.

Conversely, take any combination counted by `f[j][k] * g[j][k]`. The definition of `g` gives $i<j$ and `nums[i] < nums[k]`. The pair is an inversion, so `nums[k] < nums[j]`. The definition of `f` gives $k<l$ and `nums[j] < nums[l]`. Combining those facts produces every required index and value inequality. Thus no invalid quadruplet enters the sum, and every valid one enters exactly once.

As a small example, in `[1,3,2,4,5]` the only usable middle pair is $(j,k)=(1,2)$, with middle values $3$ and $2$. There is one smaller left value, $1$, and two larger right values, $4$ and $5$. The product is $1\cdot2=2$, matching the two possible choices of $l$.

## Complexity detail

Let $n$ be the length of `nums`. Building `f` uses a linear count and a linear scan for every eligible $j$, so it takes $O(n^2)$ time. Building `g` does the same for every eligible $k$, also taking $O(n^2)$ time. The final double sum examines $O(n^2)$ middle pairs. These phases are sequential, so the total time is $O(n^2)$, not $O(n^3)$.

The exact checked-in implementation allocates both `f` and `g` as $n$ rows of $n$ integers. Its actual auxiliary space use is therefore $O(n^2)$. The Optimal manifest lists $O(n)$ space, but that bound does not describe these two concrete matrices. The input itself is not copied, while the loop counters and accumulator use only $O(1)$ additional space beyond the tables. The returned integer may grow large, and Python integers expand as necessary.

## Alternatives and edge cases

- **Four nested loops:** Directly testing every $(i,j,k,l)$ is easy to understand but costs $O(n^4)$ time, which is far too slow when $n$ can be $4000$.
- **Three loops plus a suffix count:** Fixing three indices and counting possible fourth indices improves the brute force, but $O(n^3)$ work is still too large for the upper constraint.
- **Compressed counting formulation:** The same $O(n^2)$ idea can be organized with one-dimensional accumulated counts and achieve $O(n)$ auxiliary space. That is a worthwhile memory improvement, but it is not what the exact checked-in solution implements.
- **No middle inversion:** If `nums[j] < nums[k]`, the required relation `nums[k] < nums[j]` is already impossible. Leaving both table contributions at zero correctly skips the pair.
- **Fully increasing permutation:** There are no inversions at all, so every product is zero and the answer is zero.
- **Boundary indices:** Index $j$ starts at $1$ because an $i$ must exist before it. Index $k$ stops before $n-1$ because an $l$ must exist after it. These loop limits avoid middle pairs that could never form a quadruplet.
- **Distinct values:** The permutation guarantee removes equality. If duplicates were allowed, the strict comparisons and decrement logic would need to preserve equal values carefully rather than treating the two branches as exhaustive.
- **Large result:** The number of quadruplets can exceed a 32-bit integer even though $n$ is only $4000$. Python handles the total automatically; fixed-width implementations should use a 64-bit integer.
