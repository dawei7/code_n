## General

**Read the final texts backward without constructing them**

A backspace affects the nearest still-present character to its left. When scanning forward, we usually need a stack to know which earlier character to delete. Scanning backward reverses the dependency: when we encounter `#`, it tells us how many ordinary characters farther left should be skipped.

The solution keeps one pointer and one pending-skip count for each input string. It repeatedly finds the next character that would survive in each final editor text and compares those characters.

**Pointer and skip meaning**

`i` and `j` start at the final indices of `s` and `t`.

`skip1` is the number of ordinary characters in `s` that must still be erased by backspaces already encountered to their right. `skip2` has the same meaning for `t`.

These counts begin at zero because no characters have been examined yet.

**Find the next surviving character in `s`**

While `i >= 0`:

- if `s[i] == '#'`, increment `skip1` and move left;
- otherwise, if `skip1 > 0`, this ordinary character is erased, so decrement `skip1` and move left;
- otherwise, stop: `s[i]` survives and is the next character of the final text when read backward.

Several consecutive backspaces simply increase the count. If there are more backspaces than earlier characters, the pointer reaches `-1` with some skip count possibly remaining; this correctly represents backspacing an empty editor, which keeps it empty.

The same logic independently finds the next surviving character in `t`.

**Compare the next survivors**

After both cleanup loops:

- if both pointers are valid, the two surviving characters must match; otherwise, the final texts differ;
- if exactly one pointer is valid, one final text has an extra character, so they differ;
- if neither is valid, both final texts are exhausted for this comparison stage.

When both valid characters match, the code decrements both pointers once to continue searching leftward.

The outer loop continues while either pointer is nonnegative. When both are below zero without a mismatch, every surviving character matched in reverse order, so the final texts are equal.

**Trace `"ab#c"` and `"ad#c"`**

Both pointers first find `c`, which matches.

Moving left reaches `#` in each string, raising each skip count to one. The next characters `b` and `d` are consumed by those skips rather than compared. The next survivors are `a` and `a`, which match. Both pointers then pass the beginning, and the function returns true.

**Trace excess backspaces**

For `"a##"`, scanning from the right sees two backspaces, so `skip1=2`. The `a` consumes one skip, and the pointer ends with no surviving character. The unused skip corresponds to a backspace applied while the editor is already empty and causes no error.

**Why reverse comparison is correct**

The inner loop skips exactly the characters removed in the forward editor process: every encountered backspace is paired with the closest not-yet-skipped ordinary character to its left, if one exists.

Therefore, each stopped pointer identifies the rightmost not-yet-compared character in the final text. Comparing those survivors one by one is equivalent to comparing the fully constructed final strings from right to left. A mismatch or unequal exhaustion is decisive; matching complete exhaustion proves equality.

More formally, before each outer comparison, everything originally to the right of each pointer has already been classified as either a processed backspace, a character erased by one of those backspaces, or a surviving character that matched its counterpart. The skip count records exactly the unmatched backspaces in that processed suffix. Moving left preserves this invariant: a new `#` adds one obligation, an ordinary character consumes an obligation when one exists, and the first ordinary character with no obligation is precisely the next visible editor character. This explains why backspaces never erase a character that should have survived and why no erased character reaches the comparison step.

## Complexity detail

Each pointer only moves left. Every character of `s` and `t` is examined at most once, so time is

$$
O(|s|+|t|).
$$

The algorithm stores two indices and two integer skip counts, using `O(1)` auxiliary space. It does not construct processed strings or stacks, satisfying the follow-up requirement.

Skip counts can grow to string length but remain single integer variables.

## Alternatives and edge cases

- **Build each final string with a stack:** Push letters and pop on backspaces, then compare. It is straightforward and linear-time but uses linear extra space.

- **Repeatedly remove `letter#` patterns:** Immutable-string rebuilding can be quadratic and is harder to reason about with consecutive backspaces.

- **Strings already equal without backspaces:** Every character becomes a survivor and compares normally.

- **Both final texts empty:** Both pointers exhaust, so the result is true.

- **Only one final text empty:** The unequal-pointer check returns false.

- **Backspace at the beginning:** It increments a skip count that has no earlier character to consume, correctly leaving the editor empty.

- **Many consecutive backspaces:** Their effects accumulate in the skip count.

- **A letter erased by a backspace:** It is skipped and never compared.

- **Matching raw strings with different edits:** Only surviving characters matter; raw positions need not correspond.

- **Survivor mismatch:** The function returns false immediately.

- **Length-one `"#"`:** Its final text is empty.

- **Input immutability:** Only pointer and counter variables change.
