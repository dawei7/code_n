## Examples

**Example 1**

- **Input:** `s = "apple"`
- **Output:** `5`
- **Explanation:** The 4 distinct letters ('a', 'p', 'l', 'e') can each be placed as the 1st letter on separate buttons. Total keypresses: $1 + 2 + 1 + 1 = 5$ ('p' appears twice, costing $2 \times 1 = 2$).

**Example 2**

- **Input:** `s = "abcdefghijkl"`
- **Output:** `15`
- **Explanation:** There are 12 distinct letters each appearing once. Assign 9 letters to 1st positions (cost 1 each) and 3 letters to 2nd positions (cost 2 each). Total keypresses: $9 \times 1 + 3 \times 2 = 15$.
