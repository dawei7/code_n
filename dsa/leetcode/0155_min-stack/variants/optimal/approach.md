## General
**Each stack entry snapshots the minimum for its complete prefix**

For every pushed value, store `(value, minimum_through_here)`. The first entry uses its own value as the minimum. Because stack pop always removes a suffix, the minimum snapshot beneath it immediately becomes correct again without recomputation.

**Push needs only the previous top snapshot**

When pushing $x$, read the current top minimum when present and store `min(x, current_min)`. All older values are already summarized by that single field. `top` returns the value field; `getMin` returns the minimum field.

**Duplicated minima are represented independently at every depth**

At every position, the stored minimum equals the minimum of values from the bottom through that entry. Equal minimum values create separate entries with the same snapshot, so popping one copy still exposes another correct minimum.

**Trace a minimum being popped**

After pushes `-2, 0, -3`, snapshots are `-2, -2, -3`. Popping `-3` exposes the entry `(0,-2)`, so the minimum returns to `-2` in constant time without scanning.

**Each entry carries the minimum of its entire prefix**

For every stored pair `(value, prefix_min)`, `prefix_min` is the smallest value from the bottom of the stack through that entry. A push preserves this property by recording the smaller of the new value and the previous top's minimum. A pop removes one complete prefix snapshot, so the newly exposed pair already contains the minimum of the shortened stack.

Consequently `top` reads the current value and `getMin` reads the current prefix minimum without any search.

## Complexity detail
Each operation performs a fixed number of list and comparison operations, so all are $O(1)$. One pair is stored per stack value, giving $O(n)$ space.

## Alternatives and edge cases
- **Compute the minimum on demand:** Evaluating `min(stack)` makes `getMin` take $O(n)$ time and violates the contract.
- **Separate minimum stack:** has the same asymptotic bounds and can store only new minima, but synchronized duplicate handling needs care.
- **Encode differences in one integer stack:** can reduce fields but is less transparent and risks fixed-width overflow in some languages.
- Repeated minima must survive until every copy is popped. Values may be negative.
- Valid operation sequences never call `pop`, `top`, or `getMin` on an empty stack; a broader API would need explicit error behavior.
