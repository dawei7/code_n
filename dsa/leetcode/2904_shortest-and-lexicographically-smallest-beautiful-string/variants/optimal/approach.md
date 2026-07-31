## General

Any shortest beautiful substring must begin and end with `"1"`. If it began or ended with `"0"`, removing that boundary character would preserve exactly `k` ones while making the substring shorter.

Scan `s` with a right pointer while maintaining a left pointer and the number of ones in the current window. When the count exceeds `k`, advance the left boundary until the count returns to `k`. When the count equals `k`, discard every leading zero from the window because those characters can never belong to a shortest answer.

The resulting window is the unique shortest beautiful substring ending at the current right boundary: moving its left endpoint farther would remove a required one, while moving it left would only add zeros or extra ones. Compare this candidate with the best one seen so far, ordering first by length and then by the string itself.

Every beautiful substring has some right endpoint. At that endpoint, the scan considers a candidate no longer than it, so the global minimum length cannot be missed. Comparing all candidates of that length also selects the required lexicographically smallest one. If the running count never reaches `k`, no candidate is produced and the empty string remains the answer.

## Complexity detail

Let $n=\lvert s\rvert$. Both pointers advance at most $n$ times, but Python substring creation and lexicographic comparison can each inspect $O(n)$ characters for up to $n$ candidates. The worst-case running time is therefore $O(n^2)$. The current candidate and retained answer can each contain $O(n)$ characters, giving $O(n)$ auxiliary space when returned strings are counted.

## Alternatives and edge cases

- **Enumerate every substring:** Counting ones in every possible slice is straightforward but can take $O(n^3)$ time when each slice is rescanned.
- **Prefix sums over all endpoint pairs:** Prefix counts reduce each ones-count query to $O(1)$, but still inspect $O(n^2)$ pairs and create qualifying slices.
- **Too few ones:** When the complete string contains fewer than `k` ones, the answer is `""`.
- **One required one:** A present `"1"` is itself the unique shortest possible shape, regardless of surrounding zeros.
- **Boundary zeros:** Leading and trailing zeros never belong to a shortest beautiful substring and must not influence tie-breaking.
- **Equal minimum lengths:** Length has priority; lexicographic order is consulted only after two candidates have the same length.

