## General

A bitonic array has one transition from strict increase to strict decrease. If the peak is at index $p$, the required sums are

$$
A=\sum_{i=0}^{p}\texttt{nums}[i]
$$

and

$$
B=\sum_{i=p}^{n-1}\texttt{nums}[i].
$$

The peak belongs to both. The source begins with the whole-array sum and walks adjacent pairs until it finds the first descending pair. During that walk, it incrementally constructs $A$ and removes pre-peak values from the total to construct $B$.

**Recognizing where the peak occurs**

For adjacent values `a = nums[i]` and `b = nums[i + 1]`:

- before the peak, strict increase gives $a<b$;
- at the peak boundary, $a>b$, with `a` equal to the peak.

Because the input is guaranteed bitonic, the first pair satisfying `a > b` identifies the transition. There is no plateau case $a=b$ under the contract.

The loop uses `pairwise(nums)`, which produces consecutive pairs in index order. It stops before processing the descending boundary pair.

**Building the ascending sum**

The variable `l` begins as `nums[0]`. For every increasing pair $(a,b)$ before the peak, `b` is the next value in the ascending part, so the source performs

```text
l += b
```

If the increasing pairs processed so far end at index $t$, then

$$
\texttt{l}
=
\sum_{i=0}^{t}\texttt{nums}[i].
$$

When the last increasing pair $(\texttt{nums}[p-1],\texttt{nums}[p])$ is processed, the peak is added. The following pair $(\texttt{nums}[p],\texttt{nums}[p+1])$ is descending, so the loop breaks without adding a post-peak value.

Thus `l` equals $A$.

**Deriving the descending sum from the total**

The variable `r` starts as `sum(nums)`. During every increasing pair $(a,b)$, `a` is known to occur strictly before the peak, so it does not belong to descending part $p..n-1$. The source removes it:

```text
r -= a
```

Across all processed increasing pairs, the removed values are exactly

$$
\texttt{nums}[0],\texttt{nums}[1],\ldots,\texttt{nums}[p-1].
$$

The peak `nums[p]` is never removed, because it appears as `b` in the final increasing pair and then as `a` in the first descending pair, where the loop breaks before subtraction.

Therefore the remaining total is

$$
\texttt{r}
=
\sum_{i=p}^{n-1}\texttt{nums}[i]
=B.
$$

This careful update order is exactly what counts the peak once in each part.

**A loop invariant**

After processing all increasing pairs through endpoint $t$:

$$
\texttt{l}=\sum_{i=0}^{t}\texttt{nums}[i]
$$

and

$$
\texttt{r}=\sum_{i=t}^{n-1}\texttt{nums}[i].
$$

Initially $t=0$, so `l = nums[0]` and `r` is the full sum. Processing pair $(t,t+1)$ adds `nums[t+1]` to `l` and removes `nums[t]` from `r`, moving the shared boundary from $t$ to $t+1$. The current boundary element belongs to both summaries.

When the boundary reaches the peak, the next pair is descending and the updates stop. The invariant then gives exactly the two requested inclusive sums.

**Returning the requested code**

Once `l` and `r` are complete:

- equality returns `-1`;
- `l > r` returns `0` for the ascending part; and
- otherwise `r > l` returns `1` for the descending part.

The equality check must occur first because the final conditional expression has only the two strict-winner codes.

**Example**

For `nums = [1, 3, 2, 1]`:

- initially, `l = 1` and `r = 7`;
- pair $(1,3)$ is increasing, so `l` becomes 4 and `r` becomes 6;
- pair $(3,2)$ is descending, so the loop breaks.

The sums are $A=4$ and $B=6$. Since the descending sum is larger, the method returns 1.

For `[1,2,4,3]`, the increasing updates leave both variables at 7, so the method returns $-1$.

## Complexity detail

Let $N$ be the array length. Computing `sum(nums)` scans all $N$ values once. `pairwise` then visits adjacent pairs only until the peak transition, at most $N-1$ pairs.

Total time is

$$
O(N).
$$

The source keeps only `l`, `r`, and the current adjacent pair. `pairwise` is an iterator rather than a materialized list. Auxiliary space is

$$
O(1).
$$

The input array is not modified. Python integers safely hold sums as large as $N\cdot10^9$.

Although the loop may stop early when the peak is near the front, the initial full-array sum always costs $O(N)$, so the overall bound remains linear.

## Alternatives and edge cases

- **Find the peak, then sum two slices:** This is straightforward but may allocate slice copies in Python; using index ranges avoids copies but still makes additional passes.
- **Track two sums from scratch:** Once the peak is known, another scan can compute both inclusive sums. The source folds peak detection and boundary adjustment into one pass after the total.
- **Binary-search the peak:** Bitonic structure permits $O(\log N)$ peak discovery, but both part sums still require prefix-sum preprocessing or linear work; it does not improve the complete one-query task.
- **Peak counted twice by definition:** It must remain in both `l` and `r`; subtracting it from the total at the break would be wrong.
- **Equal sums:** The source returns `-1` before checking either winner.
- **Peak near the beginning:** The first descending pair stops the loop with `l` containing only the peak-side prefix and `r` retaining the full descending part.
- **Peak near the end:** Most adjacent pairs are processed; the last value added to `l` is still preserved in `r` as the shared peak.
- **Strict bitonic guarantee:** The source uses only `a > b` as the stopping signal. Equal adjacent values would violate the contract and blur the peak boundary.
- **Positive values:** Positivity is not required for the invariant itself, but it is guaranteed by the problem.
- **Required helper:** Standalone execution needs `pairwise` from Python's `itertools` module.
- **Input preservation:** Neither summation nor pair iteration changes `nums`.
