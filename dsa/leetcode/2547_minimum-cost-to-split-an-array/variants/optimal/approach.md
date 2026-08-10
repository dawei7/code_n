## General

**Solve the minimum cost of every suffix**

Let `dfs(i)` be the minimum cost to split suffix `nums[i:]` into non-empty subarrays.

Choose an ending index `j>=i` for the first part. Its cost is:

$$
k+\operatorname{trimmedLength}(\texttt{nums}[i..j]).
$$

The remaining optimum is `dfs(j+1)`. Taking the minimum over every possible `j` gives the recurrence.

The base case `i>=n` returns zero because no elements remain and no additional part is needed.

**Compute trimmed length through singleton count**

For a current segment of length

$$
L=j-i+1,
$$

trimmed form removes exactly the values whose frequency is one. If `one` is the number of singleton values, then exactly `one` array positions are removed, one per singleton value.

Therefore:

$$
\operatorname{trimmedLength}=L-\texttt{one}.
$$

The candidate expression in the source is:

`k+j-i+1-one+dfs(j+1)`.

**Update singleton count incrementally**

As `j` extends right, increment `cnt[nums[j]]`.

Frequency transitions affect `one` as follows:

- zero to one: this value becomes a singleton, so increment `one`;
- one to two: it stops being a singleton, so decrement `one`;
- two to three or higher: it was already non-singleton and remains so, so no change.

This lets every segment `nums[i..j]` obtain its trimmed length in constant expected time after extension.

**Why all occurrences of repeated values remain trimmed**

The definition removes numbers that appear only once. If a value appears twice, neither occurrence is removed; both belong to `trimmed(subarray)`.

That is why the second occurrence changes trimmed contribution from zero to two at once. Algebraically, segment length rises by one while `one` falls by one, so `L-one` rises by two.

A third occurrence raises segment length by one and leaves `one` unchanged, adding one more trimmed element.

**Trace an extending segment**

For segment values `[1,2,1]`:

- after first 1: `L=1`, `one=1`, trimmed length zero;
- after 2: `L=2`, `one=2`, trimmed length zero;
- after second 1: `L=3`, `one=1`, trimmed length two.

The trimmed segment contains the two occurrences of 1.

**Why the recurrence is optimal**

Every valid full split of suffix `i` has one uniquely determined first part `nums[i..j]`. The loop considers that boundary and adds its exact importance to the optimal cached cost of the remaining suffix.

Conversely, every candidate consists of one non-empty first subarray and a valid optimal split of what follows, so it constructs a legal complete split.

Taking the minimum across all first boundaries therefore gives exactly the minimum possible cost.

**Memoization removes exponential repetition**

Different first boundaries can lead to the same suffix start `j+1`. `@cache` computes each `dfs(i)` once and reuses it.

There are `n+1` suffix states. Within each, the loop extends through at most `n-i` endpoints. This yields quadratic rather than exponential work.

**Follow the actual top-down source**

The manifest describes prefix DP extending final parts backward. That is an equivalent $O(n^2)$ formulation, but the protected implementation is recursive suffix DP extending first parts forward.

Its explanation must reflect local counters per recursive state and the cache.

**Recursion-depth consideration**

The first candidate calls `dfs(i+1)`, so the initial evaluation can create a chain of depth `n`. With `n=1000`, this is near Python's usual recursion limit and may be fragile depending on harness overhead.

A bottom-up version avoids this practical risk while using the same recurrence.

**Importance constant `k`**

Every new subarray pays `k` regardless of content. Splitting more often can reduce duplicate penalties but adds another `k`. The DP explores this exact tradeoff rather than assuming fewer or more parts are always better.

This balance is why a purely local split decision is insufficient.

## Complexity detail

There are $n$ non-base suffix states. State `i` examines $n-i$ endpoints, so total iterations are

$$
\sum_{i=0}^{n-1}(n-i)=O(n^2).
$$

Expected counter operations are constant time, giving expected $O(n^2)$ total time.

The cache stores $O(n)$ results. Along the initial recursion chain, active local counters and stack frames use $O(n)$ aggregate space in the typical evaluation order, so auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Bottom-up prefix DP:** Extend each final part backward and avoid recursion; it matches the manifest summary.
- **All values distinct:** Every trimmed length is zero, so one whole segment costs only `k` and is optimal.
- **All values equal:** A segment of length one has no trimmed cost; length at least two keeps every occurrence.
- **Large `k`:** Fewer parts tend to be preferable, but DP still verifies the optimum.
- **Second occurrence:** It increases trimmed length by two.
- **Third and later occurrences:** Each increases trimmed length by one.
- **Non-empty parts:** Every loop chooses `j>=i`.
- **Cached suffix:** Its best cost is independent of earlier boundaries.
- **Input value range:** It would permit array counts, but Counter is used.
- **Recursion risk:** Bottom-up evaluation is safer near depth 1000.
