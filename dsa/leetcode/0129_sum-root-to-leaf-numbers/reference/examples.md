## Examples

**Example 1**

- Input: `root = [1, 2, 3]`
- Output: `25`
- Explanation: Paths `1 -> 2` and `1 -> 3` represent `12` and `13`. Their sum is `12 + 13 = 25`.

```text
      1
     / \
   2     3
  12    13
```

**Example 2**

- Input: `root = [4, 9, 0, 5, 1]`
- Output: `1026`
- Explanation: Paths `4 -> 9 -> 5`, `4 -> 9 -> 1`, and `4 -> 0` represent `495`, `491`, and `40`. Therefore the total is `495 + 491 + 40 = 1026`.

```text
        4
       / \
      9   0 ----> 40
     / \
    5   1
   495 491
```
