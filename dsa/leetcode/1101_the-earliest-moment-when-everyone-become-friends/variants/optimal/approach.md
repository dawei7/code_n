## General
**Process events in temporal order.** The input need not be sorted, so first order the logs by timestamp. Connectivity only gains edges over time; the first chronological prefix that forms one component determines the answer.

**Represent friendship circles with union-find.** Start with each person as a separate parent and maintain `components = n`. For every log, find the roots of its two people. If the roots differ, join the smaller tree beneath the larger one and decrement the component count. Path compression keeps later root searches short.

**Stop at the first single component.** An event whose endpoints already share a root changes nothing, even if the two people were never direct friends before. When a successful union reduces `components` to 1, every label belongs to the same transitive friendship group, so return that event's timestamp immediately.

Before processing a log, union-find's sets are exactly the connected components formed by earlier events. A successful union adds the current edge between two such components; a redundant edge leaves them unchanged. This invariant means the first moment the count becomes one is both sufficient for universal acquaintance and earlier than any later possible answer.

## Complexity detail
Sorting $m$ logs costs $O(m \log m)$. With path compression and union by size, the $m$ union-find operations cost $O(m\alpha(n))$, where $\alpha$ is the inverse Ackermann function. The sorted log copy uses $O(m)$ space and the parent and size arrays use $O(n)$.

## Alternatives and edge cases
- **Graph traversal after every event:** Rebuilding reachability is correct but can require $O(m(m+n))$ time.
- **Binary search over timestamps:** Test connectivity for chronological prefixes, but repeated graph construction is more work than the one-pass union-find method.
- **Redundant transitive edge:** If both endpoints already have the same root, the component count must not change.
- **Unsorted logs:** Returning during input order rather than timestamp order can produce the wrong moment.
- **Never connected:** Remaining with more than one component after all logs requires `-1`.
- **Two people:** Their first and only connecting event immediately supplies the answer.
