## General

Because `nums` is non-decreasing, every connected component occupies one consecutive index interval. If an adjacent gap `nums[i] - nums[i - 1]` exceeds `maxDiff`, no edge can cross that gap: every node on the right has a value at least `nums[i]`, and every node on the left has a value at most `nums[i - 1]`. The two sides must therefore belong to different components.

Conversely, when an adjacent gap is at most `maxDiff`, nodes `i - 1` and `i` share an edge. A run of such adjacent edges gives a path between any two indices inside the run, even when the difference between their endpoint values exceeds `maxDiff`.

Scan from left to right and assign a component label to every index. Copy the previous label across an allowed adjacent gap and increment it across an oversized gap. A query has a path exactly when its two labels match. This preprocessing turns every query into one constant-time comparison.

## Complexity detail

Let $Q$ be the number of queries. Labeling all nodes takes $O(n)$ time, and answering the queries takes $O(Q)$ time, for $O(n+Q)$ total. The component array uses $O(n)$ auxiliary space; the returned boolean list uses $O(Q)$ output space.

## Alternatives and edge cases

- **Build every implicit edge:** A dense value range may produce $\Theta(n^2)$ edges, even though adjacent edges alone determine connectivity.
- **Scan gaps per query:** Checking every adjacent gap between each pair of endpoints is correct but can take $O(nQ)$ time.
- **Union-Find on adjacent nodes:** Unioning every allowed adjacent pair also takes near-linear time, but component labels are simpler for the already sorted indices.
- **Binary search over breakpoints:** Store the oversized-gap indices and test whether one lies between query endpoints in $O(\log n)$ per query; labels improve this to $O(1)$.
- **Repeated values with `maxDiff = 0`:** Equal adjacent values stay connected, while every positive gap begins a new component.
- **Endpoint value difference:** Two distant endpoints may still be connected through a chain of small adjacent gaps.
- **Self-query:** Both endpoints have the same label, so a node correctly reaches itself.
- **Reversed query endpoints:** Comparing labels is symmetric and requires no endpoint reordering.
