## General

**Pairing simultaneous assignments**

Place `left` at Alice's next plant and `right` at Bob's next plant. While `left < right`, one simulation round assigns `plants[left]` to Alice and `plants[right]` to Bob. This matches the statement's simultaneous motion because watering always takes one step, independent of the amount used.

Track `remaining_a` and `remaining_b`, initialized from the two capacities. Before a gardener waters an assigned plant, compare the requirement with that remaining amount. If it is larger, count one refill and restore the can to its full capacity. Subtract the plant's requirement after that decision, then move both pointers inward.

**Handling the shared middle plant**

When the array length is odd, the pointers eventually meet. Neither gardener should water that plant during the paired loop. At the meeting point the rule assigns it to whoever has more water; for the refill count, the gardener's identity matters only through the larger remaining amount. Therefore one final refill is necessary exactly when

$$
\max(\texttt{remaining\_a},\texttt{remaining\_b}) < \texttt{plants[left]}.
$$

An equality is enough to water the plant fully, and an exact tie between the cans selects Alice without changing this condition. Every plant before the meeting point is assigned once to its required side, and the optional middle plant is handled exactly once, so the accumulated count is precisely the number of refills in the prescribed process.

## Complexity detail

Each pointer moves across at most half the array, and every plant is processed once. The running time is $O(n)$. The simulation keeps only pointers, two remaining amounts, and a counter, so it uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Recompute consumed water:** Record each gardener's latest refill boundary and repeatedly sum the plants watered since it. This can reproduce the same state but takes $O(n^2)$ time instead of carrying the remaining amounts directly.
- **Separate full simulations:** Simulating Alice and Bob independently and then trying to merge their paths complicates the meeting point and may double-water plants; paired inward pointers encode the shared stopping condition directly.
- A requirement equal to the remaining amount does not cause a refill, because the plant can be watered fully.
- With one plant, compare the two initially full cans and apply the middle-plant rule immediately.
- For an odd number of plants, only the larger current remaining amount determines whether the final refill is needed; a tie goes to Alice.
- The capacity guarantees ensure that every plant can be watered immediately after a refill.
