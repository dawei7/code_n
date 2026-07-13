# Bulb Switcher II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 672 |
| Difficulty | Medium |
| Topics | Math, Bit Manipulation, Depth-First Search, Breadth-First Search |
| Official Link | [LeetCode](https://leetcode.com/problems/bulb-switcher-ii/) |

## Problem Description
### Goal
A room contains `n` bulbs labeled `1` through `n`, all turned on initially. Four buttons flip, respectively, all bulbs; bulbs with even labels; bulbs with odd labels; or bulbs labeled $3k + 1$ for non-negative integers `k`.

You must make exactly `presses` button presses, choosing any of the four buttons on each press and allowing the same button more than once. Return the number of different final on/off statuses reachable after all presses. Different press sequences that produce the same bulb status count only once.

### Function Contract
**Inputs**

- `n`: the positive number of bulbs
- `presses`: the exact nonnegative number of button presses

**Return value**

- The number of distinct bulb configurations reachable after exactly `presses` operations

### Examples
**Example 1**

- Input: `n = 1, presses = 1`
- Output: `2`

**Example 2**

- Input: `n = 2, presses = 1`
- Output: `3`

**Example 3**

- Input: `n = 3, presses = 2`
- Output: `7`

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Only button parities affect the final state**

Pressing the same button twice cancels every flip it caused. A final configuration therefore depends only on whether each of the four buttons was pressed an odd or even number of times. Additional presses can be inserted in cancelling pairs, so a parity selection using `b` odd buttons is feasible exactly when `b <= presses` and `b` has the same parity as `presses`.

**The configuration count stabilizes after three bulbs**

The four operations are periodic combinations of odd/even positions and positions congruent to one modulo three. Their parity effects have only three independent choices, and the first three bulbs distinguish all resulting global patterns. Consequently, bulb counts greater than three introduce no new configurations; reasoning may cap `n` at three.

**Resolve the small state table**

With no presses, only the all-on state is reachable. One bulb has two states once at least one press is available. For two bulbs, one press reaches three states and two or more presses reach all four. With at least three bulbs, one press reaches four states, two presses reach seven, and three or more presses realize all eight parity-distinct states. These cases exhaust the capped bulb counts and press ranges.

#### Complexity detail

The result is selected from a fixed number of bulb-count and press-count cases, independent of the numeric input magnitudes. It therefore uses $O(1)$ time and $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Enumerate the sixteen button-parity masks:** test the exact-press feasibility condition and simulate each mask on the first few bulbs; this is also $O(1)$ because both loops have fixed bounds.
- **Breadth-first state simulation:** repeatedly generate every configuration reachable after the next press; the state set is bounded, but processing all `presses` layers costs $O(presses)$ time.
- **Simulate complete bulb arrays:** preserves the literal operations but adds an unnecessary factor of `n` to every transition.
- When `presses = 0`, the answer is always `1` regardless of `n`.
- Exactly one bulb has only the on and off states, even after many presses.
- “Exactly” does not prevent using a configuration from fewer effective presses because two identical extra presses cancel.

</details>
