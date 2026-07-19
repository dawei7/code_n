## General
**Compress earlier spans on a decreasing stack**

Maintain a stack of pairs `(price, span)` whose prices are strictly decreasing from bottom to top. For a new `price`, begin its span at one for today. While the stack top has price less than or equal to the new price, pop that pair and add its stored span.

Each popped pair summarizes a contiguous block of days that all qualify for the new span. After all qualifying blocks are merged, either the stack is empty or its top is the nearest earlier price strictly greater than today's price, exactly where the span must stop. Push the new pair with its combined span and return that span.

After each call, every stack pair represents a contiguous block ending at its recorded day, and the pair's span is that block's size. Stack prices are strictly decreasing because all smaller or equal tops are removed before the new pair is pushed. The popped blocks are consecutive and all have prices at most today's price; the first pair left behind, if any, is strictly greater. Therefore the accumulated count includes precisely the maximum valid suffix and every returned span is correct.

## Complexity detail
Each quote is pushed once and can be popped at most once over the entire stream. Across $q$ calls, the total work is $O(q)$, giving amortized $O(1)$ time per `next` call. In a strictly decreasing stream no pair is removed, so the stack can hold $q$ pairs and uses $O(q)$ space.

## Alternatives and edge cases
- **Scan all previous prices:** Walking backward until a greater price is found is correct, but a non-decreasing stream takes $O(q^2)$ total time.
- **Store previous-greater indices:** A monotonic stack of indices also works, but storing compressed spans makes the returned count direct.
- **Segment tree over prices:** Range structures can answer related history queries, but add $O(\log q)$ updates and unnecessary complexity.
- **First quote:** Its span is always one.
- **Equal prices:** The comparison is less than or equal, so equal-price blocks are popped and merged.
- **Strictly decreasing prices:** Every span is one and every quote remains on the stack.
- **Strictly increasing prices:** Each quote consumes the entire compressed history and its span equals the number of days seen.
- **Large price boundary:** Only comparisons and counts are used, so `price = 100000` needs no special handling.
