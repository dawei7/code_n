## General

**Sort identical values into groups**

The challenge is not generating permutations alone; it is preventing different physical copies of the same value from producing duplicate visible sequences. Sorting `nums` places equal values next to one another, allowing a local condition to impose a canonical usage order inside each equal-value group.

The method uses `used[i]` to track whether sorted input position `i` is already in `cur`. An input occurrence can be selected once per root-to-leaf path. However, occurrence tracking by itself would treat equal copies as distinct and would over-generate, so the loop has a second skip condition.

**Interpret the skip rule exactly**

The condition

`i > 0 and nums[i-1] == nums[i] and not used[i-1]`

means: the current value equals its immediately preceding sorted copy, and that earlier copy is still unused on this path. In that situation, the current copy is skipped. The earlier unused occurrence is the canonical representative that must be chosen first.

If the earlier occurrence *is* already used, the current copy is permitted. That distinction allows repeated values to occupy several permutation positions. For sorted `[1a, 1b, 2]`, the root explores the branch beginning with `1a` and skips `1b` as a duplicate root sibling. Inside the `1a` branch, `used[0]` is true, so `1b` may be selected and `[1, 1, 2]` can be formed.

After the root branch using `1a` returns, its flag is cleared. Now selecting `1b` first would generate the same visible results as selecting `1a`, so the rule skips it. Equal copies are ordered by index solely to choose one representation for each value sequence.

**Shared backtracking state**

At helper entry, `cur` contains the selected prefix, and a flag is true exactly for each occurrence present in that prefix. The number of true flags equals `len(cur)`. The prefix also respects the rule that copies from each equal group are selected from left to right.

For an allowed index, the source marks it used and appends its value. Recursion then fills the next output position. On return, `cur.pop()` removes the most recent value and `used[i] = False` releases the occurrence. These operations must be paired so every sibling starts from the same parent prefix and availability state.

**Why a result is copied**

When `len(cur) == len(nums)`, the path uses all input occurrences exactly once and is a complete permutation. `cur + []` creates a shallow copy equivalent to `cur[:]`. A copy is required because `cur` is immediately popped during backtracking and reused for every later result.

The values are integers, so a shallow copy is fully sufficient. There are no nested mutable elements whose contents need duplication.

**Correctness and uniqueness**

Every recorded path is valid because usage flags prohibit index reuse, and reaching length $n$ means every physical occurrence has been selected. Repeated values appear no more times than their input multiplicity.

For completeness, consider a desired unique value ordering. Label each repeated value's appearances in that ordering with its sorted occurrences from left to right. At every selection of a later occurrence, all earlier labeled copies of that value have already appeared in the prefix and are marked used. The skip rule therefore permits the canonical labeled path, and recursion eventually records the desired ordering.

For uniqueness, assume two paths generate the same value sequence and find their first differing physical choice. They choose equal values from different indices. The path choosing the later occurrence while the earlier interchangeable occurrence is not part of its identical prefix violates the skip rule. Such two paths cannot both exist, so each visible permutation appears once.

**Why adjacency is enough**

Sorting makes a value's occurrences one contiguous block. If the immediately previous equal copy is unused, choosing a still later one would also be noncanonical. If the immediately previous copy is used, the left-to-right rule implies the necessary earlier copies are already used as well. A comparison with only `i - 1` therefore enforces ordering across the entire duplicate group.

**Selected class and input mutation**

The canonical class is `Solution`, which sorts in place and uses visited flags. `Solution2` in the same file incrementally inserts values and rejects duplicate candidate lists with linear membership checks; it is an unused alternative and has different performance characteristics.

Because the selected method calls `nums.sort()`, the original list is rearranged. This is acceptable to the judge but observable to a caller that retains the list.

## Complexity detail

If repeated-value frequencies are $f_1, f_2, \ldots$, the number of unique outputs is $U = n! / \prod_k f_k!$. Copying $n$ values for every result costs $\Theta(nU)$. Candidate loops add internal search work. In the worst case, all values are distinct and $U=n!$, so the conventional upper bound is $O(n \cdot n!)$, matching the manifest. Sorting costs $O(n \log n)$ beforehand.

The `used` list, `cur`, and recursion stack are each linear in $n$, giving $O(n)$ auxiliary space. In-place sorting may also use $O(n)$ temporary memory in Python. The required result occupies $\Theta(nU)$ and is not counted as auxiliary storage.

## Alternatives and edge cases

- **Remaining-count map:** Choose a value with positive remaining frequency, decrement, recurse, and restore. This directly models a multiset and avoids sorting-based occurrence labels.
- **Per-depth seen set:** Skip a candidate value if that same value has already been used as a sibling choice at the current depth. It is flexible but introduces additional set state.
- **Insertion with membership checks:** Insert each new value into every position of existing permutations and reject duplicate lists. It is intuitive but repeated list construction and membership tests can be expensive.
- **Generate then deduplicate globally:** A set can remove repeated outputs but does not prevent factorial exploration of interchangeable copies.
- **All copies identical:** The predecessor condition permits exactly one index at each depth, so one unique permutation is returned.
- **Two equal copies in one answer:** The second is allowed once the first is marked used; the condition must test `not used[i-1]`, not simply equality.
- **Distinct input:** The duplicate clause never fires, reducing to ordinary visited-array permutation generation.
- **Single value:** One recursive choice reaches the leaf and returns one copied list.
- **Input order:** Sorting mutates `nums`; use a sorted copy if preserving the caller's list is a requirement.
- **Answer order:** Sorted depth-first traversal is deterministic, but the contract accepts any order.
