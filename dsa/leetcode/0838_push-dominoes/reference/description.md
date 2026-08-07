### 1. Description

There are `n` dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

You are given a string `dominoes` representing the initial state where:

- $\text{dominoes}[i] = 'L'$, if the $$i^{\text{th}}$$ domino has been pushed to the left,

- $\text{dominoes}[i] = 'R'$, if the $$i^{\text{th}}$$ domino has been pushed to the right, and

- $\text{dominoes}[i] = '.'$, if the $$i^{\text{th}}$$ domino has not been pushed.

Return *a string representing the final state*.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** $dominoes = "\text{RR.L}"$
- **Output:** `"RR.L"`
- **Explanation:** The first domino expends no additional force on the second domino.
#### Example 2

![](images/domino.png)

- **Input:** $dominoes = ".\text{L.R}...LR..L.."$
- **Output:** `"LL.RR.LLRRLL.."`

### 4. Constraints

- $n = \text{dominoes.length}$

- $1 \le n \le 10^{5}$

- $\text{dominoes}[i]$ is either `'L'`, `'R'`, or `'.'`.