## General
**Fixing an anchor reduces each line to a direction key**

For every anchor point $i$, compare it with each later point $j$. All lines through that anchor are distinguished by the direction of the partner's displacement, so a fresh hash map can count how many partners share each direction. Considering only later points is complete: every line has an earliest input position whose anchor pass sees all its other points.

**Reduce each integer displacement to one canonical pair**

Compute `dx = x2 - x1` and `dy = y2 - y1`. Use `(0, 1)` for every vertical direction and `(1, 0)` for every horizontal direction. Otherwise divide both components by `gcd(abs(dx), abs(dy))`, then negate both when `dx < 0`. The reduced key is exact, and forcing a positive horizontal component makes opposite displacement vectors on the same undirected line identical.

For one anchor, two partners receive the same key exactly when their displacement vectors are scalar multiples, which is equivalent to collinearity with the anchor. A bucket count plus one for the anchor is therefore the size of that line. When the earliest point of a globally optimal line is processed, its bucket contains every other point on the line, so the maximum over all anchors is the required answer.

## Complexity detail
There are $O(n^2)$ anchor-partner pairs, and one anchor's direction map contains at most $O(n)$ keys. With coordinate magnitude bounded by the verified source contract, integer arithmetic and `gcd` operate on bounded-size values, giving $O(n^2)$ legal-domain time and $O(n)$ auxiliary space. If coordinate bit width were treated as variable, each reduction would add an $O(\log C)$ factor for maximum delta magnitude $C$.

## Alternatives and edge cases
- **Floating-point slopes:** can split equal rational slopes or merge nearby unequal ones through rounding.
- **Check every point triple:** is exact but takes $O(n^3)$ time.
- **Normalized line equations:** can work but require three canonical coefficients instead of an anchor-relative direction pair.
- One or two points are always collinear.
- Vertical, horizontal, negative, and reducible slopes all need canonical forms.
- Points are distinct by contract, so the zero displacement never occurs; generalized duplicate-point input would require a separate count per anchor.
