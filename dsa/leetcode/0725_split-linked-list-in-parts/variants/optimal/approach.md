## General
**Derive every part size before cutting**

Traverse the list once to count `n` nodes. Dividing `n` by `k` gives `base`, the size of every part, and `extra`, the number of parts that need one additional node. Thus part `i` has size `base + 1` when `i < extra`, otherwise `base`. This distributes every node and places all larger parts first.

**Detach consecutive segments in place**

Keep a pointer to the first unassigned node. For each of the `k` parts, save that pointer as the part head, advance through exactly the computed part size, save the next unassigned node, and set the current part's tail link to `None`. Then continue from the saved node. A zero-sized part naturally contributes `None` without advancing.

**Why the returned parts satisfy the contract**

Write $n=qk+r$ with $0\le r<k$. The quotient-and-remainder part sizes sum to $n$, differ by at most one, and are nonincreasing. Cutting consecutive segments of exactly those sizes visits every original node once and never reorders a node. Consequently the result contains exactly $k$ disjoint parts whose concatenation reconstructs the input order.

## Complexity detail
Counting and cutting visit the `n` nodes a constant number of times, while constructing the result visits all `k` part positions, for $O(n + k)$ time. The returned list of heads occupies $O(k)$ space; excluding that required output, the algorithm uses $O(1)$ auxiliary state.

## Alternatives and edge cases
- **Store every node in an array:** index the array to find each part boundary; this is also linear but uses $O(n)$ additional storage beyond the required output.
- **Recount the remaining suffix for each part:** recompute its length and choose the next size repeatedly; it is correct but can take $O(nk)$ time.
- **Copy values into new nodes:** this can form equal-sized parts but unnecessarily loses the original node identities and uses $O(n)$ new nodes.
- **More parts than nodes:** the first `n` parts contain one node each and the remaining parts are empty.
- **Empty input:** return exactly `k` empty parts.
- **One part:** return the entire original chain as the sole part.
- **Nonzero remainder:** only the earliest $n \bmod k$ parts receive the extra node.
