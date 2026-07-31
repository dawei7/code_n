## Function Contract

**Inputs**

- `n`: The required sequence length.
- `restrictions`: Pairs `[idx, maxVal]` giving upper bounds at distinct nonzero indices.
- `diff`: Exactly `n - 1` positive edge limits; `diff[i]` applies between positions `i` and `i + 1`.

The constructed sequence is not returned. A restriction is only an upper bound, and the adjacent-difference rule limits both upward and downward changes.

**Return value**

Return the greatest value that can appear in any valid sequence while the maximum over that entire sequence is as large as possible.
