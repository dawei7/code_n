## General

**Determine every part size before cutting any links**

The result must contain exactly `k` consecutive parts. Their sizes may differ by at most one, and every earlier part must be at least as large as every later part. These rules uniquely determine the size distribution once the list length `n` is known.

The exact solution first traverses the linked list without modifying it and counts its nodes. It then computes

`cnt, mod = divmod(n, k)`.

Here `cnt = n // k` is the number of nodes every part can receive, while `mod = n % k` is the number of nodes left after giving `cnt` nodes to each of the `k` parts.

The only valid way to distribute those leftover nodes is to give one extra node to each of the first `mod` parts. Thus part `i` has size

`cnt + int(i < mod)`.

The Boolean comparison `i < mod` becomes `True` for the first `mod` indices, and converting it to an integer contributes one there and zero afterward.

**Why this distribution is balanced**

Every size is either `cnt` or `cnt + 1`, so the largest and smallest sizes differ by at most one. All `cnt + 1` parts come first because the condition `i < mod` is true only for an initial prefix of part indices. Finally, the total number of assigned nodes is

`k * cnt + mod = n`,

so the distribution uses every node exactly once.

For example, when `n = 10` and `k = 3`, `cnt = 3` and `mod = 1`. The sizes are `4, 3, 3`. When `n = 3` and `k = 5`, `cnt = 0` and `mod = 3`. The sizes are `1, 1, 1, 0, 0`.

**Reuse the original nodes**

The solution does not build copied lists. It cuts the original linked list into independent pieces by changing the `next` pointer of each part’s final node to `None`.

The answer is initialized as `[None] * k`. This immediately reserves exactly `k` output positions and also gives the correct default for any empty parts.

The pointer `cur` begins at the original head. For each nonempty part:

1. Store `cur` in `ans[i]` because it is the head of the next part.
2. Compute this part’s required size `m`.
3. Move `cur` forward `m - 1` times. It then points to the last node belonging to this part.
4. Save `cur.next` as `nxt`. That node, if present, is the head of the following part.
5. Set `cur.next = None` to terminate the current part.
6. Continue from `nxt`.

Saving `nxt` before cutting is essential. If the link were erased first, the algorithm would lose access to the unprocessed remainder.

**Why the inner loop moves only `m - 1` times**

At the beginning of a part, `cur` already points to its first node. A one-node part therefore requires no movement before its tail is reached. The range `range(1, m)` performs exactly `m - 1` advances:

- For `m = 1`, the range is empty and `cur` remains on the single tail node.
- For `m = 4`, the loop advances from the first node to the second, third, and fourth nodes, making three moves.

After those moves, `cur` is always the part’s final node, so cutting `cur.next` creates the correct boundary.

**How empty parts are represented**

If `n < k`, the first `n` parts each receive one node and the remaining parts have size zero. After the final real node is detached, `cur` becomes `None`. The outer loop detects this and breaks.

Breaking is correct because `ans` was prefilled with `None`. All untouched positions already represent the required empty linked-list parts. The algorithm never tries to dereference `cur` for a zero-size part.

The same logic handles an initially empty list: `cur` is `None` before the first part, so the loop breaks immediately and returns `k` null entries.

**A detailed cut for ten nodes and three parts**

The sizes are `4, 3, 3`.

- Part 0 stores node 1 as its head, advances to node 4, saves node 5, and changes node 4’s next pointer to `None`.
- Part 1 begins at saved node 5, advances to node 7, saves node 8, and cuts after node 7.
- Part 2 begins at node 8, advances to node 10, saves `None`, and cuts the already-null final link.

The node order is unchanged inside every part, the parts appear in original order, and no node is copied or omitted.

**Why the algorithm is correct**

The quotient-and-remainder calculation proves that the chosen sizes use all `n` nodes, differ by no more than one, and put larger sizes first. During the cutting pass, `cur` always begins at the first unassigned node. Advancing `m - 1` links selects exactly the next `m` consecutive nodes, and cutting after the tail makes them one independent part. The saved successor becomes the first unassigned node for the next iteration, preserving this invariant.

Therefore every nonempty output part contains exactly its prescribed consecutive segment. If nodes run out, only prescribed zero-size parts remain, and their prefilled `None` entries are already correct. The returned array consequently satisfies every ordering, size, and coverage requirement.

## Complexity detail

Let `n` be the number of linked-list nodes.

The first traversal visits all `n` nodes to count them. During the second pass, each node is traversed as part of exactly one output part. Initializing the answer list and considering part positions costs `O(k)`. The total time complexity is therefore `O(n + k)`.

The returned array contains `k` head references, so it requires `O(k)` output space. Beyond that required result, the algorithm stores only counters and a few node pointers, giving `O(1)` auxiliary working space.

No new `ListNode` objects are created. This is why the linked-node storage does not grow with `n`. The tradeoff is that the original list is destructively split: after the call, it no longer exists as one connected chain.

## Alternatives and edge cases

- **Copy nodes into new lists:** This preserves the original list and can follow the same size calculation, but it creates `n` new nodes and uses `O(n)` additional space. The exact solution reuses nodes.

- **Find boundaries with repeated recounting:** One could rescan the remainder for every part, but that repeats work and can become quadratic. Counting once makes all sizes immediately available.

- **Round the average size:** Floating-point rounding does not reliably enforce the exact total or the rule that larger parts come first. Integer quotient and remainder give the unique valid distribution.

- **Cut before saving the successor:** Setting `cur.next = None` first would discard the only link to the remaining nodes. Always save `nxt` before modifying the tail.

- **Empty input list:** The preallocated answer of `k` null references is returned after the immediate break.

- **More parts than nodes:** Here `cnt = 0` and `mod = n`. The first `n` parts receive one node each; all remaining entries stay `None`.

- **Exactly divisible length:** When `mod = 0`, every part has exactly `cnt` nodes and the extra-node condition is false for all indices.

- **One requested part:** `cnt = n` and `mod = 0`. The sole result head is the original head, and only its already-final tail is terminated.

- **Input mutation:** Every part boundary is formed by overwriting a `next` pointer. Callers that need the original unbroken chain must copy it before invoking this implementation.
