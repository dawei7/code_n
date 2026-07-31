## General

For one fixed substring, the trade has the same run interpretation as the single-query version. If a one run of length $A$ lies between zero runs contributing $L$ and $R$ characters inside the query, the first conversion merges all three runs into zeros and the second restores the $A$ active characters while activating those $L+R$ zeros. Its net gain is therefore $L+R$.

Run-length encode the entire string and record the run containing every character position. For each internal one run, store its full gain—the complete lengths of its neighboring zero runs. A segment tree over run IDs supports the maximum full gain across any interval of runs. Zero runs and non-eligible runs store zero.

For a query `[l, r]`, the first eligible one run depends only on the run containing `l`: if that boundary run is zero, the next run is the first candidate; if it is one, that run cannot be surrounded within the query, so skip its following zero run and use the next one run. The last candidate follows the symmetric rule at `r`. If the first candidate lies after the last, the query contains no valid trade.

Only the first candidate can have its left zero run truncated by `l`, and only the last candidate can have its right zero run truncated by `r`. Compute both gains directly by intersecting their neighboring zero runs with the query. Every candidate strictly between them has both zero neighbors fully covered, so one segment-tree query returns the best interior gain. Add the maximum of these three possibilities to the original number of ones in the whole string.

Every valid trade selects a fully included one run and some positive portion of each adjacent zero run. That run is either the first query candidate, the last, or strictly interior, so the algorithm evaluates its exact gain in one of the three categories. Conversely, each evaluated candidate has a one run and at least one neighboring zero on both sides within the augmented query, making the constructed trade valid. The reported maximum is therefore exact.

## Complexity detail

Let $n=\lvert\texttt{s}\rvert$ and let $q$ be the number of queries. Building the runs, position-to-run map, and segment tree takes $O(n)$ time. Each query performs constant boundary work and one $O(\log n)$ range-maximum query, so total time is $O(n+q\log n)$. The run arrays, position map, tree, and returned answers use $O(n+q)$ total storage, of which $O(n)$ is auxiliary space beyond the required output.

At least $\Omega(n+q)$ work is necessary to read the string and queries and produce all answers. The logarithmic query factor is the segment-tree range-maximum cost. The benchmark scales $n$ and $q$ together and contrasts this structure with a correct implementation that examines every eligible run for every query, requiring $\Theta(nq)$ time.

## Alternatives and edge cases

- **Scan each query substring:** Reusing the single-query run scan is correct but can inspect $\Theta(n)$ characters for each of $q$ ranges, reaching $O(nq)$ time.
- **Scan every candidate run per query:** Preprocessing run triples alone does not solve the range maximum; checking all triples for every query remains $O(nq)$ in an alternating string.
- **Sparse table:** Static range maxima can answer interior queries in $O(1)$ after $O(n\log n)$ preprocessing, trading more memory and build time for faster queries.
- **Candidate binary searches:** Storing only eligible one runs and locating boundaries with binary search is another $O((n+q)\log n)$ organization, but a position-to-run map makes endpoint classification direct.
- **Boundary zero run:** The artificial query-boundary one allows a partially covered endpoint zero run to contribute to the gain.
- **Boundary one run:** A one run touching `l` or `r` is not surrounded by zeros inside the query and cannot be converted first.
- **Whole-string count:** Positions outside `[l, r]` never change but their existing ones remain included in every answer.
- **Single-character query:** It cannot contain a one run plus zero characters on both sides, so the answer is the original total number of ones.
- **All zeros or all ones:** No valid first conversion exists; each query returns the unchanged total.
- **Independent queries:** A trade for one query never mutates `s` or affects any later query.
