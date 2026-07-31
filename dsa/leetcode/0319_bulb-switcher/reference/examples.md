## Examples

**Example 1**

- Input: `n = 3`
- Output: `1`
- Explanation: The bulbs begin `[off,off,off]`. Round `1` changes them to `[on,on,on]`; round `2` produces `[on,off,on]`; and round `3` produces `[on,off,off]`. Exactly one bulb remains on.

```text
initial:  off  off  off
round 1:  on   on   on
round 2:  on   off  on
round 3:  on   off  off
```

**Example 2**

- Input: `n = 0`
- Output: `0`

**Example 3**

- Input: `n = 1`
- Output: `1`
