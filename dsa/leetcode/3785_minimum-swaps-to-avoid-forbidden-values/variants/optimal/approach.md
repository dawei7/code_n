## General

**Separate global feasibility from current conflicts**

Swaps preserve the multiset of `nums`. Before minimizing swaps, the source asks whether any permutation can avoid all forbidden values.

Let $M_v$ be the number of occurrences of value $v$ in `nums`, and let $F_v$ be the number of positions whose forbidden value is $v$. An occurrence of $v$ may be placed only in the other $N-F_v$ positions. Therefore feasibility requires

$$
M_v\le N-F_v,
$$

or equivalently $M_v+F_v\le N$, for every value appearing in `nums`.

The two `Counter` objects store $M_v$ and $F_v$. If any source value violates the inequality, the method returns `-1`.

**Why that feasibility condition is also sufficient**

Think of each value occurrence as an item and each array index as a destination. An item of value $v$ connects to every destination except those with forbidden value $v$.

For a set of items all having one value $v$, the condition above guarantees enough allowed destinations. If a set contains at least two different values, its combined allowed destinations include every index: an index forbids only one value, so it cannot simultaneously forbid both distinct values.

These are exactly the restrictive cases of the matching condition. Thus the per-value inequalities guarantee a complete assignment of all occurrences to legal positions, not merely a necessary count check.

**Focus swap counting on currently bad positions**

An index is bad when `nums[i] == forbidden[i]`. The source counts bad indices by their shared offending value in `bad_count`.

Let

$$
B=\sum_v B_v
$$

be the total number of bad positions and

$$
M=\max_v B_v
$$

be the largest same-value bad group. The source computes both, using a default of zero when no bad position exists.

Good positions need not be changed unless they serve as temporary helpers. The two quantities $B$ and $M$ completely determine the minimum once global feasibility is known.

**Derive the two unavoidable lower bounds**

One swap touches only two indices, so it can repair at most two bad positions. Repairing $B$ bad positions requires at least

$$
\left\lceil\frac B2\right\rceil
$$

swaps, implemented as `(total_bad + 1) // 2`.

Now consider the largest bad group, whose positions all contain and forbid the same value $v$. Swapping two positions inside this group changes nothing because both hold $v$. A single swap can therefore repair at most one member of this group. At least $M$ swaps are required.

Both restrictions apply simultaneously, giving the lower bound

$$
\max\left(M,\left\lceil\frac B2\right\rceil\right).
$$

**Why the lower bound can be attained**

Bad positions with different offending values are natural partners. Swapping values $x$ and $y$ between an $x$-bad position and a $y$-bad position fixes both because $x\ne y$: each position receives a value different from what it forbids.

When no bad value occurs more than half the time, the groups can be paired across different values. If $B$ is even, all positions can be repaired in $B/2$ such swaps. If $B$ is odd, the final three differently compatible positions can be handled by two swaps, giving $\lceil B/2\rceil$ total.

When one value $v$ is dominant, pair every non-$v$ bad position with a $v$-bad position first. Each such swap fixes two positions. The remaining bad positions all belong to the dominant group and each needs one additional swap through a compatible already-good position or exchange chain.

The earlier feasibility inequalities guarantee enough destinations that do not forbid $v$ and enough non-$v$ values to complete these exchanges without creating a permanent conflict. The count becomes exactly one swap per original dominant-group position, namely $M$.

Thus the same maximum that is a lower bound is also achievable. The source can return the formula without constructing the actual swap sequence because only the minimum count is requested.

**Trace the examples by bad groups**

For `nums=[1,2,3]` and `forbidden=[3,2,1]`, only index one is bad with value 2. Thus $B=M=1$ and the formula returns one. A compatible good position serves as its swap partner.

For `[4,6,6,5]` against `[4,6,5,5]`, bad groups are value 4 once, value 6 once, and value 5 once. Hence $B=3$, $M=1$, and $\lceil B/2\rceil=2$. The answer is two.

For `nums=[7,7]` and `forbidden=[8,7]`, value 7 occurs twice while only one position allows it. $M_7+F_7=2+1>2$, so no permutation exists and the method correctly stops before using the swap formula.

## Complexity detail

Building the source and forbidden counters takes $O(N)$ expected time. The feasibility scan visits at most $N$ distinct source values. Building `bad_count` and summing it are also linear.

Total expected time is $O(N)$.

The counters may store $O(N)$ distinct values, so auxiliary space is $O(N)$. The arrays themselves are not mutated because the source returns only the minimum count.

## Alternatives and edge cases

- **Construct a target permutation then count cycles:** This can recover an explicit swap plan but requires a careful matching choice; the counting formula avoids unnecessary construction.
- **Greedily swap arbitrary bad pairs:** Equal offending values do not fix each other, and careless helper choices can create new conflicts.
- **Check only `nums` frequencies:** Feasibility depends on how many destinations forbid each value, so `forbidden_count` is essential.
- **Use only $\lceil B/2\rceil$:** A dominant same-value group may require more because one swap fixes at most one of its members.
- **Use only $M$:** When bad values are balanced, the two-bad-per-swap limit may be larger.
- **No bad indices:** Both $B$ and $M$ are zero, so the answer is zero.
- **One bad index:** It needs one compatible helper swap if the instance is feasible.
- **All bad indices share one value:** Feasibility may fail; if it holds through other positions, each bad member needs its own swap.
- **Odd number of balanced bad positions:** The ceiling accounts for the final repair requiring two-swap handling rather than a fractional pair.
- **Values absent from `nums`:** They need no feasibility iteration because no item of that value must be placed.
- **Large arbitrary values:** Counters avoid dependence on the numeric range.
- **Input preservation:** No actual swaps are performed.
