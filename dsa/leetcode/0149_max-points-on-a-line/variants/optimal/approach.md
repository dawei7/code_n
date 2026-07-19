## General
**Fixing an anchor reduces line identity to a direction**

Choose each point `i` as an anchor and compare it with later points `j`. Every nontrivial line through the anchor is uniquely identified by an undirected normalized direction from anchor to partner. Count partner points per direction in a fresh map for each anchor.

Considering only later partners avoids repeated pair work and is still complete: every input line has an earliest-indexed member that sees all its other members later.

**Reduce integer deltas to one canonical rational direction**

For partner difference `dx = x₂ - x₁`, `dy = y₂ - y₁`, divide both by `gcd(abs(dx), abs(dy))`. Then normalize sign so opposite delta vectors on the same geometric line share one key—for example, require `dx > 0`, or when `dx = 0`, require a fixed positive `dy`.

Canonical vertical direction can be `(0,1)` and horizontal direction `(1,0)`. Avoid floating division: rational slopes such as $1/3$ remain exact, and no infinities or signed zeroes need special hash behavior.

**One direction bucket equals one line through the anchor**

For a fixed anchor, a direction count equals the number of processed partner points lying with the anchor on that exact line. Adding one for the anchor converts the largest count into the best line through it.

**Trace reducible and sign-reversed deltas**

From anchor `[1,1]`, points `[3,2]` and `[5,3]` both reduce to direction `(2,1)`, while other directions have different normalized pairs. Their count plus the anchor yields three points on that line.

**A normalized direction identifies one line through the anchor**

Fix an anchor. Two other points receive the same reduced direction pair exactly when their displacement vectors are scalar multiples, which means those points lie on the same line through the anchor. A direction bucket therefore never combines different lines.

Every line containing at least two input points also has an earliest indexed member. When that point becomes the anchor, every later point on the line enters the same bucket, so the algorithm considers the line at its full size. Taking the largest bucket over all anchors consequently finds the global maximum.

## Complexity detail
There are $n$ anchors and at most $n-1$ partner computations per anchor, giving $O(n^2)$ time. One anchor's direction table contains at most $O(n)$ keys and is discarded before the next anchor.

## Alternatives and edge cases
- **Floating-point slope:** is concise but rounding can split equal rational slopes or merge nearby unequal ones.
- **Check every point triple:** is direct but costs $O(n^3)$.
- **Line equation keys:** can work with careful integer normalization but require more coefficients than an anchor-relative direction.
- One or two points are always collinear. Vertical, horizontal, negative, and reducible directions need canonical forms.
- Points are distinct by contract, so `(dx, dy) = (0, 0)` does not occur; a generalized input with duplicates would need a separate duplicate count per anchor.
