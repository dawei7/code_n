## General

**Maximize at the first improvable position.** Read the decimal representation from left to right and find its first digit that is not `9`. Changing this digit to `9` improves the most significant position at which any increase is possible. No remapping of a later digit can compensate for choosing a smaller digit there. Replacing every occurrence of that selected digit with `9`, as the operation requires, can only increase the result further. If every digit is already `9`, remapping `9` to itself keeps the existing maximum.

**Minimize at the leading position.** A positive integer's first decimal digit is nonzero. Since leading zeroes are explicitly allowed after remapping, changing that leading digit to `0` creates the smallest possible most significant digit. Any remapping that leaves it nonzero must produce a larger value, regardless of later positions. Replacing all other occurrences of the same digit with `0` cannot increase the result, so this choice yields the minimum.

The maximum and minimum remappings are independent. Construct both transformed digit strings, convert them back to integers so leading zeroes disappear naturally, and subtract the minimum from the maximum.

## Complexity detail

Let $d$ be the number of decimal digits in `num`. Finding the first non-`9` digit and constructing the two remapped representations takes $O(d)$ time. The digit strings use $O(d)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate all remappings:** Trying all 100 source/destination digit pairs and selecting the extrema is correct, but it repeats the same digit scan many times and obscures the greedy reason only two transformations matter.
- **Arithmetic digit extraction:** The same choices can be applied with place values instead of strings, though the string representation expresses the all-occurrences rule more directly.
- **All nines:** No digit can increase the number, so the maximum is unchanged while replacing `9` with `0` makes the minimum zero.
- **Repeated selected digit:** Every occurrence must be replaced; replacing only the first occurrence violates the remapping operation.
- **Leading zeroes:** They are permitted, so the minimum always remaps the original leading digit to `0` without a special restriction.
- **One digit:** The largest value is $9$ and the smallest is $0$, so every one-digit input has difference $9$.
