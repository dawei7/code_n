## General

**Separate validity from actually changing**

A good number must satisfy two conditions:

1. every digit must remain a valid digit after rotation;
2. the complete rotated number must differ from the original.

The valid digit mappings are:

- `0 -> 0`, `1 -> 1`, and `8 -> 8`;
- `2 -> 5` and `5 -> 2`;
- `6 -> 9` and `9 -> 6`.

Digits three, four, and seven are invalid under rotation.

A number containing only zero, one, and eight is valid but unchanged, so it is not good. A valid number containing at least one of two, five, six, or nine changes and is good.

The exact solution verifies these rules by explicitly constructing each rotated value.

**Encode the mapping in a direct lookup table**

List `d` is indexed by an original digit:

`[0, 1, 5, -1, -1, 2, 9, -1, 8, 6]`.

For example, `d[2] == 5` and `d[6] == 9`. The sentinel `-1` marks invalid digits. A ten-entry array turns every digit classification and transformation into one constant-time lookup.

**Inspect one integer digit by digit**

Function `check(x)` copies `x` to temporary variable `t`. It repeatedly takes:

`v = t % 10`

to obtain the least significant remaining digit, and then removes that digit with:

`t //= 10`.

Because every tested `x` is at least one, the loop executes at least once. It ends after every decimal digit has been processed.

If `d[v] == -1`, rotation is invalid. One invalid digit is enough to invalidate the whole number because every digit must be rotated, so `check` returns false immediately.

**Rebuild the rotated value in the same digit positions**

Variable `k` is the current decimal place value: one for units, ten for tens, one hundred for hundreds, and so on.

After mapping digit `v`, the update:

`y = d[v] * k + y`

places the rotated digit back into the same decimal position. Then `k *= 10` advances to the next place.

This is important because the operation rotates each digit individually; the implementation does not reverse the order of digit positions. For example, `126` maps by position to `159`:

- units `6` becomes `9`;
- tens `2` becomes `5`;
- hundreds `1` remains `1`.

The accumulated value is therefore 159.

**Leading zeros after rotation are naturally harmless**

A high-order zero remains zero. In integer form, such a zero does not contribute to `y`, just as ordinary integer notation does not preserve leading zeros.

The comparison still captures whether any effective digit changed. Under the input's usual decimal representation there is no leading zero before rotation, and zero itself maps to zero wherever it occurs inside the number.

For example, 10 rotates to 10 and is unchanged. The units zero contributes zero at place one, and the tens one contributes ten.

**Decide goodness by comparing complete values**

After all digits are valid and mapped, `check` returns `x != y`.

If every digit was from `{0,1,8}`, each mapped digit equals its original and therefore `y == x`. The number is valid but not good.

If at least one digit was from `{2,5,6,9}`, that digit maps to a different value in the same position. Since decimal place representation is unique and other positions cannot cancel that change, the final integer differs. The number is good.

The explicit comparison therefore combines the required “valid and changed” logic correctly.

**Count the entire requested range**

The generator evaluates `check(i)` for every integer `i` from one through `n`. In Python, booleans behave as integers in arithmetic: `True` contributes one and `False` contributes zero.

Thus:

`sum(check(i) for i in range(1, n + 1))`

counts exactly how many tested integers are good without storing a list of all Boolean results or all good numbers.

**Trace the range through ten**

From one through ten:

- one is valid but unchanged;
- two becomes five and is good;
- three and four are invalid;
- five becomes two and is good;
- six becomes nine and is good;
- seven is invalid;
- eight is valid but unchanged;
- nine becomes six and is good;
- ten remains ten and is unchanged.

Exactly four values—two, five, six, and nine—contribute true, so the result is four.


During the loop, `y` contains precisely the mapped versions of all decimal positions already removed from `t`. If an invalid digit appears, the number cannot satisfy the definition and false is correct.

If the loop finishes, every digit has a defined rotation and the invariant shows that `y` is the complete rotated value. The final inequality is exactly the remaining requirement that rotation change the number. Hence `check(x)` is true if and only if `x` is good.

The outer sum calls this correct predicate once for every integer in the inclusive range and no value outside it, so the returned count is correct.

## Complexity detail

Checking an integer `i` processes $\Theta(\log i)$ decimal digits. The exact implementation checks every integer from one to `n`, so its total time is:

$$
\Theta\left(\sum_{i=1}^{n}\log i\right)
=
\Theta(n\log n).
$$

The mapping table has fixed length ten. The generator, digit variables, and accumulator use constant auxiliary storage, so the exact implementation's auxiliary space is $O(1)$.

The current manifest lists $O(\log n)$ time and $O(\log n)$ space. Those bounds do not describe this enumeration source: even before inspecting digits, it invokes `check` exactly `n` times. A digit-DP solution can count by decimal prefix in roughly logarithmic digit depth, but this file does not implement digit DP. The approach records the source's actual behavior rather than assigning an alternative algorithm's complexity to it.

## Alternatives and edge cases

- **Digit dynamic programming:** Count valid and changed prefixes up to `n` without testing every integer. This is the appropriate route for a genuine complexity based mainly on the number of digits.

- **Validity and change sets:** While scanning a number, reject digits outside `{0,1,2,5,6,8,9}` and remember whether any digit belongs to `{2,5,6,9}`. This avoids constructing `y` but keeps the same enumeration cost.

- **Convert to a string:** Character-set tests are readable but allocate a decimal string for every integer.

- **Only unchanged valid digits:** Numbers composed solely of zero, one, and eight must not be counted.

- **One invalid digit:** Three, four, or seven anywhere makes the entire number invalid.

- **Internal zero:** It rotates to zero in the same place and needs no special handling.

- **Lower bound:** For `n = 1`, the only candidate is unchanged, so the count is zero.

- **Boolean summation:** It counts results without materializing an intermediate list.

- **ASCII or visual reversal assumptions:** The implemented rule maps decimal digits in place; it does not reverse their order.
