## Examples

**Example 1**

- **Input:** `nums = [1,3,-1,-3,5,3,6,7], k = 3`

- **Output:** `[1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]`

- **Explanation:** The bracketed values form the current window. Ordering those three values gives the median shown on
the right.

```text
Window position                         Median
[1  3  -1] -3  5  3  6  7                 1
 1 [3  -1  -3] 5  3  6  7                -1
 1  3 [-1  -3  5] 3  6  7                -1
 1  3  -1 [-3  5  3] 6  7                 3
 1  3  -1  -3 [5  3  6] 7                 5
 1  3  -1  -3  5 [3  6  7]                6
```

**Example 2**

- **Input:** `nums = [1,2,3,4,2,3,1,4,2], k = 3`

- **Output:** `[2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]`
