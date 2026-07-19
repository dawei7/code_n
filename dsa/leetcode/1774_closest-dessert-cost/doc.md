# Closest Dessert Cost

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1774 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/closest-dessert-cost/) |

## Problem Description

### Goal

Build one dessert from the available ice cream bases and toppings. Every dessert must contain exactly one base flavor. For each topping type, independently choose zero, one, or two portions; choosing no toppings at all is also valid.

The arrays `baseCosts` and `toppingCosts` give the price of each base and of one portion of each topping, respectively. Among all desserts permitted by these rules, return a total price whose distance from `target` is as small as possible. If two achievable totals are equally close to the target, return the smaller total.

### Function Contract

**Inputs**

- `baseCosts`: an integer array of length $n$ containing the available base prices.
- `toppingCosts`: an integer array of length $m$ containing the price of one portion of each topping type.
- `target`: the desired total price.
- The constraints guarantee $1 \le n, m \le 10$, and every price and `target` is between $1$ and $10^4$.

**Return value**

Return the achievable dessert cost that minimizes the ordered pair

$$
(\lvert \text{cost} - \texttt{target} \rvert,\ \text{cost}).
$$

The second component expresses the smaller-cost tie-break.

### Examples

**Example 1**

- Input: `baseCosts = [1,7], toppingCosts = [3,4], target = 10`
- Output: `10`
- Explanation: Base cost `7` plus one portion of the `3`-cost topping reaches the target exactly.

**Example 2**

- Input: `baseCosts = [2,3], toppingCosts = [4,5,100], target = 18`
- Output: `17`
- Explanation: Base cost `3`, one `4`-cost topping, and two `5`-cost toppings total `17`; no valid combination totals `18`.

**Example 3**

- Input: `baseCosts = [3,10], toppingCosts = [2,5], target = 9`
- Output: `8`
- Explanation: Costs `8` and `10` are both one unit from the target, so the lower cost `8` wins.
