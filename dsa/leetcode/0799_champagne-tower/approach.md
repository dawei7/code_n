## General

**Track how much liquid reaches each glass**

A glass can hold at most one cup, but more than one cup may flow into it before the excess leaves. The simulation table `f[i][j]` initially represents the total amount that has reached glass `(i,j)`.

The top glass receives the entire poured amount:

`f[0][0] = poured`.

All other entries begin at zero.

Processing rows from top to bottom works because liquid moves only to the next row. By the time the algorithm examines a glass, both of its possible parents have already sent all their overflow into it.

**Compute one glass's overflow**

If `f[i][j] <= 1`, the glass can contain everything it received. Nothing flows downward.

If `f[i][j] > 1`, exactly one cup remains in the glass and the excess is:

`f[i][j] - 1`.

The rules split that excess equally, so each child receives:

`half = (f[i][j] - 1) / 2`.

The left child is `(i+1,j)` and the right child is `(i+1,j+1)`. The method adds `half` to both because either child may also receive liquid from its other parent.

**Cap a processed glass at one**

After calculating overflow, the code assigns:

`f[i][j] = 1`.

This makes the table entry represent the glass's final fullness rather than its earlier flow-through amount. Descendant calculations use only the explicitly distributed `half` values, so discarding the excess from the parent entry loses no information.

Glasses receiving at most one cup are already valid fullness values and need no assignment.

**Why contributions must be added**

An interior glass `(i,j)` has two parents:

- `(i-1,j-1)` sends its right overflow;
- `(i-1,j)` sends its left overflow.

The total amount reaching the glass is the sum of both. Using assignment for either parent would overwrite the other's contribution. The `+=` operations correctly accumulate them before row `i` is processed.

Edge glasses have only one valid parent, but the same updates handle them naturally.

**Process only rows needed by the query**

The outer loop runs from row zero through `query_row` inclusive. Rows above the query must be processed so their overflow reaches it.

Processing the query row itself serves an additional purpose: if the queried glass received more than one cup, it is capped to one before the answer is returned. Overflow from that row is written to row `query_row + 1`, but those values are irrelevant to the requested result.

The fixed 101-by-101 allocation provides that extra child row safely because `query_row < 100`.

**Trace one poured cup**

Set `f[0][0] = 1`. The top glass is not above capacity, so no overflow is sent.

Every glass in row one remains zero. Querying `(1,1)` returns zero.

**Trace two poured cups**

The top glass receives two. Its excess is one, and each child receives one half.

Both row-one glasses contain 0.5, which is at most their capacity. Querying either returns 0.5.

**Trace four poured cups**

The top glass keeps one and sends 1.5 cups to each row-one glass. Each of those glasses keeps one and overflows 0.5 cup, split into 0.25 for each child.

The outer row-two glasses receive 0.25 from one parent. The middle row-two glass receives 0.25 from each parent, totaling 0.5.

This matches the described tower and demonstrates why interior additions from both parents matter.

**The row-processing invariant**

Before row `i` is processed, every `f[i][j]` equals the total liquid delivered by all paths from rows above, and no future row can send liquid upward into it.

For each glass, the algorithm retains `min(1, received)` and distributes exactly half of `max(0, received-1)` to each child. This matches the physical rule and establishes the correct delivered amounts for row `i+1`.

By induction, all glasses through the query row have correct final fullness when they are processed.

**Why floating-point division is appropriate**

Overflow may create halves, quarters, and smaller binary fractions. Python's `/` produces floating-point values.

The required answer accepts floating precision, and the simulation performs at most 100 layers. The computation directly follows the continuous quantity model rather than rounding intermediate liquid amounts to integers.

**Why the returned value is already between zero and one**

Every table entry begins nonnegative, and overflow additions are nonnegative. During the inclusive query-row pass, any queried value above one is explicitly set to one.

Therefore `f[query_row][query_glass]` is already a valid fullness fraction in `[0,1]`. The exact source does not need a final `min(1, value)` wrapper.


Each processed glass keeps exactly its capacity and sends exactly its excess, split evenly, to the correct children. Top-to-bottom order ensures all parent contributions arrive before a glass is processed.

The invariant proves the queried entry contains its physical final amount after the query row is capped. Returning that entry is therefore correct.

## Complexity detail

Let $r = query\_row$. The loops inspect:

$$
1+2+\cdots+(r+1)=O(r^2)
$$

glasses, with constant work per glass. Time is $O(r^2)$.

The exact source allocates a fixed `101 x 101` table regardless of `r`. Under the problem's permanently bounded 100-row domain, that is constant-size storage. If parameterized by a variable maximum row count, the literal table is $O(r^2)$ space, not the manifest's $O(r)$.

An $O(r)$-space implementation would keep only the current or next row. The manifest's rolling-space bound describes that optimization, while the displayed exact source deliberately uses the full fixed table.

## Alternatives and edge cases

- **Rolling one-dimensional row:** Propagate into a fresh next-row array and discard the current row, achieving $O(r)$ auxiliary space.

- **In-place one-dimensional update:** Possible with carefully chosen direction, but parent contributions are easier to reason about with separate rows.

- **Recursive simulation:** It would revisit shared interior descendants unless memoized and is less natural than topological row order.

- **Zero poured:** Every table entry remains zero.

- **Top-glass query:** The inclusive loop caps a poured amount above one and returns the correct fullness.

- **Edge glass:** It receives overflow from only one parent.

- **Interior glass:** It may accumulate contributions from two parents before being processed.

- **Exactly one cup received:** The strict `> 1` check sends no overflow.

- **Large poured value:** Repeated capping prevents returned fullness from exceeding one, while excess continues downward.

- **Extra allocated row:** It makes child writes from the maximum query row safe.
