## General

**Start from closing before every hour**

If the shop closes at hour 0, it is closed for the entire log. Every `'Y'` customer hour is missed and contributes one penalty; `'N'` hours contribute nothing.

Therefore `customers.count("Y")` is the exact penalty for closing at zero. The source stores it as both current `cost` and minimum `mn`, with earliest best answer `ans=0`.

**Move the closing boundary one hour at a time**

Changing closing time from `j-1` to `j` moves hour `j-1` from the closed interval into the open interval.

If that character is `'N'`:

- It previously caused no penalty while closed.
- It now causes one penalty because the shop was unnecessarily open.
- Current cost increases by one.

If it is `'Y'`:

- It previously caused one missed-customer penalty while closed.
- It now causes none because the shop is open.
- Current cost decreases by one.

This is the update

`cost += 1 if c=="N" else -1`.

`enumerate(customers,1)` labels the new boundary `j` after moving each character into the open side.

**Retain the earliest minimum**

After updating cost for closing at `j`, the method replaces `ans` only when `cost<mn`. It does not replace on equality.

Because boundaries are visited from 0 through `n` in increasing order, the first time a minimum penalty occurs is the earliest closing hour. Strict improvement preserves that earliest time across later ties.

For `"YYNY"`, initial cost is three. Moving past the first two Y hours reduces it to one at closing time 2. Later closing time 4 also has penalty one, but equality does not replace answer 2.

**Penalty invariant**

Before each comparison, `cost` equals:

- the number of `'N'` characters before boundary `j`, when the shop is open; plus
- the number of `'Y'` characters from `j` onward, when the shop is closed.

Initialization establishes this at zero. Crossing one character changes exactly its contribution according to the two cases above, preserving the invariant.

Thus every possible closing time's exact penalty is evaluated once. Tracking the smallest value and earliest position returns the required answer.

**Boundary meanings**

Closing at hour `j` means hours 0 through `j-1` are open and hour `j` is already closed. The one-based enumerate boundary matches that convention.

Closing at `n` leaves every logged hour open. After all characters are processed, cost equals the number of N hours, exactly its penalty.

**Extreme logs**

For all N characters, initial penalty is zero and every later boundary increases cost, so answer stays zero.

For all Y characters, cost decreases at every step, so each boundary is a strict improvement and the final answer becomes `n`.

**A complete boundary trace**

Consider `customers="YNY"`. Closing at zero misses two customers, so the initial cost is two and the current answer is zero. Moving the boundary past the first `Y` serves that customer, reducing cost to one; hour one becomes the new best answer. Moving past `N` keeps the shop open during an empty hour, increasing cost to two. Moving past the final `Y` removes another missed-customer penalty, returning cost to one.

Closing at hours one and three therefore ties with penalty one. Because hour one was encountered first and the update accepts only a strictly smaller penalty, the algorithm correctly returns one. This trace illustrates all important mechanics: initialization evaluates boundary zero, every character changes sides exactly once, and equality must not replace an earlier answer.

**Why no penalty term is forgotten**

For any fixed boundary, each character is in exactly one of two regions. A character before the boundary is an open hour and contributes precisely when it is `N`. A character at or after the boundary is a closed hour and contributes precisely when it is `Y`. There are no other penalty rules. The maintained cost partitions all characters into those two disjoint groups, so its value is neither an approximation nor a score that merely preserves ordering; it is the literal penalty.

The loop reaches $n+1$ boundaries even though the string has only $n$ characters. Boundary zero is handled before the loop, and each iteration handles the boundary immediately after one more character. Consequently neither endpoint is skipped.

## Complexity detail

`count("Y")` scans the length-$n$ string once. The boundary loop scans it once more, doing constant work per character. Total time is $O(n)$.

Only `ans`, `mn`, `cost`, and loop scalars are stored. Auxiliary space is $O(1)$.

The maximum penalty is $n\le10^5$, easily fitting ordinary integers.

## Alternatives and edge cases

- **Prefix and suffix arrays:** Precompute open-N penalties and closed-Y penalties for every boundary. This gives $O(n)$ time but uses $O(n)$ space.
- **Evaluate every boundary from scratch:** Counting both sides separately for all $n+1$ times costs $O(n^2)$.
- **Score transformation:** Maximize served Y minus open N; it is algebraically equivalent but less directly tied to penalty.
- **Tie between closing times:** Strict comparison retains the earliest boundary.
- **Close at zero:** All Y hours are penalized and no N hours are.
- **Close at `n`:** All N hours are penalized and no Y hours are missed.
- **All N:** Earliest optimum is zero.
- **All Y:** Optimum is after the final hour.
- **Single character:** Both possible boundaries are evaluated through initialization and one update.
- **Hour indexing:** The loop's displayed `j` is the boundary after processing character index `j-1`.
