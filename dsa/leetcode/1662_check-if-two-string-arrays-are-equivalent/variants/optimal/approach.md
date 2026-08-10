## General

**The array boundaries are not part of the represented string**

Each input is an array of string pieces, but equivalence is defined after concatenating those pieces in their given order. A boundary between two array entries carries no meaning in the represented result. Thus `["ab", "c"]` and `["a", "bc"]` both represent `"abc"` even though their piece lengths differ.

The exact implementation follows the definition directly:

`''.join(word1) == ''.join(word2)`.

For each array, `join` places the empty string between consecutive elements. Inserting an empty separator means the pieces are copied next to one another with no added character. Their original order is preserved. The equality operator then compares the two completed strings.

**How `join` constructs the represented value**

Consider `word1 = ["abc", "d", "defg"]`. Starting with an empty result, concatenating its entries in order yields `"abc"`, then `"abcd"`, then `"abcddefg"`. There is no delimiter between the ending `d` of one piece and the beginning `d` of the next. The array `["abcddefg"]` produces exactly the same completed string, so equality returns true.

Using `''.join(...)` is preferable to repeatedly executing something like `result += piece` in a loop. Python’s join operation knows all pieces up front, can determine the total required length, and builds the finished string in one coordinated operation. Repeated immutable-string concatenation may copy an ever-growing prefix on each iteration and can become quadratic.

The source invokes `join` once for each side. Each call creates a new Python string containing all characters represented by that input. The comparison is performed on those two new strings, not on the original arrays piece by piece.

**Why ordinary string equality is sufficient**

Python string equality requires equal lengths and equal characters at every position. It does not care how either string was constructed. Once the array boundaries have been removed by joining, those are exactly the conditions required by the problem.

If the joined lengths differ, the strings cannot represent the same character sequence, so equality is false. If their lengths match but some earliest position contains different letters, equality is also false. If every corresponding character matches, the complete represented strings are identical and equality is true.

An explicit preliminary length check is unnecessary because string equality already includes it. Likewise, the source does not need to compare the number of array elements or corresponding piece lengths. Those quantities can differ freely without affecting the concatenated value.

**A correctness argument from character positions**

Let `A` be the string obtained by concatenating `word1` in order and `B` the string obtained from `word2`. By the problem’s definition, `word1` represents exactly `A` and `word2` represents exactly `B`. The two `join` calls construct precisely those values because the separator is empty and no piece is reordered or modified.

The returned comparison is true exactly when `A == B`. If it is true, every character of the two represented strings occurs at the same position and their lengths match, so the arrays are equivalent. If it is false, either a length or character differs, so the represented strings are not the same. Therefore the one-line return expression is both necessary and sufficient.

For the false example `["a", "cb"]` versus `["ab", "c"]`, joining gives `"acb"` and `"abc"`. The first characters match, but the second positions are `c` and `b`, so equality correctly rejects them.

**What the implementation deliberately trades for simplicity**

A character-by-character solution can compare the virtual concatenations without ever materializing them. That can use constant auxiliary state, but it needs either four indices—piece and character positions for each side—or character iterators with careful end handling. The exact source instead chooses the simplest direct expression and pays for two temporary strings.

This distinction matters because the manifest lists $O(1)$ space, while the concrete Python operations allocate memory proportional to the total character count. The algorithm is still optimal in running-time order: in the worst case it must inspect every character to establish equality. Its space behavior, however, is not the streaming variant’s behavior.

## Complexity detail

Let

$$
L_1 = \sum_{w \in \texttt{word1}} \lvert w \rvert
\quad\text{and}\quad
L_2 = \sum_{w \in \texttt{word2}} \lvert w \rvert.
$$

Joining the first array takes $O(L_1)$ time, and joining the second takes $O(L_2)$ time. Equality takes up to $O(\min(L_1,L_2))$ character comparisons after a length check; in the equal or long-common-prefix case this is linear. Total time is therefore $O(L_1 + L_2)$.

The two joined strings occupy $O(L_1 + L_2)$ temporary space while the comparison is evaluated. The returned Boolean itself is constant size. Accordingly, the exact source uses linear auxiliary space, not the manifest’s $O(1)$ claim. If `N = L_1 + L_2`, both bounds can be summarized as $O(N)$ time and $O(N)$ space.

The input arrays and their original string objects are not modified. The joined strings are temporary immutable values managed by Python after the comparison.

## Alternatives and edge cases

- **Four-pointer streaming comparison:** Keep a piece index and a character index for each array, advance across piece boundaries, and compare one character at a time. This gives $O(L_1 + L_2)$ time and $O(1)$ auxiliary space, matching the manifest, but requires more boundary logic.
- **Character iterators with a sentinel:** Chain the pieces from each side into character iterators and compare with `zip_longest` using a unique sentinel. This avoids full joined strings conceptually, though iterator objects and library semantics should be explained carefully.
- **Repeated `+=` concatenation:** It is easy to write but can repeatedly copy growing immutable strings, leading to $O(N^2)$ time in unfavorable implementations. `join` is the correct materializing approach.
- **Different numbers of pieces:** This has no effect by itself. `["abc"]` and `["a", "b", "c"]` are equivalent.
- **Different piece boundaries:** Boundaries disappear during joining, so `["ab", "c"]` and `["a", "bc"]` compare true.
- **Different total lengths:** Python string equality detects the mismatch and returns false.
- **Mismatch near the beginning:** The joined strings have already been built, although equality itself can stop at the first unequal character.
- **Mismatch only at the end:** Equality may inspect the entire common prefix, which is why linear comparison time is required in the worst case.
- **Single piece on each side:** The method still works; joining a one-element array produces that element unchanged in value.
- **Nonempty-piece guarantee:** Every input piece has at least one character. The method would also handle empty pieces correctly because an empty separator plus an empty piece contributes no character.
- **Original arrays remain reusable:** `join` creates new strings and never alters the list entries or their order.
