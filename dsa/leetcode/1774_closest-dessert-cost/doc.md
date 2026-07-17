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

### Required Complexity

- **Time:** $O(n \cdot 3^m)$
- **Space:** $O(3^m)$

<details>
<summary>Approach</summary>

#### General

**Turn portion limits into three-way choices**

Each of the $m$ topping types contributes either zero, one, or two copies of its price. Therefore every complete topping selection corresponds to one length-$m$ sequence over $\{0,1,2\}$, giving at most $3^m$ selections. Start with the only sum available before processing toppings, `0`. For a topping price `cost`, extend every previously reachable sum by both `cost` and `2 * cost`, while retaining the old sum for the zero-copy choice.

**Why the generated sums are exactly the legal sums**

After the first $i$ topping types have been processed, the set contains precisely the totals obtainable using zero, one, or two portions of each of those $i$ types. This is true initially for zero types. Extending every old total by the three legal contributions of the next topping preserves all prior choices and introduces no illegal multiplicity, so the statement remains true for the next type. After all toppings, no valid topping total is missing.

**Compare complete desserts with the tie-break built in**

Pair each reachable topping sum with every base cost, because exactly one base is required. Compare a candidate total by `(abs(total - target), total)`: the distance is considered first, and the total itself selects the cheaper dessert when distances match. Since every legal base-and-topping combination is examined, the smallest comparison key is the required answer.

#### Complexity detail

There are at most $3^m$ reachable topping selections. Expanding the set and then combining its values with $n$ bases takes $O(n \cdot 3^m)$ time overall; the $O(3^m)$ generation term is absorbed because $n \ge 1$. The set of topping sums occupies $O(3^m)$ auxiliary space. Duplicate totals can make the actual set smaller, but the worst case still has exponentially many distinct sums.

#### Alternatives and edge cases

- **Depth-first enumeration:** Recurse through the zero-, one-, and two-copy choices for every topping and update the best cost at each leaf. It has the same worst-case time and uses only $O(m)$ recursion depth, but it may revisit equal topping totals produced by different choices.
- **Meet-in-the-middle:** Split the toppings, enumerate both halves, sort one side, and binary-search around the remaining target. This reduces the exponential factor for larger $m$, although the given limit $m \le 10$ makes direct generation simpler.
- **Target-bounded dynamic programming:** Track reachable sums only up to a chosen bound around `target`. This can be effective for small prices, but the stopping bound and the smallest overshoot must be handled carefully.
- A dessert may use no toppings, but it must always use exactly one base.
- A base cost can already exceed `target`; it remains a legal candidate and may be the closest total.
- When one achievable total lies below `target` and another equally far above it, the lower total must be returned.

</details>
