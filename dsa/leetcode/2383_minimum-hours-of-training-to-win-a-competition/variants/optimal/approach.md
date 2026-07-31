## General

Energy and experience evolve differently, so their minimum training requirements can be derived independently and then added.

**Account for all energy at once.** Energy only decreases. To remain strictly positive after paying every opponent's energy cost, the trained starting amount must be at least `sum(energy) + 1`. Therefore the unavoidable energy training is `max(0, sum(energy) + 1 - initial_energy)`. This condition is also sufficient: every earlier prefix consumes no more energy than the full sequence.

**Repair experience only when necessary.** Experience increases after victories, so scan the opponents in order. Immediately before an encounter, if current experience is not strictly greater than the opponent's experience, train by exactly the missing amount `opponent_experience + 1 - current_experience`. Then add the experience gained from winning.

Any smaller repair would lose the current encounter, while any extra repair could be postponed without changing future feasibility or total cost. Thus each local repair is forced and minimal. Combining these minimal experience repairs with the independently forced energy deficit gives the minimum total number of training hours.

## Complexity detail

Let $n$ be the number of opponents. Summing energy and scanning experience take $O(n)$ time. Apart from scalar totals, the algorithm uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Encounter-by-encounter energy repair:** Simulating energy and adding its deficit before each opponent is also $O(n)$ and produces the same total, but the one-sum formula makes the invariant clearer.
- **Repeated prefix recomputation:** Deriving every energy and experience prefix requirement from scratch is correct but takes $O(n^2)$ time.
- **Strict comparison:** Equality is insufficient; a statistic equal to an opponent's value needs one additional training hour.
- **No training:** If both statistics already satisfy every encounter as they evolve, the answer is zero.
- **Training separation:** One hour increases exactly one statistic, so energy and experience deficits must be added rather than taking their maximum.
- **Experience growth:** Experience gained from earlier opponents must be included before deciding whether later training is necessary.
