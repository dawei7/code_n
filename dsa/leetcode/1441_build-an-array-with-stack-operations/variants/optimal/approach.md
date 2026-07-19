## General
**Follow the stream rather than searching for operations.** Iterate `current` from `1` upward and keep an index `target_index` for the next desired value. Every current value is read exactly once, so append `"Push"` unconditionally.

**Keep or discard the pushed value.** If `current == target[target_index]`, retain it on the stack and advance `target_index`. Otherwise, the strictly increasing target can never need that smaller skipped value later, so append `"Pop"` immediately.

**Stop at the final desired value.** Once `target_index == len(target)`, the stack already equals the complete target. Stop without reading any larger values, even when `n` is greater than the target's final entry.

**Why the emitted sequence is valid.** Before each stream read, the retained stack equals the processed prefix of `target`. A matching value extends that prefix by one. A nonmatching value is pushed as required and immediately removed, restoring the same prefix. This invariant continues until every target value is retained, at which point the stack is exactly `target` and the stopping rule is satisfied.

## Complexity detail
The algorithm reads exactly the values $1$ through $L$, performing constant work per value, for $O(L)$ time. It returns between $L$ and $2L-t$ operation strings, so the required output occupies $O(L)$ space; auxiliary state aside from the output is $O(1)$.

## Alternatives and edge cases
- **List membership for every stream value:** Testing `current in target` repeatedly can take $O(Lt)$ time with an array target.
- **Build a target set:** This also gives linear expected time but uses $O(t)$ extra space and does not directly track when construction is complete.
- **Consecutive target values:** Each is kept with one `"Push"` and no intervening `"Pop"`.
- **Skipped values:** Each requires the adjacent pair `"Push","Pop"`.
- **Target begins above one:** Every earlier stream value must be pushed and popped.
- **n exceeds the final target:** Do not read the unused suffix of the stream.
- **Single target value:** Process only through that value and stop.
