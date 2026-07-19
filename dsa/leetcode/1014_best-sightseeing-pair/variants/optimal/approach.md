## General
**Separate the two index contributions:** Rewrite the score as `(values[i] + i) + (values[j] - j)`. For a fixed right index `j`, the second term is known, so only the largest `values[i] + i` among earlier indices is needed.

**Carry the best left spot forward:** Initialize `best_left = values[0]`. For each `j` from `1` onward, combine `best_left` with `values[j] - j` to update the answer. Only after scoring pairs ending at `j`, update `best_left` with `values[j] + j`; this ordering preserves the strict requirement `i < j`.

**Why one stored value is sufficient:** Any earlier spot with a smaller `values[i] + i` can never outperform the stored spot for the current or any future right endpoint, because every candidate receives the same `values[j] - j` term. Discarding it therefore loses no optimal pair.

Every possible right endpoint is processed, and `best_left` represents the best legal left endpoint at that moment. The maximum recorded score is consequently the maximum over all valid pairs.

## Complexity detail
The scan processes each of the $N$ sightseeing values once, giving $O(N)$ time. The best left contribution and answer use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Enumerate every pair:** Directly evaluating all `i < j` choices is correct but takes $O(N^2)$ time.
- **Prefix maximum array:** Precomputing the best left contribution for every position gives $O(N)$ time but unnecessarily uses $O(N)$ space.
- **Two spots:** The single available pair is the answer.
- **Equal values:** Distance favors the closest pair, so adjacent equal maximum values are optimal among those values.
- **Large late value:** It may serve as the right endpoint now and become the best left contribution for later endpoints.
