## General

**Every piece consumes one distinct starting character**

Suppose a valid partition has `p` nonempty substrings. Each has one starting character, and all those starts must be distinct. Therefore `p` cannot exceed the number of distinct characters appearing anywhere in `s`.

If `D=len(set(s))`, then

$$
p\le D.
$$

This is an immediate upper bound. The important remaining step is proving that all `D` distinct characters can actually be used as starts in one complete consecutive partition.

The bound counts characters, not occurrences. If `a` appears one hundred times, at most one substring may start with `a`, because a second such substring would repeat a starting character. On the other hand, each different character can potentially contribute one start. This makes the number of distinct characters the natural candidate answer, but a candidate upper bound is not enough until a legal partition attaining it is shown.

**Cut before each character's first occurrence**

The character `s[0]` necessarily starts the first substring. For every other distinct character, consider its first occurrence in `s`. Place a cut immediately before that position.

These first-occurrence indices are distinct and appear in increasing order. They divide `s` into consecutive, nonempty pieces that cover the string exactly.

More explicitly, collect index zero and the first index of every character whose first occurrence is not zero. Sort those indices, although scanning the string would already discover them in sorted order. A substring begins at each collected index and ends immediately before the next collected index; the final substring ends at `n-1`. Because consecutive start indices are different, no piece is empty. Because the first index is zero and the last piece reaches the end, no character is omitted.

The first piece starts with `s[0]`. Every later piece starts at the first occurrence of a character not used as an earlier start, so all starting characters are distinct.

There is one piece for each distinct character, attaining `D`. Combined with the upper bound, the maximum is exactly `D`.

This is a tight-bound argument. The distinct-start rule proves that no solution can exceed `D`; the first-occurrence construction proves that one solution reaches `D`. When a lower construction and an upper limit meet at the same value, no search over other partitions can improve the answer.

For `"abab"`, distinct characters are `a` and `b`. Cut before the first `b` to obtain `"a"` and `"bab"`.

For `"abcd"`, every position is a first occurrence, so cutting before positions one, two, and three yields four single-character pieces.

For `"aaaa"`, only `a` is distinct. No valid second piece can start without repeating `a`, and the entire string as one piece attains one.

For `"cabcaab"`, the first occurrences are `c` at zero, `a` at one, and `b` at two. Cutting at one and two produces `"c"`, `"a"`, and `"bcaab"`. Later copies of all three characters remain inside the last piece, but the three starts are still `c`, `a`, and `b`, so the partition reaches the distinct-character bound.

**Why characters inside a piece do not matter**

Only the first character of each substring is constrained. Repeated characters later in a piece do not consume or conflict with start characters. This is why cuts at first occurrences are enough even if earlier pieces contain future repetitions of already used letters.

For example, in `"abac"`, cuts at first `b` and first `c` produce `"a"`, `"ba"`, and `"c"`. The internal `a` in `"ba"` is harmless.

It would be incorrect to demand that every piece itself contain distinct characters or that characters be disjoint across pieces. Neither condition appears in the contract. The optimization concerns only the character at each selected starting position. Keeping that distinction in mind turns what looks like a partition dynamic-programming problem into a counting observation.

**Why a set gives the complete answer without constructing cuts**

The proof supplies an attainable partition, but the method only needs to return its size. `set(s)` contains each distinct lowercase character once, so its length is exactly `D`.

Constructing the actual substrings or remembering first indices would add work and storage without changing the requested count.

The method therefore separates the mathematical witness from the implementation. The proof describes where cuts could be placed so that attainability is unquestionable. The executable solution returns only `len(set(s))` because the problem asks for the maximum number, not the witnessing boundaries.

## Complexity detail

Let `n=len(s)`. Building the set scans all characters once, taking expected $O(n)$ time.

The alphabet contains only 26 lowercase letters, so the set has at most 26 entries. Its auxiliary space is $O(1)$ with respect to `n`. In a generalized unbounded alphabet, it would be $O(D)$.

Set insertion and membership are expected $O(1)$ per character in Python, which gives the expected linear scan. Since the documented input alphabet is fixed, even the number of retained hash-table entries is bounded independently of the input length.

The returned result is one integer and no input mutation occurs.

## Alternatives and edge cases

- **Dynamic programming over cut positions:** The first-occurrence construction proves no optimization state is needed.
- **Greedily cut at every new character while scanning:** This explicitly realizes the proof and gives the same count, but storing substrings is unnecessary.
- **Count character runs:** A character may reappear after other letters, but it can start at most one piece. Runs can greatly exceed distinct characters.
- **Cut before every occurrence:** Repeated occurrences would create pieces with duplicate starting characters and violate the rule.
- **Require every character inside pieces to be unique:** The contract restricts only substring starts, not contents.
- **Single-character string:** One distinct character gives one piece.
- **All characters distinct:** Every character can be its own substring, so the answer is `n`.
- **All characters equal:** Only one start character is available.
- **Repeated first character later:** It may appear inside a later piece but cannot start another one.
- **Alphabet limit:** The answer can never exceed 26 even when `n` is much larger.
- **Complete partition requirement:** First-occurrence cuts cover every source position; no suffix is discarded.
- **Nonempty pieces:** Distinct cut positions ensure every piece has at least one character.
- **Construction versus return value:** The partition proves the count is attainable, but the source correctly returns only that count.
