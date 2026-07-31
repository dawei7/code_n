## General

The value required for a missing timestamp points forward to the next entry in the same series. Processing timestamps from largest to smallest turns that forward dependency into maintained state: after all larger timestamps have been processed, `next_value1` and `next_value2` hold the first available values to the right in their respective series.

Start both indices at the ends of the sorted arrays. The larger current timestamp is the next timestamp in the descending union; if the timestamps are equal, consume both entries together. Whenever the chosen timestamp belongs to a series, replace that series' maintained value with the entry's exact value and move its index left. The sum of the two maintained values is then precisely the aggregate at that timestamp. If one series has no entry at or after the timestamp, its maintained value is still the initial zero.

Append these pairs while scanning downward, then reverse the completed list. Each distinct input timestamp is emitted once. The maintained-state definition proves every emitted sum: a value updated at timestamp $t$ remains active for every smaller union timestamp until the next smaller explicit entry in that series replaces it, exactly matching the source's next-available rule.

## Complexity detail

Let $n=\lvert\texttt{series1}\rvert$ and $m=\lvert\texttt{series2}\rvert$. Every loop iteration consumes at least one input entry, so the merge takes $O(n+m)$ time. Reversing at most $n+m$ output pairs has the same bound.

Apart from the required output array, the algorithm stores two indices, two maintained values, and one timestamp, using $O(1)$ auxiliary space. The returned array itself uses $O(n+m)$ space.

## Alternatives and edge cases

- **Forward search for every timestamp:** Scanning each series from its beginning for every union timestamp is correct but can take $O((n+m)^2)$ time.
- **Binary search per timestamp:** Finding the next entry independently with lower-bound searches takes $O((n+m)\log(n+m))$ time and repeats information that the reverse scan maintains directly.
- **Shared timestamp:** Update both maintained values before summing and emit only one row.
- **Timestamp beyond one series' end:** That series contributes zero until its largest explicit timestamp is reached while moving left.
- **Large timestamp gaps:** Gaps do not create output rows; only timestamps explicitly present in at least one input matter.
- **Values may decrease:** The maintained state follows timestamps, not numerical monotonicity of values, so rises and drops require no special handling.
- **Maximum values:** A sum may reach $2\cdot10^9$ and must be stored without truncating either input value.
