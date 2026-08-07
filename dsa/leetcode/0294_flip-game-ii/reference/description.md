## Description

You are playing a Flip Game with your friend.

You are given a string `currentState` that contains only `'+'` and `'-'`. You and your friend take turns to flip **two consecutive** `"++"` into `"--"`. The game ends when a person can no longer make a move, and therefore the other person will be the winner.

Return `true` *if the starting player can **guarantee a win***, and `false` otherwise.
### Function Contract

**Inputs**

- `currentState`: The initial string of plus and minus symbols.

**Return value**

Return `True` exactly when the first player has a winning strategy under optimal play.

### Examples
#### Example 1

- **Input:** $currentState = "++++"$
- **Output:** `true`
- **Explanation:** The starting player can guarantee a win by flipping the middle "++" to become "+--+".
#### Example 2

- **Input:** $currentState = "+"$
- **Output:** `false`
### Constraints

- $1 \le \text{currentState.length} \le 60$

- $\text{currentState}[i]$ is either `'+'` or `'-'`.

- There cannot be more than 20 consecutive `'+'`.

**Follow up:** Derive your algorithm's runtime complexity.