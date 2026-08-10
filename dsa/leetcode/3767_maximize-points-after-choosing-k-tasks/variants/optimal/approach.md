## General

**Start from one complete legal-choice baseline**

Every task must use exactly one of the two techniques. Imagine initially assigning technique 2 to all $N$ tasks. This gives the baseline

$$
B=\sum_{i=0}^{N-1}\texttt{technique2}[i].
$$

Switching task `i` from technique 2 to technique 1 changes the total by

$$
d_i=\texttt{technique1}[i]-\texttt{technique2}[i].
$$

The original problem is now: choose at least `k` gains `d_i` to add to `B`. A positive gain makes technique 1 better for that task, a zero gain makes the techniques equivalent, and a negative gain is the penalty paid for using technique 1 there.

This transformation is powerful because the baseline already accounts for every task exactly once. Each later switch only needs to replace one contribution, which the source writes as subtracting `technique2[i]` and adding `technique1[i]`.

**Sort tasks by their switching gain**

The source builds all indices and sorts them by

`-(technique1[i] - technique2[i])`.

Sorting an ascending key after negation places the actual gains in nonincreasing order. If the sorted indices are `idx`, then

$$
d_{\texttt{idx}[0]} \ge d_{\texttt{idx}[1]} \ge \cdots \ge d_{\texttt{idx}[N-1]}.
$$

Keeping indices instead of sorting gain values alone preserves access to both original technique arrays when the score is updated.

**Use technique 1 for the first `k` sorted tasks**

At least `k` tasks must use technique 1, even when every switch loses points. Among all ways to satisfy these mandatory slots, the least damaging—or most rewarding—choice is the `k` largest gains.

The first loop visits `idx[:k]` and changes each corresponding baseline assignment to technique 1. It does not test whether the gain is positive because the quota is compulsory. A negative gain among these first `k` values is still better than every gain sorted after it.

For example, suppose the gains are `[5,-2,-7]` and `k=2`. Technique 1 must be used twice. Taking 5 and -2 adds 3 to the baseline; taking 5 and -7 would subtract 2 overall, and taking both negative values would be worse still.

**Take every additional nonnegative gain**

After the quota is satisfied, each remaining task is optional: either leave its technique-2 baseline contribution or switch it to technique 1.

The source switches when

`technique1[i] >= technique2[i]`,

which is exactly `d_i >= 0`. A positive gain strictly improves the result. A zero gain leaves the score unchanged and is harmless. A negative gain would reduce the score without helping an already-satisfied minimum quota, so it is skipped.

The second loop begins at `idx[k:]`. This matters because the mandatory tasks have already been switched and must not be applied twice.

**Why the `k` largest gains satisfy the quota optimally**

Consider any feasible selection of at least `k` tasks for technique 1. If it selects a gain `d_b` while leaving a larger gain `d_a > d_b` unselected, exchanging `b` for `a` preserves the number of technique-1 tasks and increases the total by `d_a-d_b`.

Repeating this exchange means an optimal selection can always contain the first `k` gains in sorted order. This remains true when some or all gains are negative: “largest” then means closest to zero and therefore the smallest unavoidable losses.

Once those first `k` choices are fixed, optional gains are independent. Adding any remaining positive gain improves the objective, adding zero preserves it, and adding a negative gain worsens it. The source makes exactly those locally optimal optional decisions.

Equivalently, the chosen set is the union of:

- the indices of the top `k` gains, which enforce feasibility;
- every other index with nonnegative gain, which cannot hurt the score.

This set has size at least `k` and maximizes the sum of selected gains. Adding it to the all-technique-2 baseline yields the maximum original score.

**Trace the first example through gains**

For `technique1=[5,2,10]` and `technique2=[10,3,8]`, the baseline is $10+3+8=21$. The gains are -5, -1, and 2.

With `k=2`, the two largest gains are 2 and -1. Switching those tasks changes the total to

$$
21+2-1=22.
$$

The remaining gain -5 is negative and therefore skipped. This corresponds to technique 2 on task zero and technique 1 on tasks one and two.

When all gains are positive, as in the second example, the first loop enforces `k` switches and the second loop switches every remaining task too. The “at least” wording is what permits—and requires for optimality—more than `k` technique-1 tasks.

**The manifest describes a different complexity**

The manifest gives $O(N\log(K+1))$ time and $O(K)$ space, which would fit a bounded heap that retains only selected gains. The exact source sorts all $N$ indices. Its actual time is $O(N\log N)$ and its index array occupies $O(N)$ space.

The source is still algorithmically correct; the mismatch concerns the implementation strategy and resource claims. This document follows the code that actually runs.

## Complexity detail

Let $N$ be the number of tasks and $K=\texttt{k}$.

Computing the technique-2 sum costs $O(N)$ time. Sorting `range(N)` by descending difference costs $O(N\log N)$ time. The two slices together cover all sorted indices and the two loops perform $O(N)$ score updates, so sorting dominates.

The actual total time complexity is $O(N\log N)$.

The sorted `idx` list stores $N$ Python integers. The slices `idx[:k]` and `idx[k:]` also create temporary lists whose combined length is $N$, so the peak auxiliary usage remains $O(N)$. The input arrays are not modified.

The manifest's $O(N\log(K+1))$ time and $O(K)$ space do not describe this full-sort source. They would require a different selection implementation.

## Alternatives and edge cases

- **Size-`k` heap:** A bounded heap can track the `k` largest mandatory gains while separately accounting for optional positive gains, potentially achieving the manifest's $O(N\log(K+1))$ time and $O(K)$ space. It is not the exact implementation.
- **Quickselect:** Partitioning around the kth-largest gain can obtain expected linear selection time, followed by a scan, but requires careful duplicate handling.
- **Dynamic programming by task and quota:** It can model the choices but costs at least $O(NK)$ time and is unnecessary because tasks interact only through a minimum count.
- **Choose the `k` largest technique-1 values:** The correct comparison is the gain relative to technique 2. A large technique-1 score can still be a poor switch if its technique-2 score is even larger.
- **Use exactly `k` tasks:** This loses points whenever a remaining task has positive gain. The contract says at least `k`.
- **`k=0`:** The mandatory slice is empty, and the source switches exactly the tasks whose technique-1 value is at least their technique-2 value.
- **`k=N`:** Every index is in the first slice, the optional loop is empty, and all tasks use technique 1.
- **All gains negative:** The source takes exactly the `k` least-negative gains and leaves every other task on technique 2.
- **All gains positive:** Every task ultimately switches to technique 1, even when `k` is smaller than `N`.
- **Zero gain:** The second loop switches it because of `>=`, but the score is identical either way.
- **Equal gains:** Their sorted relative order does not matter because exchanging equal gains leaves the total unchanged.
- **Large total:** Python integers avoid fixed-width overflow when many large point values are added.
- **Input preservation:** The method creates and sorts an index list rather than rearranging either score array.
- **Source/manifest complexity mismatch:** Performance analysis for this file must use full sorting and $O(N)$ auxiliary storage.
