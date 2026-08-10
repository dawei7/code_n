## General

**A valid placement must occupy one complete slot**

A word cannot have an unblocked letter or space immediately before or after it along its direction. Therefore it must exactly fill a run bounded by board edges or `'#'` cells.

The source tries every cell as a possible start in four directions, but calls the detailed checker only when the cell immediately before that start is blocked or outside the board.

**Verify the boundary after the word**

Helper `check(i,j,a,b)` uses direction vector $(a,b)$. For word length `k`, coordinate

`(i + a * k, j + b * k)`

is the cell immediately after the proposed word.

If that coordinate is in bounds and is not blocked, the slot continues beyond the word and placement is invalid. Returning false before scanning letters enforces exact slot length at the far boundary.

The caller's direction-specific condition enforces the near boundary. Together, both ends are closed by an edge or block.

**Match each word character**

The helper iterates through `word` from its first character to last while advancing by the direction vector.

At each position, it rejects an out-of-bounds coordinate. An empty space accepts any character. An existing letter accepts only the same character. A block rejects because it is neither a space nor the required letter.

If all characters fit and the post-word boundary was valid, the placement succeeds.

**Try all four orientations**

For left-to-right, direction is $(0,1)$ and the preceding cell is left of the start.

For right-to-left, direction is $(0,-1)$ and the preceding cell is right of the start. The word is not reversed in memory; its first character is placed at the rightmost starting cell and later characters move left, which represents the allowed orientation.

Top-to-bottom uses $(1,0)$ with the cell above as predecessor. Bottom-to-top uses $(-1,0)$ with the cell below.

The Boolean `and` expressions short-circuit, so `check` is called only for genuine slot-start boundaries.

**Trace a slot that is too long**

Suppose a horizontal unblocked run has four cells and the word length is three. Starting at the run boundary passes the predecessor check, but the coordinate after three characters is still the fourth unblocked cell. The helper rejects immediately.

Starting one cell later fails the predecessor condition because its neighbor inside the run is not a block. Thus a word cannot be embedded inside a longer slot.

**Why every valid placement is found**

Any valid placement has one starting cell in its reading direction. The preceding coordinate must be an edge or block, so the outer loop's corresponding start condition passes. Its following coordinate is also an edge or block, and all occupied cells match, so `check` returns true.

Conversely, a true checker result proves both slot boundaries, exact in-bounds length, no blocked occupied cell, and compatibility of every fixed letter. It therefore satisfies every rule.

**Why total checking remains linear in board size**

Although a checker can inspect up to `k` cells, it is invoked at the starts of blocked-separated runs in each direction. Along one row or column, the lengths inspected across such starts are bounded by the line's cells, with overlong slots often rejected at the far boundary immediately.

Across four directions, total work is $O(MN)$ rather than $O(MNk)$.

More concretely, horizontal starts partition each row into maximal unblocked runs, and vertical starts partition each column the same way. A run contributes at most its length to successful-length checking in each reading direction. Summing all horizontal run lengths is $MN$, as is summing all vertical run lengths. The constant four orientations therefore preserve the linear cell bound.

## Complexity detail

Let $M$ and $N$ be board dimensions. The outer loops visit $MN$ cells. Across all row and column slot starts and four directions, checked cell work is $O(MN)$. Total time is $O(MN)$.

The helper stores only coordinates and loop variables, so exact auxiliary space is $O(1)$ beyond call frames. This is tighter than the manifest's safe $O(\max(M,N))$ bound. The board is not modified.

## Alternatives and edge cases

- **Split rows and columns on blocks:** Compare each exact-length segment with the word and its reverse; clear but may allocate strings or lists.
- **Transpose the board:** Reuse horizontal logic for vertical slots, at the cost of $O(MN)$ extra storage.
- **Check letters without slot boundaries:** Incorrectly allows the word inside a longer unblocked run.
- **One-cell word:** Requires a one-cell slot bounded on both sides in its direction.
- **Existing matching letters:** Allowed and need no board mutation.
- **Existing mismatching letter:** Immediately rejects that orientation.
- **Blocked cell inside the word:** Rejected by compatibility checking.
- **Right-to-left and bottom-to-top:** Direction changes traversal; `word` itself remains in normal character order.
- **Board edge:** Serves as a valid slot boundary.
- **Several valid placements:** The first discovered returns true, which is sufficient.
- **Short-circuiting:** Avoids checker calls when the near boundary is invalid.
- **Input preservation:** Placement is tested logically without writing letters into `board`.
