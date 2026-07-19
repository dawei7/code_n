## General
**Only button parities affect the final state**

Pressing the same button twice cancels every flip it caused. A final configuration therefore depends only on whether each of the four buttons was pressed an odd or even number of times. Additional presses can be inserted in cancelling pairs, so a parity selection using `b` odd buttons is feasible exactly when `b <= presses` and `b` has the same parity as `presses`.

**The configuration count stabilizes after three bulbs**

The four operations are periodic combinations of odd/even positions and positions congruent to one modulo three. Their parity effects have only three independent choices, and the first three bulbs distinguish all resulting global patterns. Consequently, bulb counts greater than three introduce no new configurations; reasoning may cap `n` at three.

**Resolve the small state table**

With no presses, only the all-on state is reachable. One bulb has two states once at least one press is available. For two bulbs, one press reaches three states and two or more presses reach all four. With at least three bulbs, one press reaches four states, two presses reach seven, and three or more presses realize all eight parity-distinct states. These cases exhaust the capped bulb counts and press ranges.

## Complexity detail
The result is selected from a fixed number of bulb-count and press-count cases, independent of the numeric input magnitudes. It therefore uses $O(1)$ time and $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Enumerate the sixteen button-parity masks:** test the exact-press feasibility condition and simulate each mask on the first few bulbs; this is also $O(1)$ because both loops have fixed bounds.
- **Breadth-first state simulation:** repeatedly generate every configuration reachable after the next press; the state set is bounded, but processing all `presses` layers costs $O(presses)$ time.
- **Simulate complete bulb arrays:** preserves the literal operations but adds an unnecessary factor of `n` to every transition.
- When `presses = 0`, the answer is always `1` regardless of `n`.
- Exactly one bulb has only the on and off states, even after many presses.
- “Exactly” does not prevent using a configuration from fewer effective presses because two identical extra presses cancel.
