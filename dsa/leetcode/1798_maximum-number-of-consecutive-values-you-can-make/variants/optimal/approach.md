## General

**Track a complete interval of constructible sums**

The empty subset always makes zero. The solution maintains `ans` as the first nonnegative value that cannot yet be made from the processed coins. Equivalently, before each iteration, every value in the interval

$$
[0,\texttt{ans}-1]
$$

is constructible.

Initially no coin has been processed. Only zero is known to be constructible, so `ans = 1`. This variable serves two roles at the end: it is the first missing value, and because the constructible run is `0, 1, ..., ans - 1`, it is also the number of consecutive values in that run.

**Process coins from smallest to largest**

The solution iterates through `sorted(coins)`. Sorting is essential because when a gap appears, the algorithm must know that every unprocessed coin is at least as large as the current one.

Consider the next coin value `v` while all sums through `ans - 1` are possible.

If `v <= ans`, using no copy of this new coin preserves all old sums `[0, ans - 1]`. Adding this coin to every old constructible sum produces every value in

$$
[v,\ v+\texttt{ans}-1].
$$

Because $v\leq\texttt{ans}$, this new interval begins no later than the first missing value. It overlaps or touches the old interval, so their union has no gap:

$$
[0,\texttt{ans}+v-1].
$$

The first missing value therefore advances by $v$, implemented as `ans += v`.

**Stop permanently when the next coin is too large**

If `v > ans`, value `ans` cannot be made.

Processed coins can produce at most the already covered range ending at `ans - 1`. Any subset that uses `v` has sum at least `v` because every coin value is positive, and `v > ans`. Since the coins are sorted, every later unprocessed coin is at least `v` and also cannot help make the smaller missing value `ans`.

The gap is permanent, so the loop can `break` immediately. Values larger than the gap do not matter because the requested sequence must start at zero and remain consecutive.

**Following the examples**

For `coins = [1, 3]`, start with `ans = 1`. Coin 1 is no larger than `ans`, so coverage expands from `[0, 0]` to `[0, 1]` and `ans` becomes 2. The next coin is 3, which exceeds 2. Value 2 cannot be formed, so the maximum consecutive count is 2: values zero and one.

For `[1, 1, 1, 4]`, the first three coins expand `ans` from 1 to 2, then 3, then 4. Coin 4 exactly touches the first missing value, so it connects old sums `[0, 3]` to new sums `[4, 7]`. The final coverage is `[0, 7]` and `ans = 8`.

For `[1, 4, 10, 3, 1]`, sorting gives `[1, 1, 3, 4, 10]`. The frontier evolves as 1, 2, 3, 6, 10, and 20. Every coin is at most the current frontier when processed, so all values from zero through 19 are constructible and the answer is 20.

**Why duplicates are useful rather than redundant**

Each physical coin can be chosen at most once, even if several coins have the same value. Duplicate values are separate resources. For example, three one-value coins make sums one, two, and three. The loop processes each occurrence and expands the reachable interval each time.

**Why the greedy invariant proves correctness**

The invariant is true initially because the empty subset makes exactly zero in the required starting range.

When `v <= ans`, every old sum remains possible and every old sum plus `v` is possible. The two intervals meet, so the updated invariant holds through `ans + v - 1`.

When `v > ans`, no subset of processed coins makes `ans` by the invariant's frontier definition, and any subset containing an unprocessed positive coin has sum greater than `ans`. Therefore `ans` is truly impossible. The run of consecutive constructible values ends at `ans - 1`, and returning `ans` gives its exact length.

**Why individual subset sums never need to be stored**

Normally, subset-sum problems may require a Boolean table of many reachable totals. Here the objective concerns only an unbroken prefix from zero. Once the invariant proves that this whole prefix is covered, its endpoint summarizes all relevant reachability information. The sorted next coin either extends the interval as one block or exposes an irreversible gap.

## Complexity detail

Let $n$ be the number of coins. Python's `sorted(coins)` creates and sorts a new list in $O(n\log n)$ time. The subsequent scan is $O(n)$, so total time is $O(n\log n)$, matching the manifest.

The sorted copy contains $n$ integers and uses $O(n)$ auxiliary space. Other state is constant. The original `coins` list is not mutated.

An in-place sort could reduce copying but would alter the caller's input and still use implementation-dependent sorting stack memory.

## Alternatives and edge cases

- **Subset-sum dynamic programming:** It records many individual sums and can depend on the potentially large total coin value, while the interval invariant needs only one frontier.
- **Enumerate all subsets:** There are $2^n$ subsets and the constraints make enumeration impossible.
- **Process unsorted coins:** Breaking on a large coin would be unsafe if a smaller helpful coin appeared later; sorting makes the gap proof valid.
- **Maximum-heap order:** Large coins first reveal no useful information about the smallest missing value.
- **Coin exactly equal to `ans`:** Its new interval starts exactly where old coverage ends, so it extends the run without a gap.
- **Coin smaller than `ans`:** New and old intervals overlap, still yielding continuous coverage.
- **Coin larger than `ans`:** The current frontier is impossible and all later positive sorted coins are too large, so stopping is conclusive.
- **First coin greater than one:** Value one is immediately missing, so the answer remains one for the constructible value zero.
- **Repeated coins:** Every occurrence is processed separately and can extend coverage.
- **Single coin of value one:** Values zero and one are possible, so the answer is two.
- **Single larger coin:** Only zero belongs to the consecutive prefix, so the answer is one.
- **Positive-value guarantee:** The gap proof relies on adding an unprocessed coin never reducing a sum.
- **Meaning of the return value:** `ans` is the first missing integer and also the count of integers from zero through `ans - 1`.
- **Input preservation:** `sorted` returns a new list instead of reordering `coins`.
