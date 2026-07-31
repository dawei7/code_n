## Examples

**Example 1**

- Input: `n = 10`
- Output: `16`
- Explanation: Use this strategy:
  - Start with range `[1,10]` and guess `7`. A correct guess costs `0`; otherwise pay `$7`.
  - If the answer is higher, the range becomes `[8,10]`. Guess `9`. A correct guess leaves the total at `$7`; otherwise pay `$9` as well.
    - If it is higher than `9`, it must be `10`; guessing `10` finishes with `$7 + $9 = $16` paid.
    - If it is lower than `9`, it must be `8`; guessing `8` also finishes with `$16` paid.
  - If the answer is lower than `7`, the range becomes `[1,6]`. Guess `3`. A correct guess costs `$7`; otherwise the total becomes `$7 + $3`.
    - If it is higher than `3`, search `[4,6]` by guessing `5`. A correct guess costs `$10`; otherwise pay another `$5`. The remaining answer is `6` or `4`, and either final guess leaves the paid total at `$7 + $3 + $5 = $15`.
    - If it is lower than `3`, search `[1,2]` by guessing `1`. A correct guess costs `$10`; otherwise pay another `$1`, then guess the forced answer `2` with `$7 + $3 + $1 = $11` paid.
  - The largest cost among every branch is `$16`, so that amount guarantees a win.

```text
                  guess 7
             lower /   \ higher
              guess 3   guess 9
             /     \    /     \
        guess 1  guess 5  8     10
            \     /   \
             2   4     6
```

**Example 2**

- Input: `n = 1`
- Output: `0`
- Explanation: Only `1` can be chosen, so guessing it immediately requires no payment.

**Example 3**

- Input: `n = 2`
- Output: `1`
- Explanation: Guess `1`. If correct, the cost is `$0`; otherwise pay `$1`, after which the higher number must be `2`. Thus the worst-case cost is `$1`.
