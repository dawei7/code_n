### 1. Description

Write a generator function that returns a generator object which yields the **fibonacci sequence**.

The **fibonacci sequence** is defined by the relation $X_{n} = X_{n}-1 + X_{n}-2$.

The first few numbers of the series are `0, 1, 1, 2, 3, 5, 8, 13`.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** $callCount = 5$
- **Output:** `[0,1,1,2,3]`
- **Explanation:**
const gen = fibGenerator();
gen.next().value; // 0
gen.next().value; // 1
gen.next().value; // 1
gen.next().value; // 2
gen.next().value; // 3
#### Example 2

- **Input:** $callCount = 0$
- **Output:** `[]`
- **Explanation:** gen.next() is never called so nothing is outputted

### 4. Constraints

- $0 \le callCount \le 50$