## General

**Rotation changes both each digit and the digit order**

Rotating an entire decimal number by 180 degrees has two effects:

- Each digit changes according to the rotation map.
- The positions reverse: the original last digit becomes the rotated first digit.

Only five digits remain valid:

```text
0 becomes 0
1 becomes 1
6 becomes 9
8 becomes 8
9 becomes 6
```

Every occurrence of two, three, four, five, or seven makes the whole rotation invalid. A number is confusing only if every digit is valid and the resulting numeric value differs from the original value.

The solution performs the transformation arithmetically. It extracts original digits from right to left, rotates each extracted digit, and appends it to the right side of a new integer. Extracting from the right already supplies the reversal required by geometric rotation, so no separate string reversal is needed.

**Preserve the original number**

The first assignment is:

```python
x, y = n, 0
```

`x` is a working copy that will be shortened one decimal digit at a time. `y` is the rotated integer being constructed. The original `n` remains unchanged so the final result can be compared with it.

Starting `y` at zero also naturally handles leading zeros in the rotated representation. Appending a rotated zero to an integer currently equal to zero still gives zero. Integer arithmetic never stores leading zeros, exactly as the problem requires.

**Use a table indexed directly by each digit**

The rotation map is stored as a ten-element list:

```python
d = [0, 1, -1, -1, -1, -1, 9, -1, 8, 6]
```

The list index is the original digit, and the value is its rotated image. For example, `d[6]` is nine and `d[9]` is six.

The value minus one is a sentinel for an invalid digit. It cannot be confused with a legal rotated digit because all legal results lie between zero and nine.

An array is a convenient map here because every decimal digit is already a small integer in the fixed range zero through nine. Lookup takes constant time and needs no conditional chain.

**Extract the last digit and remove it in one operation**

The loop runs while the working copy is nonzero:

```python
while x:
    x, v = divmod(x, 10)
```

For a non-negative integer, `divmod(x, 10)` returns two values:

- The quotient after floor division by ten.
- The remainder after division by ten.

The remainder `v` is the current last decimal digit. The quotient becomes the new `x` with that last digit removed.

For example, if `x` is 689, `divmod(689, 10)` returns quotient 68 and remainder nine. On the next iteration it returns quotient six and remainder eight. The digits are therefore visited in the order nine, eight, six, which is the reverse of their written order.

**Reject an invalid digit immediately**

After extracting `v`, the code checks:

```python
if d[v] < 0:
    return False
```

If even one digit has no valid rotated image, the rotated number is invalid regardless of every other digit. No later work can repair that fact, so returning immediately is both correct and efficient.

This check occurs before the mapping value is appended. The minus-one sentinel can never enter `y`.

**Append the rotated digit**

For a valid digit, the update is:

```python
y = y * 10 + d[v]
```

Multiplying `y` by ten shifts all digits already constructed one decimal place to the left. Adding `d[v]` places the newly rotated digit in the empty units position.

Suppose `n` is 89:

- The first extracted digit is nine. It rotates to six, so `y` becomes six.
- The next extracted digit is eight. It rotates to eight, so `y` becomes `6 * 10 + 8 = 68`.

The geometric rotation of 89 is indeed 68.

For `n = 8000`, the extracted zeros each rotate to zero while `y` remains zero. Finally eight rotates to eight, and `y` becomes eight. This arithmetic result is the numeric interpretation of `0008`, so the required leading-zero rule is satisfied without a special case.

**Loop meaning and correctness**

After processing some number of iterations, `x` contains exactly the unprocessed prefix of the original number. At the same time, `y` is the correct rotation of the suffix already removed from `x`, in the order that suffix appears after a full 180-degree rotation.

Initially, no digits have been removed and `y` is zero, so this statement holds. One iteration extracts the rightmost remaining digit, verifies that it is rotatable, and appends its rotated image to `y`. Because that rightmost original digit is the next digit from the left in the rotated number, the statement remains true.

When `x` reaches zero, every original digit has been processed. If the loop has not returned false, all digits are valid, and `y` is exactly the rotated numeric value.

**Different valid value is the final requirement**

The final line is:

```python
return y != n
```

Validity alone is insufficient. Numbers such as 11 and 69 rotate to themselves, so they are not confusing. The inequality returns true only when the valid rotated value changes the number.

The input zero deserves attention. Because `x` begins at zero, the loop does not execute. `y` also equals zero, so `y != n` is false. This is correct: zero rotates validly to zero but does not become a different number.

## Complexity detail

Let `D` be the number of decimal digits in `n`, treating zero as one digit.

Every loop iteration removes exactly one digit from `x`. Each iteration performs one division with remainder, one table lookup, and a constant number of arithmetic operations. Under the standard fixed-width integer model used for this constraint, the total time is `O(D)`.

The mapping list always contains exactly ten entries, independent of `n`. The solution also stores only `x`, `y`, and `v`. Its auxiliary-space complexity is therefore `O(1)` under the standard model, matching the manifest.

In a bit-complexity model for arbitrary-precision integers, arithmetic cost and the storage for `x` and `y` grow with the number of bits. The problem bounds `n` by `10^9`, so those integers fit within a fixed finite word range for this task. The conventional interview analysis consequently treats their operations and storage as constant per digit.

The solution does not allocate a string proportional to the number of digits and does not use recursion.

## Alternatives and edge cases

- **String transformation:** Convert `n` to text, map each character, reverse the mapped characters, parse the result, and compare it with `n`. This is straightforward but uses `O(D)` auxiliary space for the transformed representation.
- **Dictionary mapping:** A dictionary from valid digits to rotated digits expresses the same rule. The fixed ten-entry list is simpler and guarantees direct constant-time indexing.
- **Large conditional chain:** Separate cases for zero, one, six, eight, and nine can avoid a table, but they are more verbose and easier to implement inconsistently.
- **Zero:** The loop is skipped and zero is compared with zero, correctly returning false.
- **Single six or nine:** Six becomes nine and nine becomes six, so either input is valid and confusing.
- **Single zero, one, or eight:** Each rotates to itself, so the result is valid but not confusing.
- **Any invalid digit:** Encountering two, three, four, five, or seven returns false immediately, even if all remaining digits would be valid.
- **Rotationally symmetric multi-digit number:** Values such as 11, 69, 88, and 96 remain equal after rotation and therefore return false.
- **Leading zeros after rotation:** Trailing zeros in the original number become leading zeros after rotation. Integer construction drops them naturally, as required.
- **Original leading zeros:** An integer input has no represented leading zeros, so there is nothing additional to preserve.
- **Upper bound:** The largest legal input still has only ten decimal digits at most under the stated bound, and the same loop handles it without a separate case.
- **Input preservation:** `x` is reduced destructively, but `n` is never changed. The final comparison therefore uses the true original value.
