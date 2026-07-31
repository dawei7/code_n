## General

**Only sorted neighboring special floors can bound a maximal interval**

Sort `special` in increasing order. Any special-free interval strictly between
two designated floors is longest when its boundaries are consecutive special
floors in that order. If their numbers are $a<b$, the eligible floors are
$a+1$ through $b-1$, so the interval length is $b-a-1$.

**Include both rented-range boundaries**

The first possible interval begins at `bottom` and ends immediately before the
smallest special floor, giving `special[0] - bottom` floors. Likewise, the last
possible interval begins immediately after the largest special floor and ends
at `top`, giving `top - special[-1]` floors.

Initialize the answer with the lower boundary gap, scan every adjacent sorted
pair for an interior gap, and finally compare the upper boundary gap.

**Why these gaps cover every answer**

Take any consecutive interval without a special floor. Moving its left
endpoint downward and its right endpoint upward remains valid until each side
reaches either the rented-range boundary or a special floor. Therefore every
maximal valid interval is exactly one of the two boundary gaps or a gap between
adjacent sorted special floors. The scan measures all of them, so their maximum
is the requested length.

## Complexity detail

Let $m=\lvert\texttt{special}\rvert$. In-place sorting costs
$O(m\log m)$ time, and the following gap scan costs $O(m)$ time. Python's
comparison sort uses $O(\log m)$ auxiliary stack space on ordinary inputs; the
gap scan itself uses $O(1)$ space.

## Alternatives and edge cases

- **Boolean array over all rented floors:** Marking every floor makes the scan straightforward, but `top - bottom` may approach $10^9$, far beyond practical array size.
- **Repeatedly select the next special floor:** This avoids calling a sort but takes $O(m^2)$ time when each next boundary is found by a fresh scan.
- **Sentinel boundaries:** Adding `bottom - 1` and `top + 1` can unify the gap formula, but it either copies the list or mutates it with artificial values.
- **Every floor is special:** Every measured gap is zero, so the answer is zero.
- **Special floor at a boundary:** The corresponding lower or upper boundary gap is zero.
- **One special floor:** Compare only the floors below and above that floor.
- **Large floor numbers:** Complexity depends on the number of special floors, not on the numeric width of the rented interval.
