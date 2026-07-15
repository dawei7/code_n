# Online Stock Span

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 901 |
| Difficulty | Medium |
| Topics | Stack, Design, Monotonic Stack, Data Stream |
| Official Link | [LeetCode](https://leetcode.com/problems/online-stock-span/) |

## Problem Description
### Goal
Design an online algorithm that receives one stock price per day and reports the current day's price span.

For a given day, the span is the maximum number of consecutive days ending today for which every price is less than or equal to today's price. The interval always includes today and extends backward until the beginning of the stream or the first earlier price that is strictly greater.

Implement `StockSpanner` so each new quote is incorporated before its span is returned.

### Function Contract
Let $q$ be the number of calls made to `next`.

**Operations**

- `StockSpanner()`: initialize an empty price stream.
- `next(price)`: record today's price and return its span, where $1 \leq \texttt{price} \leq 10^5$.
- At most $10^4$ calls are made.

**App-local input**

- `operations`: calls encoded as `["next", price]`.

**Return value**

Return the span produced by every `next` call in order.

### Examples
**Example 1**

- Input: `operations = [["next",100],["next",80],["next",60],["next",70],["next",60],["next",75],["next",85]]`
- Output: `[1,1,1,2,1,4,6]`

**Example 2**

- Input: `operations = [["next",7],["next",2],["next",1],["next",2]]`
- Output: `[1,1,1,3]`

The final price `2` covers today and the preceding prices `1` and `2`, but stops before `7`.

**Example 3**

- Input: `operations = [["next",5],["next",5],["next",5]]`
- Output: `[1,2,3]`

### Required Complexity
- **Time:** $O(q)$
- **Space:** $O(q)$

<details>
<summary>Approach</summary>

#### General

**Compress earlier spans on a decreasing stack**

Maintain a stack of pairs `(price, span)` whose prices are strictly decreasing from bottom to top. For a new `price`, begin its span at one for today. While the stack top has price less than or equal to the new price, pop that pair and add its stored span.

Each popped pair summarizes a contiguous block of days that all qualify for the new span. After all qualifying blocks are merged, either the stack is empty or its top is the nearest earlier price strictly greater than today's price, exactly where the span must stop. Push the new pair with its combined span and return that span.

After each call, every stack pair represents a contiguous block ending at its recorded day, and the pair's span is that block's size. Stack prices are strictly decreasing because all smaller or equal tops are removed before the new pair is pushed. The popped blocks are consecutive and all have prices at most today's price; the first pair left behind, if any, is strictly greater. Therefore the accumulated count includes precisely the maximum valid suffix and every returned span is correct.

#### Complexity detail

Each quote is pushed once and can be popped at most once over the entire stream. Across $q$ calls, the total work is $O(q)$, giving amortized $O(1)$ time per `next` call. In a strictly decreasing stream no pair is removed, so the stack can hold $q$ pairs and uses $O(q)$ space.

#### Alternatives and edge cases

- **Scan all previous prices:** Walking backward until a greater price is found is correct, but a non-decreasing stream takes $O(q^2)$ total time.
- **Store previous-greater indices:** A monotonic stack of indices also works, but storing compressed spans makes the returned count direct.
- **Segment tree over prices:** Range structures can answer related history queries, but add $O(\log q)$ updates and unnecessary complexity.
- **First quote:** Its span is always one.
- **Equal prices:** The comparison is less than or equal, so equal-price blocks are popped and merged.
- **Strictly decreasing prices:** Every span is one and every quote remains on the stack.
- **Strictly increasing prices:** Each quote consumes the entire compressed history and its span equals the number of days seen.
- **Large price boundary:** Only comparisons and counts are used, so `price = 100000` needs no special handling.

</details>
