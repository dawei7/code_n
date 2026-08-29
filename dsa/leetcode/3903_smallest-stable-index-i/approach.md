## General

For each index $i$, the required score combines information from two different ranges:

$$
\operatorname{score}(i)
=
\max(\texttt{nums}[0..i])
-
\min(\texttt{nums}[i..n-1]).
$$

Computing both ranges from scratch at every index repeats almost all the same work. The source instead prepares every suffix minimum once, then walks from left to right while maintaining the current prefix maximum.

**Why the suffix side is prepared first**

When testing index $i$ during a left-to-right scan, the prefix `nums[0..i]` has already been seen, but the suffix `nums[i..n-1]` mostly lies ahead. The source stores the needed future information in `right`, where

$$
\texttt{right}[i]
=
\min(\texttt{nums}[i],\texttt{nums}[i+1],\ldots,\texttt{nums}[n-1]).
$$

The last suffix contains only `nums[n-1]`, so

$$
\texttt{right}[n-1]=\texttt{nums}[n-1].
$$

For every earlier index, the suffix beginning at $i$ consists of `nums[i]` followed by the suffix beginning at $i+1$. Therefore

$$
\texttt{right}[i]
=
\min(\texttt{nums}[i],\texttt{right}[i+1]).
$$

The backward loop evaluates exactly this recurrence from $n-2$ down to 0. When it finishes, every candidate index can retrieve its suffix minimum in constant time.

**Maintaining the prefix maximum**

The variable `left` represents

$$
\max(\texttt{nums}[0..i])
$$

at the moment index $i$ is checked.

Before the scan, `left` is zero. This initialization is safe because every array value is nonnegative. At index $i$ with current value `x`, the update

```text
left = max(left, x)
```

extends the previous prefix by one element. After it executes:

- every earlier prefix element was already summarized by the old `left`; and
- `x` is the newly included endpoint.

Their maximum is exactly the current inclusive prefix maximum.

The update happens before the stability test because `nums[i]` belongs to both ranges in the definition. Testing first would accidentally use prefix `nums[0..i-1]` and omit the current element.

**Testing the exact instability score**

At index $i$, the source now has:

$$
\texttt{left}
=
\max(\texttt{nums}[0..i])
$$

and

$$
\texttt{right}[i]
=
\min(\texttt{nums}[i..n-1]).
$$

Their difference is exactly the specified instability score. The condition

```text
left - right[i] <= k
```

uses an inclusive comparison, so a score equal to $k$ is stable.

**Why the first return is the smallest stable index**

The second loop visits indices in increasing order: 0, 1, 2, and so on. If the condition succeeds at index $i$, every smaller index was already tested and failed. Returning immediately therefore gives the least stable index without needing to compute or store every score.

If the loop ends, every index has failed the inequality, so returning `-1` is correct.

**A full trace**

For `nums = [5, 0, 1, 4]`, the backward pass builds:

$$
\texttt{right}=[0,0,1,4].
$$

These values summarize suffixes `[5,0,1,4]`, `[0,1,4]`, `[1,4]`, and `[4]`.

The forward scan keeps `left = 5` after seeing the first value, and it remains 5 throughout:

- $i=0$: score $5-0=5$;
- $i=1$: score $5-0=5$;
- $i=2$: score $5-1=4$;
- $i=3$: score $5-4=1$.

With $k=3$, the first three indices fail and index 3 succeeds. The method returns 3.

**Why both summaries remain exact**

The backward recurrence proves each suffix entry from the already-correct next entry. The forward update proves the prefix maximum by extending one index at a time. Therefore, at every test, neither aggregate is an approximation: both equal the precise ranges in the problem statement. The ascending scan then turns those exact scores into the required smallest index.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. Initializing `right` creates $N$ entries. The backward pass processes $N-1$ indices, and the forward pass processes at most $N$ indices.

The total running time is

$$
O(N).
$$

Early return may reduce the forward work for a particular input, but the suffix array has already been built, so worst-case time remains linear.

The `right` array stores one minimum per index and uses

$$
O(N)
$$

auxiliary space. The remaining variables use $O(1)$ space. The input array is never modified.

For this first version, $N\le100$, so a quadratic scan could pass the small limit. The linear design nevertheless avoids repeated work and is already suitable for the larger companion version.

## Alternatives and edge cases

- **Recompute both ranges at every index:** This direct method is easy to derive but costs $O(N^2)$ time because overlapping prefixes and suffixes are rescanned.
- **Prefix and suffix arrays:** Storing both aggregates also gives $O(N)$ time but uses two $O(N)$ arrays; the running variable removes the need for the prefix array.
- **Range-query structures:** Segment trees or sparse tables can answer maxima and minima, but they add complexity without improving this one-pass static problem.
- **Single element:** Both the prefix maximum and suffix minimum equal that value, so the score is zero and index 0 is stable for every allowed $k$.
- **Score equal to \(k\):** The index is stable because the comparison is `<=`, not strict.
- **Non-monotone scores:** The score need not change monotonically with $i$, so binary search on indices is not justified; scanning in order is safe.
- **Repeated values:** `min` and `max` naturally handle duplicates, and no special counting is required.
- **All zeros:** Every score is zero, so index 0 is returned.
- **Nonnegative-value assumption:** Initializing `left` to zero relies on all values being at least zero. With unrestricted negatives, initialization should use the first element or negative infinity.
- **No stable index:** Exhausting the ascending scan proves every candidate failed, so the method returns `-1`.
- **Input preservation:** Only `right` and scalar variables are changed; `nums` retains its original contents.
