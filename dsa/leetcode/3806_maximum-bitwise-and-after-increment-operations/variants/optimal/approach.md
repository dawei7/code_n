## General

**Build the AND mask from its most valuable bits**

Bitwise AND contains a bit only when every selected final value contains it. The source greedily considers answer bits from high to low.

At one iteration, `target = ans | (1<<bit)` asks whether the already accepted bits plus this new bit can simultaneously be forced into at least `m` array values within budget `k`.

If feasible, keeping the bit maximizes the result lexicographically in binary. No combination of lower bits can compensate for rejecting a feasible higher bit.

**Find the cheapest increment for one value**

For original value `x` and required mask `target`, the final value `y>=x` must satisfy

$$
y\mathbin{\&}\texttt{target}=\texttt{target}.
$$

`target & ~x` identifies required bits currently missing from `x`. Its `bit_length()`, named `j`, is one above the highest missing bit.

If no bit is missing, `j=0` and cost is zero.

Otherwise, only the low `j` bits must be changed. Higher required bits are already present in `x` and can remain unchanged.

`mask=(1<<j)-1` selects those low bits. The source computes

`cost = (target&mask) - (x&mask)`.

At the highest differing low bit, target has one and `x` has zero, so the target low pattern is numerically larger regardless of lower bits. Adding this positive difference changes the low `j` bits exactly to the minimal pattern containing every required bit and does not carry into higher bits.

**Why that increment is minimal**

Any smaller nonnegative increment leaves the low `j`-bit value below `target&mask`. Because the highest missing bit is the most significant difference, such a value cannot contain that required bit together with the required higher-low bits.

The computed final low pattern sets non-required lower bits to zero where doing so minimizes value. Thus no smaller reachable integer can satisfy the mask.

**Choose the cheapest `m` indices**

The method computes this independent cost for every `nums[i]` and sorts `cost`.

Any size-`m` subset requires the sum of its individual forcing costs. Since operations on different indices do not interact, the cheapest feasible subset is exactly the first `m` sorted costs.

If their sum is at most `k`, `target` is feasible and becomes the new `ans`. Otherwise no other subset can meet the mask within budget.

The cost list is reused. Although sorting changes its order, the next bit iteration overwrites every position while enumerating `nums`, so no association from the previous sort is needed.

Only the sum of the cheapest `m` costs matters. The source does not retain their indices because every later candidate recomputes all costs from the original `nums` values.

**Why greedy bit acceptance is globally optimal**

Feasibility is downward-closed in masks: if values can contain all bits of `target`, they also contain any subset of those bits.

Processing high to low maintains the greatest feasible prefix of the answer's binary representation. When a candidate high bit is infeasible together with accepted bits, every number containing that same prefix and bit is infeasible regardless of lower choices. When feasible, any answer omitting it is smaller than one retaining it.

After the final bit, `ans` is the largest feasible mask and therefore the maximum attainable AND.

**Choose a sufficient bit range**

One index can increase by at most the whole budget, so no final selected value exceeds `max(nums)+k`. The AND cannot contain a bit above that number's bit length.

`mx=(max(nums)+k).bit_length()` gives a safe highest exclusive bit. The loop tests every potentially useful bit down to zero.

## Complexity detail

Let $B$ be the bit length of `max(nums)+k`, at most about 31 under the constraints.

For each bit, the source computes $N$ costs, sorts them in $O(N\log N)$, and sums `m` entries. Total time is $O(BN\log N)$, simplified to $O(N\log N)$ when fixed-width $B$ is treated as a constant.

The cost array uses $O(N)$ auxiliary space. Inputs are not modified.

## Alternatives and edge cases

- **Binary search the numeric answer:** Feasibility is not monotone in ordinary numeric order; bitwise greedy uses mask containment.
- **Try every subset:** There may be exponentially many size-`m` choices; sorting costs selects the cheapest.
- **Increase every chosen value to `target` exactly:** Values may already exceed target while containing its bits; the low-bit formula finds the next minimal satisfying value.
- **Ignore carries:** Selecting through the highest missing bit is what makes the subtraction and higher-bit preservation valid.
- **`m=1`:** The method chooses the single cheapest value for each candidate mask.
- **`m=N`:** All individual costs must fit the budget.
- **Already contains target:** Missing-bit expression is zero and cost is zero.
- **Unused budget:** The contract allows at most `k` operations.
- **Equal costs:** Any tied indices form an equally valid subset.
- **Bit range:** No bit above `max(nums)+k` can appear.
- **Input preservation:** Sorting applies to `cost`, not `nums`.
- **Reused buffer:** Every cost slot is overwritten before the next sort.
