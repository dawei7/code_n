## General

Sort the available side lengths into non-decreasing order. When the current
length `side` is treated as the polygon's longest side, including every
preceding length is always best: all are positive, so they maximize both the
supporting sum and the resulting perimeter. Maintain their total as
`prefix_sum`.

**Test the complete prefix.** If `prefix_sum > side`, the sorted prefix ending
at `side` satisfies the polygon inequality and its perimeter is
`prefix_sum + side`. Record that total, then include `side` in the prefix sum
for later candidates.

If the inequality fails, removing any preceding side cannot help because it
only decreases the sum opposing the same longest side. The failed `side`
should nevertheless remain available when a later, longer candidate is
tested: it is then one of the smaller supporting sides and its positive length
can help that later prefix succeed.

**Why the last valid prefix is optimal.** Every valid subset has some longest
side. For that same longest side, replacing its chosen smaller sides by all
available preceding sides cannot invalidate the inequality and cannot reduce
the perimeter. Therefore an optimum is one of the valid sorted prefixes the
scan tests. Prefix sums strictly increase, so the latest valid prefix has the
largest perimeter among them.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. Sorting costs $O(N\log N)$ time and the
subsequent scan costs $O(N)$ time. The sorted copy uses $O(N)$ auxiliary space.

## Alternatives and edge cases

- **Repeatedly discard the largest side:** Sorting once, tracking the total sum, and removing an invalid maximum from right to left is also $O(N\log N)$ and reaches the same prefixes.
- **Enumerate subsets:** Testing every selection is exponential and unnecessary because all positive smaller sides can safely accompany a fixed longest side.
- **Selection sort:** It preserves the greedy reasoning but raises the sorting cost to $O(N^2)$.
- **Equality:** A longest side equal to the sum of the others is degenerate and does not form a polygon; the comparison must be strict.
- **Large totals:** A perimeter may exceed 32-bit signed range because both $N$ and each side length are large.
- **No valid prefix:** Return `-1`, including when every potential longest side is at least the sum of all smaller sides.
