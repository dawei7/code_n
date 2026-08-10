## General

A verbal arithmetic puzzle assigns one decimal digit to each distinct letter. The assignment must be one-to-one, multi-character words cannot begin with zero, and the sum of all left-side words must equal `result`.

Trying all complete digit assignments and converting every word to an integer would work in principle, but it delays arithmetic failure until very late. The exact Optimal solution uses backtracking column by column from right to left, just as hand addition does. After one column's letters have been assigned, divisibility by ten checks that column immediately and carries the remaining balance into the next column.

**Treating the result as a signed final row**

`isSolvable` appends `result` to `words`. The last row is then treated differently from all preceding rows:

- letters in addend rows have `sign = 1`;
- letters in the final result row have `sign = -1`.

For one column, the recursion accumulates

$$
\text{incoming balance}
+\text{sum of addend digits}
-\text{result digit}.
$$

For the column equation to hold, this quantity must be divisible by ten. Dividing it by ten produces the carry-like balance passed to the next more significant column.

Appending `result` mutates the caller-provided `words` list. The algorithm relies on the result being the final row after that append.

**Reading columns from least significant to most significant**

`col = 0` means the rightmost character, `col = 1` means the next character to the left, and so on. For a row string `w`, the current character is

`w[len(w) - 1 - col]`.

This indexing reverses the usual left-to-right string order without reversing or padding the strings.

Words can have different lengths. If `col >= len(w)`, that word has no digit in the current column, so the recursion advances to `row + 1` without changing `bal`.

`totalCols` is the maximum row length after including the result. Once `col == totalCols`, every real digit position has been processed. The puzzle is solvable along the current branch exactly when `bal == 0`, meaning no unmatched carry or difference remains.

**Moving from one column to the next**

When `row == totalRows`, all addends and the result have contributed their current-column digits. The code requires `bal % 10 == 0`. If the units digit of the signed balance is nonzero, no choice in a more significant column can repair the current decimal column, so the branch fails immediately.

If divisible, recursion restarts at row zero, advances `col` by one, and passes `bal // 10`. This is the decimal carry relation. Because division happens only after exact divisibility is confirmed, Python's floor division also gives the exact integer quotient if the signed balance is negative.

This early column test is the main pruning mechanism. Backtracking does not wait until all letters are assigned before noticing an impossible units or tens column.

**Maintaining a one-to-one mapping**

`letToDig` maps a letter to its chosen digit. `digToLet` is a ten-entry reverse structure whose `i`th slot is `"-"` when digit `i` is unused.

The forward map lets a repeated letter reuse the same digit consistently. The reverse structure prevents two different letters from selecting the same digit.

If the current letter already has a mapping that is legal at this position, the recursion adds `sign * letToDig[letter]` to `bal` and moves to the next row without branching.

If a new mapping is needed, the loop tests digits zero through nine. `digToLet[i] == "-"` requires the digit to be unused. The candidate is installed in both directions, recursion explores the remainder of the puzzle, and a failed branch undoes the assignments before trying the next digit. This choose, recurse, and unchoose sequence is standard backtracking.

As soon as any recursive call returns true, the method returns true upward without exploring alternative mappings because the problem asks only whether a solution exists.

**Preventing leading zeros**

A zero is legal for a one-character word because its only digit is also the whole number. For a longer word, zero is illegal at its leftmost position.

Because columns are counted from the right, the leftmost position of `w` has

`col == len(w) - 1`.

The candidate condition allows zero only when `len(w) == 1` or the current position is not leftmost. The already-mapped branch performs the same logical test before reusing a zero mapping.

There is a subtle implementation detail. If a letter was previously mapped to zero at a nonleading occurrence and later appears as the leading character of a multi-character word, the already-mapped condition fails and control enters the “choose a new mapping” branch even though the letter is present in `letToDig`. The code can temporarily overwrite its forward mapping without first clearing the old reverse slot. This is unconventional bookkeeping. It does not express the clean invariant that the two maps are exact inverses throughout every recursion frame.

A clearer implementation would immediately reject that branch: a fixed letter mapped to zero cannot be made legal merely because it is encountered at a leading occurrence later. Ordinary backtracking at the frame where zero was first selected will eventually try a nonzero digit. Keeping both maps exact makes the proof and state restoration much safer.

**How the balance represents the full equation**

For each processed column, the divisibility test enforces equality of that decimal digit after accounting for the carry from less significant columns. The quotient passes exactly the remaining multiple of ten into the next column.

Every occurrence of a letter obtains its value from one shared mapping, every chosen digit is reserved, and leading positions reject zero. Thus, a branch that reaches `col == totalCols` with zero balance defines legal numbers and satisfies the entire signed sum.

Conversely, consider any valid puzzle assignment. Backtracking tries available digits in order, so it eventually follows the choices from that assignment unless a column check prunes them. But every column of a valid arithmetic equation has a balance divisible by ten and passes its correct carry onward, so that branch is never pruned. It reaches the final zero balance and returns true.

This completeness argument is cleanest with the mapping-inverse issue corrected as described above. The exact code's unusual zero remapping may still explore useful branches, but it should not be presented as the ideal state invariant.

## Complexity detail

Let $U$ be the number of distinct letters, at most ten, and let $L$ represent the total row-position work across the puzzle's columns.

In the worst case, backtracking explores injective assignments of digits to letters. The number of complete assignments is

$$
P(10,U)=\frac{10!}{(10-U)!},
$$

which is at most $10!$. Column divisibility and leading-zero checks prune many branches in practice, but worst-case search remains factorial. Including the work to walk row and column positions, a more explicit upper description is $O(L\cdot P(10,U))$; the manifest abbreviates this as $O(10!)$ because word lengths and row counts are tightly bounded.

`letToDig` stores at most $U$ mappings and `digToLet` always has ten slots. The recursive call chain advances through rows and columns and can have depth proportional to the number of visited row-column positions, represented by $L$. Auxiliary space is therefore $O(U+L)$, matching the manifest.

The input `words` gains one element because `result` is appended. That side effect does not change the asymptotic bound, but it matters if the caller reuses the list.

## Alternatives and edge cases

- **Whole-assignment brute force:** Assign every distinct letter before checking the equation. It has the same factorial ceiling but misses powerful per-column pruning and repeatedly converts full words.
- **Column backtracking with an explicit carry:** A more conventional formulation processes addend rows in a column, determines the result digit from the sum modulo ten, and passes a nonnegative carry. It can reduce branching and keeps the arithmetic invariant easier to read.
- **Coefficient equation:** Precompute each letter's signed place-value coefficient and search assignments for a weighted sum of zero. This makes full-equation evaluation fast but may prune less locally than column arithmetic unless bounds are added.
- **More than ten letters:** No injective digit assignment can exist. The local contract already caps distinct letters at ten; a generalized implementation can reject larger sets immediately.
- **Single-character word mapped to zero:** This is legal because there is no leading-zero representation with extra digits.
- **Multi-character leading letter mapped to zero:** The branch must be rejected. Reassigning a previously fixed letter in place complicates the exact source's map invariant.
- **Repeated letter in one or several words:** `letToDig` ensures every occurrence uses the same digit.
- **Digit uniqueness:** `digToLet` prevents a new letter from choosing an occupied digit.
- **Different word lengths:** Missing high-order positions are skipped and contribute zero to that column.
- **Result longer than every addend:** Carry propagation can fill the leading result position; the final balance test decides whether it is possible.
- **Result too short:** A nonzero remaining balance after the last column causes false.
- **Early column failure:** If `bal % 10 != 0` after a column, more significant assignments cannot change that column's units digit, so pruning is safe.
- **Input mutation:** `words.append(result)` permanently changes the supplied list. A side-effect-free version would create `words + [result]` instead.
- **No official local editorial:** The explanation is derived from the exact recursive source and local statement, with the mapping caveat called out rather than importing a different implementation.
