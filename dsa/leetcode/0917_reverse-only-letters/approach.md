## General

Non-letter characters must remain at their exact indices, while the sequence of letters must appear in reverse order. Two pointers can swap the outermost remaining letters and skip every fixed non-letter.

The solution first converts immutable string `s` to mutable character list `cs`. Pointer `i` starts at the left end and `j` at the right end.

**Find the next movable character on each side.**

- While `cs[i]` is not alphabetic, increment `i`. Those characters stay untouched in their original positions.
- While `cs[j]` is not alphabetic, decrement `j`.

Both inner loops include `i < j` so indices do not cross or leave the valid range.

When both pointers identify letters and `i < j`, swap them. Then move both pointers inward. Repeating pairs the first letter with the last letter, the second letter with the second-to-last letter, and so on.

**Why fixed characters never move.** A swap occurs only after both `isalpha()` checks have found letters. Non-letters are passed over by pointer movement but are never assigned. Converting to a list preserves their original indices, so they occupy the same positions in the joined result.

**Why the letter sequence is reversed.** Imagine extracting only the letters into sequence

$$
L_0,L_1,\ldots,L_{m-1}.
$$

The first swap places $L_{m-1}$ at the original position of $L_0$ and $L_0$ at the original position of $L_{m-1}$. The next swap does the same for $L_1$ and $L_{m-2}$. Inductively, every letter position receives the letter at the mirrored index in the extracted sequence.

If the number of letters is odd, the middle letter is never swapped after pointers meet. It is its own mirror and is already correct.

**Example `ab-cd`.** Pointers first swap `a` and `d`, producing `db-ca`. They move inward; the right pointer skips the hyphen only when appropriate, and `b` swaps with `c`. The hyphen remains at index 2, yielding `dc-ba`.

For `a-bC-dEf-ghIj`, the extracted letter sequence is `abcdEfghIj`. Reversing that sequence gives `jIhgfEdCba`. Writing those reversed letters back only into the original letter slots while retaining hyphens at their fixed indices produces `j-Ih-gfE-dCba`. The two-pointer swaps perform exactly this extraction-and-reinsertion effect without building a separate letters stack.

**Pointers cannot skip a required letter.** The left pointer advances past a position without swapping only when that character is non-alphabetic. Once it reaches a letter, it stops until the right pointer also reaches a letter and the pair is exchanged. The right side follows the symmetric rule. Therefore every letter outside a possible single center participates in exactly one swap.

Each swap also fixes both positions permanently. Later pointer values lie strictly inside the swapped indices, so the algorithm never revisits or disturbs an already placed outer letter.
Before each outer iteration:

- all letter positions outside `[i,j]` already contain their correct reversed letters;
- every non-letter outside or inside the interval remains at its original index;
- unprocessed letters within the interval retain the order needed for the next outer pair.

Skipping non-letters preserves the invariant. Swapping the next outer letters fixes two more positions. When pointers meet or cross, no unresolved letter pair remains, so the whole list satisfies both output rules.

The input constraints use ASCII characters, so `isalpha()` recognizes exactly the uppercase and lowercase English letters that may appear. In broader Unicode text, `isalpha()` would also treat non-English alphabetic characters as letters, which would be a semantic difference from an English-only requirement.

Finally, `"".join(cs)` creates the required result string.

Notice that reversal preserves each character's case; it moves the entire character rather than converting it. An uppercase letter from the right therefore appears uppercase when moved to a left-side letter slot.

## Complexity detail

Let $n$ be the string length. Each pointer moves only inward and visits each position at most once.

- **Time complexity:** $O(n)$.
- **Space complexity:** $O(n)$ for the mutable character list and returned string.

Pointer variables use constant space. Python strings cannot be modified in place, so linear output construction is necessary.

## Alternatives and edge cases

- **Stack of letters:** Extract all letters, then scan original positions and pop replacements for letter slots. It is also $O(n)$ time and space but stores a separate letter collection.
- **Reverse extracted letters and rebuild:** This is clear and equivalent, with $O(n)$ extra storage.
- **Reverse the entire string:** It moves punctuation and digits, violating fixed positions.
- **Swap without skipping both sides:** A letter could exchange with a non-letter and move a fixed character.
- **No letters:** Both pointers only skip; the original string is returned unchanged.
- **All letters:** The method becomes ordinary in-place list reversal.
- **One letter:** It remains at its position.
- **Odd number of letters:** The central extracted letter remains unchanged.
- **Adjacent punctuation:** Inner loops skip any number of consecutive fixed characters.
- **Uppercase and lowercase:** Both are alphabetic and participate in the same reversal sequence; case stays attached to each character.
- **Digits and symbols:** They are non-alphabetic and remain fixed.
- **ASCII contract:** Makes Python `isalpha` behavior align with English-letter semantics.
- **Immutable input:** A list is required for swaps; joining produces a new string rather than altering `s`.
- **Pointers meet on punctuation:** No swap occurs, and that fixed character remains untouched.
- **Pointers meet on a letter:** It is the middle letter of the extracted sequence and correctly stays where it is.
