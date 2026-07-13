# Freedom Trail

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 514 |
| Difficulty | Hard |
| Topics | String, Dynamic Programming, Depth-First Search, Breadth-First Search |
| Official Link | [LeetCode](https://leetcode.com/problems/freedom-trail/) |

## Problem Description
### Goal
The circular string `ring` is engraved around a dial, initially with `ring[0]` aligned at the 12 o'clock position. To spell `key` from left to right, rotate the ring in place clockwise or counterclockwise until the required character is aligned, then press the center button to select it.

Each one-position rotation costs one step and each button press costs one step. Return the minimum total steps needed to spell every character of `key`. Repeated ring characters offer alternative alignments, and the cheapest occurrence for one key character may depend on the positions needed later; the key is guaranteed to be spellable.

### Function Contract
**Inputs**

- `ring`: a nonempty circular string whose index `0` initially faces the selector
- `key`: a nonempty string whose characters all occur in `ring`

**Return value**

- The minimum number of rotations and button presses needed to spell `key` in order

### Examples
**Example 1**

- Input: `ring = "godding", key = "gd"`
- Output: `4`

**Example 2**

- Input: `ring = "godding", key = "godding"`
- Output: `13`

**Example 3**

- Input: `ring = "a", key = "a"`
- Output: `1`

### Required Complexity

- **Time:** $O(|ring| \cdot |key|)$
- **Space:** $O(|ring|)$

<details>
<summary>Approach</summary>

#### General

**Represent the best cost at every ring position**

Let `cost[position]` be the minimum rotation cost after spelling the processed key prefix and leaving that ring position at the selector. Initially only position `0` is reachable with cost zero. Button presses are identical for every complete solution, so add `abs(key)` once after minimizing rotations.

**Apply a circular distance transform**

For the next key character, every target position needs
`min(source_cost + circular_distance(source, target))` over all current positions. Duplicate the cost array to length `2n`. A left-to-right pass relaxes movement from the left, and a right-to-left pass relaxes movement from the right. Repeated sources in the second copy model crossing the ring boundary, so the minimum of transformed positions `target` and `target + n` is the best circular arrival cost.

**Keep only positions bearing the required character**

After the transform, set every nonmatching position back to infinity. Matching positions become exactly the possible states after selecting the current key character. Repeating this for every character preserves all choices between duplicate letters without enumerating every source-target pair.

**Why the transform is exact**

On a line, the two directional passes compute the minimum initial cost plus absolute distance from any source. In the duplicated ring, a source appears at both `source` and `source + n`; reaching either copy of a target therefore considers both clockwise and counterclockwise wrap distances. Filtering changes no path cost—it only enforces that the selected position contains the required character. Induction over the key prefix gives the minimum rotation cost for every valid ending position.

#### Complexity detail

For each of `abs(key)` characters, two passes over `2 * abs(ring)` entries and one filter take $O(|ring|)$ time. The two cost arrays use $O(|ring|)$ space. Adding button presses is constant time.

#### Alternatives and edge cases

- **Occurrence-to-occurrence dynamic programming:** is straightforward but can take $O(|key| \cdot |ring|^2)$ time when a character appears everywhere.
- **Memoized depth-first search:** uses states `(key_index, ring_position)` and tries every matching occurrence, with the same quadratic transition factor.
- **Dijkstra on layered ring states:** is correct but introduces heap overhead for a graph whose cycle distances admit linear transforms.
- **One-character ring:** requires no rotation, only one press per key character.
- **Repeated target character:** staying at the current matching position may cost zero rotation.
- **Duplicate letters:** all occurrences must remain candidates because a locally farther choice can help later characters.
- **Wraparound:** distance between indices is $\min(\left\lvert a - b \right\rvert, n - \left\lvert a - b \right\rvert)$.

</details>
