# Guided Example: Put Marbles in Bags

## 1. The instance, and the one decision a distribution makes

Take the first official sample: `weights = [1,3,5,1]` with `k = 2`, whose required output is `4`. The marbles must be split into exactly $k$ non-empty bags, and each bag must occupy a **contiguous** block of the array — the statement forbids interleaving, so a bag is always a block `weights[i..j]` and costs $\text{weights}[i] + \text{weights}[j]$, the weight of its two end marbles. The score of a distribution is the sum of its bag costs, and we must return the maximum score minus the minimum score over all legal distributions.

The critical observation is that a distribution into $k$ contiguous bags is nothing more than a choice of $k - 1$ cut positions: the gaps between consecutive bags. With $n$ marbles there are $n - 1$ gaps, numbered by the left marble of the gap, so gap $c$ separates index $c$ from index $c+1$ for $0 \le c \le n - 2$. Choosing a set $S$ of $k - 1$ distinct gaps produces exactly one distribution, and every distribution arises that way.

```text
index     0     1     2     3
weight    1     3     5     1
gap 0       \___/                   a_0 = w0 + w1 = 1 + 3 = 4
gap 1             \___/             a_1 = w1 + w2 = 3 + 5 = 8
gap 2                   \___/       a_2 = w2 + w3 = 5 + 1 = 6
```

For the traced instance $k - 1 = 1$, so each distribution is a single cut, and there are only three of them. Enumerating them by hand shows exactly what the score depends on.

| Cut set $S$ | Distribution | Bag costs | Score |
|---|---|---|---|
| $\{0\}$ | `[1]`, `[3,5,1]` | $(1+1) + (3+1) = 2 + 4$ | 6 |
| $\{1\}$ | `[1,3]`, `[5,1]` | $(1+3) + (5+1) = 4 + 6$ | 10 |
| $\{2\}$ | `[1,3,5]`, `[1]` | $(1+5) + (1+1) = 6 + 2$ | 8 |

The maximum score is $10$, the minimum is $6$, and the required difference is $10 - 6 = 4$. The middle marble `5` never appears in any bag cost, even though it is the largest weight in the array — the first clue that this problem is about boundaries rather than about marble weights.

## 2. The telescoping identity: what a cut actually costs

Write $S = \{c_1 < c_2 < \dots < c_{k-1}\}$ for the chosen gaps. The bags are then `weights[0..c_1]`, `weights[c_1+1..c_2]`, and so on up to `weights[c_{k-1}+1..n-1]`. Each bag cost is the sum of its two end weights, so the score is

$$
w[0] + w[c_1] \;+\; w[c_1 + 1] + w[c_2] \;+\; \dots \;+\; w[c_{k-1}] + w[c_{k-1} + 1] \;+\; w[n-1],
$$

which regroups into a fixed part and a part charged per cut:

$$
\text{score}(S) \;=\; \underbrace{w[0] + w[n-1]}_{\text{fixed base}} \;+\; \sum_{c \in S} \underbrace{\bigl(w[c] + w[c+1]\bigr)}_{a_c}.
$$

The identity is an accounting statement about each array index. Index $0$ is the left end of the first bag no matter where the cuts fall, and index $n-1$ is the right end of the last bag, so both are charged exactly once in every distribution. An interior index $c$ is charged as the *right* end of the bag that ends at $c$ exactly when $c$ is a cut, and as the *left* end of the bag that starts at $c$ exactly when $c - 1$ is a cut. Nothing else is ever charged: a marble strictly inside a bag is neither an end of that bag nor adjacent to a cut, so its weight never enters the score.

| Cut $c$ | Left bag ends at $c$, charging $w[c]$ | Right bag starts at $c+1$, charging $w[c+1]$ | Total added $a_c$ |
|---|---|---|---|
| 0 | `[1]` ends at index 0, charging 1 | `[3,5,1]` starts at index 1, charging 3 | 4 |
| 1 | `[1,3]` ends at index 1, charging 3 | `[5,1]` starts at index 2, charging 5 | 8 |
| 2 | `[1,3,5]` ends at index 2, charging 5 | `[1]` starts at index 3, charging 1 | 6 |

Check the identity against the enumeration: cut $0$ gives base $w[0] + w[3] = 1 + 1 = 2$ plus $a_0 = 4$, so $6$; cut $1$ gives $2 + 8 = 10$; cut $2$ gives $2 + 6 = 8$. All three match Section 1, and the enumerated bag costs now have a closed form.

The base is the same $2$ in every distribution of this instance, and that is general: $w[0] + w[n-1]$ does not depend on $S$ at all. It therefore adds the same constant to the maximum and to the minimum score.

## 3. Two independent selections, and how the base cancels

Because the base is constant across the family of legal distributions,

$$
\max_S \text{score}(S) = \bigl(w[0] + w[n-1]\bigr) + \max_{S}\, \sum_{c \in S} a_c,
\qquad
\min_S \text{score}(S) = \bigl(w[0] + w[n-1]\bigr) + \min_{S}\, \sum_{c \in S} a_c,
$$

and subtracting the second from the first removes the base entirely:

$$
\max - \min \;=\; \Bigl(\text{sum of the } k-1 \text{ largest } a_c\Bigr) \;-\; \Bigl(\text{sum of the } k-1 \text{ smallest } a_c\Bigr).
$$

The two selections are independent because the maximum and the minimum are taken over the *same* family of $(k-1)$-subsets of gaps, with no coupling between them; the difference of two independent optima is a well-defined number even though no single distribution attains both. Sorting the adjacency sums makes both visible at once.

| Rank | Gap $c$ | $a_c = w[c] + w[c+1]$ | Used by the maximum? | Used by the minimum? |
|---|---|---|---|---|
| smallest | 0 | 4 | no | yes |
| middle | 2 | 6 | no | no |
| largest | 1 | 8 | yes | no |

With $k - 1 = 1$, the maximum takes the single largest sum $8$ and the minimum takes the single smallest sum $4$; their difference is $4$, matching the required output. Note how the *middle* value is used by neither extreme: the extremes of a score are decided by the extremes of $a$, not by the middle of anything.

## 4. Why sorting settles both extremes exactly

The family of legal distributions is in bijection with the $(k-1)$-subsets of the $n-1$ gaps, and feasibility is automatic for every such subset: distinct gaps produce non-empty bags in order, and $k \le n$ guarantees that $k - 1$ distinct gaps exist. The objective restricted to that family is $\sum_{c \in S} a_c$, an additive function of the chosen subset with no other constraint. Two standard facts then apply, and together they are the correctness argument:

- **Exchange for the maximum.** If a chosen $(k-1)$-subset contains a gap with sum $a$ while some unchosen gap has a strictly larger sum $a'$, replacing $a$ by $a'$ keeps the subset size at $k-1$ and increases the total. Repeating the exchange removes every such pair, so the maximum is attained exactly by the $k-1$ gaps with the largest sums.
- **Exchange for the minimum.** The same swap argument with the inequality reversed forces the minimum to be attained exactly by the $k-1$ gaps with the smallest sums.

Ties are harmless: the set of values in the greedy choice is unique even when the achieving gaps are not, and the returned difference depends only on those values. This is why the answer for an instance whose adjacency sums are all equal must be $0$ — the largest and smallest selections contain the same multiset of values.

## 5. Boundaries this instance exposes

| Instance | $k$ | Cuts chosen | Largest selection | Smallest selection | Difference |
|---|---|---|---|---|---|
| `[9,2,7,4]` | 1 | 0 | empty sum, 0 | empty sum, 0 | 0 |
| `[1,3]` | 2 | 1 of 1 gaps | the only sum | the same sum | 0 |
| `[5,1,8,3]` | 4 | all 3 gaps | every sum | every sum | 0 |
| `[4,4,4,4,4]` | 3 | 2 of 4 gaps | e.g. $8 + 8$ | the same value $8 + 8$ | 0 |
| `[1,3,5,1]` | 2 | 1 of 3 gaps | $8$ | $4$ | 4 |
| `[1,2,3,4,5,6]` | 3 | 2 of 5 gaps | $11 + 9 = 20$ | $3 + 5 = 8$ | 12 |
| `[8,1,6,3,9,2,7]` | 4 | 3 of 6 gaps | $12 + 11 + 9 = 32$ | $7 + 9 + 9 = 25$ | 7 |

The first three rows are the forced cases. When $k = 1$ or $k = n$ there is only one legal distribution, so the maximum and the minimum coincide; when $n = 2$ there is a single gap and it must be cut. The fourth row shows that ties in $a$ also collapse the difference to $0$ without changing the number of distributions. For `[1,2,3,4,5,6]` the adjacency sums are $3, 5, 7, 9, 11$ — strictly increasing, so the two largest and two smallest are unambiguous — while `[8,1,6,3,9,2,7]` produces the multiset $9, 7, 9, 12, 11, 9$, whose duplicate $9$ values appear on both sides of the difference and matter in both selections.

## 6. Traps this instance exposes

| Situation | Naive expectation | Actual behaviour | Where it bites |
|---|---|---|---|
| The largest marble | it should dominate the maximum score | strictly interior marbles are never charged | weight `5` in `[1,3,5,1]` contributes nothing |
| Counting cuts | $k$ cuts for $k$ bags | exactly $k - 1$ cuts are needed | off by one changes both selections |
| What is selected | choose the largest single weights | choose the largest adjacency sums $w[c] + w[c+1]$ | the two criteria disagree on `[1,3,5,1]` |
| Minimizing the score | maximize the "gaps" between bags | there is no reward for gaps, only the charged pair at each cut | a minimum-score search for big jumps finds nothing |
| Independence of extremes | one distribution must achieve both | the difference compares two different optima | the minimum-score cut is not the maximum-score cut |
| Ties in adjacency sums | ties make the answer ambiguous | only the multiset of chosen values matters | `[4,4,4,4,4]` with `k = 3` returns `0` |
| Reusing a gap | cut the cheapest gap twice | gaps must be distinct, so bags stay non-empty | a repeated cut would create an empty bag |
| Numeric range | the difference is small | weights reach $10^9$ over up to $10^5$ terms | totals near $2 \times 10^{14}$ overflow 32-bit arithmetic |

The extreme value of the last row is worth checking against the closed form: for `[1000000000, 1, 999999999, 2, 999999998]` with `k = 2`, the adjacency sums are $1000000001$, $1000000000$, $1000000001$, $1000000000$, so the largest is $1000000001$ and the smallest is $1000000000$, giving the difference `1` — a result that is invisible if the sums are computed in a type that cannot hold them.

## 7. Time and auxiliary space

Let $n = \text{weights.length}$. Forming the $n - 1$ adjacency sums is one linear pass. Ordering them is a comparison sort costing $\Theta(n \log n)$, and summing the smallest $k - 1$ and the largest $k - 1$ entries of the sorted array is another linear pass. The total running time is therefore

$$
O(n \log n),
$$

with $n \le 10^5$ giving about $1.7 \times 10^6$ comparisons — comfortably fast. Auxiliary space is $O(n)$: the array of $n - 1$ adjacency sums is the only non-constant structure, and the base term, the cut count, and the two running sums are scalars. A partial selection would reduce the time to $O(n \log k)$ with a bounded heap or $O(n)$ expected with quickselect, and space to $O(k)$, but neither is needed at this input size and both make the tie behaviour harder to reason about.

For contrast, the natural but unnecessary approach — a dynamic program that considers bag boundaries in order — would need a state for the current position and the number of bags used, costing $\Theta(n^2 k)$ time in its straightforward form, or $\Theta(nk)$ with a careful recurrence. That entire axis of complexity exists only because a boundary DP is the reflex for partition problems. The telescoping identity of Section 2 shows that the objective is additive over the *gap set* rather than over the pieces, which collapses the problem to two selection problems on $n - 1$ numbers and removes the partition structure altogether.
