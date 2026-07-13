# Baseball Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 682 |
| Difficulty | Easy |
| Topics | Array, Stack, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/baseball-game/) |

## Problem Description
### Goal
You are keeping a baseball game's scores under unusual rules, beginning with an empty record. Process each string in `operations` in order: an integer records that score, `+` records the sum of the previous two valid scores, `D` records double the previous valid score, and `C` invalidates and removes the previous valid score.

Return the sum of all scores remaining in the record after every operation. Removed scores no longer count and are also ignored by later `+` and `D` operations. The input guarantees that each operation has enough preceding valid scores when its rule requires them.

### Function Contract
**Inputs**

- `operations`: a valid sequence of integer strings and the commands `+`, `D`, and `C`

**Return value**

- The total of all scores that remain valid after every operation is processed

### Examples
**Example 1**

- Input: `operations = ["5","2","C","D","+"]`
- Output: `30`

**Example 2**

- Input: `operations = ["5","-2","4","C","D","9","+","+"]`
- Output: `27`

**Example 3**

- Input: `operations = ["1","C"]`
- Output: `0`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Keep exactly the currently valid scores**

Use a stack whose entries are the valid round scores in chronological order. Parsing an integer pushes it. Command `C` pops the most recent valid score, while `D` and `+` read the top one or two stack entries and push their derived score. The input guarantees those referenced entries exist.

**Update the total with every stack change**

Maintain a running total beside the stack. Add every newly pushed score and subtract a cancelled score when it is popped. This avoids a separate final pass, though summing the stack at the end would have the same linear complexity.

**Why command references remain correct**

After every processed operation, the stack contains exactly the uncancelled scores in their original order: each command performs the same append or removal defined by the record rules. Therefore its top entries are precisely the previous valid rounds needed by `D` and `+`. The running total changes by exactly the value added to or removed from that valid record, so it equals the required sum at completion.

#### Complexity detail

Each of the `N` operations performs constant-time stack and arithmetic work, for $O(N)$ time. In the worst case every operation records a score, so the stack uses $O(N)$ space.

#### Alternatives and edge cases

- **Sum the stack after simulation:** removes the running-total variable and remains $O(N)$ overall, adding one final pass.
- **Copy the record for every update:** can model each prefix immutably, but copying a growing stack takes $O(N^2)$ total time.
- **Replay all preceding operations after each command:** produces correct prefix states but repeats work and is also quadratic.
- Negative integer score strings must be parsed as scores rather than mistaken for commands.
- `C` removes the previous valid score, so later commands cannot reference it.
- The final valid record may be empty, in which case the total is zero.

</details>
