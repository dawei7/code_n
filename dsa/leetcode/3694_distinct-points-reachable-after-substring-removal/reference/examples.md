## Examples

**Example 1**

- Input: `s = "LUL", k = 1`
- Output: `2`
- Explanation: Removing one character can leave `"UL"`, `"LL"`, or `"LU"`. Those walks end at $(-1,1)$, $(-2,0)$, and $(-1,1)$, respectively. The repeated endpoint is counted once, so the two distinct reachable points are $(-1,1)$ and $(-2,0)$.

**Example 2**

- Input: `s = "UDLR", k = 4`
- Output: `1`
- Explanation: The only legal choice removes the complete string. Executing the resulting empty string leaves the walker at $(0,0)$, producing one distinct endpoint.

**Example 3**

- Input: `s = "UU", k = 1`
- Output: `1`
- Explanation: Removing either occurrence leaves `"U"`. Both choices therefore finish at $(0,1)$, so only one final coordinate is distinct.
