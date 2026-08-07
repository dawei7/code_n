## Description

You are playing a Flip Game with your friend.

You are given a string `currentState` that contains only `'+'` and `'-'`. You and your friend take turns to flip **two consecutive** `"++"` into `"--"`. The game ends when a person can no longer make a move, and therefore the other person will be the winner.

Return all possible states of the string `currentState` after **one valid move**. You may return the answer in **any order**. If there is no valid move, return an empty list `[]`.
### Function Contract

**Inputs**

- `currentState`: The current string of plus and minus symbols.

**Return value**

Return one next-state string for each adjacent `"++"` pair. The app implementation emits these states in left-to-right pair order, although any order satisfies the problem contract.

### Examples

#### Example 1

- **Input:** $currentState = "++++"$
- **Output:** `["--++","+--+","++--"]`
#### Example 2

- **Input:** $currentState = "+"$
- **Output:** `[]`
### Constraints

- $1 \le \text{currentState.length} \le 500$

- $\text{currentState}[i]$ is either `'+'` or `'-'`.