## General

**Resizing divides time into constant-capacity segments**

The initial size is free. With at most $k$ resizing operations, the timeline can be divided into at most $k+1$ consecutive segments, each using one fixed capacity. The solution increments `k` immediately so that its variable means the number of allowed capacity segments rather than the number of later resizes.

For one segment covering times $i$ through $j$, capacity must be at least every `nums[t]` in that interval. Choosing anything above the maximum only increases waste, so the optimal capacity is

$$
\max_{i\le t\le j}\texttt{nums}[t].
$$

The segment's waste is that maximum times its length minus the sum of actual sizes.

**Precompute every interval cost**

`g[i][j]` stores the minimum waste for one fixed-capacity segment spanning $i$ through $j$. For each start `i`, the inner loop extends `j` rightward while maintaining running sum `s` and running maximum `mx`. It records:

`g[i][j] = mx * (j - i + 1) - s`.

Updating the maximum and sum incrementally makes all interval costs $O(N^2)$ rather than recomputing every interval from scratch.

**Partition prefixes with dynamic programming**

`f[i][j]` is the minimum waste for the first $i$ time points, partitioned into exactly $j$ capacity segments. The base `f[0][0] = 0` represents no time points using no segments. Other states begin at infinity.

For a state ending after time `i - 1`, choose `h` as the start of its final segment. The earlier prefix contains times zero through `h - 1` and uses `j - 1` segments; the final interval `h` through `i - 1` costs `g[h][i - 1]`. The recurrence is:

`f[i][j] = min(f[h][j - 1] + g[h][i - 1] for h in range(i))`.

Trying every `h` considers every possible last resize boundary.

**Why exactly $k+1$ segments represents “at most” $k$ resizes**

More allowed boundaries can never make the optimum worse. If an optimal schedule uses fewer segments, one of its time intervals can be split while retaining the same capacity on both pieces, leaving waste unchanged. Adjacent equal-capacity pieces can be understood as no effective resize, so the exact-segment DP still represents a schedule using at most the allowed number of actual changes.

Because original $k\le N-1$, the incremented segment count is at most $N$, so enough time positions exist to form the DP partition.

**Why the recurrence is correct**

Every valid schedule has a last constant-capacity segment beginning at some $h$. The prefix before $h$ is an independent smaller partition problem, and the last segment's best possible cost is `g[h][i - 1]`. The recurrence checks that boundary and cannot exceed the schedule's cost.

Conversely, every finite recurrence candidate joins a valid prefix partition with one valid fixed-capacity last interval, producing a valid partition. Taking the minimum is exact. By induction over prefix length and segment count, `f[n][k+1]` is the requested minimum.

**Trace the one-resize example**

For `nums = [10, 20, 30]` and original `k = 1`, the source changes `k` to two segments. Splitting before index two makes prefix `[10,20]` cost $20\cdot2-30=10$, while singleton `[30]` costs zero. Splitting after the first time gives zero waste on `[10]` and $30\cdot2-50=10$ on `[20,30]`. The DP examines both and keeps ten.

The no-split schedule would use capacity 30 throughout and waste 30, so the allowed resize is useful.

**Why future information belongs in interval preprocessing**

At one time, a capacity choice for a segment must accommodate values later in that segment. A greedy online choice based only on current `nums[i]` can resize too often or waste excessive space. The DP chooses complete boundaries, and `g` summarizes the future maximum and total needed to evaluate each interval exactly.

## Complexity detail

Let $N$ be the timeline length and let $K=k+1$ be the number of DP segments after the source increments `k`.

Precomputing `g` takes $O(N^2)$ time. The DP has $NK$ meaningful states, and each scans up to $N$ split points, taking $O(KN^2)$ time. This dominates interval preprocessing.

The interval table uses $O(N^2)$ space. The DP table uses $O(NK)$ space. Exact auxiliary space is therefore $O(N^2+NK)$, which is $O(N^2)$ because $K\le N$. This does not match the manifest's $O(N)$ space claim; the source stores both full tables.

## Alternatives and edge cases

- **On-demand interval costs:** Compute maximum and sum while scanning split points backward for each DP state, avoiding `g` but still requiring careful $O(KN^2)$ work.
- **Rolling DP rows:** Since segment count transitions from `j-1` to `j`, the DP dimension can be reduced to $O(N)$, though the precomputed interval table remains $O(N^2)$.
- **No resizes:** Incremented `k` is one, so the entire timeline is one segment with capacity equal to the global maximum.
- **Resize every boundary:** When original $k=N-1$, each time can be its own segment and waste is zero.
- **Constant `nums`:** One capacity fits every time exactly, so the answer is zero for any $k$.
- **Capacity may shrink:** Segment maxima are independent; a later resize can choose any size, including smaller.
- **Using fewer than $k$ resizes:** Equal-capacity adjacent DP segments can be merged, so the exact-segment state still represents a legal at-most-$k$ schedule.
- **Initial sizing:** It is represented by the first segment and does not consume an original resize.
- **Impossible DP states:** They remain infinity and cannot improve later states.
- **Positive sizes:** Every interval maximum is well-defined, and calculated waste is nonnegative.
- **One time point:** Its only interval capacity equals `nums[0]`, producing zero waste.
- **Exact-space warning:** Full `g` and `f` allocations make the concrete implementation quadratic-space.
