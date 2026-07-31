## General

Let $n$ be the number of enemies. Enemy $i$ requires

$$
t_i = \left\lceil \frac{\texttt{health}[i]}{\texttt{power}} \right\rceil
$$

attack seconds and has damage rate $d_i$.

**Reduce the fight to a completion-order problem**

Splitting attacks between enemies cannot make either one stop attacking earlier than completing one of them. Any schedule can therefore be rearranged into contiguous blocks with the same enemy completion order and no larger damage. For a fixed order, enemy $i$ contributes $d_i$ times its completion time, so the objective is the weighted sum $\sum_i d_i C_i$.

**Derive the optimal pair order**

Consider two adjacent enemies `a` and `b` after the same prefix. Ordering `a` first adds the cross-term $t_a d_b$, while ordering `b` first adds $t_b d_a$. Thus `a` should precede `b` exactly when

$$
t_a d_b \le t_b d_a,
$$

equivalently when $t_a/d_a \le t_b/d_b$. Sort using cross multiplication so no floating-point rounding can alter close ratios. Repeatedly fixing inverted adjacent pairs proves the resulting order is globally optimal.

**Accumulate damage by surviving rate**

Start with the sum of all damage rates. When an enemy requiring `t` seconds is next, every currently living enemy attacks during all `t` seconds, contributing `active_damage * t`. Then subtract the defeated enemy's rate and continue.

## Complexity detail

Computing attack counts and the initial rate sum is $O(n)$. Sorting dominates at $O(n \log n)$ time, followed by one linear accumulation pass. The enemy tuples and sort storage use $O(n)$ space.

## Alternatives and edge cases

- **Try every defeat order:** Evaluating all $n!$ permutations is infeasible.
- **Repeatedly scan for the best ratio:** This produces the same order but takes $O(n^2)$ time.
- **Defeat the highest damage first:** Damage alone ignores how many seconds are needed to remove that rate.
- **Defeat the lowest health first:** Attack time alone ignores the rate that remains active.
- **Sort floating-point ratios:** Cross multiplication preserves exact ordering for all legal integers.
- A lone enemy contributes its rate for every required attack second.
- Health not divisible by `power` rounds up to one additional attack.
- Equal ratios may appear in either order without changing the objective.
- Damage can exceed 32-bit range after rates are multiplied by completion times, so the result requires a wide integer type.
