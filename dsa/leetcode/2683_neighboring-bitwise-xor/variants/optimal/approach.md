## General

XOR all equations that define `derived`. Every `original[i]` appears exactly twice: once in the edge entering its position and once in the edge leaving it. Because $x \mathbin{\mathrm{XOR}} x = 0$, all original values cancel. A necessary condition is therefore that the XOR of every value in `derived` equals zero.

That condition is also sufficient. Choose `original[0] = 0`, then construct each next bit with `original[i + 1] = original[i] ^ derived[i]`. These assignments satisfy every non-closing edge. After processing through index $n-2$, the last edge closes precisely when the XOR of all derived bits is zero. Choosing `original[0] = 1` would produce the complementary valid array under the same condition.

Thus no explicit reconstruction is required: fold the input with XOR and return whether the result is zero.

## Complexity detail

Let $n$ be `len(derived)`. The algorithm reads every entry once, taking $O(n)$ time, and stores only the running XOR, using $O(1)$ auxiliary space. The linear time is optimal because flipping any single unread bit can change validity.

## Alternatives and edge cases

- **Construct an original array:** Trying either starting bit and propagating the equations also takes $O(n)$ time but allocates $O(n)$ space if the full candidate is stored.
- **Count set bits:** Since the input is binary, validity is equivalent to an even number of ones; XOR expresses the same condition without a separate count.
- **Single element:** Its circular neighbor is itself, so the only possible derived value is zero.
- **Two elements:** Both derived positions are the same XOR in any valid construction, so `[0,0]` and `[1,1]` are valid while mixed pairs are not.
- **All zeros:** Either an all-zero or all-one original array is valid.
