## General

**Precompute the longest special suffix ending at every position**

Answering each query by scanning its subarray could take $O(nq)$. The exact solution instead builds array `d`, where `d[i]` is the earliest index at which a special subarray ending at $i$ can start.

Equivalently, `nums[d[i]..i]` is the maximal alternating-parity suffix ending at $i$.

Initially, `d = list(range(n))`, so `d[i] = i`. A one-element subarray is always special, making this a valid default.

For each $i>0$:

- if `nums[i]` and `nums[i-1]` have different parity, index $i$ can extend the special suffix ending at $i-1$, so `d[i] = d[i-1]`;
- if they have the same parity, adjacency $(i-1,i)$ is a violation. No special subarray ending at $i$ can include $i-1$, so the earliest valid start remains $i$.

This differs from the manifest's prefix-count description. A prefix count of bad adjacencies is another valid solution, but the exact code stores maximal-run starts.

**Answer one query**

For query `[f, t]`, the subarray is special exactly when its start $f$ lies inside the maximal special suffix ending at $t$:

$$
\texttt{d[t]}\le f.
$$

If this inequality holds, `nums[f..t]` is a suffix of `nums[d[t]..t]`. Removing elements from the beginning of a special array cannot create a new bad adjacency, so the query is special.

If `d[t] > f`, there is a same-parity adjacency somewhere after or at $f$ that forced the current alternating run to begin later. That violation lies inside `nums[f..t]`, so the query is not special.

The list comprehension applies this test to every query in constant time.

**Invariant proof for d**

Base case $i=0$: `d[0]=0`, and the single element is the earliest possible special suffix.

For $i>0$, suppose the invariant is correct at $i-1$.

If the new adjacency alternates parity, appending `nums[i]` preserves every previous valid adjacency. The maximal suffix can extend back exactly to `d[i-1]`. It cannot extend earlier, because any earlier start would already contradict maximality at $i-1$.

If the new adjacency has equal parity, every subarray ending at $i$ and starting before $i$ contains this bad final pair. Only the singleton at $i$ is special, so `d[i]=i`.

Thus the invariant holds for all indices, and the query inequality follows.

**Example**

For `nums = [4,3,1,6]`:

- `d[0]=0`;
- 4 and 3 differ in parity, so `d[1]=0`;
- 3 and 1 are both odd, so `d[2]=2`;
- 1 and 6 differ, so `d[3]=d[2]=2`.

Query `[0,2]` tests `d[2] <= 0`, or $2\le0$, which is false. Query `[2,3]` tests $2\le2$, which is true.

**Why only the right endpoint's state is needed**

`d[t]` summarizes the most recent parity violation before or at $t$. Any query start at or after this boundary excludes that violation and lies in the clean alternating run. Any earlier start includes it. The left endpoint does not need its own precomputed value.

Length-one queries always pass because `d[t]\le t`.

## Complexity detail

Let $n$ be the array length and $q$ the number of queries.

Creating `d` and scanning adjacent pairs takes $O(n)$ time. Each query performs one array lookup and one comparison, so all queries take $O(q)$. Total time is $O(n+q)$.

The `d` array uses $O(n)$ auxiliary space. The output list uses $O(q)$ required result space. Excluding output, no other input-sized structure is allocated.

Unlike a prefix-violation-count approach, this state stores indices rather than counts, but its asymptotic resource use is the same.

All parity operations are constant time for the bounded integers.

## Alternatives and edge cases

- **Prefix count of bad adjacencies:** Mark positions where neighboring parities match and build a prefix sum. A query is special when its interior bad-count difference is zero.
- **Last bad position:** Store only the most recent violation index for every right endpoint. This is essentially the same boundary information as `d` with a slightly different convention.
- **Scan every query:** It uses $O(1)$ extra space but can take $O(nq)$ time.
- **Segment tree:** It can answer whether a range contains a bad edge, but is unnecessary because the array never changes and prefix preprocessing is simpler.
- **Length-one query:** It contains no adjacent pair and always satisfies `d[t] <= t`.
- **Violation immediately before f:** It is outside the queried subarray and does not matter; the boundary inequality still passes.
- **Violation at pair (f, f+1):** It lies inside the query and forces `d[t] > f` for right endpoints in that run.
- **Entire array alternating:** Every `d[i]` is zero, so all queries return true.
- **All values same parity:** For every $i>0$, `d[i]=i`; only length-one queries pass.
- **Repeated values:** Adjacent equal values necessarily have equal parity and start a new run.
- **Inclusive endpoints:** The comparison is with `d[t]` and query start `f` because both endpoints belong to the subarray.
- **Input immutability:** Preprocessing writes only `d` and leaves `nums` and `queries` unchanged.
