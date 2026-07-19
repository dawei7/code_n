## General
Let $j$ be the number of jumbo burgers and $s$ the number of small burgers. Cheese gives $j+s=\texttt{cheese_slices}$. If every cheese slice were initially assigned to a small burger, that would consume twice as many tomato slices as cheese slices. Changing one of those burgers from small to jumbo consumes two additional tomato slices, so

$$
j = \frac{\texttt{tomato_slices}-2\,\texttt{cheese_slices}}{2},
\qquad
s = \texttt{cheese_slices}-j.
$$

These equations determine at most one answer. It is valid only when the numerator for $j$ is even and both computed counts are nonnegative. Those checks also cover having too few tomatoes to make every burger small or too many tomatoes even if every burger is jumbo. When all conditions hold, substituting the two values back into the equations accounts for every tomato and cheese slice exactly.

## Complexity detail
The method performs a fixed number of integer arithmetic operations and comparisons, independent of the ingredient counts, for $O(1)$ time and $O(1)$ auxiliary space. The benchmark uses the total burger count as its scaling size and contrasts this direct calculation with enumerating possible jumbo counts.

## Alternatives and edge cases
- **Enumerate jumbo counts:** Trying every value from zero through `cheese_slices` finds the same unique answer but requires $O(\texttt{cheese_slices})$ time.
- **Solve with floating-point arithmetic:** It risks unnecessary representation and equality problems; the equations and divisibility conditions are entirely integral.
- **Odd tomato count:** Every burger consumes an even number of tomato slices, so no solution exists.
- **No ingredients:** `[0,0]` is valid because it uses both zero totals without waste.
- **All one size:** Either computed count may be zero and remains a valid answer.
- **Insufficient or excess tomatoes:** Counts outside the range from twice to four times the cheese count make one computed burger count negative.
