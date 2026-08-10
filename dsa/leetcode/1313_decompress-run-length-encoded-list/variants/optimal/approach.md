## General

The compressed list is organized into adjacent pairs:

`[frequency, value]`.

For each pair, the output must contain `frequency` copies of `value`, and pair outputs must be concatenated in their original left-to-right order. The exact Optimal solution expresses those two nested repetitions in one list comprehension:

`[nums[i + 1] for i in range(0, len(nums), 2) for _ in range(nums[i])]`.

Reading a comprehension with two `for` clauses is easiest from left to right as nested loops. The first clause chooses a compressed pair. The second repeats that pair's value.

**Stepping through pair starts**

`range(0, len(nums), 2)` produces indices

$$
0,2,4,\ldots,\texttt{len(nums)}-2.
$$

The length is guaranteed even, so every produced `i` is a frequency position and `i + 1` is a valid value position. No incomplete final pair exists.

At pair start `i`:

- `nums[i]` is the frequency, and
- `nums[i + 1]` is the value.

Advancing by two preserves the pair boundaries. Advancing by one would mistakenly interpret a value as the next frequency.

**Repeating one value**

For a fixed `i`, `range(nums[i])` has exactly `nums[i]` iterations. The variable name `_` signals that the particular repetition number is irrelevant. Only the number of iterations matters.

On each of those iterations, the expression `nums[i + 1]` is evaluated and appended to the new result list. Consequently, that value appears exactly its requested number of times.

The inner repetition completes before the outer loop advances to the next pair. This is the same order as:

`for i in pair starts`, then `for each repetition`, then `append the pair's value`.

It therefore concatenates runs rather than interleaving them.

**Tracing the first example**

For `nums = [1,2,3,4]`, the outer index first equals zero. The frequency is one and the value is two, so the inner loop emits one `2`.

The next outer index is two. The frequency is three and the value is four, so the inner loop emits `4` three times.

Because the first run finishes before the second starts, the final list is `[2,4,4,4]`.

For `[1,1,2,3]`, pair zero emits one `1` and pair one emits two `3` values, producing `[1,3,3]`.

**Why the comprehension is exact**

The outer range visits every compressed pair exactly once because it enumerates all even indices from zero through the last valid frequency index. For each pair, the inner range has exactly the stated frequency, and every iteration emits the paired value.

No element from another pair can be emitted during that inner loop because `i` stays fixed. Pair order matches increasing `i`. Therefore, the result contains exactly the concatenation defined by the run-length encoding.

The input frequencies are at least one, so every pair produces at least one output element. Even if zero frequencies were allowed in a generalized version, `range(0)` would correctly emit an empty run.

**Why a direct construction is necessary**

The decompressed list itself can be much longer than the compressed input. Any algorithm returning it must materialize every required output occurrence, so work proportional to the output length is unavoidable.

The one-line comprehension does not hide an asymptotically faster trick. It is a concise syntax for the optimal amount of generation work.

## Complexity detail

Let $n$ be the compressed list length and define

$$
S=\sum_{i=0,\;i\text{ even}}^{n-2}\texttt{nums}[i],
$$

the decompressed output length.

The outer loop visits $n/2$ pairs, contributing $O(n)$ control work. Across all pairs, the inner loops execute exactly $S$ times and create exactly $S$ output entries. Total time is $O(n+S)$.

The returned list uses $O(S)$ space, matching the manifest. Apart from that required output, the comprehension keeps only loop indices and constant interpreter state, so auxiliary working space is $O(1)$.

Under the local bounds, there are at most 50 pairs and each frequency is at most 100, so $S$ is at most 5000. The asymptotic expression remains more informative than relying only on that fixed maximum.

## Alternatives and edge cases

- **Explicit nested loops:** Initialize `ans`, iterate pair starts, and append in an inner loop. It has identical behavior and complexity and may be easier to debug for beginners.
- **List multiplication and extension:** `ans.extend([value] * frequency)` handles one run compactly. It creates a temporary list for each pair in addition to the final output.
- **Iterator repetition utilities:** Functions such as `repeat` and `chain` can express runs lazily, but returning a list still requires materializing all $S$ entries.
- **Single pair:** The outer range contains only index zero, and the output is that value repeated by its frequency.
- **Frequency one:** The inner range has one iteration, so the value appears once.
- **Repeated values in adjacent pairs:** Their runs become adjacent identical values in the output. They need not be merged because the returned decompression is the same either way.
- **Even-length guarantee:** It ensures `nums[i + 1]` is always valid. Malformed odd-length input would need validation.
- **Positive-frequency guarantee:** Every run contributes at least one value; the code would also naturally skip a zero-frequency run outside the contract.
- **Output can exceed input:** Space and time must be measured using $S$, not only the compressed length $n$.
- **Order of comprehension clauses:** Swapping them would not preserve independent pair-specific repetition and would either be invalid or emit a different order.
- **Underscore variable:** `_` is an ordinary loop variable by language rules, but convention indicates its value is intentionally unused.
