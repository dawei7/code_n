## General

**A character stops being distinct only when all copies are deleted**

Suppose character `c` appears `f_c` times. Deleting fewer than `f_c` copies leaves at least one `c` in the string, so `c` still contributes one distinct character.

Therefore, partial deletion of a character class cannot help satisfy the distinct-count limit. In an optimal solution, every character is either:

- kept with all its occurrences;
- removed by deleting all its occurrences at cost `f_c`.

The order of characters in the string is irrelevant. Only the frequency of each distinct letter matters.

**How many classes must disappear**

Let `d` be the current number of distinct letters.

If `d <= k`, the string already meets the requirement and the answer is zero.

If `d > k`, at least `d-k` character classes must be removed completely. Removing more classes would add positive deletion cost without being required, so an optimum removes exactly `d-k` classes.

The problem becomes:

choose `d-k` frequencies with minimum possible sum.

**Delete the least frequent classes**

Sort the frequencies in non-decreasing order:

`f_1 <= f_2 <= ... <= f_d`.

The minimum sum of any `d-k` frequencies is the sum of the first `d-k`. Equivalently, keep the `k` most frequent character classes and delete everything else.

An exchange argument proves this. If a proposed solution deletes a class of frequency `b` but keeps another class of smaller frequency `a < b`, swap their roles. The resulting string still has the same number of distinct characters, while deletion cost decreases from `b` to `a`. Repeating removes every such inversion and leaves exactly the least frequent classes deleted.

**Understand the compact slice**

The source computes:

`sorted(Counter(s).values())[:-k]`.

`Counter(s).values()` gives one frequency per present character. Sorting places the smallest first.

For a list of length `d`, slicing off the final `k` entries with `[:-k]` leaves the first `d-k` entries—the frequencies to delete.

If `d <= k`, Python slicing returns an empty list. For example, a two-entry list with `k=3` sliced as `[:-3]` is empty. Summing it gives zero automatically.

The constraint `k >= 1` matters to this exact syntax. If `k=0`, `[:-0]` means `[:0]` and would also be empty instead of selecting all frequencies. Zero is outside the documented domain.

**Why keeping frequent classes minimizes deletions**

The number of retained characters equals:

`len(s) - deletions`.

Among at most `k` distinct classes, retaining the `k` largest frequencies maximizes the number of characters kept. Minimizing deletions and maximizing retained characters are the same objective.

This equivalent perspective often makes the greedy rule intuitive: expensive-to-delete classes should be preserved.

**Trace yyyzz**

Frequencies are three for `y` and two for `z`. With `k=1`, sorted frequencies are `[2,3]`. Slice `[:-1]` keeps only `[2]`, whose sum is two. Delete both `z` characters and retain all three `y` characters.

**Why positions and resulting order do not matter**

Deleting all occurrences of a chosen letter may remove characters from many separated positions, but each individual character deletion costs one and there is no restriction on which positions may be deleted. The remaining string's order is inherited automatically, and the requirement examines only its distinct set.

Thus a frequency-only solution is complete.

## Complexity detail

Let `n = len(s)` and `U` be the number of distinct letters. Building the Counter takes `O(n)` expected time. Sorting its `U` frequencies costs `O(U log U)`.

Because the input alphabet is fixed to 26 lowercase letters, `U <= 26` is a problem constant. The sorting cost is therefore `O(1)` relative to `n`, and total time is `O(n)` as stated in the manifest.

The Counter and sorted frequency list contain at most 26 entries, so auxiliary space is `O(1)` under the fixed-alphabet model. For an unbounded alphabet, the exact same code would be `O(U)` space and `O(n+U log U)` time.

## Alternatives and edge cases

- **Delete arbitrary occurrences greedily:** Removing some copies of a still-present letter cannot lower the distinct count and wastes deletions.
- **Keep the k most frequent classes:** This is exactly equivalent and may be implemented by sorting descending and subtracting their sum from `n`.
- **Use a 26-slot count array:** It avoids hashing and retains the same linear/fixed-space bounds.
- **Try every subset of letters:** At most 26 makes it theoretically bounded, but frequency sorting gives the optimum directly.
- **Already at most k distinct:** The slice is empty and the answer is zero.
- **k larger than the string length:** Distinct count is at most string length, so no deletion is needed.
- **All characters identical:** One class is within every legal `k>=1`, so answer zero.
- **Every character unique:** All frequencies are one; delete exactly `d-k` arbitrary characters.
- **Tied frequencies:** Any tied classes can be removed; deletion total is identical.
- **k equals one:** Keep only a most frequent letter and delete all other classes.
- **k equals zero:** Not allowed; the compact negative-zero slice would need special handling in a generalized problem.
- **Lowercase guarantee:** It is what makes the Counter's maximum size a constant 26.
- **Partial class deletion:** Never useful for the distinct-count objective, which is the key reduction.
