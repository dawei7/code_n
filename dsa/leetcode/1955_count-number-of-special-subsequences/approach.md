## General

**Track how far a subsequence has progressed**

A special subsequence has three nonempty phases: zeroes, then ones, then twos. For each prefix ending at input index $i$, the table stores:

- `f[i][0]`: subsequences consisting of one or more zeroes;
- `f[i][1]`: subsequences consisting of one or more zeroes followed by one or more ones;
- `f[i][2]`: complete special subsequences with positive zero, one, and two phases.

Subsequences are distinguished by chosen indices. This is why including or excluding a newly encountered matching value creates different counted choices even when their value sequences look identical.

**Initialize the first position**

At index zero, the only state that can exist is a zero-only subsequence, and only when `nums[0] == 0`. Python stores that Boolean as zero or one in `f[0][0]`. The other two entries remain zero because no earlier zero and later phase value exist.

**Transition on a zero**

When current value is zero, each existing zero-only subsequence has two choices: skip this zero or append it. That doubles `f[i - 1][0]`. The singleton subsequence containing only the current zero supplies one more:

`f[i][0] = 2 * f[i - 1][0] + 1`.

States one and two are copied unchanged. Appending a zero after a one or two would violate phase order, so the current zero can only be skipped for those states.

**Transition on a one**

An existing zero-only subsequence can append the current one and start its required one phase, contributing `f[i - 1][0]` new state-one subsequences.

Each existing zero-one subsequence may skip or append the current one, contributing twice `f[i - 1][1]`. Therefore:

`f[i][1] = f[i - 1][0] + 2 * f[i - 1][1]`.

Zero-only and complete states are copied. A one cannot be appended after twos.

**Transition on a two**

The same reasoning advances state one into state two. Every zero-one subsequence can append the current two to create its first two, while every already complete subsequence can either skip or append it:

`f[i][2] = f[i - 1][1] + 2 * f[i - 1][2]`.

Earlier states are copied because a two cannot help them without skipping the required intermediate phase.

Every updated expression is reduced modulo $10^9+7$.

**Why the recurrence counts exactly the right index sets**

For the current value, every valid subsequence either excludes its index or includes it. Excluding it accounts for one copy of the prior same-phase count. Including it either extends the same phase or starts the next phase from the immediately previous phase. These cases are disjoint because they differ on whether the current index is chosen and on the earlier phase state.

No transition skips a required positive phase: state one can start only from a nonempty state zero, and state two only from a nonempty state one. No transition moves backward. By induction over input prefixes, the three table entries have exactly their stated meanings.

After the full array, `f[n - 1][2]` counts all and only complete special subsequences.

For `[0,1,2,2]`, the first two values establish one zero-one subsequence. The first two creates one complete subsequence. The second two can be excluded from that existing subsequence, appended to it, or appended as the first two to the zero-one prefix, producing three total index selections.

## Complexity detail

Let $N$ be the input length.

The loop processes each element once and performs a constant number of arithmetic operations, so time is $O(N)$.

The exact source allocates `f` as $N$ rows of three integers, so auxiliary space is $O(N)$. This differs from the manifest's $O(1)$ claim. Because each row depends only on the previous row, three scalar counters or two rows would achieve constant space, but that optimization is not present in the provided solution.

Modulo reduction keeps stored values bounded while preserving the final requested remainder.

## Alternatives and edge cases

- **Three scalar counters:** Update zero, one, or two phase counts in place according to the current value. This implements the same recurrence in $O(1)$ space.
- **Enumerate subsequences:** There are $2^N$ index subsets, so direct generation is infeasible.
- **No zero:** State zero never becomes positive, so no later state can start and the answer is zero.
- **No one after a zero:** State one remains zero, preventing complete subsequences.
- **No two after both earlier phases:** State two remains zero.
- **Values in reverse order:** Later zeroes cannot extend one/two states, so an array such as `[2,1,0]` yields zero.
- **Repeated value in a phase:** Include-or-exclude choices double existing subsequences, correctly distinguishing index sets.
- **Single element:** Initialization may create a zero-only subsequence, but state two remains zero.
- **Positive phase requirement:** There is no transition directly from zero state to two state, so ones cannot be omitted.
- **Modulo:** Every state-changing recurrence applies the modulus; copied prior entries are already reduced.
- **Exact-space distinction:** The table is pedagogically explicit but linear-space; describing this exact source as constant-space would be inaccurate.
