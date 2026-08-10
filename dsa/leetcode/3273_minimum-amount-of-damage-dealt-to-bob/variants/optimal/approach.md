## General

An enemy deals damage during every second it remains alive, including the second in which Bob lands the killing attack because enemies attack first. If enemy `i` needs `t_i` attacks and deals `d_i` damage per second, its contribution is `d_i` multiplied by the time at which Bob finishes it.

The number of required attack seconds is the ceiling of health divided by power:

`t_i = (health[i] + power - 1) // power`.

Splitting attacks between enemies cannot reduce the total compared with finishing enemies in some order. While two enemies remain alive, delaying completion of either keeps both damage rates active. An optimal schedule can therefore be represented as a non-preemptive order of enemies, with each attacked until dead.

For an order, the objective is

$$
\sum_i d_i C_i,
$$

where $C_i$ is enemy `i`'s completion time. This is the classic minimum weighted completion-time problem.

**Derive the correct order from two enemies.** Suppose enemy $A$ needs $t_A$ seconds and deals $d_A$ damage, while $B$ has $t_B,d_B$. Terms involving enemies before or after this pair are unchanged by swapping them. Ordering $A$ before $B$ adds the cross-delay cost $t_A d_B$: $B$ remains alive during all of $A$'s attacks. Ordering $B$ before $A$ instead adds $t_B d_A$.

Therefore $A$ should precede $B$ exactly when

$$
t_A d_B\le t_B d_A.
$$

Equivalently, sort by increasing ratio $t_i/d_i$. The source avoids floating-point division and compares cross-products exactly.

`compare(first,second)` calculates `first[0] * second[1]` and `second[0] * first[1]`. It returns negative when the first cross-product is smaller, which places `first` earlier under Python sorting. Equal cross-products may appear in either order; their swap cost is identical.

After sorting, `active_damage` is the sum of every living enemy's damage rate. Killing one enemy requiring `attack_seconds` takes that many seconds, and during each of those seconds all currently active enemies attack. Thus `active_damage * attack_seconds` is added. The dead enemy's rate is then subtracted before the next block.

For example one, required seconds are one, two, two, and two. The comparator places the high-damage enemies early according to the time-to-damage ratios, producing the demonstrated total thirty-nine.

**Why the exchange argument proves global optimality.** Any order containing an adjacent inverted pair that violates the cross-product rule can be improved or left equal by swapping that pair. Repeating swaps removes every inversion and reaches the comparator-sorted order. Therefore no other order has smaller total damage.

The source creates new `enemies` tuples and leaves `damage` and `health` unchanged. Positive damage values make every ratio well-defined.

## Complexity detail

Let $n$ be the enemy count. Building attack-time tuples and summing damage take $O(n)$. Comparator sorting takes $O(n\log n)$ comparisons, each constant-time integer arithmetic. The final accumulation is $O(n)$, so total time is $O(n\log n)$.

The tuple list and sorting workspace use $O(n)$ space. Scalar totals use $O(1)$. Python integers safely hold cross-products and the potentially large accumulated damage.

## Alternatives and edge cases

- **Sort by damage alone:** A high-damage enemy may require extremely many attacks; ratio ordering correctly balances damage removed against time spent.
- **Sort by health or attack time alone:** This ignores the rate kept alive during delay and can be suboptimal.
- **Floating-point ratios:** Sorting by `t/d` is conceptually correct, but cross-products avoid precision errors and division.
- **Attack enemies in alternating turns:** Preemption cannot beat a completion order because partial attacks remove no damage rate until an enemy dies.
- **One enemy:** It attacks for exactly its ceiling health-to-power seconds, and the result is `damage * attacks`.
- **Health divisible by power:** Ceiling division gives the exact quotient without an extra attack.
- **Health not divisible by power:** The final partial-health attack still consumes a full second and is included by ceiling division.
- **Equal ordering ratios:** Either order has the same pairwise cross cost, so sort stability is irrelevant to the optimum.
- **Enemies with equal damage:** Shorter attack time comes first through the comparator.
- **Enemies with equal attack time:** Greater damage comes first.
- **Attack-before-damage variant:** The accumulation would differ if Bob attacked first. The source correctly follows the stated enemies-first timing by charging the killing second.
- **Input preservation:** Only derived tuples are sorted; the original parallel arrays keep their order.
- **Why `active_damage` starts with every rate:** Before Bob's first attack, every enemy is alive and attacks. Omitting the target enemy during its own attack block would incorrectly assume Bob strikes before damage is dealt.
- **Why subtraction happens after the block:** The enemy remains alive for all `attack_seconds` seconds assigned to it. Its rate disappears only after the final one of those seconds has already contributed damage.
- **Comparator transitivity:** The cross-product rule is equivalent to ordering positive ratios `t/d`, so it defines a consistent sortable order rather than a collection of contradictory pair preferences.
- **Large accumulated answer:** Up to $10^5$ enemies can remain active for many seconds, making the total far exceed 32-bit range. Python integers prevent overflow; fixed-width implementations need 64-bit arithmetic.
