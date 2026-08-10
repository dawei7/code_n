## General

**Locate the row containing the target**

Ignoring the alternating direction for a moment, row $r$ of a complete binary tree contains labels from $2^{r-1}$ through $2^r-1$. Therefore, the target’s row is determined by the greatest power of two not exceeding `label`.

The first loop starts with `x = 1` and row number `i = 1`. While doubling `x` would still not exceed the target, it doubles `x` and increments `i`. When the loop stops, `x` is the first label value of the target’s row in ordinary left-to-right numbering, and `i` is the number of nodes on the root-to-target path.

The answer array is allocated with exactly `i` positions. The reconstruction works upward from the target, so it fills this array from right to left.

**Mirror a zigzag label within its row**

At row `i`, the numeric range is:

`low = 1 << (i - 1)` through `high = (1 << i) - 1`.

Two labels symmetric within this range sum to `low + high`. Thus the mirror of current zigzag label `label` is `low + high - label`.

For example, row four spans eight through fifteen and is labelled right to left. Zigzag label fourteen mirrors to ordinary positional label nine because `8 + 15 - 14 = 9`. In an ordinarily labelled complete binary tree, node nine has parent four.

**Move to the parent**

Ordinary complete-tree numbering gives a node’s parent by integer division by two. The expression:

`((1 << (i - 1)) + (1 << i) - 1 - label) >> 1`

first mirrors the current label and then shifts right, which is division by two. Because the labelling direction flips on the parent row, this resulting integer is exactly the parent’s displayed zigzag label.

The loop stores the current label in `ans[i - 1]` before computing its parent. It then decrements the row number and repeats. For label fourteen, the stored sequence from bottom upward is fourteen, four, three, one, which becomes `[1,3,4,14]` because positions are filled backward.

**Why the formula works at every level**

Within one row, zigzag labelling reverses the positional order precisely when ordinary row order and displayed row order disagree. Mirroring maps a displayed label to the corresponding position measured in the opposite direction. Dividing that positional label by two selects the parent position. The next row reverses direction, so the computed parent position is already expressed as that row’s displayed label.

Every iteration moves up exactly one row. The tree has one parent for every non-root node, so no choice or search is involved. After `i` iterations, the root has been written at index zero and the complete path is returned.

The root case also works. With `label = 1`, the first loop performs no doubling, the answer length is one, and the reconstruction writes one before terminating.

It is useful to distinguish the two roles of `label`. Initially it is the requested node, but during reconstruction it becomes the current ancestor’s displayed label. The row counter decreases in lockstep, so each mirror uses the correct range for that ancestor rather than the original target row.

## Complexity detail

Let $L$ be the requested label. The number of rows through $L$ is $\lfloor\log_2 L\rfloor+1$. The first loop advances once per row, and the reconstruction also advances once per row, so total time is $O(\log L)$.

The returned path contains one label per row and therefore requires $O(\log L)$ space. Apart from that required output, the algorithm uses only a few integer variables, so auxiliary working space is $O(1)$.

Bit shifts are constant-time under the usual fixed-width model. Python integers are arbitrary precision, but the constraint $L \le 10^6$ keeps every value small.

## Alternatives and edge cases

- **Convert through ordinary labels explicitly:** Determine row parity, mirror only reversed rows, compute a conventional parent, and mirror into the parent row. This is more verbose but can make the geometry easier to visualize.
- **Build the tree:** Generating every node through `label` wastes $O(L)$ time and space when only one logarithmic path is needed.
- **Use logarithms for depth:** `label.bit_length()` directly gives the row count in Python. The doubling loop avoids floating-point concerns and mirrors the mathematical derivation.
- **Root label one:** The result is the one-element path `[1]`.
- **First label of a row:** Mirroring sends it to the last positional label of that row before parent division.
- **Last label of a row:** Mirroring sends it to the first positional label.
- **Odd-numbered row:** The displayed order is ordinary, yet the combined mirror-and-parent formula still produces the correct displayed parent because the parent row reverses.
- **Even-numbered row:** Mirroring accounts for its right-to-left display before moving upward.
- **Power-of-two label:** The depth loop includes it in the newly started row because doubling `x` is allowed when equal to the target.
- **Maximum constraint:** Only about twenty rows are involved for a label up to one million.
- **Backward filling:** Appending parents would produce target-to-root order and require reversal; preallocating writes the requested root-to-target order directly.
