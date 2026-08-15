### 1. Description

You are given two integer arrays `value` and `decay`, and an integer `m`.

- $\text{value}[i]$ represents the initial value at index `i`.

- $\text{decay}[i]$ represents how much the value decreases after each selection of index `i`.

You may select any index **multiple** times. The total number of selections across all indices must not exceed `m`.

If you select index `i` for the $$t^{\text{th}}$$ time, where `t` is 1-indexed, the value gained is $\text{value}[i] - \text{decay}[i] * (t - 1)$.

Return the **maximum** total value you can obtain. Since the answer may be large, return it **modulo** $10^{9} + 7$.

### 2. Function Contract

**Inputs**

- `value`: A nonempty list whose entry $\text{value}[i]$ is the first gain available from index `i`.
- `decay`: A list of the same length; $\text{decay}[i]$ is the fixed amount subtracted after each selection of index `i`.
- `m`: The maximum total number of selections allowed across all indices.

Let $n = \lvert\texttt{value}\rvert = \lvert\texttt{decay}\rvert$ and let $A = \max(\texttt{value})$. Each index can be selected any number of times, and selections at one index do not change the progression belonging to another index.

**Return value**

Return the greatest total obtainable with at most `m` selections, reduced modulo $10^9 + 7$. Maximization is performed on the actual gains before applying the modulus.

### 3. Examples

#### Example 1

- **Input:** value = [6,5,4], decay = [2,1,1], m = 4

- **Output:** 19

- **Explanation:** One optimal sequence of selections is as follows:

- By selecting index 0, the value gained is 6.

- By selecting index 1, the value gained is 5.

- By selecting index 2, the value gained is 4.

- By selecting index 0 again, the value gained is $6 - 2 = 4$.

The total value is $6 + 5 + 4 + 4 = 19$. No other sequence of at most 4 selections gives a higher total value.

#### Example 2

- **Input:** value = [7,2,2], decay = [3,2,1], m = 2

- **Output:** 11

- **Explanation:** One optimal sequence of selections is as follows:

- By selecting index 0, the value gained is 7.

- By selecting index 0 again, the value gained is $7 - 3 = 4$.

The total value is $7 + 4 = 11$.

#### Example 3

- **Input:** value = [4,3], decay = [5,4], m = 5

- **Output:** 7

- **Explanation:** One optimal sequence of selections is as follows:

- By selecting index 0, the value gained is 4.

- By selecting index 1, the value gained is 3.

The total value is $4 + 3 = 7$.

### 4. Constraints

- $1 \le \text{value.length} = \text{decay.length} \le 10^{5}$

- $1 \le \text{value}[i], \text{decay}[i] \le 10^{9}​​​​​​​$

- $1 \le m \le 10^{9}$
