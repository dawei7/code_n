# Bitwise AND of Numbers Range

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 201 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/bitwise-and-of-numbers-range/) |

## Problem Description
### Goal
Given two nonnegative integers `left` and `right` with `left <= right`, consider every integer in the inclusive interval between them. Combine all of those values using the bitwise AND operation, retaining a bit only when it is set in every member of the range.

Return the resulting integer. Both endpoints participate, so an interval containing one value returns that value unchanged, while bits that flip anywhere inside a larger interval become zero. The range may be too large to enumerate value by value, so meet the required logarithmic or fixed-bit-width behavior rather than iterating across every integer.

### Function Contract
**Inputs**

- `left`: the nonnegative lower endpoint
- `right`: the nonnegative upper endpoint, at least `left`

**Return value**

The bitwise AND of all integers in the range.

### Examples
**Example 1**

- Input: `left = 5, right = 7`
- Output: `4`

**Example 2**

- Input: `left = 0, right = 0`
- Output: `0`

**Example 3**

- Input: `left = 49, right = 62`
- Output: `48`

### Required Complexity

- **Time:** $O(\log r)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

Only the common high-order binary prefix of `left` and `right` can survive the AND. Once the endpoints differ at some bit, the inclusive integer range crosses a boundary where that bit or every lower bit takes both zero and one values. Since AND needs a one in every number, all such suffix positions become zero.

Shift both endpoints right until they are equal, counting the shifts. The equal value is their common prefix with the unstable suffix removed. Shift it left by the same count to restore its original positions and fill the suffix with zeroes.

For `left = 5` (`101`) and `right = 7` (`111`), one shift gives `10` and `11`; a second gives `1` and `1`. The common prefix is `1`, and shifting it back two places yields `100`, or `4`, matching $5 \mathbin{\&} 6 \mathbin{\&} 7$.

Another way to see the suffix argument is through carry boundaries. If the endpoints differ above a low position, walking through every integer between them necessarily includes a number whose carry resets that low position to zero. No bit below the first endpoint difference can remain set throughout the range.

When the shifting stops, the remaining endpoint value consists exactly of all leading bits shared by both endpoints. Every number between the endpoints has that same prefix, so those prefix one-bits survive the range AND. Every removed position lies at or below the first differing position; the contiguous range contains at least one number with zero in each such position, so none can survive. Restoring only the shared prefix with zero suffix therefore equals the AND of the entire range.

#### Complexity detail

Each iteration removes one binary position. There are at most $O(\log right)$ significant positions, so time is $O(\log r)$ and the endpoint values plus shift count use $O(1)$ space.

#### Alternatives and edge cases

- ANDing every integer is correct but takes $O(right - left)$ operations in the worst case.
- Repeatedly clearing the lowest set bit of `right` while `right > left` is another efficient method; it removes suffix bits that cannot survive.
- Decimal prefixes have no relevance to bitwise stability.
- Equal endpoints return that value immediately. A range beginning at zero returns zero.
- Crossing a high power-of-two boundary can leave no common one-prefix and produce zero.

</details>
