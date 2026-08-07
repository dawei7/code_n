### 1. Description

You are given a string `s` consisting of `n` characters which are either `'X'` or `'O'`.

A **move** is defined as selecting **three** **consecutive characters** of `s` and converting them to `'O'`. Note that if a move is applied to the character `'O'`, it will stay the **same**.

Return *the **minimum** number of moves required so that all the characters of *`s`* are converted to *`'O'`.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** `s = "XXX"`
- **Output:** `1`
- **Explanation:** <u>XXX</u> -> OOO
We select all the 3 characters and convert them in one move.
#### Example 2

- **Input:** `s = "XXOX"`
- **Output:** `2`
- **Explanation:** <u>XXO</u>X -> O<u>OOX</u> -> OOOO
We select the first 3 characters in the first move, and convert them to 'O'.
Then we select the last 3 characters and convert them so that the final string contains all 'O's.
#### Example 3

- **Input:** `s = "OOOO"`
- **Output:** `0`
- **Explanation:** There are no 'X's in s to convert.

### 4. Constraints

- $3 \le \text{s.length} \le 1000$

- $s[i]$ is either `'X'` or `'O'`.