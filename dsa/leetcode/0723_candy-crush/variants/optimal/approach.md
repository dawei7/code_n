## General

**Simulate rounds until no crush is possible**

One crush can cause candies above it to fall, and those moved candies may create new groups. Therefore a single scan is not sufficient. The exact solution repeats complete rounds:

1. Find and mark every horizontal group that must be crushed.
2. Find and mark every vertical group that must be crushed.
3. If anything was marked, apply gravity to every column.
4. Start another round on the changed board.

The loop ends only when a full marking pass finds no group. At that moment gravity is unnecessary and the board is stable by definition.

**Why crushing must be simultaneous within a round**

All groups present at the beginning of a round must disappear together. If a horizontal group were immediately replaced with zero before checking vertical groups, an intersecting vertical group might be broken and missed.

The solution solves this by marking a candy for removal with the negative version of its type. A positive value is a live candy. A negative value is scheduled to be removed in the current round. Zero is empty.

The candy’s magnitude is preserved, so comparisons use `abs(board[i][j])`. A horizontally marked candy can still participate in a vertical match during the same marking phase. This is exactly what simultaneous detection requires.

**Mark every horizontal run**

For each row, the scan considers every position `j` from `2` onward as the right endpoint of a length-three window. It checks that the current cell is nonzero and that the absolute values at `j`, `j - 1`, and `j - 2` are equal.

When they match, all three cells are assigned the negative absolute candy type and `run` becomes true.

Checking overlapping triples is sufficient for runs longer than three. A run of four equal candies contains triples ending at its third and fourth positions. The first triple marks the first three; the next comparison still recognizes their type through `abs` and marks the fourth as part of the overlapping triple. The same reasoning covers any longer run.

The nonzero check prevents three empty cells from being treated as a candy group. A negative marked value remains truthy, so it can still extend another same-type triple in the current phase.

**Mark every vertical run without erasing horizontal evidence**

The vertical scan applies the same ending-window idea to each column, considering rows `i - 2`, `i - 1`, and `i`.

It also compares absolute values. Consequently, if a candy was already marked by a horizontal run, its original type remains visible to the vertical scan. A cross-shaped intersection is marked completely in one round rather than allowing the first direction checked to hide the other.

At the end of both scans, every cell belonging to at least one qualifying run is negative. Cells not belonging to such a run remain positive or zero.

**Gravity removes marked cells in place**

If `run` is true, each column is compacted independently. A write pointer `k` begins at the bottom row. Another pointer `i` scans from bottom to top.

Whenever `board[i][j] > 0`, that cell is a surviving candy. The solution copies it to `board[k][j]` and decrements `k`. Zero cells and negative marked candies are skipped.

After all rows have been scanned, positions from `k` up to the top are filled with zero. Thus all surviving candies keep their original bottom-to-top order and settle as low as possible, while every removed or previously empty position becomes part of the empty region above them.

No separate “turn negative cells into zero” pass is needed. The compaction copies only positive survivors, and the zero-fill overwrites everything not occupied by those survivors.

**Why the in-place copy is safe**

During the bottom-up scan, the write pointer is never above the current read position. Skipped empty or marked cells create space below, so a survivor is either left in place or copied downward. The algorithm never overwrites an unread survivor above the scan position.

Preserving order matters. Gravity moves candies vertically but does not allow them to pass through one another. Reading and writing from the bottom upward keeps the lowest survivor lowest, followed by the next survivor, and so on.

**Why another round is necessary**

Gravity changes adjacency. Candies that were separated by a crushed group may become neighbors, potentially creating a new horizontal or vertical run. The next iteration detects those newly formed groups.

On the other hand, if both marking scans leave `run` false, the board was not modified during that iteration. There are no horizontal or vertical triples, so no longer run can exist either: every run of at least three contains a triple. The board is stable and can be returned.


During one marking phase, every qualifying horizontal or vertical run is found because each contains at least one scanned length-three window. Every marked cell belongs to a qualifying window, so no unrelated candy is removed. Absolute-value comparison ensures overlaps and intersections are evaluated against the pre-crush candy types, giving simultaneous removal.

The gravity phase deletes exactly the marked candies, retains exactly the positive candies, preserves their vertical order, and places them at the lowest possible rows. It therefore produces exactly the board dictated by one legal crush-and-fall round.

Each successful loop iteration performs one correct round. When the loop stops, no qualifying group exists, so the returned board is stable. By induction over rounds, it is the same stable board obtained by repeatedly applying the problem’s rules.

## Complexity detail

Let `m` be the number of rows, `n` the number of columns, and `R` the number of successful crushing rounds.

In one iteration, the horizontal scan examines `O(mn)` cells, the vertical scan examines `O(mn)` cells, and gravity, when needed, examines and writes `O(mn)` cells. A final unsuccessful stability scan also costs `O(mn)`. The total time is therefore `O((R + 1)mn)`, commonly stated as `O(Rmn)` when focusing on successful rounds.

Every successful round removes at least three positive candies, and no new candies enter the board. Hence `R` is at most on the order of `mn`, giving a conservative worst-case bound of `O((mn)^2)` time. In ordinary boards the number of rounds is usually much smaller, so the parameterized `O(Rmn)` description is more informative.

The algorithm modifies `board` in place. Beyond loop indices, the Boolean `run`, and the gravity write pointer, it allocates no structure proportional to board size. Auxiliary space is `O(1)`, excluding the input board that is also returned.

## Alternatives and edge cases

- **Collect coordinates in a set:** Scan the board and add every crushable position to a set, then clear those cells and apply gravity. This is conceptually direct but needs `O(mn)` extra space in the worst case. Negative marking stores the same information inside the board.

- **Crush immediately while scanning:** This is incorrect because an erased cell may belong to another horizontal or vertical group that must be detected simultaneously. Mark first, then remove.

- **Copy the board for each round:** Comparing against an unchanged snapshot also preserves simultaneity, but it requires `O(mn)` additional memory per working copy. Absolute-value marking achieves the same effect in place.

- **Recursive simulation:** Recursively process another board after every gravity step. It expresses the repeated rounds but uses stack depth proportional to the number of rounds. The iterative loop avoids that risk.

- **Runs longer than three:** Overlapping length-three windows mark the whole run. There is no need to measure its complete length separately.

- **Horizontal and vertical intersection:** The shared cell may already be negative when the second direction is scanned. Using absolute values preserves its candy type, so both full groups are marked.

- **Zero regions:** The explicit nonzero check prevents empty cells from being falsely recognized as equal candies.

- **Already stable board:** The first scans leave `run` false. Gravity is skipped, the loop exits, and the original board is returned unchanged.

- **Cascading groups:** Only groups present before the current gravity step are crushed in that round. New groups caused by falling are correctly deferred to the next iteration.

- **Input mutation:** The method intentionally changes `board` in place and returns the same board object. Callers needing the original layout would have to provide a copy.
