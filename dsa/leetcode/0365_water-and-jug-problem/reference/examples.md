## Examples

**Example 1**

- Input: `x = 3, y = 5, target = 4`
- Output: `true`
- Explanation: One sequence, commonly associated with the *Die Hard* jug example, is:
  1. Fill the five-liter jug: `(0,5)`.
  2. Pour into the three-liter jug, leaving two liters: `(3,2)`.
  3. Empty the three-liter jug: `(0,2)`.
  4. Transfer the remaining two liters into it: `(2,0)`.
  5. Fill the five-liter jug again: `(2,5)`.
  6. Pour from it until the three-liter jug is full, leaving four liters in the other jug: `(3,4)`.
  7. Empty the three-liter jug, leaving exactly four liters total: `(0,4)`.

**Example 2**

- Input: `x = 2, y = 6, target = 5`
- Output: `false`

**Example 3**

- Input: `x = 1, y = 2, target = 3`
- Output: `true`
- Explanation: Fill both jugs; their combined amount is then exactly `3` liters.
