## General

The greatest possible distance is obtained by pushing a valid pair toward the array boundaries. Compare every word with the first word and with the last word. When `words[index]` differs from the first entry, the pair `(0, index)` is valid and has distance `index + 1`. When it differs from the last entry, `(index, n - 1)` is valid and has distance `n - index`.

**Why an endpoint pair is sufficient.** If the first and last words differ, their pair already has distance $n$, the largest possible value. Otherwise both endpoints contain some word $x$. Any valid unequal pair must include at least one position $k$ whose word is not $x$. Pairing $k$ with index `0` gives distance $k+1$, and pairing it with index `n - 1` gives distance $n-k$; both are valid. Whichever side of the original pair contains $k$, extending that side to the corresponding endpoint cannot shorten the distance. Thus a globally optimal pair is among the endpoint comparisons performed by the scan.

Track the largest valid endpoint distance. When every word is identical, neither comparison ever succeeds and the initial answer `0` is returned.

## Complexity detail

Let $n=\lvert\texttt{words}\rvert$. Each array position is compared with two endpoint words, giving $O(n)$ time under the source's fixed maximum word length of 10. The scan stores only the current index and answer, so it uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate every index pair:** Checking all $\binom{n}{2}$ pairs is straightforward but takes $O(n^2)$ time.
- **Record first and last occurrence of every word:** This can also find distant unequal values but needs additional maps and is unnecessary when the two array endpoints suffice.
- **All words equal:** No distinct-index pair satisfies the unequal-word condition, so the required result is `0` rather than a positive span.
- **One word:** There is no pair at all; the same zero initialization handles this minimum input.
- **Inclusive distance:** A pair at indices `0` and `1` has distance `2`, because the definition is $j-i+1$.
- **Repeated endpoint word:** Interior words equal to an endpoint do not form a valid pair with that endpoint and must be skipped.
