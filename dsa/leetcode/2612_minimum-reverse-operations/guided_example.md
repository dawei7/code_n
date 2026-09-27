# Guided Example: Minimum Reverse Operations

## 1. The instance, the operation, and the required answer

The array has length $n = 6$ and holds a single `1`, initially at position $p = 0$; every other cell holds `0`. Position $1$ is **banned**, the reversal length is $k = 4$, and the required output is the array of minimum operation counts

$$[0, -1, 2, 1, 2, 3].$$

| Parameter | Value | Meaning |
|---|---|---|
| $n$ | 6 | number of cells, positions $0$ through $5$ |
| $p$ | 0 | starting position of the single `1` |
| `banned` | `[1]` | a position the `1` may never occupy |
| $k$ | 4 | every reversal must cover exactly 4 consecutive cells |

One operation chooses a subarray of exactly $k$ consecutive cells and reverses it. Since the array contains a single `1` and otherwise only zeroes, the only observable effect is that the `1` moves: a reversal that does not cover the `1` leaves the array unchanged and is therefore never useful, while a reversal that covers it reflects its position inside the reversed block.

The instance is chosen because it separates the three ideas that decide the whole problem. Position $1$ is banned, yet the search must pass *through* it — the reversal over positions `[0, 3]` sweeps across the banned cell and lands on position `3`, which is legal, while landing *on* position `1` never is. The parity of the destinations alternates because $k$ is even. And several positions are reached only after two or three operations, so the answer is a genuine breadth-first distance rather than a one-step reachability question.

## 2. What a single reversal does to the position

Let the chosen subarray be positions $L$ through $L + k - 1$, with $0 \le L \le n - k$. Reversal is a reflection: a cell at offset $t$ from the left end of that block moves to offset $k - 1 - t$ from the same left end. The `1` sitting at position $i$ inside the block therefore lands at

$$j = L + \bigl((L + k - 1) - i\bigr) = 2L + k - 1 - i.$$

Two consequences follow directly.

- **Reachability is about the block, not the cell.** The `1` can reach $j$ exactly when some legal $L$ produces that $j$. For the block to cover $i$ we need $L \le i \le L + k - 1$, which is equivalent to
  $$\max(0,\; i - k + 1) \;\le\; L \;\le\; \min(i,\; n - k).$$
- **Every move changes position by an odd or even amount fixed by $k$.** Subtracting $i$ gives $j - i = 2(L - i) + k - 1$, and $2(L-i)$ is even, so
  $$j \equiv i + k - 1 \pmod 2.$$
  All destinations of one move share one parity, and that parity is determined by $k$: an **even** $k$ flips the position's parity on every move, an **odd** $k$ preserves it.

For this instance $k = 4$ is even, so the `1` alternates between the even positions $\{0, 2, 4\}$ and the odd positions $\{1, 3, 5\}$ on successive moves. This is not a detail of one instance: it partitions the search space into two independent parity classes, which is what makes the efficient search of Section 6 possible.

## 3. The complete one-move reachable set from a position

As $L$ sweeps its legal range, $j = 2L + k - 1 - i$ sweeps upward in steps of $2$. The reachable set is therefore a contiguous arithmetic progression, and its two endpoints come from the two extreme choices of $L$:

$$j_{\min} = \max(i - k + 1,\; k - 1 - i), \qquad j_{\max} = \min(i + k - 1,\; 2n - k - 1 - i).$$

The two terms inside each bound are worth naming, because they are easy to collapse into one and get wrong. The pair $i - k + 1$ and $i + k - 1$ is the range for a block that can slide freely; the pair $k - 1 - i$ and $2n - k - 1 - i$ is the correction that appears when the block is pinned against the left or the right edge of the array and can no longer be centred on $i$. The right-hand correction $2n - k - 1 - i$ is *not* symmetric to $i - k + 1$, and dropping it overstates reachability near the right end.

Applying the two bounds to every position of the instance gives the following reachability table. The parity column is $j_{\min} \bmod 2$, and the reachable set lists the same-parity values between the endpoints.

| From $i$ | Legal block starts $L$ | $j_{\min}$ | $j_{\max}$ | Parity of destinations | Reachable set |
|---|---|---|---|---|---|
| 0 | 0 only | 3 | 3 | odd | `{3}` |
| 1 | 0–1 | 2 | 4 | even | `{2, 4}` |
| 2 | 0–2 | 1 | 5 | odd | `{1, 3, 5}` |
| 3 | 0–2 | 0 | 4 | even | `{0, 2, 4}` |
| 4 | 1–2 | 1 | 3 | odd | `{1, 3}` |
| 5 | 2 only | 2 | 2 | even | `{2}` |

Two rows carry the instance's traps. Row $i = 1$ shows a reachable set that fits entirely in the even class even though position $1$ itself is odd — a banned cell, once entered in the table, is simply never available as a destination, and its own row would never be expanded. Row $i = 0$ shows the edge correction in action: with $k = 4$ and only the block `[0, 3]` available, the `1` has exactly one legal destination, and it is $3$, not the $2$ that a free-sliding formula would suggest.

## 4. Breadth-first search over the positions

Every legal reversal is an edge of weight $1$ between positions, so the minimum number of operations from $p$ to $i$ is exactly the breadth-first distance from $p$ to $i$ in the graph whose edges are the one-move reachability relations. The search is layered.

| Level $d$ | Frontier | Expansions at this level | Newly labelled at $d + 1$ |
|---|---|---|---|
| 0 | `{0}` | from 0 the reachable set is `{3}`; 3 is unbanned and unvisited | `{3}` |
| 1 | `{3}` | from 3 the reachable set is `{0, 2, 4}`; 0 is already labelled, 2 and 4 are fresh | `{2, 4}` |
| 2 | `{2, 4}` | from 2 the set is `{1, 3, 5}`: 1 is banned, 3 is labelled, 5 is fresh; from 4 the set is `{1, 3}`: both banned or labelled | `{5}` |
| 3 | `{5}` | from 5 the set is `{2}`, already labelled | none; queue exhausted |

The layering makes the minimality visible: position $3$ is discovered at level 1 and is never reconsidered, position $5$ is discovered at level 3 only after both level-2 sources were expanded, and no position receives a second, shorter label because breadth-first search settles a vertex the first time it is dequeued.

| Position | Final distance | The move that certifies it |
|---|---|---|
| 0 | 0 | the initial position, by definition |
| 1 | $-1$ | banned: it may be crossed by a reversal but never occupied |
| 2 | 2 | reached from 3 by reversing block `[1, 4]`, which sends 3 to 2 |
| 3 | 1 | reached from 0 by reversing block `[0, 3]`, which sends 0 to 3 |
| 4 | 2 | reached from 3 by reversing block `[2, 5]`, which sends 3 to 4 |
| 5 | 3 | reached from 2 by reversing block `[2, 5]`, which sends 2 to 5 |

The distances $0, 1, 2, 3$ follow the parity alternation predicted in Section 2: every move from an even position lands on an odd one and conversely, so even positions are reached in an even number of moves and odd positions in an odd number — with position $1$ the sole exception, unavailable for the reason the table gives.

## 5. Invariant and correctness of the layered search

**The graph model.** The state of the array is fully determined by the position of the `1`, because everything else is `0` and reversal never changes the multiset of values. Two arrays with the `1` in the same cell are identical, so modelling a state as an integer position loses nothing; the answer array is precisely the vector of distances in that model.

**Reflection is exact.** Reversal of a block sets the value at position $x$ inside the block to the value formerly at $L + (L + k - 1) - x$. Because exactly one cell holds `1`, the new position of the `1` is the reflection of the old one, $j = 2L + k - 1 - i$, and no other cell matters. A reversal of a block not containing the `1` fixes the state; such an operation is legal but never shortens anything, so ignoring it cannot change a minimum.

**The reachable set is exactly the progression.** For a fixed $i$ the map $L \mapsto 2L + k - 1 - i$ is strictly increasing in $L$, so the image of the legal interval of $L$ is the full set of values between $j_{\min}$ and $j_{\max}$ that share the parity $i + k - 1$. Nothing outside those two bounds is produced by any legal block, and every value inside them with the right parity is produced — by the block start $L = (j - k + 1 + i) / 2$, which the parity condition makes an integer. The search therefore neither invents moves nor misses any.

**Breadth-first layering gives minima.** Labels are assigned when a position is first extracted, and positions are extracted in non-decreasing order of distance because the frontier is a queue. If a position $i$ is labelled $d$, then every legal predecessor of $i$ either was labelled no later than $d - 1$, or is unlabelled and will discover $i$ at distance $d + 1$ or more; in the first case no shorter route exists, and in the second case $i$ could not have been reached earlier. This is the standard breadth-first certificate of minimality, and it requires only that each edge has weight $1$ — which the operation guarantees, since every reversal costs exactly one operation.

**Bans are enforced structurally.** Banned positions are removed from the structure of unvisited positions before the search begins, so they are never extracted, never labelled, and never expanded. Their answers stay at the sentinel $-1$ by construction. The ban constrains only the destination: a block may cover banned cells, as the move from $0$ to $3$ does.

## 6. Why the naive expansion is too slow, and what replaces it

A literal implementation of Section 4 would, for each expanded position, walk the whole integer interval from $j_{\min}$ to $j_{\max}$ and test every value for parity, bans, and previous visits. Near the middle of a long array those intervals have length close to $k$, so the search can inspect $\Theta(nk)$ cells in total, which is $\Theta(n^{2})$ when $k$ is comparable to $n$ and far beyond the $10^{5}$ ceiling on $n$.

The fix follows from one observation: **each position is labelled at most once for the entire search, and once labelled it can never be useful again.** So instead of scanning intervals repeatedly, keep the positions that have *not* yet been labelled, split into two classes by parity, in a structure that supports two operations: find the smallest unvisited position of a given parity that is at least $j_{\min}$, and delete a position. Expanding $i$ then means repeatedly taking the next unvisited same-parity position and stopping as soon as it exceeds $j_{\max}$.

| Structure for unvisited positions | Cost of one extraction | Total extraction cost over the search |
|---|---|---|
| Plain visited flags, rescanning each interval | $O(k)$ per expansion | $\Theta(nk)$, up to $\Theta(n^{2})$ |
| One balanced sorted set per parity, deleting on extraction | $O(\log n)$ | $O(n \log n)$ |
| Disjoint-set successor per parity, unioning forward on extraction | $O(\alpha(n))$ amortized | $O(n\,\alpha(n))$ |

The total is governed by the number of deletions, not by the number of expansions: there are at most $n$ positions in the two classes, and each is deleted once. An expansion that finds nothing new is cheap because the structure answers "smallest unvisited of this parity at or above $j_{\min}$" directly and reports that it already lies past $j_{\max}$. Keeping the two parities in separate structures is what makes the parity condition free: a class never has to be filtered, so the next candidate is genuinely the next candidate.

## 7. Boundary cases and traps

| Situation | Instance | Correct behaviour |
|---|---|---|
| $k = 1$ | $n = 4$, $p = 2$, `banned = [0, 1, 3]` | the only block containing $p$ is `[2, 2]`, so nothing moves and every other position is $-1$ |
| $k = n$ | $n = 5$, $p = 1$, `banned = [0, 2]` | only the whole-array block exists, so $j = n - 1 - p = 3$ in one move and nothing else is reachable |
| The only destination is banned | $n = 5$, $p = 0$, `banned = [2, 4]`, $k = 3$ | the single move from $0$ goes to $2$, which is banned; the search dies and all other positions stay $-1$ |
| A banned cell lies inside the block | $n = 6$, $p = 0$, `banned = [1]`, $k = 4$ | the block `[0, 3]` crosses position $1$ and the move is legal; only position $1$ itself stays unavailable |
| Even $k$ | $n = 8$, $p = 3$, `banned = [0, 6]`, $k = 4$ | destinations alternate parity: $\{2, 4\}$ at distance 1, then $\{1, 5, 7\}$ at distance 2 |
| Odd $k$ | $n = 7$, $p = 3$, `banned = [0, 6]`, $k = 3$ | destinations keep the parity of $p$: only $\{1, 5\}$ are reachable, both at distance 1 |

Three traps are worth stating separately. First, the ban is a constraint on the destination, not on the cells reversed — reading it as the latter makes the move from $0$ to $3$ illegal and the whole instance collapse to a single zero. Second, reachability is not the same as being unbanned: positions near the ends of the array can be permanently unreachable even when nothing is banned, as the $k = n$ row shows. Third, the reflected position formula must be applied to the *chosen* block, not to a block centred on $i$: when the centre would fall outside the array, the block is pinned and the mirrored destination is not the one a symmetric formula predicts.

## 8. Complexity of the parity-class breadth-first search

Building the parity classes costs $O(n)$ time plus one insertion per position, and the search performs at most $n$ expansions — each position is dequeued at most once, because it is labelled exactly when it is removed from its class. Each expansion performs a constant number of range lookups and then one deletion for every position it labels, and the total number of deletions across the whole search is at most $n$. With balanced sorted sets the running time is therefore

$$O(n \log n),$$

and with disjoint-set successors it falls to $O(n\,\alpha(n))$, which is effectively linear. The rejected alternative of rescanning each reachability interval costs $\Theta(nk)$ time, which is $\Theta(n^{2})$ in the worst case and cannot pass at $n = 10^{5}$.

Auxiliary space is $O(n)$: one distance slot per position for the answer array, and at most $n$ stored positions spread over the two parity classes, plus the queue, which also holds at most $n$ entries. The reachability bounds themselves need only a constant number of integers per expansion, and no information about the array contents is stored, because the position of the `1` is the entire state.
