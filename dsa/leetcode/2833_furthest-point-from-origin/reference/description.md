## Description

You are given a string `moves` of length `n` consisting only of characters `'L'`, `'R'`, and `'_'`. The string represents your movement on a number line starting from the origin `0`.

In the $$i^{\text{th}}$$ move, you can choose one of the following directions:

- move to the left if $\text{moves}[i] = 'L'$ or $\text{moves}[i] = '_'$

- move to the right if $\text{moves}[i] = 'R'$ or $\text{moves}[i] = '_'$

Return *the **distance from the origin** of the **furthest** point you can get to after *`n`* moves*.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** $moves = "L_{RL\_\_R}"$
- **Output:** `3`
- **Explanation:** The furthest point we can reach from the origin 0 is point -3 through the following sequence of moves "LLRLLLR".
#### Example 2

- **Input:** $moves = "_R_{\_LL\_}"$
- **Output:** `5`
- **Explanation:** The furthest point we can reach from the origin 0 is point -5 through the following sequence of moves "LRLLLLL".
#### Example 3

- **Input:** $moves = "_______"$
- **Output:** `7`
- **Explanation:** The furthest point we can reach from the origin 0 is point 7 through the following sequence of moves "RRRRRRR".
### Constraints

- $1 \le \text{moves.length} = n \le 50$

- `moves` consists only of characters `'L'`, `'R'` and `'_'`.