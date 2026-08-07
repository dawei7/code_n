### 1. Description

Write a function `argumentsLength` that returns the count of arguments passed to it.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** $args = [5]$
- **Output:** `1`
- **Explanation:**
argumentsLength(5); // 1
One value was passed to the function so it should return 1.
#### Example 2

- **Input:** $args = [{}, null, "3"]$
- **Output:** `3`
- **Explanation:**
argumentsLength({}, null, "3"); // 3
Three values were passed to the function so it should return 3.

### 4. Constraints

- `args` is a valid JSON array

- $0 \le \text{args.length} \le 100$