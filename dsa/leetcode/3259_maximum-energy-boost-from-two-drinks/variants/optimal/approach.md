## General

At each hour, the schedule is aligned with drink A or drink B. Staying with the same drink earns that hour's boost. Switching uses the entire hour for cleansing and earns zero, but leaves the schedule aligned with the new drink for following hours.

The DP state `f[i][0]` is the greatest energy obtainable through hour `i` while ending aligned with A. This includes two possibilities: A was consumed at hour `i`, or hour `i` was the cleanse hour used to switch from B to A. `f[i][1]` has the symmetric meaning for B.

At hour zero there is no previous drink to cleanse. The statement allows starting with either drink, so `f[0][0] = energyDrinkA[0]` and `f[0][1] = energyDrinkB[0]`.

To end hour `i` aligned with A, there are two optimal candidates:

- The previous state was already aligned with A, so consume A now and gain `energyDrinkA[i]`.
- The previous state was aligned with B, so use the current hour to switch and gain nothing.

This gives

`f[i][0] = max(f[i - 1][0] + energyDrinkA[i], f[i - 1][1])`.

The B recurrence is symmetric:

`f[i][1] = max(f[i - 1][1] + energyDrinkB[i], f[i - 1][0])`.

This state interpretation explains why the cross-drink term does not add the new drink's boost. That transition represents the required waiting hour. The newly aligned drink can be consumed starting in the next hour.

For `A = [4,1,1]` and `B = [1,1,3]`, the first row is `[4,1]`. At hour one, the best A-aligned total is five by drinking A again. The best B-aligned total is four by spending hour one switching from A, rather than two by drinking B twice. At hour two, that B-aligned state consumes B for three more, reaching seven.

The DP permits schedules with consecutive switching hours, such as A-aligned to B-aligned and immediately back to A-aligned. They earn no energy during those hours and cannot improve over positive available boosts, but including them as legal state transitions does not harm optimality. All boosts are positive, so an optimal schedule consumes a drink whenever it is not purposefully cleansing for a profitable future switch.

**Why no explicit “cleansing” state is needed.** A switch consumes exactly one hour and its destination is known. The cross transition folds that action into the new alignment state at the end of the same hour. A three-state DP could represent cleansing separately, but it would store redundant timing information.

**Why the final maximum is sufficient.** After the last hour, it does not matter which drink the schedule is aligned with. Every legal schedule belongs to one of the two final states, so `max(f[n - 1])` is the best total.

Inductively, assume each state at hour `i-1` is optimal for its ending alignment. Any schedule ending aligned with A at hour `i` either stayed with A and consumed it, or arrived from B through a cleanse hour. The recurrence considers both and attaches the correct reward. The same holds for B. Thus both current states are optimal, and induction reaches the final answer.

**Exact implementation versus its summary.** The manifest summary mentions tracking values across the previous two hours, a common alternative recurrence where switching from B consumption at `i-2` allows A consumption at `i`. The exact source instead uses the end-of-hour alignment interpretation above and references only row `i-1`. These formulations are equivalent when their states are defined consistently.

## Complexity detail

Let $n$ be the number of hours. The loop computes two states with constant work for every hour after the first, so time complexity is $O(n)$.

The exact source allocates an $n\times2$ table, using $O(n)$ auxiliary space. This conflicts with the manifest's $O(1)$ claim. Only the previous pair is needed to compute the next pair, so two rolling scalars or two two-entry rows would reduce auxiliary space to $O(1)$. The provided file keeps the complete history even though it never reads rows older than `i-1`.

The maximum sum is at most $10^5n$, and Python integers represent it safely.

## Alternatives and edge cases

- **Rolling two-state DP:** Store only current A-aligned and B-aligned totals. It preserves the recurrence and realizes $O(1)$ auxiliary space.
- **Consumption-ending recurrence:** Define best totals that actually consume A or B at hour `i`, then a switch candidate comes from the other drink at `i-2` plus the current boost. This needs careful base cases but is equivalent.
- **Explicit cleansing state:** Three states can model consuming A, consuming B, or waiting. It is correct but more state than necessary because a wait always has a destination.
- **Greedy choose the larger hourly boost:** A locally larger drink may cause an unprofitable switch hour or prevent a beneficial future run. DP accounts for switching cost across time.
- **Never switch:** Summing all A or all B gives valid baseline schedules and appears through repeated same-state transitions.
- **Switch once:** The cross transition pays exactly one zero-reward hour before the new same-state transition begins earning.
- **Equal choices:** Either predecessor can be retained by `max`; only the total, not the schedule, is requested.
- **Positive boosts:** Starting with a drink at hour zero is always at least as good as voluntarily waiting, so no zero base state is needed.
- **Minimum length three:** The recurrence also makes sense for shorter arrays, but the documented domain begins at three.
- **Source-space mismatch:** The algorithmic dependency is constant-space, but the exact `f` allocation is linear and should be reported as such.
