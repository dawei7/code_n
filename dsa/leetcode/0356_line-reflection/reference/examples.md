## Examples

**Example 1**

- Input: `points = [[1,1],[-1,1]]`
- Output: `true`
- Explanation: The vertical line $x=0$ reflects the two points onto one another.

```text
(-1,1)  | x = 0 |  (1,1)
    *    |       |    *
```

**Example 2**

- Input: `points = [[1,1],[-1,-1]]`
- Output: `false`
- Explanation: No vertical reflection line maps this point set back to itself.

```text
                    * (1,1)

* (-1,-1)          no vertical axis pairs these points
```
