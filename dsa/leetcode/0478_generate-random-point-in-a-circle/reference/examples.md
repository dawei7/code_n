## Examples

**Example 1**

- Input: `operations = ["Solution", "randPoint", "randPoint", "randPoint"], arguments = [[1.0, 0.0, 0.0], [], [], []]`
- Output: `[null, [-0.02493, -0.38077], [0.82314, 0.38945], [0.36572, 0.17248]]`
- Explanation: Construct `Solution(1.0, 0.0, 0.0)`, then call `randPoint()` three times. The displayed calls return
  `[-0.02493, -0.38077]`, `[0.82314, 0.38945]`, and `[0.36572, 0.17248]`. These coordinates illustrate valid
  random results; another execution may return different points from the same uniform distribution.
