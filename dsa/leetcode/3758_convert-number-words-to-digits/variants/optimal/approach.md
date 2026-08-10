## General

**Follow the parsing rule literally from left to right**

At source index `i`, the parser asks whether any complete digit word begins exactly there. If one matches, it emits that digit and skips the entire word. If none matches, it advances by exactly one character.

This is not a general word-segmentation problem that may choose among competing decompositions. The contract specifies a deterministic local scan, and the ten valid words are fixed.

**Try the ten digit words**

The list `d` stores words in numeric order, so list index `j` is the digit to emit. For each candidate word `t`, the source first verifies `i+len(t)<=n`, preventing a partial suffix from matching.

It then compares `s[i:i+m]` with `t`. On equality, `str(j)` is appended to `ans`.

No two distinct English digit words are identical, so at most one candidate can match a position. The list order does not change successful parsing, but directly supplies the correct numeric mapping.

**Understand the index update**

On a match of length `m`, the inner branch adds `m-1` to `i` and breaks. The unconditional `i+=1` after the loop makes the net advance exactly `m`.

On a miss, no inner update occurs, so the same unconditional increment advances exactly one character.

This compact structure implements both contract branches without a separate matched flag.

It helps to view `i` as the first unprocessed source position. The loop never moves it backward. It also never leaves it unchanged: a failed position advances by one, while a successful position advances by the matched word's positive length. Therefore every iteration makes progress and the loop must eventually terminate.

For `"onefourthree"`, index zero matches `"one"` and jumps to three, where `"four"` matches, then `"three"`. The result list becomes `["1","4","3"]`.

For `"ninexsix"`, `"nine"` is consumed, `x` fails all ten comparisons and is skipped alone, and `"six"` then matches.

For `"zeero"`, the failed `z` position advances to the first `e`, then each later position is tested independently. No complete `"zero"` occurs, so the result is empty.

**Why failed fragments are not skipped wholesale**

A failed prefix can contain the beginning of a valid word at its next character. Advancing one preserves that possibility. For example, arbitrary noise ending just before `"two"` must not cause the parser to leap over the `t`.

Conversely, after a successful match, positions inside that word are not reconsidered because the rule consumes the whole word. This prevents overlapping matches that start within an already extracted token.

This consumption rule resolves cases that may look ambiguous at first. In `"oneight"`, `"one"` matches at index zero and consumes its final `e`. The scan resumes at `i`, not at that already-consumed `e`, so the overlapping spelling of `"eight"` is not extracted. The result is `"1"`. By contrast, `"oneeight"` contains a complete non-overlapping `"eight"` after `"one"`, so it produces `"18"`. The parser does not search globally for every recognizable spelling; it follows the local consume-or-skip rule.

**Separate recognition from output construction**

Each successful match contributes exactly one character to `ans`, even though the source word occupies between three and five characters. Keeping these characters in a list avoids repeatedly rebuilding an immutable result string. Only after scanning finishes does `"".join(ans)` allocate the final contiguous string.

The numeric position of a word in `d` is part of the implementation. When `"zero"` matches, `j` is zero; when `"nine"` matches, `j` is nine. There is no second dictionary to keep synchronized and no conversion from an English word after the match.

**Why the output is exact**

Inductively, before each loop iteration, all source positions below `i` have been processed exactly according to the rule, and `ans` contains their discovered digits in order. A match performs the required emission and word-length advance; a miss performs the required one-character skip. Either preserves the invariant.

When `i==n`, the entire source has been processed. Joining the list concatenates emitted digit characters without repeated immutable-string appends.

There are two complementary directions in this reasoning. Every emitted digit is sound because it came from a complete word comparison at the current position. Every digit that the deterministic scan requires is complete because the loop tests all ten candidates before declaring that position a miss. Together, these show that the result contains neither invented digits nor omitted matches.

## Complexity detail

Let `n=len(s)`. At every visited position, at most ten words of maximum length five are compared. Both are fixed constants, so this is $O(1)$ work per position and $O(n)$ total time.

Python slices create strings of at most five characters, also constant-size. The result list can contain $O(n)$ digits, and the joined return string has the same order, so output construction space is $O(n)$. The fixed word list uses $O(1)$ space.

The scan may visit fewer than `n` starting positions because a successful match jumps across several characters. This can improve the concrete running time, but the worst case is a string with no matches, where all `n` positions are visited. The $O(n)$ bound covers both cases.

## Alternatives and edge cases

- **Trie matching:** A trie can share prefix comparisons, but ten words of bounded length make the simple constant scan sufficient.
- **Regular expression extraction:** It may obscure the mandated one-character fallback and overlapping-start semantics.
- **Skip an entire failed fragment:** This can miss a word starting one position later. Failure advances exactly one.
- **Advance only `m-1` total after a match:** The unconditional increment must be included; the source's net movement is `m`.
- **Partial word at the end:** The bounds check rejects it.
- **No matches:** Joining an empty list returns `""`.
- **Back-to-back words:** Consuming one lands exactly at the next word's first character.
- **Noise between words:** Each noise character is skipped separately until a new match begins.
- **Overlapping letter patterns:** Positions inside a successfully consumed word are intentionally unavailable to later matches.
- **An apparent word that begins inside a consumed word:** It is ignored because parsing resumes after the entire successful token.
- **Large input:** The parser is iterative and does not risk recursion depth.
- **Output digits including zero:** `str(0)` appends the character `'0'` normally when `"zero"` matches.
