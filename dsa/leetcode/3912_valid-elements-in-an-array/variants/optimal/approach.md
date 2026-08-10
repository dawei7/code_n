## General

An element is valid when it is a strict record from at least one direction:

- larger than every value before it; or
- larger than every value after it.

The source precomputes suffix maxima for the right-side condition, maintains one running maximum for the left-side condition, and emits an element when either test succeeds.

The output asks for values in original order, so the final decision pass moves from left to right and appends immediately.

**Precomputing suffix maxima**

The list `right` is defined by

$$
\texttt{right}[i]
=
\max(\texttt{nums}[i],\texttt{nums}[i+1],\ldots,\texttt{nums}[n-1]).
$$

The final suffix contains only the last value, giving the base case

$$
\texttt{right}[n-1]=\texttt{nums}[n-1].
$$

For an earlier index:

$$
\texttt{right}[i]
=
\max(\texttt{nums}[i],\texttt{right}[i+1]).
$$

The source computes this recurrence from right to left. Once complete, `right[i + 1]` is the maximum of every element strictly to the right of index $i$.

Using $i+1$ rather than $i$ is crucial. The condition compares `nums[i]` only with other elements to its right; including itself in the comparison would make strict `x > maximum` impossible.

**Maintaining the maximum strictly to the left**

The variable `left` is updated after the current element is tested. At the start of iteration $i$, it therefore equals

$$
\max(\texttt{nums}[0],\ldots,\texttt{nums}[i-1])
$$

for $i>0$.

The condition `x > left` is exactly “the current value is strictly greater than every value to its left.”

The source initializes `left` to zero. Input values are positive, so the first value is always greater than this sentinel and is included automatically. After each decision:

```text
left = max(left, x)
```

extends the summary to include the current value for the next index.

Updating before the test would be wrong: `left` would then be at least `x`, preventing any strict left-record condition from succeeding.

**Handling the last position safely**

The last element is always valid, but it has no `right[i + 1]` entry. The source's condition is:

```text
x > left or i == n - 1 or x > right[i + 1]
```

Python evaluates `or` from left to right and stops once a term is true. At the last index, `i == n - 1` is true, so `right[i + 1]` is never accessed. This both includes the required endpoint and avoids an out-of-range lookup.

For earlier positions, the third term compares `x` against the precomputed maximum strictly to its right.

**Why one OR expresses the union**

The problem says “at least one” condition. An element that is a record from the left, from the right, or from both directions must appear exactly once.

The single `if` with logical `or` performs this set union naturally. If both comparisons succeed, `ans.append(x)` still executes only once. No deduplication by value is used or wanted: different valid indices holding equal values must each appear in the result when their endpoint status or comparisons permit it.

**Strictness and duplicate values**

Suppose a value equal to `x` appears earlier. Then `left >= x` and `x > left` is false. Likewise, an equal later value makes `right[i + 1] >= x` and the right condition false.

This exactly enforces “strictly greater.” For `[5,5,5,5]`:

- index 0 is included as the first element;
- the two middle values are neither strict left nor right records;
- index 3 is included as the last element.

The output is `[5,5]`. The equal endpoint values correspond to two different always-valid indices, so both belong.

**A trace**

For `nums = [1,2,4,2,3,2]`, the suffix maxima are

$$
[4,4,4,3,3,2].
$$

During the forward scan:

- 1 is a new left record and is included;
- 2 is a new left record and is included;
- 4 is a new left record and is included;
- the next 2 is below the left maximum 4 and below the right maximum 3, so it is excluded;
- 3 is not a left record, but it exceeds the only value 2 to its right, so it is included;
- the final 2 is included by the endpoint rule.

The result is `[1,2,4,3,2]` in original order.

**Why every output decision is exact**

The backward recurrence makes `right[i+1]` the exact maximum of the strict right side. The delayed update makes `left` the exact maximum of the strict left side. Therefore each non-endpoint comparison is equivalent to one of the two definition clauses.

The endpoints are included explicitly or through the positive sentinel, and the ascending output scan preserves occurrence order. Every valid position is appended, and no invalid interior position passes either exact test.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. The backward suffix pass visits $N-1$ indices. The forward decision pass visits all $N$ indices.

Total time is

$$
O(N).
$$

The `right` array stores $N$ maxima. The result may also contain up to $N$ values. Auxiliary space is

$$
O(N),
$$

matching the manifest when the suffix structure is counted. Including output does not change the asymptotic bound.

The source reads but never modifies `nums`.

## Alternatives and edge cases

- **Scan both sides for every element:** This mirrors the definition directly but costs $O(N^2)$ because the same ranges are repeatedly examined.
- **Two record-marker arrays:** Mark left records in one pass and right records in another, then emit their union. It also costs $O(N)$ space but stores more state than the source.
- **Use a right-to-left result set:** Combining valid indices in a set can lose ordering unless a final forward pass is added; the source emits in order directly.
- **Single element:** It is both first and last and is appended exactly once.
- **First element:** The positive-value contract and `left = 0` make it pass the left condition.
- **Last element:** The explicit index test includes it and short-circuits the unavailable suffix lookup.
- **Equal values:** Equality fails both strict comparisons; only endpoint rules may still make such occurrences valid.
- **Strictly increasing array:** Every element is a new left record, so all values are returned.
- **Strictly decreasing array:** Every element exceeds everything to its right, so all values are returned.
- **Interior global maximum:** It passes both directional conditions but is appended only once.
- **Positive-value assumption:** Initializing `left` to zero relies on all values being at least one. Negative inputs would require negative infinity or separate first-index handling.
- **Original order:** Appending during the forward scan guarantees the result is not sorted by value or discovery direction.
- **Input preservation:** Suffix information is stored separately; the original array remains unchanged.
