## Examples

**Example 1**

- Input: `operations = ["PhoneDirectory","get","get","check","get","check","release","check"], arguments = [[3],[],[],[2],[],[2],[2],[2]]`
- Output: `[null,0,1,true,2,false,null,true]`
- Explanation:
  1. Construct a directory with slots `0`, `1`, and `2` available.
  2. The first two `get()` calls may choose any available numbers; the displayed run reserves `0` and then `1`.
  3. `check(2)` returns `true` because slot `2` remains free.
  4. The next `get()` reserves `2`, the only remaining number.
  5. `check(2)` now returns `false`.
  6. `release(2)` recycles that slot, after which `check(2)` returns `true`.
