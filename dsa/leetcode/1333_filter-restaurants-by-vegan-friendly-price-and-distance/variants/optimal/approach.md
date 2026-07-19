## General
**Filter before ordering**

Scan each record once. Reject it when its price exceeds `max_price`, its distance exceeds `max_distance`, or the caller requires vegan-friendly choices and the record's flag is 0. Store only the pair `(rating, id)` for every remaining record.

Sort these pairs in reverse lexicographic order. Python compares the rating first and the ID second, so reversing the pair order implements both required descending keys without a custom comparator. Project the sorted pairs to their IDs for the result.

Every returned ID passed all three filters because pairs are appended only after the checks. Conversely, every qualifying record is appended. The pair ordering then places a higher rating first and uses the higher ID exactly when ratings tie, so the output satisfies the complete ordering contract.

## Complexity detail
Let $k$ be the number of qualifying restaurants. Filtering costs $O(n)$ time and sorting costs $O(k\log k)$, bounded by $O(n\log n)$. The filtered pairs and returned IDs require $O(k)$ space, bounded by $O(n)$.

## Alternatives and edge cases
- **Sort every record first:** Sorting all $n$ records and filtering afterward is correct but may perform unnecessary comparisons when few records qualify.
- **Selection sort:** Repeatedly choosing the best remaining qualifying record avoids relying on a library sort but takes $O(k^2)$ time.
- **No qualifying restaurant:** Return an empty array.
- **Inclusive limits:** A restaurant whose price or distance equals its corresponding maximum remains eligible.
- **Vegan flag disabled:** A value of 0 does not require non-vegan restaurants; it permits both flag values.
- **Equal ratings:** Compare IDs descending rather than preserving input order.
