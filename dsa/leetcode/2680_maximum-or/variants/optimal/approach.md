## General

**Multiplying by two is a left shift**

For a nonnegative integer $x$, multiplying by two moves every set bit one position left. Applying the operation $k$ times to the same element produces:

$$
x\cdot 2^k=\texttt{x << k}.
$$

The question is therefore where to concentrate up to $k$ left shifts before taking the bitwise OR of all elements.

**Why an optimum concentrates all shifts on one element**

Consider any allocation of the $k$ operations among several positive elements. Look at an element whose shifted value contains the highest set bit in the resulting array, and suppose that element received $s$ shifts.

If $s<k$, shifting that same element all $k$ times instead moves its highest set bit another $k-s$ positions left. This creates a set bit strictly above the highest bit of the distributed result. Any integer with that higher leading bit is numerically larger than the entire distributed OR, regardless of lower bits that may disappear when other elements are left unshifted.

If $s=k$, all operations were already concentrated on that element.

Thus a distributed allocation cannot beat every concentrated candidate. It is sufficient to try each index as the one element receiving all $k$ shifts. Since inputs are positive, an optimal result can use all available operations.

**What remains unchanged for one candidate**

When index $i$ is chosen:

- `nums[i]` becomes `nums[i] << k`;
- every index before $i$ stays unchanged;
- every index after $i$ stays unchanged.

The candidate result is:

$$
\operatorname{OR}(\text{before }i)
\mathbin{|}
(\texttt{nums[i] << k})
\mathbin{|}
\operatorname{OR}(\text{after }i).
$$

Computing the unchanged OR from scratch for every index would make the algorithm quadratic. Prefix and suffix summaries supply those two parts in constant time.

**Build suffix OR values**

Array `suf` has length $n+1$. Entry `suf[i]` stores the OR of `nums[i]` through `nums[n-1]`.

The extra entry `suf[n] = 0` represents an empty range because zero is the identity for OR.

Moving from right to left, the recurrence is:

`suf[i] = suf[i + 1] | nums[i]`.

Therefore `suf[i + 1]` is exactly the OR strictly after candidate index $i$.

**Maintain the prefix incrementally**

Variable `pre` begins at zero and, before processing index $i$, equals the OR of all elements strictly before $i$.

The candidate is evaluated as:

`pre | (x << k) | suf[i + 1]`.

Only after evaluation does the code execute `pre |= x`. This ordering is essential: including `x` in `pre` would incorrectly keep both the original and shifted versions of the chosen element.

At the next iteration, the invariant advances by one position.

**Trace a two-element example**

For `nums = [12, 9]` and `k = 1`, suffix preprocessing gives the unchanged ORs to the right.

Choosing 12 yields `24 | 9 = 25`. Choosing 9 yields `12 | 18 = 30`. The algorithm records the larger candidate, 30.

This corresponds to changing the array to `[12, 18]`.

**Trace prefix and suffix boundaries**

At index zero, `pre` is zero because nothing lies to the left. At the last index, `suf[i + 1]` is `suf[n] = 0` because nothing lies to the right.

The identity value makes the same formula valid at both ends, avoiding special-case branches.

For a one-element array, both unchanged sides are zero, so the only candidate is that value shifted $k$ times.

**Why ordinary OR monotonicity is not enough**

Left-shifting an element can remove set bits from their original positions, so it is not correct merely to say that every individual bit of the old OR is preserved.

The concentration proof instead relies on numeric significance: moving the selected leading bit strictly higher dominates all possible lower-bit losses. This explains why testing concentrated choices is valid even though their lower-bit patterns can differ greatly.


The concentration argument proves that at least one optimal operation plan applies all $k$ shifts to a single index.

For every possible chosen index, the prefix invariant supplies the OR of unchanged earlier elements, the shifted expression supplies the transformed chosen value, and `suf[i + 1]` supplies the OR of unchanged later elements. Their OR is exactly that plan's result.

The loop takes the maximum over all indices, so it includes an optimal concentrated plan and returns the global maximum.

**Why summaries are preferable to division or bit removal**

OR has no inverse. Given the OR of the full array, one cannot reliably “remove” one element's bits because the same bits may also be supplied by other elements.

Separate prefix and suffix ORs avoid needing an inverse. They construct the OR excluding index $i$ from ranges that never included it.

## Complexity detail

Suffix construction visits $n$ elements once, and the candidate loop visits them once more. Each shift, OR, comparison, and assignment is constant time under the problem's bounded integer widths. Total time is $O(n)$.

The suffix array uses $n+1$ integers, so auxiliary space is $O(n)$. The prefix, answer, loop index, and current value use $O(1)$ additional space. The input is not modified.

## Alternatives and edge cases

- **Try every index and recompute all other ORs:** Correct but $O(n^2)$.
- **Prefix and suffix arrays both:** Also $O(n)$ time, but one running prefix is enough.
- **Bit-frequency counts:** Counts can maintain the OR excluding one index with constant bounded-bit work and reduce range storage.
- **Distribute shifts greedily by current value:** Not justified by bitwise interactions; the concentration theorem is the needed argument.
- **Single element:** The result is simply `nums[0] << k`.
- **Chosen first element:** Empty prefix contributes zero.
- **Chosen last element:** Empty suffix contributes zero.
- **Duplicate bits across elements:** Prefix and suffix OR naturally preserve a bit if any unchanged element supplies it.
- **Large values:** Python integers avoid overflow when shifting.
- **Use exactly all operations:** Positive inputs and the leading-bit argument ensure an optimum need not leave shifts unused.
- **Do not mutate `nums`:** Candidates are evaluated algebraically, so each starts from the original array.
- **Update prefix too early:** This would include the chosen number both unshifted and shifted and produce an invalid candidate.
