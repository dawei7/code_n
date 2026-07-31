## Examples

**Example 1**

- Input: `n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 1`
- Output: `3`
- **Explanation:** The direct route `0 -> 2` has label string `"ab"`, so it respects the limit and costs `3`. The cheaper route `0 -> 1 -> 2` begins with two consecutive `a` characters and is therefore invalid when `k = 1`.

**Example 2**

- Input: `n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 2`
- Output: `2`
- **Explanation:** With two identical consecutive labels allowed, route `0 -> 1 -> 2` produces `"aab"`. It is valid and has cost `1 + 1 = 2`, which is less than the direct route's cost of `3`.

**Example 3**

- Input: `n = 3, edges = [[0,1,1],[1,2,1]], labels = "aaa", k = 2`
- Output: `-1`
- **Explanation:** The only route to node `2` is `0 -> 1 -> 2`, whose label string is `"aaa"`. Its run of three `a` characters exceeds `k = 2`, so no valid route reaches the destination.
