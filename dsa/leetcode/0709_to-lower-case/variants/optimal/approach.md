## General

The task changes only uppercase English letters. Lowercase letters, digits, punctuation, and every other printable ASCII character must remain exactly as they are.

The solution processes each character independently, converts uppercase characters through their ASCII code, collects the resulting characters, and joins them into one new string.

**The relevant ASCII relationship**

In ASCII, corresponding uppercase and lowercase English letters differ by `32`:

$$
\operatorname{ord}(\texttt{'a'})
=
\operatorname{ord}(\texttt{'A'})+32.
$$

The same relation holds from `A/a` through `Z/z`.

In binary, the uppercase and lowercase codes differ in the bit whose value is `32 = 2^5`. That bit is zero for an uppercase code and one for its lowercase partner.

For example:

- `'A'` is decimal `65`, binary `1000001`;
- `'a'` is decimal `97`, binary `1100001`.

Setting the value-32 bit changes `65` to `97`.

**Why bitwise OR performs the conversion**

For an uppercase character `c`, the expression:

`ord(c) | 32`

sets the `32` bit to one while leaving every other bit unchanged. `chr(...)` then converts the resulting integer code back into a character.

Thus:

`chr(ord(c) | 32)`

is the lowercase partner of an ASCII uppercase letter.

This is not a general conversion that should be applied blindly to every printable character. Setting bit 32 can change punctuation into unrelated symbols. The uppercase test is what makes the operation safe.

**Guarding the bit operation**

The conditional expression is:

`chr(ord(c) | 32) if c.isupper() else c`.

Because the input contains only printable ASCII, `c.isupper()` is true exactly for `A` through `Z`. Those are the characters for which the bit relationship is intended.

If the character is lowercase, a digit, a space, or punctuation, the `else` branch returns the original character unchanged.

For lowercase ASCII letters, OR with 32 would happen to leave the code unchanged because that bit is already one, but guarding still expresses the contract accurately and protects nonletters.

**Building a new string**

Python strings are immutable. The algorithm cannot replace characters inside `s` in place.

The list comprehension produces one output character for each input character, in the same order. `"".join(...)` concatenates that list into the final string without inserting separators.

The exact expression uses square brackets, so it constructs a complete temporary list before joining. A generator expression could avoid that list container, but the returned string itself would still require linear storage.

**A character-by-character trace**

For `s = "Hello!"`:

- `'H'` is uppercase. Its code `72` OR `32` becomes `104`, which is `'h'`.
- `'e'` is not uppercase, so it remains `'e'`.
- Both `'l'` characters remain unchanged.
- `'o'` remains unchanged.
- `'!'` is punctuation and remains `'!'`.

Joining the results gives `"hello!"`.

For `"LOVELY"`, every character takes the conversion branch. For `"here"`, none do, but a new equal string is still produced by `join`.

**Why character order and length are preserved**

The comprehension emits exactly one character for every input character. Uppercase conversion maps one ASCII character to one lowercase character. No character is inserted, removed, split, or reordered.

Therefore, output length equals input length, and the character at every position is either the required lowercase replacement or the untouched original.

**Why the algorithm is correct**

Consider any input position.

If its character is uppercase, `isupper` selects the conversion branch, and the ASCII bit relation produces precisely its lowercase counterpart.

If it is not uppercase, the specification says it should not be replaced, and the else branch preserves it.

These are all possible printable ASCII characters. Since each position is handled correctly and order is preserved, the complete joined string is exactly the requested result.

## Complexity detail

Let `n = len(s)`.

The comprehension examines `n` characters, and every uppercase test, code conversion, and bit operation is constant time for ASCII. Joining `n` one-character strings also takes `O(n)` time. Total time is

$$
O(n).
$$

The temporary list contains `n` character references, and the output string contains `n` characters. Auxiliary/output construction space is

$$
O(n).
$$

Python's immutable-string model prevents an in-place `O(1)`-space result.

## Alternatives and edge cases

- **Built-in `s.lower()`:** It is concise and correct for the input, but using the ASCII relationship demonstrates the requested conversion mechanics.

- **Add 32 arithmetically:** `chr(ord(c) + 32)` works for guarded ASCII uppercase letters. Bitwise OR makes the specific differing bit explicit.

- **Dictionary mapping:** Map every uppercase letter to its lowercase partner. It remains linear but stores a fixed mapping.

- **Already lowercase input:** Every character follows the else branch and remains unchanged.

- **All uppercase input:** Every character is converted.

- **Digits and punctuation:** `isupper` is false, preventing unsafe bit modification.

- **Spaces:** They are printable ASCII and remain spaces.

- **Input length one:** Exactly one character is converted or preserved.

- **ASCII-only guarantee:** Outside ASCII, `isupper` recognizes additional Unicode uppercase characters for which OR 32 is not a valid lowercase conversion. The source restriction is essential.

- **Immutability:** The method returns a new string; it does not alter the caller's original string.

- **Square brackets in the comprehension:** They intentionally create a list. Replacing them with a generator can reduce temporary container space but not output space.
