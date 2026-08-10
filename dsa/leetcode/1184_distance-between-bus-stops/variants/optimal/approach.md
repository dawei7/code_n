## General

The stops and road segments form one cycle. Between any two stops, there are exactly two directions around that cycle: follow increasing stop numbers with wraparound, or travel along all remaining segments in the opposite direction. The shortest distance is therefore the smaller of one route’s length and the complementary route’s length.

The array entry `distance[i]` describes the segment from stop `i` to stop `(i + 1) % n`. In particular, `distance[n - 1]` connects the final numbered stop back to stop zero. The modulo operation is what turns the ordinary array order into a circle.

**Measure the whole circumference first**

The solution computes `s = sum(distance)`. This is the total length of every segment in the circle, or the circle’s circumference. Once one directional route has length `t`, the other route must contain exactly the segments not used by the first route, so its length is `s - t`.

This complementary-sum idea avoids running a second traversal in the opposite direction. It is valid even when some segments have length zero because the two routes still partition the segment positions, and subtraction still gives the other total.

**Walk one direction from start to destination**

The variable `t` begins at zero. While `start != destination`, the current `start` identifies the next clockwise segment to cross. The code adds `distance[start]` and advances the stop with

`start = (start + 1) % n`.

If `start` is not the final stop, this simply moves to the next number. If it is `n - 1`, adding one gives `n` and taking modulo `n` wraps the value to zero. The loop ends immediately upon arriving at `destination`, so the segment leaving the destination is not included.

Although the function parameter named `start` is updated, the original value is no longer needed after traversal begins. The mutation changes only the local parameter binding; it does not alter the caller’s integer.

Because the stops form a cycle and the destination is a valid stop, repeatedly moving forward must reach it. If the stops differ, this takes between one and `n - 1` segment crossings. If they are equal, the loop performs no work and `t` remains zero.

**How the two routes partition the circle**

The walked route begins at the original start, follows consecutive forward segments, and ends at the destination. The reverse-direction route from the same start to the same destination uses every other segment. No segment belongs to both route interiors, and together the routes cover the full cycle once. Their lengths add to `s`, so the unwalked route has length `s - t`.

The return expression `min(t, s - t)` selects the shorter direction. If both routes have equal length, either one is shortest and their common value is returned.

For `distance = [1, 2, 3, 4]`, start zero, and destination two, the forward traversal adds the segment from zero to one and then the segment from one to two. Thus `t = 1 + 2 = 3`. The circumference is ten, so the other direction has length seven. The answer is three.

For the same array with destination three, the forward route adds `1 + 2 + 3 = 6`. The complement is `10 - 6 = 4`, corresponding to traveling from zero backward across the segment that connects stop three to stop zero. Taking the minimum correctly returns four even though the explicitly traversed direction was longer.

**Why the returned value is necessarily optimal**

On a simple cycle, any route from the start to the destination that does not repeat unnecessary segments must choose one of the two arcs separated by those endpoints. Repeating a segment cannot produce a shorter distance because every segment length is nonnegative. The loop measures one arc exactly, while subtracting from the circumference measures the other exactly. The smaller of the only two relevant arc lengths is therefore the global shortest distance.

This reasoning also explains why there is no need for a graph algorithm such as Dijkstra’s algorithm. The topology is already known to be one cycle, and the two candidate paths can be described directly.

## Complexity detail

Let $n$ be the number of stops, which is also the length of `distance`.

Computing `sum(distance)` visits all $n$ segment lengths and takes $O(n)$ time. The while loop crosses at most $n-1$ segments before reaching the destination, so it also takes $O(n)$ time in the worst case. The final subtraction and minimum are constant-time operations. Overall time complexity is $O(n)$.

The solution uses only the total `s`, route total `t`, `n`, and the locally advancing stop index. It allocates no array proportional to the input size. Its auxiliary-space complexity is $O(1)$.

The circumference can reach $10^8$ under the given bounds, which fits ordinary 32-bit signed arithmetic. Python integers handle it without any special consideration.

## Alternatives and edge cases

- **Sum a normalized index interval:** Swap `start` and `destination` so the first is smaller, sum the direct array slice between them, and compare it with the circumference complement. This avoids modulo traversal but may allocate a temporary slice in Python if written carelessly.
- **Traverse both directions separately:** Walking clockwise and counterclockwise gives the same two totals, but the second walk is unnecessary after the circumference is known.
- **General shortest-path algorithm:** Modeling stops as a weighted graph and running Dijkstra’s algorithm would work for nonnegative edges, but it ignores the special cycle structure and adds needless complexity.
- **Start equals destination:** The empty route has distance zero. The loop does not execute, and `min(0, s)` returns zero.
- **One-stop circle:** Both valid indices are zero, so this reduces to the equal-endpoint case and returns zero.
- **Wraparound route is shorter:** The explicit traversal may take the long arc. The complementary value `s - t` still captures the shorter wraparound direction.
- **Zero-length segments:** They are valid and do not disrupt the partition argument. Multiple stops can be separated by total distance zero.
- **Equal route lengths:** `min` returns their shared length, and no tie-breaking direction is required.
- **Final segment indexing:** `distance[n - 1]` connects stop `n - 1` back to zero. The modulo update is necessary to cross that boundary correctly.
- **Nonnegative-distance guarantee:** The claim that repeated travel cannot improve a route relies on segment lengths being nonnegative, which the constraints guarantee.
