# Sell Diminishing-Valued Colored Balls

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1648 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Binary Search, Greedy, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sell-diminishing-valued-colored-balls/) |

## Problem Description
### Goal
You manage an inventory of colored balls. The value of a ball is not fixed: at the moment it is sold, its value equals the number of balls of the same color that remain, including that ball. Selling one ball therefore decreases the value of every later ball of that color by one.

Given the starting quantity for every color and the exact number of customer orders, choose which color supplies each order so that the total profit is as large as possible. There are enough balls to fill all orders. Return the maximum profit modulo $10^9 + 7$.

### Function Contract
**Inputs**

- `inventory`: a list of $n$ positive integers, where `inventory[i]` is the initial number of balls of color `i`, $1 \le n \le 10^5$, and $1 \le \texttt{inventory[i]} \le 10^9$.
- `orders`: the exact number of balls to sell, where $1 \le \texttt{orders} \le \min\!\left(\sum_i \texttt{inventory[i]}, 10^9\right)$.

**Return value**

Return the greatest obtainable profit modulo $1{,}000{,}000{,}007$.

### Examples
**Example 1**

- Input: `inventory = [2, 5], orders = 4`
- Output: `14`

Selling from current values 5, 4, 3, and 2 earns $14$.

**Example 2**

- Input: `inventory = [3, 5], orders = 6`
- Output: `19`

**Example 3**

- Input: `inventory = [2, 8, 4, 10, 6], orders = 20`
- Output: `110`

### Required Complexity
- **Time:** $O(n\log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Always take a currently most valuable ball.** If one available color has value $a$ and another has the smaller value $b$, selling the $b$-valued ball first cannot improve the result: exchanging that sale for the $a$-valued ball gains at least as much now and leaves the lower-valued ball available. Thus an optimal schedule repeatedly sells from the highest current inventory levels.

**Process equal value bands together.** Sort the inventories in descending order and append a zero sentinel. After the first $k$ colors have been reached, all $k$ can be lowered from the current height $h$ to the next distinct height $\ell$. That complete band contains $k(h-\ell)$ balls and earns

$$
k\sum_{v=\ell+1}^{h} v
= k\frac{(h+\ell+1)(h-\ell)}{2}.
$$

If enough orders remain, add the complete band and continue with one more color tied at the top.

**Stop inside the final band.** When fewer than $k(h-\ell)$ orders remain, divide the remaining order count by $k$. Each complete round sells one ball from every active color and covers the next lower value. The quotient determines how many full value levels to include; the remainder sells that many additional balls at the resulting cutoff value. This exactly realizes the greedy sequence without simulating individual sales. Apply the modulus only to the final accumulated profit; arbitrary-precision arithmetic keeps the intermediate series exact.

#### Complexity detail

Sorting the $n$ inventory counts costs $O(n\log n)$. The subsequent band scan visits each sorted count once, so it costs $O(n)$. The sorted copy and sentinel use $O(n)$ auxiliary space.

#### Alternatives and edge cases

- **Max-heap simulation:** Repeatedly remove the largest count, add it to the profit, decrement it, and reinsert it. This directly follows the greedy rule but costs $O((n+\texttt{orders})\log n)$ and is too slow when `orders` approaches $10^9$.
- **Binary-search a cutoff value:** Find the lowest fully sold value level and sum all contributions above it, then account for the remaining orders at the cutoff. This can avoid sorting but requires careful boundary arithmetic and runs in $O(n\log V)$ for maximum inventory value $V$.
- **Sell colors in their input order:** Exhausting one color before considering a more valuable color can sacrifice profit and violates the exchange argument.
- Equal inventory counts simply enlarge the active group; a zero-width band contributes no sales.
- If the order count ends partway through a level, every active color has the same sale value, so which colors receive the remainder does not affect profit.
- A single color reduces to an arithmetic-series sum over exactly the requested number of balls.
- The guarantee on total inventory means the scan must encounter enough balls before the zero sentinel is exhausted.
- Large raw profits can exceed fixed-width integer ranges, so implementations in fixed-width languages need a sufficiently wide intermediate type and modular arithmetic.

</details>
