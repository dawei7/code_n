## General

Every move changes two resources: the visible board and the multiset of balls still in hand. The objective is to minimize how many insertions are made, so the solution explores possible game states with breadth-first search. Breadth-first search is appropriate because every edge in the state graph represents exactly one insertion and therefore has the same cost.

The queue begins with `(board, hand)`. A queue entry contains the current reduced board string and the still-available hand string. States are removed in first-in, first-out order, so all states reached with zero insertions are examined before states reached with one, all one-insertion states before two-insertion states, and so on. Consequently, when an empty board is first removed from the queue, its depth is the minimum number of balls needed.

The code does not store depth explicitly. Every transition removes exactly one character from `balls`, while the original `hand` never changes. Thus

`len(hand) - len(balls)`

is precisely the number of insertions used to reach the state. This value is returned when `state` is empty.

**Use one representative for each available color.** The loop `for ball in set(balls)` considers each distinct color currently in hand once. If the hand contains several identical red balls, choosing the first red occurrence or the second red occurrence creates the same board and leaves the same multiset, so branching on each physical copy would duplicate work. After choosing a color, `balls.replace(ball, '', 1)` removes exactly one occurrence and leaves the other copies available.

**Try insertion boundaries, then fully resolve the board.** For the selected color, the code tries `i` from `1` through `len(state)`. The expression

`state[:i] + ball + state[i:]`

inserts the ball at that boundary. The endpoint `i == len(state)` places it after the final ball. Index zero is omitted by this source as a symmetry/redundancy pruning choice; inserting inside the first run covers the equivalent same-color placement, and the search assumes a different-color prefix insertion need not be an indispensable first move. A fully literal enumeration of every rule-authorized boundary would use `0` through `len(state)`.

After an insertion, all forced removals must finish before another player move occurs. The helper `remove` implements that chain reaction. Its regular expression finds every run of at least three `B`, `G`, `R`, `W`, or `Y` characters and replaces those runs with the empty string. Removing a group may bring two separated groups of the same color together, producing a new removable run. The helper therefore repeats the substitution until a pass leaves the string length unchanged.

Checking length is sufficient because a substitution only deletes characters; it never changes a surviving character. If the length did not decrease, no run matched and the board is stable. If it did decrease, another pass is necessary because the new adjacencies did not exist before the deletion.

For example, inserting a red ball into a red pair may delete the three reds. If that red group lay between two white pairs, deletion joins the white pairs into a run of four, which the next `remove` pass deletes. The queue receives only the final stable board, matching the game's rule that all cascaded groups disappear before the next insertion.

**Why breadth-first order gives the minimum.** View each stable game configuration as a node and every legal one-ball insertion followed by complete collapse as an edge. A path of length `d` uses exactly `d` hand balls. The queue explores nodes by nondecreasing path length. Therefore no solution using fewer insertions can remain unexplored when an empty-board state at depth `d` is dequeued. The returned depth is minimal.

If the queue empties without reaching an empty board, every state retained by the search has been exhausted and no balls remain along deeper branches. The method returns `-1` to report that the board cannot be cleared under the explored transitions.

**Deduplicate revisited boards.** Different insertions can collapse to the same board. `visited` prevents repeatedly enqueueing the same board string, which dramatically reduces the search. Notice that the queue itself stores both `state` and `balls`, but the exact source's visited key is only `s`. Because BFS finds a board first at the shallowest insertion depth, this safely prevents strictly deeper rediscovery under the source's intended dominance assumption.

There is a subtle state-model point: two paths can conceptually reach the same board with different remaining color inventories. Board-only deduplication assumes the first retained inventory is sufficient to dominate later occurrences. The local Reference and unavailable editorial do not provide a formal proof of that stronger claim. A fully general state-space implementation can key visited states by `(s, normalized_remaining_hand)`; that preserves distinct future resources while keeping the same BFS idea. The approach here describes the exact source honestly, including its more aggressive pruning.

The initial board contains no group of three or more, so it is already stable. Every queued successor is also stable because `remove` is called before enqueueing. That invariant means the search never needs a separate collapse when a state is dequeued.

The tiny hand limit is what makes exhaustive search plausible. With at most five balls, the search depth is at most five. The board may briefly grow by one per insertion, but it begins with at most sixteen characters and often shrinks sharply after removals.

## Complexity detail

Let $n$ be the initial board length and $h$ the hand length. Search depth is at most $h$. At a level, a state can branch on at most $h$ colors and at most $n+h$ insertion positions. A loose upper bound on the number of generated configurations is exponential in the hand size; the manifest records $O((n+h)^{h+1})$ time.

Collapsing a board requires regular-expression scans over at most $n+h$ characters, possibly repeated as chain reactions occur. Those scan costs are absorbed into the manifest's conservative polynomial factor per exponentially many generated states. Deduplication can greatly reduce actual work but does not improve the worst-case exponential nature of exploring insertion sequences.

The queue and visited set retain exponentially many board configurations in the worst case. The manifest bounds this as $O((n+h)^h)$ space. Each stored string also has length $O(n+h)$; depending on whether string contents are counted separately, a more explicit character-storage bound includes another factor of $n+h$. The recursion stack is irrelevant because the search is iterative.

## Alternatives and edge cases

- **Depth-first search with memoization:** Explore insertions recursively and return the minimum remaining cost. It can use the same collapse routine, but breadth-first search obtains the minimum naturally from levels.
- **Count-based run removal search:** Process maximal board runs and insert only the number of matching balls required to reach three. This prunes many unproductive placements but needs careful reasoning about cascades and hand counts.
- **Full state deduplication:** Use `(board, sorted_remaining_hand)` as the visited key. This avoids merging equal boards that retain different color resources and gives the cleanest general correctness argument, at the cost of more states.
- **Insertion at index zero:** The source tries boundaries `1` through the end. A fully exhaustive formulation includes zero as well; same-color insertion at the first run is already equivalent to an internal position.
- **Repeated colors in hand:** `set(balls)` removes duplicate branches only for the current choice. `replace(..., 1)` consumes one copy, so remaining identical balls are not lost.
- **Chain reactions:** One regex substitution is insufficient. `remove` repeats until no deletion occurs, ensuring the queued board is stable.
- **Board clears immediately after insertion:** `remove` returns the empty string, which is enqueued and then recognized when popped at the next BFS step.
- **Hand becomes empty while the board remains:** That state generates no children because `set(balls)` is empty. If every branch reaches this condition, the queue drains and the result is `-1`.
- **Initial board stability:** The contract guarantees no initial run of three, so the source does not call `remove` before starting BFS.
- **Color alphabet:** The regular expression explicitly lists all five allowed colors. A new color outside that contract would never be removed and would require updating the pattern.
