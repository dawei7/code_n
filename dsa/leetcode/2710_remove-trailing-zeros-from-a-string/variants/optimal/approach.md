## General

**Trailing means one maximal suffix**

A trailing zero is a `"0"` occurring at the very end of the decimal string, or immediately before only other trailing zeros.

The required result removes the maximal suffix consisting entirely of zero characters.

Zeros before the final nonzero digit are internal and must remain. For `"51230100"`, the two final zeros are removed while the zero between 3 and 1 stays.

**Use `rstrip` with the zero-character set**

Python `num.rstrip("0")` scans from the right and removes characters while they belong to the supplied character set.

Because the argument contains only `"0"`, the scan stops at the first character that is not zero.

It returns the untouched prefix ending at that character.

**The argument is not a substring pattern**

`rstrip(chars)` treats `chars` as a set of removable individual characters, not as one suffix word.

Here that distinction causes no complication because the set has exactly one member. Every removed character is a zero, and no other digit qualifies.

Passing a broader string such as `"01"` would incorrectly remove both zeros and ones from the end.

**Trace a number with trailing zeros**

For `"51230100"`, the scan examines:

- final zero, remove;
- preceding zero, remove;
- preceding one, stop.

The returned prefix is `"512301"`.

The internal zero remains because scanning stops as soon as it reaches the one.

**Trace a number without trailing zeros**

For `"123"`, the final character is three and does not belong to `"0"`.

No character is stripped, so the returned string has the same contents as the input.

There is no need to search for a zero elsewhere because only the suffix matters.

**Why leading zeros are irrelevant**

The input has no leading zeros. Even if a zero appeared at the beginning of a longer string outside the contract, `rstrip` would not remove it unless every character to its right were also removable zeros.

The operation direction is fixed at the right end and never calls `lstrip` or `strip`.

**Why the result remains a valid positive integer representation**

The input represents a positive integer and has no leading zeros, so it contains at least one nonzero digit.

Removing only a zero suffix cannot remove that nonzero digit. The result is therefore nonempty and still has no leading zeros.

The method does not need to parse the number, which avoids numeric-size limits for strings up to length 1000.

**String processing is preferable to integer conversion**

One alternative is to convert the text to an integer, repeatedly divide by ten, then convert back.

That performs arithmetic on a potentially very large integer and introduces unnecessary representation changes. The desired transformation is purely textual and depends only on suffix characters.

`rstrip` expresses it directly.

**Maximality of the removed suffix**

Every removed position is a zero at the end after later zeros have been removed.

The first retained final character is nonzero, so no additional trailing zero remains. At the same time, removing that nonzero character would violate the requirement.

Thus the operation removes exactly the maximal trailing-zero suffix, neither less nor more.

**Input preservation**

Python strings are immutable. `rstrip` returns a string result and does not modify `num`.

An implementation detail may reuse the same string object when no removal occurs, but callers should rely only on equal contents, not identity.

**Why one library call is still an algorithm**

The library method performs the same right-to-left scan a manual loop would implement.

Its concise form reduces off-by-one risks such as slicing one character too far or failing when the string has no trailing zero.

The constraints guarantee the exact character class, so no validation branch is needed.


By `rstrip("0")` semantics, the method removes consecutive zero characters beginning at the final position until either a nonzero character is reached or the string ends.

The positive-input guarantee ensures a nonzero character is reached. All and only zeros after that last nonzero digit are removed, which is precisely the requested output.

**Why scanning from the left would be less direct**

A left-to-right scan could remember the last nonzero position and slice afterward. That is correct but examines every character even when there are only a few trailing zeros.

A right-to-left suffix scan stops at the first nonzero, though its worst case remains linear.

## Complexity detail

For a string of length $n$, `rstrip` may inspect $O(n)$ characters in the worst case and must produce a result of up to length $n$. Time is $O(n)$.

The returned string can require $O(n)$ space because strings are immutable. Apart from that output, the operation uses $O(1)$ conceptual scanning state.

## Alternatives and edge cases

- **Manual right pointer:** Decrement while `num[i] == "0"` and return the prefix; same $O(n)$ bound.
- **Remember last nonzero during a forward scan:** Correct but always traverses the whole input.
- **Convert to integer and divide by ten:** Unnecessary and potentially expensive for a 1000-digit value.
- **Use `strip("0")`:** Incorrect because it also removes leading zeros from both ends.
- **Use `lstrip("0")`:** Removes the wrong end.
- **No trailing zero:** Return unchanged contents.
- **One trailing zero:** Remove exactly one character.
- **Many trailing zeros:** Remove the complete suffix.
- **Internal zeros:** Always preserved.
- **Input ending in nonzero:** The scan stops immediately.
- **Positive-number guarantee:** Ensures the result is not empty.
- **No leading zeros:** The retained prefix remains canonical decimal text.
