## General

For a fixed cap $x$, every original value falls into one of two groups:

- if `nums[i] <= x`, capping does not change it, so its contribution remains `nums[i]`; or
- if `nums[i] > x`, capping changes it to exactly $x$.

This split is the central idea. The first group contains ordinary values whose subset sums can be maintained with a bitset. Every value in the second group is identical after capping, so choosing from that group depends only on **how many copies of $x$** are selected.

The algorithm processes caps from $1$ through $n$. As the cap increases, more original values permanently enter the first group. Values still above the cap remain in the identical-copy group and do not need to be inserted into the subset-sum state yet.

**Counting values before processing caps**

The constraints guarantee `1 <= nums[i] <= n`, so the source builds an array

`frequency = [0] * (n + 1)`

and increments `frequency[value]` for every input element. This lets the outer loop find all occurrences that become fixed when the cap reaches a particular value without rescanning `nums`.

Across all caps, the inner insertion loop runs once per original occurrence:

`for _ in range(frequency[cap]):`

An element with original value $v$ is inserted exactly when `cap == v`. Before that moment it belongs to the group that gets changed to the current cap. From that moment onward, increasing the cap no longer changes it, so its original value can remain permanently in the subset-sum state.

**Representing many subset sums in one integer**

The integer `reachable` is used as a bitset. Bit position $s$ is one exactly when the already-fixed elements contain a subsequence whose sum is $s$.

Initially,

`reachable = 1`

which has only bit zero set. This represents the empty subsequence with sum zero. Keeping sum zero is essential because a valid target may be formed entirely from currently capped copies, or a fixed value may begin a new nonempty selection.

When one fixed element of value `cap` is introduced, the update is:

`reachable |= reachable << cap`

Every old set bit at position $s$ moves to $s+\textit{cap}$ after the left shift. Those shifted bits represent taking the new occurrence. OR-ing with the original bits preserves the option of not taking it.

The update is performed once for every occurrence, even when several elements have the same value. This is still a zero-or-one subsequence choice per array position: during one update, that occurrence can be included once; the next repeated update corresponds to a different occurrence and permits another copy.

Only sums from zero through $k$ can help. All values are positive, so once a partial sum exceeds $k$, adding more elements can never bring it back down. The mask

`mask = (1 << (k + 1)) - 1`

has bits $0$ through $k$ set. Applying

`reachable &= mask`

after each insertion discards every larger sum and keeps the bitset bounded.

**The meaning of the bitset after each insertion phase**

Immediately after all `frequency[cap]` updates, `reachable` describes exactly the subset sums up to $k$ obtainable from original elements whose values are at most `cap`.

It contains no value greater than the current cap because those elements have not been inserted. That omission is deliberate. Such an element currently contributes `cap` regardless of its original value, and its contribution will change again at the next cap. Permanently inserting its current capped value would leave stale contributions in future iterations.

The variable `fixed_count` records how many input occurrences have now entered the fixed group. After

`fixed_count += frequency[cap]`

the number of still-larger elements is

`capped_count = n - fixed_count`.

Every one of those `capped_count` elements has value exactly `cap` in the array capped by this iteration's value.

**Combining fixed subset sums with identical capped copies**

Suppose a desired subsequence chooses `copies` elements from the still-larger group. Their total contribution is

$$
\textit{copies}\cdot\textit{cap}.
$$

The fixed group must then supply the remainder

$$
k-\textit{copies}\cdot\textit{cap}.
$$

The source enumerates every feasible count from zero upward. There are two upper bounds:

- no more than `capped_count` such elements physically exist; and
- no more than $\lfloor k/\textit{cap}\rfloor$ can be selected without their positive sum exceeding $k$.

Therefore, the exact range is:

`range(min(capped_count, k // cap) + 1)`.

For each count, the expression

`(reachable >> (k - copies * cap)) & 1`

reads the bit for the required remainder. If it is one, a fixed-element subsequence supplies that remainder, and combining it with the chosen capped copies makes exactly $k$. The answer for this cap becomes true and the loop stops early.

If every feasible copy count fails, no decomposition reaches $k$, so the answer for this cap is false.

**Why the two-group test covers every subsequence**

Take any subsequence from the array capped by the current value. Partition its selected indices according to their original values.

Selected indices with original value at most the cap form a subset of the fixed group. Their total is represented in `reachable` because each such occurrence has been inserted with its unchanged value.

Selected indices with original value greater than the cap all contribute the same number, `cap`. Their identities do not affect the sum; only their count matters, and that count lies in the enumerated range.

Thus every possible subsequence appears as one of the tested “fixed remainder plus identical copies” combinations.

Conversely, whenever a tested remainder bit is set, it corresponds to actual fixed occurrences. The chosen number of capped copies does not exceed `capped_count`, so those copies can also be taken from actual distinct array positions. Their union is a real subsequence—any chosen index set can be listed in original order—and its capped sum is exactly $k$. The test cannot report a sum that is not realizable.

**Walking through the first example**

For `nums = [4, 3, 2, 4]` and `k = 5`:

- At cap $1$, no original element is fixed. All four elements become $1$. The only fixed sum is zero, and at most four capped copies total $4$, so $5$ is impossible.
- At cap $2$, the original $2$ enters the bitset, making fixed sums zero and $2$. Three larger elements also become $2$. Testing zero, one, or two capped copies requires fixed remainders $5$, $3$, or $1$, none reachable.
- At cap $3$, the original $3$ is inserted. The fixed values $2$ and $3$ can form sum $5$, so the zero-capped-copy test succeeds immediately.
- At cap $4$, all original values are fixed. The previously reachable sum $5$ remains available, so this cap is also true.

The resulting booleans are `[false, false, true, true]`.

## Complexity detail

Let $n$ be the array length and let the target be $k$.

Building `frequency` takes $O(n)$ time. Across the complete outer loop, every original occurrence is inserted into `reachable` exactly once. In the conventional bitset analysis, shifting and combining a $k+1$-bit state costs $O(k)$ bit work, so these insertions contribute $O(nk)$ time.

For cap $x$, the copy loop executes at most

$$
1+\left\lfloor\frac{k}{x}\right\rfloor
$$

iterations. Summing the nonconstant part over caps gives a harmonic series:

$$
\sum_{x=1}^{n}\left\lfloor\frac{k}{x}\right\rfloor
=O\!\left(k\log(\min(n,k))\right).
$$

Caps larger than $k$ test only zero copies. Their $O(n)$ total work is absorbed by $O(nk)$ because $k \ge 1$. Under the standard bitset model used by the manifest, the total time is therefore $O(nk + k\log n)$.

The exact Python implementation stores the bitset as an arbitrary-precision integer. Its shifts and masks process machine-word chunks of the represented $k+1$ bits rather than performing literally one hardware operation. The stated bound is the conventional algorithmic bitset bound; a low-level interpreter analysis would express these operations in terms of the number of big-integer limbs copied.

The frequency array uses $O(n)$ integer slots. `reachable` and `mask` each represent $O(k)$ bits. The returned `answer` list contains $n$ booleans. Including the output, storage is $O(n+k)$, matching the manifest. If returned output is excluded from auxiliary-space accounting, the working state is still $O(n+k)$ because of `frequency` and the bitsets.

## Alternatives and edge cases

- **Rebuild subset-sum DP for every cap:** Constructing the capped array and running an $O(nk)$ DP independently for all $n$ caps costs $O(n^2k)$. The evolving fixed-group bitset avoids restarting.
- **Insert every currently capped element into the persistent bitset:** This is incorrect because an element with original value above the cap changes from $x$ to $x+1$ on the next iteration. Its old contribution would remain as stale state.
- **Boolean-array knapsack:** A length-$k+1$ boolean array can perform the same zero-or-one updates in $O(nk)$ scalar time. The integer bitset batches many sum states into each shift and OR.
- **Unbounded knapsack update:** Updating in a way that reuses the same occurrence repeatedly would invent copies that do not exist. Repeating the shift once per frequency entry correctly models distinct positions.
- **Empty subsequence:** Bit zero begins set. The target is positive, so the empty subsequence is never the final answer by itself, but it enables selections composed solely of capped copies.
- **Cap equals an original value:** Such occurrences enter the fixed bitset at that cap. Elements originally greater than the cap remain in `capped_count`; both groups may contribute copies of the same numerical value without confusing their available multiplicities.
- **`cap > k`:** No positive capped copy can be used in a sum of $k$, so `k // cap` is zero. The algorithm tests only whether fixed elements already form $k$.
- **Target already reachable:** Once fixed elements can form $k$, that bit remains set as later elements are added. Every later cap will succeed at `copies = 0`.
- **Repeated values:** `frequency` preserves multiplicity, and repeated bitset updates allow selecting any number of distinct occurrences up to that multiplicity.
- **Dropping sums above `k`:** This is safe only because every number is positive. No future addition can reduce an oversized sum back to the target.
