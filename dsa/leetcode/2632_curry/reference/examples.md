## Examples

**Example 1**

- **Input:** `fn = (a, b, c) => a + b + c`, `inputs = [[1], [2], [3]]`
- **Output:** `6`
- **Explanation:** Three one-argument calls collectively supply the three declared parameters ($1 + 2 + 3 = 6$).

**Example 2**

- **Input:** `fn = (a, b, c) => a + b + c`, `inputs = [[1, 2], [3]]`
- **Output:** `6`
- **Explanation:** The first call supplies two parameters `(1, 2)` and the second completes the invocation with `3`.

**Example 3**

- **Input:** `fn = (a, b, c) => a + b + c`, `inputs = [[], [], [1, 2, 3]]`
- **Output:** `6`
- **Explanation:** Empty calls preserve the pending curry without adding arguments until `[1, 2, 3]` is passed.

**Example 4**

- **Input:** `fn = () => 42`, `inputs = [[]]`
- **Output:** `42`
- **Explanation:** Calling a zero-parameter curried function with no arguments evaluates `fn` immediately.
