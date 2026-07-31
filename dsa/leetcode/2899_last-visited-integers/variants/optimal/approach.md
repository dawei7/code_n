## General

The positive integers form a history in encounter order. Appending each new positive value to the end of a list keeps the most recent value at position `-1`, the second most recent at position `-2`, and so on. This avoids the linear cost that physically prepending each value would incur.

Maintain `consecutive_queries`, the number of adjacent `-1` markers ending at the current position. A positive value is appended to history and resets this counter to zero. For `-1`, increment the counter to obtain $k$. If $k$ does not exceed the history length, `history[-k]` is exactly the requested $k$-th most recently visited integer; otherwise no such integer has been seen, so append `-1`.

The history list contains every positive value processed so far in chronological order, and the counter equals the length of the current query run. Those two facts hold initially and are preserved by both input cases. Therefore every emitted answer follows the operation prescribed for that `-1`.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Each element causes one constant-time list append or indexed lookup, so the total time is $O(n)$. The history and returned answer can each contain $O(n)$ values, giving $O(n)$ space.

## Alternatives and edge cases

- **Prepend every positive value:** Keeping the newest item at index zero makes queries direct, but shifting the list on every insertion can take $O(n^2)$ total time.
- **Search backward for every query:** Repeatedly rescanning the processed prefix is unnecessary and can also become quadratic.
- **Query before any positive value:** The history is empty, so the result is `-1`.
- **Query run longer than history:** Every request beyond the number of seen positives yields `-1` without changing the history.
- **Positive value after queries:** It resets the consecutive-query count; the next `-1` asks for the newest value again.
- **Repeated positive values:** Each occurrence is a separate history entry and must remain available at its own recency position.
