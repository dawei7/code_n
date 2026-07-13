# Card Flipping Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 822 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/card-flipping-game/) |

## Problem Description

### Goal

You are given two zero-indexed arrays `fronts` and `backs` describing cards on a table. Card `i` initially shows positive integer `fronts[i]` face up and has `backs[i]` face down. You may flip any number of cards, including none.

After the flips, an integer is good when it is face down on at least one card and is not face up on any card. Return the minimum possible good integer obtainable by choosing which cards to flip. If no integer can satisfy both conditions, return `0`.

### Function Contract

**Inputs**

- `fronts`: the positive integers initially facing up
- `backs`: the positive integers initially facing down, with `len(backs) = len(fronts)`

**Return value**

- The smallest integer that can be made good by flipping cards, or `0` when no good integer exists

### Examples

**Example 1**

- Input: `fronts = [1, 2, 4, 4, 7], backs = [1, 3, 4, 1, 3]`
- Output: `2`
- Explanation: Flip the second card so `2` is down and no card shows `2` face up.

**Example 2**

- Input: `fronts = [1], backs = [1]`
- Output: `0`
- Explanation: The same value remains face up regardless of this card's orientation.

**Example 3**

- Input: `fronts = [1], backs = [2]`
- Output: `1`
- Explanation: Flipping the card places `1` face down and `2` face up.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Identify values that can never be hidden**

If a card has the same value `x` on both sides, then `x` faces up on that card in every possible orientation. Consequently, `x` can never be good, even if another card can place `x` face down. Collect every value appearing on both sides of one card into a blocked set.

**Every other printed value is achievable**

Consider a value `x` printed anywhere that is not blocked. Orient one card containing `x` so that side faces down. For every other card currently showing `x`, its opposite side must differ from `x`; otherwise `x` would have been blocked. Flip each such card to hide `x`. These choices make at least one `x` face down and no `x` face up, so every printed, nonblocked value can be good.

**Choose the minimum feasible candidate**

Scan both sides of every card and take the smallest value absent from the blocked set. The impossibility result proves no blocked value can qualify, while the construction above proves every scanned nonblocked value can qualify. If the scan finds none, all printed values are permanently exposed somewhere and the required result is `0`.

#### Complexity detail

Let `n` be the number of cards. One pass builds the blocked set and a second pass examines the `2n` printed values, so time is $O(n)$. At most `n` distinct equal-sided values enter the set, giving $O(n)$ auxiliary space.

#### Alternatives and edge cases

- **Test every candidate by simulating orientations:** Trying each distinct printed value and rescanning every card can establish feasibility, but takes $O(n^2)$ time in the worst case.
- **Bounded Boolean table:** Because the original constraints bound printed values, an indexed blocked array can replace the hash set, but it ties the solution to that numeric limit.
- **Sort all printed values:** Sorting can find the smallest unblocked candidate after building the blocked set, but costs $O(n \log n)$ time when a linear scan is sufficient.
- **Equal-sided card:** Its value is blocked globally, not merely on that one card.
- **One card with different sides:** Either printed value can be made good; return the smaller one.
- **All cards have equal sides:** Every candidate is blocked, so return `0`.
- **A blocked value appears on other cards:** Those extra occurrences do not help because the equal-sided card always exposes it.
- **Duplicate nonblocked values:** They remain one candidate; orient every card that would otherwise show the value face up.

</details>
