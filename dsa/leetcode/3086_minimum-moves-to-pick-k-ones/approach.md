## General

**What one pick costs.** Alice stands at one fixed index. If that index already contains `1`, she can pick it immediately at cost zero. An original `1` one position away can be swapped onto Alice's index in one move, an original `1` two positions away costs two swaps, and so on. Therefore, for a fixed Alice position, collecting an original one at position $p$ costs exactly $\lvert p-i\rvert$.

A change operation has a different but equally simple cost. Alice may change a zero that is not currently at her index into `1`, and then needs a swap to bring that one onto her index. Once the immediately adjacent original ones have been consumed, an available change can always be placed beside Alice. Creating the one costs one move and swapping it costs one more, so each manufactured pick costs exactly two moves.

These observations explain the order used by the exact source:

1. take a one already at Alice's position for zero moves;
2. take original adjacent ones for one move each;
3. use as many allowed changes as possible for two moves each;
4. if more picks are required, bring in farther original ones by distance.

The third step is safe because every original one left after the adjacent positions have been handled is at distance at least two. A change also costs two, so using a change cannot be worse than saving it and choosing one of those farther originals. It may tie a distance-two original, which is harmless.

**Prefix information about original ones.** The arrays `cnt` and `s` are built with 1-based positions. For every prefix ending at position $r$:

- `cnt[r]` is the number of original ones in positions $1$ through $r$;
- `s[r]` is the sum of the positions at which those ones occur.

Consequently, the number of ones in an inclusive interval $[l,r]$ is:

$$
\texttt{cnt[r]}-\texttt{cnt[l-1]}.
$$

The same prefix subtraction on `s` gives the sum of their positions. That sum lets the code obtain the total travel distance without visiting each one separately. For ones strictly left of Alice at position $i$, the distance total is:

$$
c i-\sum p,
$$

where $c$ is the number of selected positions and $\sum p$ is their position sum. For ones on the right, it is:

$$
\sum p-c i.
$$

**Trying every place Alice could stand.** The outer loop considers all $n$ possible values of `i`. Its `x` is the original bit at that position. The variable `need` begins as `k - x`: if `x` is one, that free pick is already accounted for.

The small inner loop checks positions `i - 1` and `i + 1`. It consumes an adjacent original one only while another pick is needed, adding one move for each. This detail prevents the nearby step from picking more ones than requested.

Next, `c = min(need, maxChanges)` chooses the number of changes actually used. The code subtracts `c` from `need` and adds `2 * c` to the candidate cost `t`. If this is enough, the candidate is complete and can immediately update the global answer.

**Finding enough distant originals.** If `need` is still positive, the code has deliberately excluded the center and the two adjacent positions; those have already been considered. It binary-searches a radius from two up to the farther end of the array. For a radius `mid`, it forms a left interval ending at `i - 2` and a right interval beginning at `i + 2`, clipped to the array boundaries. Prefix counts reveal whether these intervals contain at least `need` original ones.

If too few ones are present, a larger radius is necessary. If enough are present, the prefix position sums compute their complete movement cost and the code records the resulting candidate. It then continues into the smaller half of the radius range, looking for the first radius that reaches the needed count.

A subtle implementation detail is worth noticing: the source sums every original one found inside the first sufficient radius rather than explicitly removing a possible excess one at the outer boundary. At a newly sufficient radius, any excess can only come from the two equally distant boundary positions. The exact implementation relies on its enumeration of every Alice position and takes the minimum of all recorded candidates. The documentation here describes that behavior exactly; it does not replace it with the more common median-of-one-positions formulation.

**Why the global minimum represents the best plan.** Every legal strategy fixes some place where Alice receives the picked ones. For that place, zero-distance and distance-one originals are never worse than any alternative. Changes are never worse than the remaining originals, whose distances are at least two. The only unresolved choice is then how far Alice must reach for the remaining original ones, and the monotonic count of ones inside a growing radius makes binary search valid. Since the outer loop evaluates every receiving position, taking the smallest candidate covers the best location as well as the best mix of free, adjacent, changed, and distant picks.

For example, suppose Alice stands on an existing one, one neighboring position is also one, and three more picks are required after those. If two changes remain, the costs accumulated are zero, one, then four for the two manufactured ones. Only one distant original is still necessary. The radius search finds when such an original first becomes reachable and adds its swap distance.

## Complexity detail

Let $n$ be `len(nums)`. Building both prefix arrays takes $O(n)$ time and $O(n)$ space. The outer loop runs once for every possible Alice position. Its adjacent checks and change calculation take constant time, while its radius search performs $O(\log n)$ iterations. Every radius check uses a constant number of prefix-array lookups and arithmetic operations.

The exact implementation therefore takes $O(n\log n)$ time and $O(n)$ auxiliary space. This is an important source-level correction: the local Optimal manifest states $O(n)$ time, but that does not match the binary-search loop present in `solution.py`. No case or benchmark evidence is needed to see the discrepancy; it follows directly from the nested outer scan and radius binary search.

The integer prefix sums can reach $O(n^2)$ in value because they add positions, but Python integers safely represent them. The two prefix arrays dominate the extra memory.

## Alternatives and edge cases

- **Median over positions of ones:** A common formulation stores only one positions and evaluates groups around a median with prefix sums. It can be more compact and can achieve a linear scan after preprocessing, but it is not the algorithm implemented by this source.
- **Expand one step at a time:** Growing a radius and examining positions directly is easier to visualize, but doing it for every Alice position can degrade to $O(n^2)$.
- **No changes allowed:** The candidate must obtain all `k` picks from original ones; the prefix counts and distances handle this without a special branch.
- **Enough changes after local picks:** Once `need <= maxChanges`, the answer for that center is the accumulated local cost plus exactly two per missing pick, so no radius search is needed.
- **Alice starts on zero:** Then `x` is zero and there is no free pick. A change is still charged as two moves because the operation requires changing an index other than Alice's current index and then swapping the new one to her.
- **Alice starts on one:** That one reduces `need` before any move is counted.
- **Adjacent ones:** Each is consumed for one move, but only until `need` reaches zero.
- **Distant ones at the same radius:** The source's prefix query includes both sides at that radius; this is the subtle boundary behavior described above.
- **Array boundaries:** `max`, `min`, and the clipped interval endpoints prevent prefix queries from leaving positions $1$ through $n$.
- **Feasibility guarantee:** `maxChanges + sum(nums) >= k` ensures some legal plan exists, so the answer eventually becomes finite.
- **Shadowed built-ins:** The source assigns two-argument lambdas to the names `min` and `max`. Every later call supplies exactly two arguments, so this unusual style still behaves as intended.
- **Why changes precede distance-two originals:** Both cost two; selecting the change first preserves original ones without increasing the cost.
- **Why changes precede farther originals:** A manufactured pick costs two, whereas an original at distance three or more costs strictly more.
- **Large position sums:** Python avoids overflow; a fixed-width implementation should use a sufficiently wide integer type.
