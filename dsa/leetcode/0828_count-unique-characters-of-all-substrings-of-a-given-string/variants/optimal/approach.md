## General

**Reverse the counting perspective**

Enumerating every substring is too expensive. A string of length `n` has `n(n+1)/2` substring occurrences, and counting character frequencies separately inside each one would add still more work.

Instead of asking, “How many unique characters does this substring contain?”, ask:

> For one particular occurrence of one character, in how many substrings is this occurrence the only copy of that character?

Each time a character is unique in a substring, exactly one occurrence of that character deserves one contribution. Summing the contribution of every occurrence therefore produces the same total as summing unique-character counts over every substring.

This is a standard double-counting change of viewpoint. The objects being counted are pairs consisting of a substring occurrence and a character that appears exactly once in it.

**Store occurrence indices by character**

The dictionary `d` maps each uppercase character to the increasing list of indices where it occurs. Enumerating `s` left to right automatically appends positions in sorted order.

For `s = "ABA"`:

- `d["A"] = [0,2]`;
- `d["B"] = [1]`.

The calculation for one occurrence needs only the previous and next occurrence of the same character. Positions of other characters are irrelevant to whether this particular character is unique.

**Bound one occurrence by its equal neighbors**

Suppose a character occurs at current index `cur`. Let `prev` be its preceding occurrence, or `-1` if none exists. Let `next` be its following occurrence, or `n` if none exists.

A substring is represented by inclusive boundaries `[L,R]`. For the occurrence at `cur` to appear and be the only copy of its character:

- `L` must be greater than `prev` and no greater than `cur`;
- `R` must be at least `cur` and less than `next`.

Thus, valid starts are

$$
prev+1,prev+2,\ldots,cur,
$$

giving `cur - prev` choices. Valid ends are

$$
cur,cur+1,\ldots,next-1,
$$

giving `next - cur` choices.

Every valid start can be paired independently with every valid end, so the occurrence contributes

$$
(cur-prev)(next-cur).
$$

**Why the previous and next equal occurrences are the only boundaries needed**

Choosing `L <= prev` would include the preceding copy, so the current occurrence would no longer be unique. Choosing `R >= next` would include the following copy, causing the same problem.

If `L > prev` and `R < next`, there cannot be another equal character inside the substring. Any earlier equal occurrence lies at or before `prev`, and any later equal occurrence lies at or after `next`. Therefore, the two nearest equal occurrences provide both necessary and sufficient boundaries.

**Sentinels remove special cases**

For one occurrence list `v`, the solution constructs

`v = [-1] + v + [len(s)]`.

The sentinel `-1` acts as an imaginary occurrence immediately before the string, and `n` acts as one immediately after it. Now every real occurrence `v[i]` has a predecessor `v[i-1]` and successor `v[i+1]`, including the first and last occurrence of that character.

The loop over `range(1, len(v) - 1)` visits only real occurrence entries and adds

`(v[i] - v[i - 1]) * (v[i + 1] - v[i])`.

No separate edge formulas are needed.

**Trace `"ABA"`**

For A, the augmented list is `[-1,0,2,3]`.

- The occurrence at 0 contributes `(0 - (-1))(2 - 0) = 1 * 2 = 2`. It is unique in `"A"` at indices 0–0 and `"AB"` at 0–1.
- The occurrence at 2 contributes `(2 - 0)(3 - 2) = 2 * 1 = 2`. It is unique in `"A"` at 2–2 and `"BA"` at 1–2.

For B, the augmented list is `[-1,1,3]`. Its contribution is

`(1 - (-1))(3 - 1) = 2 * 2 = 4`,

covering `"B"`, `"AB"`, `"BA"`, and `"ABA"`.

The total is 2 + 2 + 4 = 8. In the full substring view, the two single A substrings contribute one each, B contributes one, AB and BA contribute two each, and ABA contributes only B, also totaling 8.

**Why repeated substring text is still counted correctly**

The problem counts substring occurrences by their index boundaries, even when two substrings have the same text. The contribution method also chooses concrete start and end indices. Two equal-looking substrings at different positions correspond to different boundary pairs and are counted separately.

**Why the total is correct**

Consider any substring and any character unique inside it. That character has one occurrence `cur` in the substring. Its start lies after the preceding equal occurrence and at or before `cur`; its end lies at or after `cur` and before the following equal occurrence. Therefore, the substring-character pair appears once among `cur`'s counted boundary choices.

Conversely, every boundary pair counted for `cur` contains `cur` and excludes its nearest equal occurrence on both sides, so the character is unique in that substring. This is a one-to-one correspondence. Summing all occurrence contributions yields exactly the requested sum.

## Complexity detail

Let `n = len(s)` and let `A` be the alphabet size.

Building the occurrence lists visits each index once, taking `O(n)` time. Across all dictionary values, the inner contribution loops also visit each stored occurrence once. Sentinel-list construction copies each character's occurrence list, and the total number of copied real indices across all characters is `n`. Total time is `O(n)`.

For the exact source, the lists in `d` collectively store all `n` indices, so they use `O(n + A)` space. One augmented list can contain up to `n+2` entries, giving `O(n)` additional temporary space. Thus, the precise auxiliary bound of this implementation is `O(n + A)`, which simplifies to `O(n)`.

The manifest's `O(A)` space target is achievable with a streaming contribution method that stores only the two most recent positions for each character and finalizes remaining contributions at the end. The protected implementation instead favors the especially direct occurrence-list proof, so its actual position storage is linear in `n`.

Because the input uses only 26 uppercase English letters, dictionary key count is bounded, but the lists attached to those keys can still collectively contain `n` positions.

## Alternatives and edge cases

- **Enumerate all substrings:** There are `O(n^2)` of them, and maintaining or recomputing unique counts is too slow for `n = 10^5`.

- **Streaming last-two-occurrences method:** Update each character's contribution as new occurrences arrive, storing only a constant number of positions per alphabet symbol. It reaches `O(A)` space but has a less immediately visual derivation.

- **One character appears once:** With sentinels, its contribution is `(i+1)(n-i)`, exactly the number of substrings containing that index.

- **All characters distinct:** Every character is unique in every substring containing it. The contribution formula sums to the total lengths of all substrings.

- **All characters equal:** Only length-one substrings have a unique character. Each occurrence's neighboring equal positions restrict its contribution to one, so the answer is `n`.

- **First occurrence of a character:** The `-1` sentinel gives `cur+1` possible starts.

- **Last occurrence of a character:** The `n` sentinel gives `n-cur` possible ends.

- **Adjacent equal characters:** The gap between their indices is one, sharply limiting boundary choices so a substring cannot include both and call either unique.

- **Repeated substring values:** Different start/end positions remain different boundary choices and are counted separately.

- **Uppercase alphabet:** Dictionary grouping uses the characters exactly as supplied; no case normalization is needed.

- **Answer size:** The Reference guarantees that the final sum fits in a 32-bit integer, while Python integers would also handle larger values.

- **Input immutability:** Occurrence and sentinel lists are new objects; `s` is unchanged.
