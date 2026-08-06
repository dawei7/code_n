## Examples

**Example 1**

- **Input:** `data = [1,0,1,0,1]`
- **Output:** `1`
- **Explanation:** There are three possible contiguous locations for all three ones. Producing `[1,1,1,0,0]` takes one swap, producing `[0,1,1,1,0]` takes two swaps, and producing `[0,0,1,1,1]` takes one swap. The minimum is therefore `1`.

**Example 2**

- **Input:** `data = [0,0,0,1,0]`
- **Output:** `0`
- **Explanation:** The array contains only one `1`, so it is already grouped and requires no swap.

**Example 3**

- **Input:** `data = [1,0,1,0,1,0,0,1,1,0,1]`
- **Output:** `3`
- **Explanation:** One arrangement achievable with three swaps is `[0,0,0,0,0,1,1,1,1,1,1]`.
