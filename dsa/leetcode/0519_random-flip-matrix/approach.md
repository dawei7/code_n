## General

Materializing an `m` by `n` matrix would be wasteful because each dimension may be as large as $10^4$, while at most 1000 operations are performed. The solution instead treats every cell as one number in a flattened range and stores only the positions whose virtual meaning has changed.

For a zero-based flattened index `idx`, the corresponding coordinates are:

- row `idx // n`;
- column `idx % n`.

This mapping is a bijection between integers from zero through `m * n - 1` and all matrix cells. Selecting a uniformly random available flat index is therefore equivalent to selecting a uniformly random available cell.

The design is a lazy version of the Fisher–Yates shuffle. Imagine an array initially containing:

`[0, 1, 2, ..., m * n - 1]`.

Only a prefix of this imaginary array represents cells still available for selection. `self.total` is the prefix length. Initially it is `m * n`, so every cell is available.

If the full array existed, one `flip` could choose a random slot in the available prefix, return the value stored there, move the value from the prefix's last slot into the chosen slot, and shorten the prefix by one. This is the same removal technique used by Fisher–Yates: the selected value leaves the active range, while every remaining value still occupies exactly one active position.

The dictionary `self.mp` makes those swaps sparse. A missing key `p` means the imaginary array still stores value `p` at position `p`. A present entry `mp[p]` records the value that a previous virtual swap moved into position `p`. The matrix itself and unchanged array positions never need to be stored.

**Choose one active position with one random call.** At the start of `flip` there is guaranteed to be at least one free cell. The code first decrements `self.total`. If there were `t` cells available, the new value is `t - 1`, which is both the final valid random index and the position of the active prefix's last element.

Then:

`x = random.randint(0, self.total)`

chooses each of the old `t` active positions with probability $1/t$. Python's `randint` includes both endpoints, so the interval contains exactly `t` positions. Only one built-in random call is needed.

**Resolve the value stored at the selected virtual position.** The expression `self.mp.get(x, x)` means “use the remapped value when one exists; otherwise this position still represents itself.” The result is stored in `idx`. That is the actual previously unflipped cell being selected.

The position and value must be distinguished. `x` is a slot in the shrinking virtual prefix. `idx` is the flattened matrix cell currently stored in that slot. After earlier removals, they need not be equal.

**Fill the hole from the active tail.** The selected position `x` must no longer represent `idx`. The code assigns:

`self.mp[x] = self.mp.get(self.total, self.total)`.

The right side resolves the value currently held at the last active position. Moving it to `x` preserves every unselected value in the shortened prefix. The tail position itself lies outside the active range after the decrement, so it does not need to be cleaned up.

This assignment is harmless when `x == self.total`. It writes the tail value back under the same position, but that position is now inactive and will not be sampled until a reset clears the dictionary.

**Why every free cell remains equally likely.** Before a flip, the active virtual positions contain every unflipped cell exactly once. This is true initially because position `p` represents cell `p`. A flip chooses an active position uniformly, so the unique cell stored there is uniform among all free cells. Replacing that position with the tail value and shrinking the range removes exactly the returned cell while retaining every other free cell once. The invariant and uniformity therefore continue by induction.

For a two-by-two matrix, the initial active values are conceptually `[0, 1, 2, 3]`. Suppose slot one is selected. Cell one is returned, value three is virtually moved into slot one, and the active prefix becomes conceptually `[0, 3, 2]`. A later choice of slot one returns cell three, not cell one; the dictionary lookup supplies that remapping and prevents duplicates.

Finally, `idx // self.n` and `idx % self.n` convert the selected flat cell back into the required coordinate pair.

**Reset without reconstructing a matrix.** `reset` restores `self.total` to `m * n` and clears all sparse remappings. With an empty dictionary, each virtual position again maps to itself, exactly recreating the initial conceptual array. Previously returned cells become eligible again.

## Complexity detail

Let $N = mn$ be the number of matrix cells and let $f$ be the number of flips since the most recent reset. Construction stores four scalar fields and an empty dictionary, so it takes $O(1)$ time and space beyond the object.

Each `flip` performs one random call, a constant number of arithmetic operations, and expected-$O(1)$ dictionary accesses. Its expected time is $O(1)$, and it adds at most one dictionary entry. Across $q$ flip calls, expected time is $O(q)$, matching the manifest. The sparse map occupies $O(f)$ entries instead of $O(N)$ cells.

`reset` restores a scalar and clears a dictionary containing $O(f)$ entries. Clearing is commonly described as $O(f)$ time because the stored entries must be released, after which retained logical space is $O(1)$. Hash-table operations have expected constant time; adversarial collision behavior is outside the usual Python dictionary model.

## Alternatives and edge cases

- **Materialized list plus Fisher–Yates:** Store all $N$ flattened indices and swap selected values with the tail. It gives the same uniform process but requires $O(N)$ initialization and memory.
- **Rejection sampling:** Randomly choose cells until an unflipped one appears. It is simple, but calls to randomness and running time grow badly when few cells remain.
- **Store a set of flipped cells:** This still needs rejection sampling unless an additional searchable structure is used, so it does not guarantee one random call per flip.
- **Sparse virtual swaps:** The implemented dictionary records only positions changed by removals, giving expected constant-time flips with memory proportional to performed flips.
- **Last free cell:** After decrement, `self.total` is zero and `randint(0, 0)` deterministically selects the sole active slot.
- **Selecting the tail slot:** The returned tail value is removed directly; the self-mapping written at an inactive key cannot be sampled.
- **One-row or one-column matrix:** Flat division and remainder still produce correct coordinates.
- **Repeated flips without reset:** The active-prefix invariant ensures a cell cannot be returned twice.
- **Flip after reset:** Clearing `mp` removes every stale virtual swap, so all $mn$ cells are equally eligible again.
- **Operation guarantee:** The source promises a free cell before every `flip`, so the code never calls `randint` with an invalid empty interval.
- **Large dimensions:** Only `m * n` and sparse mappings are stored; Python integers safely hold the product.
