## General
**Solve every substring as an interval state**

Let `best[i][j]` be a shortest encoding of `s[i:j + 1]`. Process intervals from short to long so every proper subinterval already has its optimum. Initialize each state with its literal substring, which guarantees a valid fallback.

**Consider every concatenation boundary**

For each split `k`, concatenate `best[i][k]` and `best[k + 1][j]`. If that is shorter, keep it. This covers optimal encodings whose outermost structure is a concatenation, including a repeated prefix followed by unrelated text.

**Detect a repeated whole interval**

For interval text `t`, search for `t` inside $(t + t)$ starting after position zero. A match position smaller than `len(t)` is its shortest period. When that period divides the length, the interval consists of repeated copies of its prefix. Form `repeat_count[best encoding of that prefix]`, allowing nested compression inside the repeated unit.

**Why the recurrence is complete**

The outermost form of any valid encoding is either literal text, a concatenation of two encoded substrings, or one repetition wrapper around a shorter decoded block. The transition examines all three forms, and induction on interval length makes every inner encoding shortest. Selecting the shortest candidate therefore yields a global optimum.

## Complexity detail
There are $O(n^2)$ intervals. Trying all split points and performing linear periodicity work costs $O(n)$ per interval, for $O(n^3)$ time. The interval table has $O(n^2)$ entries; stored output strings add implementation-dependent character storage beyond the state count.

## Alternatives and edge cases
- **Top-down memoization:** uses the same recurrence and asymptotic bounds while evaluating only reached intervals.
- **Try every candidate period manually:** is correct but repeated character comparisons can add another factor of `n`.
- **Greedy longest repetition:** can miss a shorter encoding formed by splitting or by nesting a compressed unit.
- **Short repetition:** keep literal text when brackets and count are not shorter.
- **Nested pattern:** use the already optimal encoding of the repeated unit inside brackets.
- **Tied minimum encodings:** any shortest equivalent representation satisfies the contract; deterministic strict improvements keep a stable choice.
- **Partial repeated prefix:** concatenation states handle compressed regions followed by unmatched suffixes.
