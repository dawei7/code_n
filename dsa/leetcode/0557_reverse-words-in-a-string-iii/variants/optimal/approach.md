## General

The operation has two independent preservation rules:

- words must remain in their original left-to-right order;
- only the characters inside each word are reversed.

The solution separates the sentence into words, reverses each word independently, and joins the transformed words back with one space.

**Split at the guaranteed separators.** `s.split()` returns the words in their original order. With the source constraints, there are no leading or trailing spaces and every neighboring pair of words is separated by exactly one space. Therefore splitting without an explicit separator loses no meaningful spacing information for any legal input.

For:

`"Let's take LeetCode contest"`,

the pieces are `"Let's"`, `"take"`, `"LeetCode"`, and `"contest"`.

The split step changes only representation. It does not reorder the pieces.

**Reverse one word with slicing.** For each word `t`, slice `t[::-1]` traverses its characters from the final index to the first. The step value negative one means move backward one position at a time.

For `"Let's"`, the characters are reversed as a complete sequence, producing `"s'teL"`. The apostrophe is printable ASCII and is treated like any other character. The algorithm does not attempt to interpret punctuation, capitalization, or language; a word is simply the complete non-space token supplied by `split`.

The generator expression:

`(t[::-1] for t in s.split())`

produces reversed words one at a time for the join operation.

**Restore exactly one separator between words.** `" ".join(...)` places a single space between each consecutive generated word and no space at either end.

That matches the legal input format exactly. If the input contains `m` words, join inserts `m - 1` spaces, the same number and positions between word groups as the source sentence.

The first example becomes:

- `"Let's"` → `"s'teL"`;
- `"take"` → `"ekat"`;
- `"LeetCode"` → `"edoCteeL"`;
- `"contest"` → `"tsetnoc"`.

Joining them yields `"s'teL ekat edoCteeL tsetnoc"`.

For `"Mr Ding"`, the two words become `"rM"` and `"gniD"`, while their order remains first-word then second-word.

**Why words do not become reordered.** The generator visits the list returned by `split` from beginning to end. Reversing `t` affects only characters inside that one token. Join consumes tokens in the same sequence, so word index zero remains word index zero, and so on.

**Why character reversal is exact.** For a word of length `q`, output position zero receives original position `q - 1`, output position one receives original `q - 2`, and the final output position receives original position zero. Every character appears exactly once, establishing a full reversal rather than a rotation or partial swap.

**Why whitespace is correct under the contract.** The description says whitespace should be preserved, and the constraints specialize that whitespace to a single ordinary space between words with none outside. Splitting and joining one space reconstructs that exact legal form.

For a generalized string with tabs, multiple spaces, or leading spaces, this exact implementation would normalize them and would not preserve them byte for byte. Those inputs are explicitly outside the source constraints; an in-place character scan would be needed for the broader interpretation.

**Single-character words need no branch.** Reversing a one-character slice returns the same character. A sentence containing `"a b"` is reconstructed unchanged, which is correct.

**The input remains immutable.** Python strings cannot be changed in place. Every reversed word and the final sentence are new strings, while `s` remains unchanged.

The generator form also keeps the transformation readable: it describes “reverse each word” directly, while `join` describes the separator policy. There is no index arithmetic that could accidentally move a character across a word boundary. Each temporary reversed token is consumed in sequence as the output is assembled.

## Complexity detail

Let $n$ be the number of characters in `s`. Splitting scans the sentence and creates word strings totaling $O(n)$ characters. Across all words, reversing copies each non-space character once. Joining writes every reversed character and separator once. Total time is $O(n)$.

The word list, reversed-word strings, and final output together require $O(n)$ storage under peak asymptotic accounting, matching the manifest. The generator itself is lazy, but `split` and the result necessarily retain linear text.

The returned output has the same length as the input because every character and every legal separator is represented once.

## Alternatives and edge cases

- **Mutable character-array scan:** Reverse the complete array, then reverse each word, or directly reverse each word interval. It can preserve arbitrary whitespace positions more exactly.
- **Reverse the whole sentence:** That also reverses word order, violating the contract.
- **Reverse word order only:** It preserves word characters rather than reversing them, solving a different problem.
- **Multiple or tab whitespace:** The exact `split()/join` implementation normalizes it; legal inputs contain only single spaces.
- **One word:** The entire string is reversed.
- **One-character word:** It remains unchanged.
- **Printable punctuation:** Apostrophes and other non-space ASCII characters reverse with their word.
- **Mixed uppercase and lowercase:** Character case is preserved while positions reverse.
- **No leading or trailing spaces:** Join correctly produces none.
- **Very long word:** Slicing remains linear in that word's length.
- **Input order:** Generator iteration and join preserve it exactly.
