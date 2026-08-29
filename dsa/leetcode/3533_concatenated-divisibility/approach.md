## General

**Track only the remainder of the growing decimal concatenation**

If a current concatenated number is `A` and the next array value is `v` with `d` decimal digits, appending `v` produces:

`A * 10^d + v`.

Modulo `k`, only `A mod k` is needed:

`new_remainder = (old_remainder * (10^d mod k) + v) mod k`.

The source precomputes:

`shifts[i] = pow(10, len(str(nums[i])), k)`.

Python's three-argument `pow` obtains `10^d mod k` without constructing an unnecessarily large power. This formula preserves decimal leading structure correctly: appending `12` shifts the earlier digits by two positions, while appending `3` shifts them by one.

**Use a bitmask to identify which occurrences are already used**

`nums` may contain equal values, but its array positions are distinct permutation occurrences. Bit `i` in `mask` records whether occurrence `nums[i]` has been placed.

The full mask:

`(1 << length) - 1`

has every occurrence selected. A state needs both `mask` and the current remainder. The same set of used values can lead to different remainders, and those remainders can have different completion possibilities.

**Define the feasibility question**

`can_finish(mask, remainder)` means:

starting from the prefix represented by this state, can the unused occurrences be appended in some order so that the final concatenation has remainder zero modulo `k`?

At `mask == full_mask`, nothing remains. The state succeeds exactly when `remainder == 0`.

Otherwise, the function tries each unused occurrence, computes the next remainder with the concatenation formula, and recursively asks whether that choice can finish. If any choice succeeds, the state is feasible.

This is a decision DP rather than a maximum/minimum-value DP. It provides precisely the oracle needed later to construct the smallest feasible permutation greedily.

**Memoize every subset-remainder state compactly**

There are at most `2^n * k` states. The source flattens `(mask,remainder)` to:

`state = mask * k + remainder`.

A `bytearray` stores one byte per state:

- zero means not computed;
- one means computed and impossible;
- two means computed and possible.

When recursion revisits a state, it returns the stored boolean result immediately. Different prefix orders that lead to the same used subset and remainder have identical unused occurrences and identical future behavior, so merging them is safe.

The completed full-mask states are cheap base cases and are not explicitly stored, which does not affect correctness.

**Why the feasibility recurrence is complete**

Any completion must choose one unused occurrence next. The loop tries every such index, so the first step of every possible completion is represented. Removing that first choice leaves exactly the recursive subproblem with the updated mask and remainder.

Conversely, every recursive success corresponds to appending real unused occurrences exactly once and ending with remainder zero. Thus `can_finish` returns true if and only if at least one valid completion exists.

**Sort candidate occurrences by numeric value**

Lexicographic comparison treats each permutation as a list of integers, not as one concatenated string. Therefore, at the first differing list position, the permutation with the smaller integer is lexicographically smaller.

The source builds:

`order = sorted(range(length), key=lambda index: nums[index])`.

This lists occurrence indices in non-decreasing numeric value order. Equal values may appear in either stable index order, but choosing one equal occurrence rather than another does not change the output list at that position.

**First test whether any solution exists**

Before reconstruction, the source calls:

`can_finish(0, 0)`.

The empty concatenation has remainder zero before any digits are appended. If this initial state is impossible, no permutation produces a divisible concatenation, so returning `[]` is correct.

This also prevents the reconstruction loop from reaching a state where no candidate can be chosen.

**Greedily reconstruct the lexicographically smallest valid list**

At the current prefix, the source tries unused occurrences in `order`. For candidate `i`, it computes the next state and asks whether `can_finish` is true.

The first candidate that preserves feasibility is appended. All smaller candidate values were tested and found unable to lead to any complete valid permutation. Therefore, no valid answer can have a smaller next integer after the already-fixed prefix.

This argument repeats at every position. Once a candidate is chosen, the prefix remains extendable by the feasibility oracle. Inductively, the completed list is valid and is lexicographically no larger than any other valid list.

This is a standard “greedy with exact feasibility oracle” pattern: feasibility prevents the locally smallest choice from leading into a dead end.

**Handle duplicate values correctly**

If two unused indices contain the same number, the DP treats them as distinct bits. This may explore symmetric states, increasing constant work, but it does not change the returned lexicographic list.

During reconstruction, selecting either equal occurrence produces the same next output integer. If one occurrence has a feasible completion and the other does not because of index identity, their values are still identical and the first feasible one gives the same visible prefix. Since all future occurrences include the remaining equal copy, correctness is preserved.

**A divisibility trace**

For prefix remainder `r` and next value `45`, which has two digits, the source uses:

`(r * (100 mod k) + 45) mod k`.

It never constructs the full concatenated integer. For `nums = [3,12,45]` and `k = 5`, reconstruction first tests value three. The oracle confirms some completion exists, so three is fixed. It next tests twelve before forty-five; that branch can finish with remainder zero, producing the lexicographically smallest valid list `[3,12,45]`.

## Complexity detail

Let `n = len(nums)`. There are `2^n * k` possible memoized states. Each previously unseen nonterminal state may try up to `n` indices, performing constant-time bit and modular arithmetic per transition. Worst-case time is `O(n * k * 2^n)`.

Sorting the `n` indices costs `O(n log n)` and precomputing shifts costs `O(n log d)` at most for tiny decimal lengths; both are dominated by the subset DP.

The memo bytearray uses exactly `O(k * 2^n)` bytes. Recursion depth is at most `n <= 13`, and reconstruction stores `O(n)` output/state. Total auxiliary space is `O(k * 2^n)`.

The source's byte encoding is substantially more compact than a Python dictionary keyed by tuples, which matters at the upper state count.

## Alternatives and edge cases

- **Enumerate all permutations:** `n!` reaches over six billion at `n=13`. Subset/remainder memoization merges repeated suffix subproblems.
- **Construct each concatenated integer or string:** Only the remainder matters for divisibility. Modular concatenation avoids large integer and parsing work.
- **Greedily sort nums without feasibility checks:** The sorted permutation may not be divisible. The oracle is what makes the lexicographic greedy choice safe.
- **Store only mask in memo:** The same subset can yield multiple prefix remainders with different futures, so remainder is essential state.
- **Memoize the lexicographically smallest suffix itself:** It can work but stores much larger objects. Boolean feasibility plus reconstruction is more memory efficient.
- **k equals one:** Every integer is divisible by one. All shifts and remainders are zero, and reconstruction returns `nums` sorted numerically.
- **One number:** The answer is that singleton if its value is divisible by `k`, otherwise empty.
- **Duplicate numbers:** Occurrence bits ensure each copy is used once; visible equal choices do not disturb lexicographic order.
- **Value with several digits:** `len(str(value))` supplies the exact decimal shift width.
- **No leading zeros:** Inputs are positive integers, so their decimal representations are canonical and concatenation has no ambiguous leading-zero segments.
- **No valid permutation:** The initial feasibility call returns false and the source returns an empty list.
- **Already sorted valid permutation:** Reconstruction accepts each smallest remaining value and returns it.
- **Remainder zero before completion:** This does not imply success; later appended digits can change the remainder. Only the full-mask base case tests final divisibility.
- **Bytearray codes:** Zero cannot mean false because it denotes uncomputed; explicit codes one and two separate cached failure and success.
