## Examples

**Example 1**

- **Input:** `nums = [4, 3, 2, 1, 2, 3, 1]`
- **Output:** `2`
- **Explanation:** Merge `1 + 2` at indices 3 and 4 to get `[4, 3, 2, 3, 3, 1]`. Then merge `3 + 1` at indices 4 and 5 to get `[4, 3, 2, 3, 4]`, which is a palindrome. Total operations = 2.

**Example 2**

- **Input:** `nums = [1, 2, 3, 4]`
- **Output:** `3`
- **Explanation:** Merging 3 adjacent pairs reduces the array to `[10]`, which is a 1-element palindrome. Total operations = 3.

**Example 3**

- **Input:** `nums = [1, 2, 3, 2, 1]`
- **Output:** `0`
- **Explanation:** The array is already a palindrome, requiring 0 operations.
