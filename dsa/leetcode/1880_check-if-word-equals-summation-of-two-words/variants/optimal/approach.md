## General

**Each permitted letter is exactly one decimal digit.** The strings contain only letters from `'a'` through `'j'`. Subtracting the character code of `'a'` maps them to `0` through `9`: `'a' -> 0`, `'b' -> 1`, and `'j' -> 9`. The upper bound at `'j'` is essential. If letters could map to values above nine, simply treating every value as one base-ten digit would no longer match concatenation.

**Build the numerical value from left to right.** Helper `f(s)` starts `ans` at zero. For each mapped digit `x`, the update `ans = ans * 10 + x` shifts the value already constructed one decimal place to the left and puts `x` into the newly opened units place. After reading digits `d_0, d_1, ..., d_i`, the accumulator equals the integer represented by their concatenation. This is the same operation people use when reading a decimal number one digit at a time.

For example, `acb` maps to digits `0, 2, 1`. The accumulator progresses as `0`, then `0 * 10 + 2 = 2`, then `2 * 10 + 1 = 21`. The conceptual digit string is `"021"`, and its integer value is `21`. Leading zeros need no explicit removal because integer arithmetic naturally gives them no positional contribution while still shifting correctly for later digits.

**Map characters without creating a digit string.** The helper stores `a = ord("a")` once. `map(ord, s)` lazily supplies the numeric code of each character, and `x = c - a` converts that code to the required letter value. This avoids building an intermediate list of codes, an intermediate string of decimal characters, and then parsing that string. Only the running integer and current code are needed.

**Evaluate all three words by the same definition.** The return expression computes `f(firstWord) + f(secondWord) == f(targetWord)`. Using one helper for all three prevents subtle inconsistencies such as treating leading `a` letters differently in one position. Python evaluates both addends and the target value, then compares the two integers. The method returns the Boolean comparison result directly.

**Why the accumulator formula is correct.** Before reading the next character, suppose `ans` equals the numerical value of the already-read letter-value sequence. Appending a new decimal digit `x` to that sequence multiplies the old value by ten and adds `x`. Therefore the update preserves the intended value after one more character. The initial empty prefix has value zero, so induction proves that `f(s)` equals the numerical value of the entire word.

Once each helper result is correct, the final equality has exactly the problem's meaning: it is true precisely when the first numerical value plus the second numerical value equals the target numerical value. There are no alternative rearrangements or choices, so direct conversion and comparison completely solve the task.

**Trace all-zero mappings.** For `firstWord = "aaa"`, every iteration applies `ans = ans * 10 + 0`, leaving zero. `secondWord = "a"` also becomes zero. Target `"aaaa"` likewise becomes zero, so the comparison returns true even though the words have different lengths. This is correct because the task compares integer numerical values, not digit-string representations. In contrast, target `"aab"` becomes one, so zero plus zero does not match.

**Why ordinary integer conversion is not applied to the original word.** The letters themselves are not decimal text, so `int(s)` would be invalid. The conversion must first use alphabet positions. Conversely, after that mapping, a custom arbitrary-precision decimal-string addition is unnecessary because word lengths are at most eight and Python integers safely hold the resulting values and their sum.

## Complexity detail

Let $S$ be the total number of characters across `firstWord`, `secondWord`, and `targetWord`. Each character is visited exactly once and performs one character-code subtraction, multiplication by ten, and addition. Under the stated maximum word length of eight, these integers have bounded size, so each operation is constant time and total time is $O(S)$.

The helper retains only `ans`, the code for `'a'`, and the current mapped character. `map` is lazy, so no collection proportional to a word's length is created. Auxiliary space is $O(1)$. The three helper calls run sequentially as part of the expression and return integers; they do not retain per-character histories.

The largest word maps to at most eight decimal digits, so an individual numerical value is at most `99,999,999` and the sum of two is at most `199,999,998`. Python has no overflow issue. In a fixed-width language, a signed 32-bit integer is still sufficient for these exact constraints.

If the word-length bound were removed, arithmetic on an ever-growing integer would no longer be constant time in a bit-complexity model. The stated $O(S)$ analysis is appropriate for the bounded eight-digit contract and for the conventional unit-cost integer model used here.

## Alternatives and edge cases

- **Create a mapped digit string and parse it:** Joining `str(ord(c) - ord('a'))` for all letters and calling `int` matches the definition, but allocates intermediate strings and needs care if the mapped text is empty. The running accumulator is simpler and constant-space.
- **Dictionary lookup:** A mapping from each letter to its digit would work, but the values are consecutive character-code offsets, so a table adds unnecessary storage and setup.
- **Leading `a` letters:** They represent leading zero digits and vanish in the integer value. Words such as `aab` and `b` both evaluate to one, which is intentional.
- **All letters `a`:** Any nonempty all-`a` word evaluates to zero regardless of length. Equality is numeric, not textual.
- **Letter `j`:** It maps to digit nine, confirming that every mapped value remains a single decimal digit. This is the largest supported letter.
- **Different word lengths:** Lengths do not need to match. Each complete word is converted independently before addition.
- **Case sensitivity and alphabet range:** The code assumes lowercase consecutive letters beginning at `'a'`. Uppercase or letters after `'j'` would violate the contract and would not preserve the intended one-digit mapping.
- **Boolean result:** The equality expression already returns Python `True` or `False`. Wrapping it in another conditional would add no behavior.
