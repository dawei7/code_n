# Guided Example: Minimum Total Cost to Make Arrays Unequal

## 1. The instance we will solve

Two 0-indexed arrays `nums1` and `nums2` have the same length `n`. A single operation
swaps the values stored at any two indices of `nums1`, and its cost is the **sum of
those two indices**. Operations may be repeated as often as we like. We must make
`nums1[i]` differ from `nums2[i]` at every index simultaneously, at the least possible
total cost, or report `-1` when no sequence of swaps can achieve that.

We trace the second official instance:

- $\text{nums1} = [2, 2, 2, 1, 3]$
- $\text{nums2} = [1, 2, 2, 3, 3]$
- required output: `10`

It is the right representative because it contains all three ingredients of the
method: a set of indices that already agree and must be repaired, one value that
dominates that set, and a cheap outside index that must be recruited to break the
domination. The first official instance (no dominating value at all) and the third
(domination that cannot be repaired) appear later as contrasts.

## 2. What one operation really buys

Only `nums1` changes, so the multiset of values in `nums1` is invariant: every swap
just permutes it. The cost of a swap between indices $i$ and $j$ is $i + j$, which is
exactly the price of moving each of the two indices' values.

| index $i$ | `nums1[i]` | `nums2[i]` | already unequal? | must some operation touch $i$? |
|:---|:---|:---|:---|:---|
| 0 | 2 | 1 | yes | no, it already satisfies the condition |
| 1 | 2 | 2 | no | yes, `nums1[1]` must change |
| 2 | 2 | 2 | no | yes, `nums1[2]` must change |
| 3 | 1 | 3 | yes | no |
| 4 | 3 | 3 | no | yes, `nums1[4]` must change |

Two accounting facts follow, and they organise the whole solution.

**Mandatory charges.** If `nums1[i] = nums2[i]`, then the value at $i$ has to be
replaced, and the only thing that changes a value is a swap involving $i$. So index
$i$ takes part in at least one operation and therefore contributes its own index at
least once to the total cost. Writing

$$
C = \{\, i : \text{nums1}[i] = \text{nums2}[i] \,\}, \qquad s = \lvert C \rvert,
$$

every plan pays at least

$$
B = \sum_{i \in C} i ,
$$

which for the traced instance is $B = 1 + 2 + 4 = 7$.

**Disjoint swaps pay each index once.** If the plan is a collection of swaps on
pairwise disjoint index pairs, then no index is charged twice and the total cost is
exactly the sum of the indices involved, with every index in $C$ involved. Cheap
indices are therefore precious, and the interesting question is which *extra* indices
must be drawn into the plan.

## 3. The conflict set and the values it holds

Write $v_i = \text{nums1}[i] = \text{nums2}[i]$ for a conflict index. At such an
index the incoming value must be different from $v_i$, and the values available are
exactly the values currently stored at other indices. Group the conflict indices by
the value they hold:

| conflict value | conflict indices holding it | count $c$ | $2c$ | $s$ | does $2c > s$ hold? |
|:---|:---|:---|:---|:---|:---|
| 2 | 1, 2 | 2 | 4 | 3 | yes |
| 3 | 4 | 1 | 2 | 3 | no |

At most one value can satisfy $2c > s$, because two such values would already account
for more than $s$ conflict indices. In the traced instance the dominating value is
$x = 2$, held by the conflict indices $A = \{1, 2\}$, while $B = \{4\}$ holds the
non-dominating value $3$.

The structure of the repair is now clear. Call a conflict index **x-heavy** if it
holds $x$; there are $c$ of them. Every $x$-heavy index must end up holding something
other than $x$. A swap between one $x$-heavy index and one non-$x$-heavy conflict
index is a double repair: the $x$ moves to the partner, where it is legal because the
partner's own value is not $x$, and the partner's value moves to the heavy index,
where it is legal because it is not $x$. Such internal swaps can fix one $x$-heavy
index each, and there are only $s - c$ non-heavy conflict indices to pair them with.
The number of heavy indices left over is therefore

$$
m = c - (s - c) = 2c - s .
$$

Every one of those $m$ indices needs a value from *outside* the conflict set. In the
traced instance $m = 4 - 3 = 1$: after pairing conflict indices `1` and `2` with the
single non-heavy conflict index `4`, one heavy index still needs an outsider.

When no value satisfies $2c > s$, we set $x$ to nothing and $m = 0$: the conflict set
can repair itself entirely through internal swaps.

## 4. Which outside indices may be recruited

An outside index $j \notin C$ can serve as a partner for a leftover heavy index only
if it survives the exchange. The swap sends its current value into the heavy index,
and it receives the value $x$ that the heavy index is shedding. Both endpoints must
end unequal, so an eligible partner must satisfy three conditions.

| index $j$ | `nums1[j]` | `nums2[j]` | outside the conflict set? | hands over a value $\ne x = 2$? | can end holding $x = 2$? | eligible? |
|:---|:---|:---|:---|:---|:---|:---|
| 0 | 2 | 1 | yes | no, it holds $x$ itself | yes | no |
| 1 | 2 | 2 | no | — | — | no, it is already charged in $B$ |
| 2 | 2 | 2 | no | — | — | no, it is already charged in $B$ |
| 3 | 1 | 3 | yes | yes, the value 1 | yes, `nums2[3] = 3` | yes, cost 3 |
| 4 | 3 | 3 | no | — | — | no, it is already charged in $B$ |

The three conditions are exactly: $\text{nums1}[j] \ne x$ (so the heavy index receives
a genuinely different value), $\text{nums2}[j] \ne x$ (so index $j$ may hold $x$ at the
end), and $j \notin C$ (so that index $j$ does not itself need repairing; a conflict
index is already counted in $B$ and can only be reused at the price of a second
charge).

Only one eligible index exists here, at cost $3$, and exactly $m = 1$ is needed.
Adding it to the mandatory sum gives $B + 3 = 7 + 3 = 10$, the expected output. If
fewer than $m$ eligible indices existed, the instance would be impossible and the
answer would be `-1`.

## 5. Worked trace: repairing the traced instance

The plan consists of two disjoint swaps. The first pairs the non-heavy conflict index
`4` with one heavy index, the second pairs the remaining heavy index with the
recruited helper.

| Swap | Role | Value arriving at the first index | Value arriving at the second index | Both endpoints unequal after? | Cost |
|:---|:---|:---|:---|:---|:---|
| indices `2` and `4` | internal heavy–light repair | index 2 holds 3, against `nums2[2] = 2` | index 4 holds 2, against `nums2[4] = 3` | yes | 6 |
| indices `1` and `3` | heavy index repaired by the helper | index 1 holds 1, against `nums2[1] = 2` | index 3 holds 2, against `nums2[3] = 3` | yes | 4 |
| total | two disjoint swaps, three conflict indices, one helper | — | — | — | 10 |

Checking the final array directly closes the trace. Index `0` was never touched, and
it already satisfied the condition.

| index | final `nums1` | `nums2` | unequal? |
|:---|:---|:---|:---|
| 0 | 2 | 1 | yes |
| 1 | 1 | 2 | yes |
| 2 | 3 | 2 | yes |
| 3 | 2 | 3 | yes |
| 4 | 2 | 3 | yes |

The total cost is $6 + 4 = 10$, matching the mandatory sum plus the one helper:
$1 + 2 + 4 + 3 = 10$. Note that no swap ever reused an index, so each index was
charged exactly once and the accounting is tight.

The next table places this instance beside its neighbours, which show the other two
regimes of the method.

| Instance | $s$ | Mandatory sum $B$ | Dominating value and $c$ | $m = 2c - s$ | Eligible helpers used | Answer |
|:---|:---|:---|:---|:---|:---|:---|
| `nums1 = nums2 = [1,2,3,4,5]` | 5 | 10 | none, $2c \le s$ for every value | 0 | none needed | 10 |
| `nums1 = [2,2,2,1,3]`, `nums2 = [1,2,2,3,3]` | 3 | 7 | $x = 2$, $c = 2$ | 1 | index 3 | 10 |
| `nums1 = nums2 = [1,2,2]` | 3 | 3 | $x = 2$, $c = 2$ | 1 | none exist | -1 |

The first row shows that when no value dominates, repairing the conflict indices
inside their own set already attains the mandatory sum, so the answer is exactly $B$.
The third row is the failure mode: the deficit $m = 1$ cannot be paid at all.

## 6. Invariant and correctness

**Lower bound.** Every conflict index takes part in at least one operation, so the
total cost is at least $B = \sum_{i \in C} i$. If some value $x$ has $2c > s$, then
each of the $c$ heavy indices must shed its $x$. Inside the conflict set only
$s - c$ indices hold a non-$x$ value, so at most $s - c$ heavy indices can be repaired
internally, and at least $m = 2c - s$ replacements must arrive from outside $C$.
An outside index that participates hands over a value different from $x$ and ends up
holding an $x$, so it must satisfy $\text{nums1}[j] \ne x$ and $\text{nums2}[j] \ne x$,
and it must lie outside $C$. Charging every participating index once, the total cost is
at least

$$
B + \bigl(\text{sum of the } m \text{ cheapest eligible indices}\bigr),
$$

and routing a value through several outside indices before it reaches a heavy index
only adds more charged indices to the bill, so an optimal plan may be taken to consist
of disjoint swaps.

**Attainment.** The plan that realises the bound is explicit. If no value dominates,
order the conflict values in a cyclic sequence in which no two neighbours are equal,
which is possible precisely when no value exceeds half of $s$; realise that cycle with
a pivot at index `0`, charging index `0` for free at each step, plus transpositions
for any remaining pairs. Every conflict index is charged once and nothing else is
charged, so the cost is exactly $B$. If a value $x$ dominates, pair each of the
$s - c$ non-heavy conflict indices with a distinct heavy index and swap them, which
repairs both ends; then pair each of the $m = 2c - s$ leftover heavy indices with a
distinct eligible helper and swap those. That plan covers every conflict index exactly
once and every helper exactly once, so it costs exactly
$B + \sum_{j \in H} j$ for the chosen helper set $H$, and its total matches the lower
bound. Hence the method's output is optimal whenever $m$ eligible helpers exist.

**Feasibility.** If fewer than $m$ eligible indices exist, the lower-bound deficit
cannot be paid, so no plan exists and `-1` is correct. The invariant maintained by the
computation is that the pair (conflict set, dominant value and its count) is the
complete description of the obstruction: two instances with the same $s$, the same
dominating count $c$, and the same multiset of eligible helper indices have the same
answer, no matter how the remaining values are arranged.

## 7. Boundaries and traps

| Situation | Instance | Correct reading | Answer |
|:---|:---|:---|:---|
| No index conflicts | `nums1 = [1, 2]`, `nums2 = [2, 1]` | no operation is needed; $s = 0$, $B = 0$ | 0 |
| Every index conflicts, values balanced | `nums1 = nums2 = [1, 1, 2, 2]` | $s = 4$, each value has $c = 2$, so $2c = 4$ does **not** exceed $s$ | 6 |
| Every index conflicts, one value dominates | `nums1 = nums2 = [1, 2, 2]` | $s = 3$, $c = 2$ for value 2, $m = 1$, no eligible index exists | -1 |
| Constant identical arrays | `nums1 = nums2 = [1, 1, 1, 1]` | $s = 4$, $c = 4$, $m = 4$, no eligible index exists | -1 |
| One conflict and a cheap repair | `nums1 = [1, 2, 3]`, `nums2 = [1, 3, 2]` | $s = 1$, $c = 1$, $m = 1$; index `1` is eligible and cheapest | 1 |
| A repeated conflicting value | `nums1 = [1, 2, 2, 3]`, `nums2 = [1, 2, 2, 1]` | $s = 3$, $c = 2$ for value 2, $m = 1$; index `3` is eligible | 6 |
| Several helpers are all required | `nums1 = [1, 1, 1, 2, 3, 4]`, `nums2 = [1, 1, 1, 3, 4, 2]` | $s = 3$, $c = 3$ for value 1, $m = 3$; indices `3`, `4`, `5` are eligible | 15 |

| Plausible mistake | What it does | Why it is wrong |
|:---|:---|:---|
| Charge only the conflict indices and ignore the deficit | reports `B = 3` for `nums1 = nums2 = [1, 2, 2]` | the two heavy indices cannot both be fixed from a set that holds only one non-heavy value |
| Use any non-conflict index as a helper | recruits index `0` in the traced instance | index `0` holds the dominating value $x$, so it hands the heavy index the very value it must shed |
| Require $\text{nums1}[j] \ne x$ but not $\text{nums2}[j] \ne x$ | recruits an index whose `nums2` value is $x$ | that index would end holding $x$ and would itself become a conflict |
| Reuse a conflict index as its own helper | charges it twice | a second charge is never cheaper than a fresh eligible index, and when no eligible index exists the reuse cannot create the missing non-$x$ value either |
| Assume the number of groups must be even | expects a perfect matching of conflict indices | an odd conflict set is handled by a cycle using index `0` as a free pivot, so the mandatory sum is still attainable |
| Answer with the number of conflict indices | reports `3` for the traced instance | the cost is a sum of indices, not a count; cheap indices make repairs cheaper |

## 8. Complexity: time and auxiliary space

Let $n$ be the length of the arrays. The method needs two linear passes over the
indices and one pass over the distinct conflict values.

| Phase | Work | Cost |
|:---|:---|:---|
| Mark the conflict indices, add their indices to $B$, count their values | one left-to-right pass with a hash count | $O(n)$ expected |
| Find the dominating value, if any, and compute $m = 2c - s$ | one pass over the distinct conflict values | $O(d)$, where $d$ is the number of distinct conflict values |
| Collect the eligible helper indices and take the $m$ cheapest | one pass to test eligibility plus one selection of the $m$ smallest | $O(n)$ with a size-$m$ heap, or $O(n \log n)$ if the candidates are sorted |

Total time is

$$
O(n \log n)
$$

in the sort-based implementation and $O(n)$ expected with hashing plus a
selection structure, since $d \le n$ and the helper selection only ever needs the
$m$ smallest indices. With $n \le 10^5$ every variant is comfortably within limits.

Auxiliary space is

$$
O(n),
$$

for the frequency map of conflict values, which holds at most $\min(s, n)$ entries,
together with the candidate helper list and the selected helpers, each bounded by
$n$. The arrays themselves are never copied: the method reads them twice and stores
only counts and indices.