## Examples

**Example 1**

- Input: `secret = "1807", guess = "7810"`
- Output: `"1A3B"`
- Explanation: The `8` is a bull because it occupies the same position in both strings. The remaining guessed digits `7`, `1`, and `0` can each be paired with the same digit elsewhere in the secret, so all three are cows.

```text
index:   0 1 2 3
secret:  1 8 0 7
guess:   7 8 1 0
           B
cows:    C   C C
```

**Example 2**

- Input: `secret = "1123", guess = "0111"`
- Output: `"1A1B"`
- Explanation: The `1` at index `1` is the single bull. Of the two other unmatched `1` digits in `guess`, only one can use the remaining unmatched `1` in `secret`, so there is exactly one cow. Either unmatched occurrence may represent that same one-to-one match; the other must remain uncounted.

```text
bull:  guess[1] = 1  -> secret[1] = 1
cow:   guess[2] = 1  -> secret[0] = 1
       (guess[3] could be chosen instead, but not as an additional cow)
```
