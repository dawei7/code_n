## General
**Every source character needs one destination.** A global conversion cannot distinguish two occurrences of the same current character. Therefore, whenever `str1[i]` has appeared before, its aligned target `str2[i]` must equal the destination already assigned to that source character. A single left-to-right pass builds this mapping and rejects any contradiction. Different source characters may map to the same target character; merging them is allowed.

**A spare character breaks conversion cycles.** View each nontrivial mapping as a directed edge from a source letter to its target. Acyclic chains can be executed from their target end backward. A directed cycle, however, cannot be rotated directly: changing any cycle letter first would merge it with another letter whose occurrences still need a different final value. If at least one lowercase letter is absent from `str2`, that letter can temporarily hold one group of occurrences, opening every cycle so the remaining conversions can be ordered safely.

If `str1 == str2`, zero conversions already solve the problem, even when the target contains all 26 letters. Otherwise at least one nontrivial mapping exists. After mapping consistency has been established, using all 26 letters in `str2` means every letter is a required final label, leaving no temporary label and making any necessary permutation cycle impossible. Using fewer than 26 target letters supplies the required spare. Thus a consistent mapping succeeds exactly when the strings are already equal or `len(set(str2)) < 26`.

## Complexity detail
The aligned scan and target-character set each inspect $n$ positions, so the time cost is $O(n)$. The mapping and set contain at most the 26 lowercase English letters, which is constant auxiliary space, giving $O(1)$ space with respect to $n$.

## Alternatives and edge cases
- **Simulate conversion sequences:** Searching possible operation orders branches heavily and is unnecessary because mapping consistency and the existence of a spare letter completely characterize feasibility.
- **Check only the character mapping:** A consistent mapping is necessary but not sufficient when a nontrivial cycle occupies all 26 target letters.
- **Require a one-to-one mapping:** This is too strict; several source letters may safely merge into the same target letter.
- **Already equal strings:** Return `true` immediately, including when all 26 letters occur, because zero conversions are allowed.
- **Conflicting occurrences:** If one source letter aligns with two different target letters, no sequence of global conversions can separate its occurrences again.
- **Conversion order:** Chains and cycles may require conversions in a carefully chosen order; the test proves that such an order exists without constructing it.
