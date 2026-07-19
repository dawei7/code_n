## General
**Resolve the bounded manager chain with self-joins**

Alias `Employees` three times. The first alias is the candidate employee, the second is that employee's direct manager, and the third is the next manager. Join each `manager_id` to the following alias's `employee_id`. Because a chain contains at most three managers, checking whether the third alias's `manager_id` is `1` covers direct reports, reports through one intermediate manager, and reports through two intermediate managers.

The head's self-reference makes shorter chains naturally fill the remaining joins with employee `1`. For example, a direct report follows candidate -> head -> head, while a three-manager chain follows candidate -> manager -> manager -> head. Explicitly exclude candidate `1` so that this useful self-reference does not place the head in its own result.

Every returned employee has a concrete joined chain ending at `1`, so no unrelated hierarchy can pass. Conversely, any allowed reporting chain has at most three manager edges; padding a shorter chain with the head's self-reference satisfies the same joins and condition, so every qualifying employee is returned.

## Complexity detail
With indexed lookup on the unique `employee_id`, each of the $n$ candidate rows performs a constant number of manager lookups, giving $O(n)$ logical time. The result and database join state can contain $O(n)$ rows, so the space bound is $O(n)$. A physical engine without usable indexes may choose a slower join plan.

## Alternatives and edge cases
- **Recursive common table expression:** Traversing outward from the head generalizes to arbitrary hierarchy depth, but the source's three-manager bound makes fixed self-joins simpler.
- **Unconstrained cross joins:** Filtering a Cartesian product can produce the same rows but may examine $O(n^3)$ combinations.
- **Direct reports only:** Testing `manager_id = 1` misses employees reached through intermediate managers.
- **Head row:** Employee `1` must be excluded even though its self-reference reaches `1`.
- **Separate self-managed hierarchy:** A chain rooted at an employee other than `1` never satisfies the final head condition.
- **Maximum-depth chain:** A candidate three manager edges from the head is still included.
- **Output order:** The contract accepts any order; the app-local query orders identifiers only for deterministic display.
