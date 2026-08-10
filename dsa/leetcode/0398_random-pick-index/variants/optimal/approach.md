## General

**Sample matching indices without storing them**

The method must choose uniformly among all indices whose value equals `target`. It could first collect those indices and then choose one, but that allocates space proportional to the number of matches on every call. The exact solution instead applies reservoir sampling with reservoir size one while scanning the stored array.

The constructor simply retains the array as `self.nums`. During `pick(target)`:

- `n` counts how many matching indices have been seen so far;
- `ans` stores one candidate index selected uniformly from those matches.

Nonmatching elements are ignored. A match is allowed to replace the current candidate with probability $1/n$, where `n` is the updated number of matches.

**Process only the relevant population**

The loop visits every `(i, v)` pair from `enumerate(self.nums)`. When `v != target`, the index does not belong to the sampling population, so neither `n` nor `ans` changes.

When `v == target`, `n += 1` gives this occurrence its one-based rank among matching indices. The code draws

```text
x = random.randint(1, n)
```

uniformly from the inclusive integers `1` through `n`. It replaces `ans` with `i` exactly when `x == n`. Since one of the `n` equally likely results triggers replacement, the new matching index is selected with probability $1/n$.

The specific trigger could be `x == 1` instead; choosing the endpoint `n` has the same probability. What matters is one successful outcome among `n` uniform outcomes.

**Why the first match always initializes a real answer**

The method begins with `n = ans = 0`. Index zero is a legal array index and is not being used as a safely distinguishable sentinel. The target-exists guarantee makes that harmless.

At the first match, `n` becomes one. `random.randint(1, 1)` must return one, so `x == n` is true and `ans` is replaced by the actual matching index. From then onward, `ans` always refers to one of the matches seen so far.

If the target did not exist, the placeholder zero would be returned incorrectly. The problem explicitly rules out that call, so the implementation needs no absent-target behavior.

**The reservoir invariant**

After processing any prefix containing $j$ matching indices, each of those $j$ indices has probability exactly $1/j$ of being stored in `ans`.

The base case is $j=1$: the first matching index is selected with probability one.

Assume the invariant holds after $j-1$ matches. When match $j$ arrives:

- the new index replaces the reservoir with probability $1/j$, so its selection probability is $1/j$;
- any earlier index was selected with probability $1/(j-1)$ and remains selected only when no replacement occurs, with probability $(j-1)/j$.

For an earlier index, the combined probability is

$$
\frac{1}{j-1}\cdot\frac{j-1}{j}=\frac{1}{j}.
$$

Thus all $j$ matching indices are uniform after the update. By induction, when the array scan ends with $m$ total matches, every valid index is returned with probability $1/m$.

**A survival view of one fixed match**

Suppose an index is the $j^{\text{th}}$ target occurrence among $m$ total matches. It enters the reservoir with probability $1/j$. At the next match it survives with probability $j/(j+1)$, then $(j+1)/(j+2)$, and so on. Its final probability is

$$
\frac{1}{j}
\cdot\frac{j}{j+1}
\cdot\frac{j+1}{j+2}
\cdots
\frac{m-1}{m}
=\frac{1}{m}.
$$

The factors cancel. Early matches enter more easily but face more future replacement opportunities. Late matches enter less often but have fewer chances to be displaced. These effects balance exactly.

**Tracing the example target**

For `nums = [1, 2, 3, 3, 3]` and `target = 3`, matches occur at indices `2`, `3`, and `4`.

- At index `2`, `n = 1`, so it is chosen with certainty.
- At index `3`, `n = 2`, so it replaces index `2` with probability $1/2$. Afterward, each of indices `2` and `3` has probability $1/2$.
- At index `4`, `n = 3`, so it replaces the current candidate with probability $1/3$. If it does not replace, the existing uniform choice survives with probability $2/3$.

The final probabilities are:

$$
P(2)=\frac12\cdot\frac23=\frac13,
\qquad
P(3)=\frac12\cdot\frac23=\frac13,
\qquad
P(4)=\frac13.
$$

A particular call may return any one of them. Uniformity concerns the distribution over many independent calls, not a fixed output order.

**Why matching values do not need to be distinct**

The sampling objects are indices, not values. Every qualifying index participates as a separate event even though all contain the same `target`. This is exactly what the interface requests: choose among positions where the target occurs.

If there is only one match, it is selected at `n = 1` and can never be replaced by a nonmatching element, so the answer is deterministic.

**Every call starts a fresh sample**

`pick` resets `n` and `ans`, then scans from the beginning. Random choices from earlier calls do not affect the next call. The same index may be returned on consecutive calls because sampling is with replacement across calls; `pick` never removes an array occurrence.

## Complexity detail

Let $N$ be the array length and $Q$ be the number of `pick` calls.

The constructor stores one reference and takes $O(1)$ time in the exact source. One `pick` visits all $N$ array elements, performing constant work per element and random generation only at matches. Its time is $O(N)$. Across $Q$ calls, total time is $O(NQ)$.

This differs from the variant manifest’s `O(n + q)` time and `O(n)` space, which describe preprocessing a map from values to their index lists once and then choosing from a stored list in $O(1)$ per query. The exact solution performs no such preprocessing; it chooses constant extra space at the cost of rescanning for every query.

Beyond the input reference, `pick` uses only `n`, `ans`, `i`, `v`, and `x`, so auxiliary working space is $O(1)$. The object retains the caller’s array reference but does not copy it. If retained input storage is counted as object state, the referenced data has size $O(N)$ but is not newly allocated by this implementation.

## Alternatives and edge cases

- **Preprocess value-to-indices lists:** In the constructor, append every index to a dictionary bucket for its value. Initialization takes $O(N)$ time and space, and each `pick` uses `random.choice` in $O(1)$. Across many calls this gives $O(N+Q)$ time, matching the manifest, but uses linear extra storage.

- **Collect matches on every call:** Build a temporary list of all qualifying indices and choose from it. This is $O(N)$ time and up to $O(N)$ temporary space per call; reservoir sampling achieves the same distribution with constant space.

- **Choose a random array index until it matches:** Rejection sampling is unbiased, but expected time can be very large when the target is rare and has no finite worst-case bound. A full reservoir scan has deterministic linear work.

- **One matching index:** The first-match rule selects it with probability one, regardless of how many nonmatching values surround it.

- **Every index matches:** Reservoir sampling becomes a uniform sample from all indices, still using constant space.

- **Target at index zero:** Initial `ans = 0` does not create bias; index zero is selected only through the mandatory first-match replacement, then participates in normal survival probabilities.

- **Target guaranteed present:** This guarantee is essential to the exact initialization. Without it, an explicit sentinel or exception would be required.

- **Negative and extreme values:** Values are compared for equality only, so their numeric range does not affect the algorithm.

- **Repeated calls for different targets:** Each call filters the array anew and establishes a separate reservoir over only that target’s matching indices.

- **Random repeat outcomes:** Returning the same valid index several times in a row is possible and does not indicate incorrectness. Statistical validation needs many trials and tolerance for sampling variance.

- **Input aliasing:** The constructor stores `nums` directly. If external code mutates that list later, subsequent calls sample the modified contents. The challenge’s normal object model treats the input array as stable; a defensive API could copy it at $O(N)$ cost.

- **Random API endpoints:** `randint(1, n)` is inclusive at both ends. Exactly one outcome must trigger replacement to obtain probability $1/n$.
