## General

Removing one group can make equal letters on its two sides become adjacent, creating a new removable group. The solution represents the already reduced prefix as a stack of runs `[character, count]`. Every stored count is between one and `k - 1`, and adjacent stack entries have different characters.

**Process one maximal original run at a time**

Pointers `i` and `j` find the maximal run beginning at `i`. When the inner loop ends, `cnt = j - i` is its length.

`cnt %= k` removes every complete group of `k` identical letters inside that run. Only the remainder can affect later characters. If the remainder is zero, that original run vanishes entirely.

**Merge with the reduced prefix**

If the stack is nonempty and its final character equals `s[i]`, all original material between that stored run and the current run has already vanished. They are now adjacent and must combine.

The code replaces the top count by `(old + cnt) % k`. Modulo removes any newly formed groups of `k`. If the new count is zero, it pops the run completely. That pop may expose an earlier character, which can merge with a future run processed later.

If the top character differs and `cnt` is nonzero, the current remainder becomes a new stack run. A zero remainder adds nothing.

For `"deeedbbcccbdaa"` with `k = 3`, the `eee` and `ccc` runs reduce to zero. Their disappearance lets surrounding runs eventually combine: the three `b` characters vanish, then separated `d` portions merge to three and vanish, leaving `aa`.

**Why one pass captures repeated removals**

After each original run is processed, the stack represents exactly the fully reduced form of the input prefix. It contains no count reaching `k` and no adjacent equal run entries.

For the next run, internal groups are removed by modulo. If its character differs from the stack top, appending preserves reduction. If it matches, combining is the only new interaction created at the boundary; modulo and a possible pop fully resolve it. This maintains the invariant by induction.

Because the final reduced string is unique, the stack’s deterministic left-to-right reductions produce the required result regardless of another possible removal order.

**Reconstruct the remaining characters**

The comprehension creates `c * v` for every stored run, repeating its character by its residual count. Joining those fragments produces the final bracket-free string. Every stored count is positive and below `k`, so no removable group remains.

**A smaller cascade example**

Take `s = "abbbaa"` and `k = 3`. The first `a` becomes stack run `[a, 1]`. The `bbb` run has remainder zero and disappears. The final `aa` run now sees `a` at the top, even though those letters were not adjacent in the original string. Their counts combine to three, reduce to zero, and pop. The final answer is empty.

This example shows why merely reducing each original maximal run and concatenating the remainders would be insufficient. Deletion changes adjacency. The stack is not just a compressed output buffer; its top is the boundary of the fully reduced prefix and is the only earlier run that a new suffix can interact with.

The stack also avoids storing a count of zero. A zero-count entry would not represent any actual character and could incorrectly block two equal runs on its sides from seeing each other. Popping immediately maintains the invariant that every stack entry corresponds to visible output.

## Complexity detail

Let $n$ be the length of `s`. The run pointers advance only forward, so all original characters are examined $O(n)$ times in total. Each run causes constant stack work, and every stack entry is pushed and popped at most once. Reconstruction writes exactly the output characters, at most $n$. Total time is $O(n)$.

The stack can contain $O(n)$ runs in an alternating string. The fragment list and returned string also use $O(n)$ space. Auxiliary-space complexity is $O(n)$, with $O(n)$ output space.

## Alternatives and edge cases

- **Character-by-character run stack:** Push or increment one character at a time and pop at count `k`. It has the same $O(n)$ bounds and may be simpler to recognize.
- **Repeated immutable-string deletion:** Rescanning and slicing after every removal can take quadratic time.
- **No removable group:** Every residual run remains and reconstruction returns the original string.
- **Whole run length is a multiple of `k`:** Its remainder is zero and it contributes nothing.
- **Run longer than `k`:** Modulo correctly removes several complete groups at once.
- **Cascade across deleted text:** Matching the current character against the stack top detects newly adjacent equal runs.
- **Combined count exactly `k`:** Modulo makes it zero and the stack entry is popped.
- **`k = 2`:** Counts are only one after reduction, and matching adjacent runs cancel in pairs.
- **Unique final answer:** The invariant computes the canonical reduced prefix, so no removal-order branching is needed.
- **Output may be empty:** An empty stack reconstructs to `""` through `join`.
