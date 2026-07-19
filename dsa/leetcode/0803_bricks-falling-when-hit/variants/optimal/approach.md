## General
**Reverse removals into additions**

Connectivity is difficult to maintain while vertices are deleted, but union-find handles additions efficiently. Copy the grid, apply all hits, and build connected components among the bricks that remain. Add one virtual roof node and join every brick in the top row to it; a brick is stable exactly when it belongs to the roof component.

**Restore each hit backward**

Process hits in reverse order. A hit that originally struck empty space changes nothing. Otherwise, record the roof component size, restore that brick, and union it with the roof when it is in row zero and with every present orthogonal neighbor.

The increase in roof-component size counts all bricks that become stable when this brick is restored. Subtract one for the restored brick itself, and clamp at zero. Reversing the event again means those other newly connected bricks are exactly the ones that fell after the corresponding forward hit.

The union-find state initially represents the grid after every hit. By backward induction, before restoring a hit it represents the grid immediately after that forward hit, and afterward it represents the grid immediately before it. Roof membership therefore matches stability at both times, making the component-size difference the exact answer.

## Complexity detail
Let the grid have $r \cdot c$ cells and let `h` be the number of hits. Building the final-state components and restoring all hits performs $O(r \cdot c + h)$ union-find operations, each amortized $O(\alpha(r \cdot c))$. The copied grid and union-find arrays use $O(r \cdot c)$ space; the output uses $O(h)$ additional required space.

## Alternatives and edge cases
- **Reverse flood fill:** After all hits, mark roof-connected bricks; when restoring a brick adjacent to stability, flood only newly stable bricks. Each brick is marked once, giving linear total traversal without union-find.
- **Forward rescan after every hit:** Recompute roof reachability and remove unstable bricks after each strike; it is direct but can take $O(h \cdot r \cdot c)$ time.
- **Offline dynamic connectivity:** More general deletion structures are possible, but reversing the fixed hit sequence is simpler.
- **Hit on empty space:** Record zero and do not add a brick during reversal.
- **Removed brick:** The directly hit brick is never included in the fallen count, which is why the restored brick is subtracted.
- **Multiple roof connections:** Unions within an already stable component do not increase its size and correctly contribute zero.
- **Top-row brick:** Restoring it connects directly to the virtual roof before neighboring components are measured.
