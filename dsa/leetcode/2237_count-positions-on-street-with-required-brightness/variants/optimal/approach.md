## General

**Replace every illuminated interval with two events**

Let $m$ be the number of lamps. Updating every position covered by every lamp
can repeat work for as many as $nm$ position-lamp pairs. Instead, maintain a
difference array. For a lamp whose clipped interval is `[left, right]`, add one
at `changes[left]` and subtract one at `changes[right + 1]`. These two events
say that one lamp begins contributing at `left` and stops contributing
immediately after `right`.

**Recover brightness with a prefix sum**

Scan positions from left to right while accumulating the difference events.
At position $i$, the running total equals the number of intervals that have
started but not yet ended, which is exactly the brightness at $i$. Count the
position when this total is at least `requirement[i]`.

Each lamp contributes one start and one end event. During the prefix scan, an
interval contributes to precisely the positions between those events,
including both clipped endpoints. Therefore the computed brightness and the
problem's inclusive coverage definition agree at every position, so the final
count includes exactly the positions meeting their requirements.

## Complexity detail

Let $n$ be the number of street positions and
$m=\lvert\texttt{lights}\rvert$. Creating two events per lamp costs $O(m)$
time, and the prefix scan costs $O(n)$ time. The total is $O(n+m)$ time and the
difference array uses $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Mark every covered position:** Directly incrementing each lamp's full interval is simple and correct, but its worst-case time is $O(nm)$ when many lamps cover the entire street.
- **Sorted sweep events:** A map of interval endpoints avoids allocating $n+1$ entries but adds sorting or ordered-map overhead even though all street positions must still be inspected.
- **Zero requirements:** A position requiring brightness zero always qualifies, even when no lamp covers it.
- **Zero range:** A lamp with range zero illuminates only its own position.
- **Clipped intervals:** Lamps near either boundary may extend conceptually beyond the street; both endpoints must be clipped before events are recorded.
- **Inclusive right endpoint:** The removal event belongs at `right + 1`, not at `right`.
- **Overlapping lamps:** Every active interval contributes separately, including lamps with identical positions and ranges.
