## General

Each sticker may be used any number of times, but each use contributes only the letters printed on one copy. Letters may be cut out and rearranged, so their order inside a sticker and their positions inside `target` do not matter. What matters is how many still-needed occurrences of each target character one sticker can satisfy.

The target length is at most `15`. That small bound makes it practical to represent progress with a bitmask and search at most `2^T` states, where

$$
T=\lvert\texttt{target}\rvert.
$$

The solution treats every application of one sticker as one unit-cost transition and uses breadth-first search to find the fewest transitions needed to reach the complete target.

**Bitmask state meaning**

Target position `i` corresponds to bit `i`.

- Bit `i` equal to `1` means that occurrence of `target[i]` has already been supplied.
- Bit `i` equal to `0` means it is still missing.

The empty state is integer zero because no bits are set. The complete state is

`(1 << n) - 1`,

whose lowest `n` bits are all one.

Representing positions rather than only distinct characters handles repeated target letters naturally. If `target` contains three occurrences of `a`, there are three separate bits. A sticker containing two `a` characters can set at most two of those currently unset bits.

**Why breadth-first search matches minimum sticker count**

Think of the `2^T` masks as vertices in an implicit directed graph. From state `cur`, applying one sticker produces another state `nxt`. Every such edge costs exactly one because it represents consuming one sticker copy.

Breadth-first search explores all states reachable with zero stickers, then all states first reachable with one sticker, then two, and so on. The variable `ans` records the current BFS depth.

The queue begins with state zero, `vis[0]` is marked true, and `ans` begins at zero. At the start of each layer, `len(q)` is the number of states at exactly that sticker count. Processing exactly that many entries keeps newly enqueued next-layer states separate.

When the complete mask is popped, `ans` is therefore the smallest number of sticker uses that can reach it.

**Applying one sticker to a state**

For each sticker string `s`, the code creates `cnt = Counter(s)`. This mutable frequency table represents the letters available from one fresh copy of that sticker.

The next mask begins as `nxt = cur`. Then the solution scans target positions from left to right.

For a position `i` with character `c`, it checks two facts:

1. `(cur >> i & 1) == 0`, so this target occurrence was not already satisfied before applying the sticker.
2. `cnt[c] > 0`, so the current sticker copy still has an unused `c`.

When both hold, one `c` is consumed with `cnt[c] -= 1` and bit `i` is set using

`nxt |= 1 << i`.

The frequency decrement is crucial. Without it, one printed character could incorrectly satisfy multiple equal target positions.

**Why checking bits from `cur` is safe**

The condition tests `cur` rather than `nxt`. At first this may look suspicious because `nxt` changes during the scan.

However, each target index `i` is visited exactly once in that scan. A bit newly set at index `i` will never be examined again during the same sticker application. For every later index, its bit in `nxt` is still identical to its bit in `cur` until that later index is processed. Therefore, using `cur` in the “already satisfied” test produces the same decisions as using `nxt` would.

**Why greedily filling the earliest matching positions loses nothing**

Suppose multiple unsatisfied target positions contain the same letter. The code uses a sticker's available copies of that letter on the earliest such positions.

Those occurrences are interchangeable because the target may be assembled by cutting and rearranging letters. No later decision depends on the original position of one `a` versus another `a`; it depends only on how many unsatisfied `a` occurrences remain.

Choosing earliest positions gives a canonical mask for each multiset of supplied letters. If another valid application used the same sticker letters on later equal-character positions, swapping those assignments to the earlier positions would not change future feasibility or sticker count. Thus the deterministic left-to-right choice does not discard an optimal solution.

**Avoiding repeated states**

After applying a sticker, the method checks `vis[nxt]`. A mask is enqueued only the first time it is discovered.

In an unweighted BFS, the first discovery always occurs through a shortest path. Reaching the same mask again with the same or more stickers cannot lead to a better final answer, because all future options depend only on the mask, not on which sticker sequence produced it.

This also handles a sticker that makes no progress. In that case `nxt == cur`, and `cur` is already visited, so the useless self-loop is not enqueued.

**A small state example**

Let `target = "aba"`. Its positions are:

- bit `0` for the first `a`;
- bit `1` for `b`;
- bit `2` for the second `a`.

From state `000`, applying sticker `"aa"` creates a counter with two `a` letters. The scan fills position `0`, then skips position `1` because the sticker has no `b`, then fills position `2`. The result is mask `101`.

Applying sticker `"b"` to `101` sets bit `1` and reaches `111`. BFS finds the complete state at depth two.

**Why impossible targets return `-1`**

If some required character can never be supplied, or sticker combinations cannot cover all occurrences, the full mask is unreachable. BFS still explores every reachable mask at most once. Eventually the queue becomes empty.

At that point no unexamined sequence can reach a new state, so the method returns `-1`.

**Why the algorithm is correct**

Every transition consumes exactly the characters available on one sticker copy and sets only previously missing occurrences, so every path from zero to a mask corresponds to a feasible collection of stickers.

Conversely, take any feasible sticker sequence. Apply its stickers in the same order using the solution's canonical earliest-position matching. Because equal-character target occurrences are interchangeable, each sticker can satisfy the same number of outstanding occurrences of each letter. The canonical transitions therefore reach the full mask in no more sticker uses than that feasible sequence.

BFS returns the shortest feasible path to the full mask. Hence its depth is exactly the minimum number of stickers.

## Complexity detail

Let `T = len(target)`, let `M` be the number of sticker types, and let

$$
S=\sum_{s\in\texttt{stickers}}\lvert s\rvert
$$

be the total number of characters across all sticker strings.

There are at most `2^T` masks, and each is processed once. For one state, the algorithm constructs a `Counter` for every sticker, costing `O(S)` total, and scans all `T` target positions for each of the `M` stickers, costing `O(MT)`.

The literal running-time bound is therefore

$$
O\!\left(2^T(S+MT)\right).
$$

A looser commonly stated bound such as `O(ST2^T)` also covers the work under the positive sticker-length constraints, but the expression above reflects the actual Counter construction and target scan separately.

The `vis` array has `2^T` Boolean entries, and the queue can hold `O(2^T)` masks. A temporary Counter uses space proportional to one sticker's distinct characters, at most `26` here. Under the usual unit-cost integer model, auxiliary space is

$$
O(2^T).
$$

If the bit storage of each mask is counted explicitly rather than treating a machine-sized integer as one word, storing `O(2^T)` masks takes `O(T2^T)` bits.

## Alternatives and edge cases

- **Bottom-up bitmask DP:** Store the minimum sticker count for each mask and relax every sticker transition. It visits the same state space and has similar complexity; BFS makes the unit-cost shortest-path interpretation explicit.

- **Memoized search on remaining letter counts:** Canonicalize the still-needed letters and recursively try stickers, caching each remainder. This often prunes well and can avoid distinguishing equal-letter positions.

- **Precompute sticker counters:** The exact code rebuilds `Counter(s)` for every state-sticker pair. Constructing the counters once would remove the repeated `O(S)` work per mask without changing transitions.

- **Discard irrelevant or dominated stickers:** A sticker with no target letters can be removed. A sticker whose useful letter counts are all no greater than another's can also be dropped as dominated.

- **Target length one:** The state space has only masks zero and one. BFS returns one if any sticker contains the character, otherwise `-1`.

- **Repeated target letters:** Separate bits represent separate required copies, while Counter decrements prevent one sticker letter from filling more than one bit.

- **Sticker with repeated letters:** Each occurrence in its Counter may satisfy one missing target occurrence.

- **Sticker makes no progress:** `nxt == cur` is already visited, so no self-loop enters the queue.

- **Unlimited sticker copies:** Every transition creates a fresh Counter, correctly restoring all characters for another use of the same sticker type.

- **Character absent from every sticker:** The corresponding target bit can never be set; BFS exhausts reachable states and returns `-1`.

- **Layer accounting:** The method checks for the complete state when popping, before expanding it. `ans` therefore equals the number of transitions used to reach that layer.

- **Small target bound:** Exponential state space is acceptable only because `T <= 15`, giving at most `32768` masks.
