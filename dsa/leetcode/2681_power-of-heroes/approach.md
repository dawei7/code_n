## General

**Assign every group a unique minimum**

The power of a nonempty group is:

$$
(\text{maximum strength})^2\cdot(\text{minimum strength}).
$$

Enumerating all $2^n-1$ groups is impossible for $n$ up to $10^5$. The solution instead sorts the strengths and processes them from largest to smallest.

When the current strength is $x$, all previously processed heroes have strength at least $x$. The groups counted now are exactly the groups whose newly included current hero is the chosen minimum-position anchor. Such a group consists of $x$ plus any subset of the already processed heroes.

Using sorted positions rather than only values keeps duplicate-strength heroes distinct. Every nonempty subset has one unique position that is processed last, so it is counted once even when several strengths are equal.

**Separate the singleton group**

The group containing only the current hero has both minimum and maximum equal to $x$. Its power is:

$$
x^2\cdot x=x^3.
$$

The first answer update,

`ans = (ans + (x * x % mod) * x) % mod`,

adds this singleton contribution.

Writing the multiplication in modular steps prevents intermediate values from growing unnecessarily, although Python could represent large integers.

**Summarize all choices among larger heroes**

For groups containing $x$ and at least one previously processed hero, $x$ is the minimum. The maximum comes from the chosen subset of larger-or-equal heroes.

Let `p` mean:

> the sum of the squared maximum strength over every nonempty subset of heroes already processed.

For every such old subset with maximum $M$, adding current $x$ creates a group whose power is $M^2\cdot x$. Summing over all old subsets gives:

$$
x\cdot p.
$$

That is the second answer update, `ans = (ans + x * p) % mod`.

**Derive the recurrence for `p`**

After counting groups anchored at $x$, the current hero joins the processed pool. We need the new sum of squared maxima for all nonempty subsets of that enlarged pool.

Those subsets fall into three categories:

1. an old nonempty subset without $x$, contributing the old `p`;
2. that same old subset with $x$ added, whose maximum is unchanged because every old strength is at least $x$, contributing another `p`;
3. the singleton subset containing only $x$, contributing $x^2$.

Therefore:

$$
p_{\text{new}}=2p_{\text{old}}+x^2.
$$

The code implements `p = (p * 2 + x * x) % mod`.

**Why the update order matters**

The contribution `x * p` must use only subsets of heroes processed before $x$. If `p` were updated first, it would include the singleton `{x}` and subsets already containing $x$, causing groups to be counted incorrectly or twice.

The exact order is:

1. add the singleton power;
2. add contributions formed with old subsets;
3. extend `p` for future, smaller heroes.

This mirrors the combinatorial partition directly.

**Trace `[1, 2, 4]`**

After sorting, iteration order is 4, 2, 1.

For $x=4$, `p=0`. The singleton contributes $4^3=64$. Then `p` becomes $4^2=16$, representing the one subset `{4}`.

For $x=2$, the singleton contributes 8. The term `2 * 16 = 32` represents group `{2,4}`. Then `p` becomes `2 * 16 + 4 = 36`. Its meaning is:

- maximum-square 16 for `{4}`;
- maximum-square 4 for `{2}`;
- maximum-square 16 for `{4,2}`.

For $x=1$, the singleton contributes 1 and `1 * 36` contributes all groups containing 1 and at least one larger hero. The total becomes 141.

**Why equal values still work**

Suppose all three strengths are 1. The processing order distinguishes their array positions even though the values match.

The first iteration counts one singleton. The second counts its singleton plus the group using both processed positions. The third counts all four groups containing the third position as the last-processed anchor.

Together the iterations count $1+2+4=7$ nonempty subsets, each with power one.

**Modulo arithmetic preserves the result**

Addition and multiplication can be reduced modulo $10^9+7$ at every step:

$$
(a+b)\bmod M
=
((a\bmod M)+(b\bmod M))\bmod M,
$$

and the analogous rule holds for multiplication.

Thus keeping `ans` and `p` reduced never changes the final required remainder. It only bounds stored numeric values.


Every nonempty group has a unique sorted position that is processed last. At that iteration, its hero is a minimum, and the other chosen heroes form either an empty subset or one of the nonempty previously processed subsets.

The singleton term handles the empty choice. The `x * p` term handles every nonempty choice, with `p` weighting it by the square of its actual maximum. The recurrence proves `p` contains exactly those weights before each iteration.

Therefore every group contributes its power once, no group is omitted, and no group is duplicated.

**Why sorting is essential**

The recurrence assumes adding $x$ to an old nonempty subset never changes that subset's maximum. Processing from largest to smallest guarantees this.

Without ordering, a newly added value might be larger than an old subset's maximum, so duplicating `p` would no longer represent the correct squared maxima.

## Complexity detail

Sorting $n$ strengths costs $O(n\log n)$. The reverse loop performs constant modular arithmetic per element, costing $O(n)$. Total time is $O(n\log n)$.

The in-place sort may use $O(n)$ temporary memory in Python, and `nums[::-1]` explicitly creates a reversed list copy of length $n$. Thus auxiliary space is $O(n)$. The input order is mutated by sorting.

## Alternatives and edge cases

- **Enumerate all subsets:** Direct but exponential, $O(2^n)$, and infeasible.
- **Process ascending by maximum:** A symmetric recurrence can summarize minimum contributions, but its state must be derived carefully.
- **Use reversed iteration without slicing:** `reversed(nums)` avoids the explicit $O(n)$ reversed copy while keeping the same logic.
- **Single hero:** Only the singleton term contributes, returning its cube modulo $M$.
- **Duplicate strengths:** Positions remain distinct, and each subset still has a unique processing anchor.
- **All strengths equal one:** The answer is the number of nonempty subsets, $2^n-1$.
- **Large strengths:** Modular reduction after updates prevents unbounded accumulated state.
- **Input mutation:** `nums.sort()` destroys the original ordering.
- **Update `p` too early:** This would include the current hero in the old-subset summary and double-count groups.
- **Forget the singleton:** `x * p` covers only groups with another processed hero.
- **Maximum and minimum roles:** The current descending value is the minimum anchor, while `p` encodes squared maxima.
