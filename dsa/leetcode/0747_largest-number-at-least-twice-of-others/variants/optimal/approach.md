## General
**Reduce every comparison to the runner-up**

Let `largest` be the unique maximum and `second_largest` the greatest remaining value. If `largest >= 2 * second_largest`, then the inequality also holds for every smaller number. If it fails for `second_largest`, the required condition is already false. Only these two values and the maximum's index matter.

**Maintain the two greatest values in one pass**

For each number, compare it with the current `largest`. A new maximum moves the old maximum into `second_largest` and records the new index. Otherwise, update `second_largest` when the number exceeds it. After the scan, test the single inequality against the runner-up.

The update rules keep `largest` and `second_largest` equal to the two greatest values in the processed prefix: a new greatest value shifts the previous leader down, while any other value can affect only the runner-up. Thus the final dominance check is equivalent to checking the maximum against every other array element.

## Complexity detail
The array is scanned once, so the running time is $O(n)$. A fixed number of values and one index are stored, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Sort values with their indices:** The two greatest values become adjacent after sorting, but sorting costs $O(n \log n)$ time and $O(n)$ space for decorated entries.
- **Compare every candidate with every other value:** This directly mirrors the definition but can take $O(n^2)$ time.
- **Exactly two values:** The larger value needs to be at least twice the smaller one; the same runner-up test applies.
- **Zero runner-up:** Any non-negative unique maximum is at least twice zero.
- **Equality at twice the runner-up:** The condition is inclusive, so exact equality succeeds.
- **Original index:** Track the maximum's position during the scan; do not return its rank after sorting.
