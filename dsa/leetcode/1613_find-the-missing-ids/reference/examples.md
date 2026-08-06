## Examples

**Example 1**

- **Input:** `Customers` containing IDs `[1, 4, 5]`
- **Output:**
  | ids |
  | --- |
  | 2 |
  | 3 |
- **Explanation:** Max ID is 5. Missing IDs between 1 and 5 are 2 and 3.

**Example 2**

- **Input:** `Customers` containing IDs `[1, 2, 3]`
- **Output:**
  | ids |
  | --- |
- **Explanation:** The range 1 to 3 is consecutive, so no IDs are missing.

**Example 3**

- **Input:** `Customers` containing only ID `[5]`
- **Output:**
  | ids |
  | --- |
  | 1 |
  | 2 |
  | 3 |
  | 4 |
- **Explanation:** Max ID is 5. Missing IDs between 1 and 5 are 1, 2, 3, 4.
