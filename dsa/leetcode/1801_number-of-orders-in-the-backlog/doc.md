# Number of Orders in the Backlog

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/number-of-orders-in-the-backlog/) |
| Frontend ID | 1801 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Heap (Priority Queue), Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A stream of stock orders arrives in the form `[price, amount, orderType]`. Type `0` is a buy order and type `1` is a sell order. Unfilled quantities remain in a backlog while later orders are processed.

For a buy order, repeatedly match against the backlog sell order with the lowest price while that price is at most the buy price. For a sell order, repeatedly match against the backlog buy order with the highest price while that price is at least the sell price. Each match removes the smaller remaining amount from both sides; any unmatched part of the arriving order joins its own backlog.

After processing every order, return the total amount still present across both backlogs, reduced modulo $10^9+7$.

### Function Contract

**Inputs**

- `orders`: a list of $n$ triples `[price, amount, orderType]`, where $1 \le n \le 10^5$.
- $1 \le \texttt{price},\texttt{amount} \le 10^9$.
- `orderType` is `0` for buy and `1` for sell.

**Return value**

- Return the sum of all unfilled order amounts modulo $10^9+7$.

### Examples

**Example 1**

- Input: `orders = [[10,5,0],[15,2,1],[25,1,1],[30,4,0]]`
- Output: `6`

The final buy consumes both sell orders, leaving two units of that buy and four units from the first buy.

**Example 2**

- Input: `orders = [[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]]`
- Output: `999999984`

The remaining total is reduced modulo $10^9+7$ only after matching is complete.

**Example 3**

- Input: `orders = [[19,28,0],[9,4,1],[25,15,1]]`
- Output: `39`

The price-nine sell consumes four units of the buy; the price-25 sell cannot match the remaining price-19 buy.

### Required Complexity

- **Time:** $O(n \log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Expose the best price on each side**

Maintain sell orders in a min-heap by price and buy orders in a max-heap, represented in Python by negated prices. The heap roots are exactly the orders that the contract requires a new opposite order to consider first.

**Consume quantities without losing a partial order**

While prices cross, remove the best opposite order and trade the smaller of its amount and the arriving amount. If the removed order retains some quantity, push that remainder back with the same price. Continue until the arriving amount is exhausted or the best opposite price no longer permits a match.

**Store only the unmatched remainder**

If some of the arriving amount remains after matching, push it into its own side's heap. Thus, after every input order, the heaps contain exactly the unmatched backlog. Moreover, if both heaps are nonempty, their best prices do not cross; otherwise the processing loop would have matched them.

Each match follows the mandated price priority, preserves any unfilled quantity, and strictly reduces at least one order to zero. Induction over the input stream therefore proves the heaps represent the correct backlog, so summing their amounts gives the required result.

#### Complexity detail

Each of the $n$ arriving orders is inserted at most once. A heap entry may be popped and reinserted after a partial match, but every match completely removes either the arriving order or one existing entry; total heap operations remain $O(n)$. Each operation costs $O(\log n)$, giving $O(n\log n)$ time. The two heaps store at most $n$ entries and use $O(n)$ space.

#### Alternatives and edge cases

- **Unsorted backlog lists:** Scanning for the lowest sell or highest buy is correct but can require $O(n^2)$ total time.
- **Balanced ordered maps:** Price-to-amount maps also support best-price access in $O(\log n)$ time and can aggregate equal prices, but Python has no built-in balanced tree.
- **Exact fill:** When both quantities reach zero, push neither order back.
- **Partial fill of a backlog order:** Reinsert its remaining amount at the same price.
- **One order crosses several prices:** Continue matching until its amount is zero or the next best price is incompatible.
- **Equal prices:** Buy and sell prices may match because both price comparisons are inclusive.
- **Large amounts:** Keep full integer quantities during simulation and apply the modulus only to the final backlog total.

</details>
