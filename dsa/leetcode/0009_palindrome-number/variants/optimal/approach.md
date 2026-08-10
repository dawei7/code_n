## General

**Compare two numeric halves instead of converting to text**

A decimal palindrome has mirrored digits. For an even number of digits, its left half equals the reversal of its right half. For an odd number of digits, the same statement holds after ignoring the single middle digit, because that digit mirrors only itself.

For example:

```text
1221  -> left 12, right 21, reverse(right) = 12
12321 -> left 12, middle 3, right 21, reverse(right) = 12
```

The method repeatedly removes the last digit from `x` and appends it to `y`. It stops after roughly half the digits have moved. At that point, `x` is the unprocessed left part and `y` is the reversed right part.

Reversing only half has two advantages:

- it avoids creating a string or digit array;
- it avoids the overflow risk of reversing all digits in a fixed-width integer.

**Reject signs and impossible trailing-zero shapes first**

The guard is

```python
if x < 0 or (x and x % 10 == 0):
    return False
```

Every negative number is rejected. In the normal written representation, the minus sign appears only at the left. Reversing the complete representation would put it on the right, so a negative integer cannot read the same in both directions.

The second condition rejects a nonzero number ending in zero. For such a number to be palindromic, it would also need to begin with zero. Standard integer notation has no leading zeros, so that is impossible. The expression `x and ...` deliberately excludes zero itself: `0` is a one-digit palindrome and must return `True`.

This trailing-zero guard is also operationally important. Reversing integer digits discards leading zeros. Without the guard, `10` could be reduced to states that make the odd-length comparison accidentally accept it.

**Move one low-order digit per iteration**

The state starts with `y = 0`. One transfer is

```python
y = y * 10 + x % 10
x //= 10
```

`x % 10` extracts the current last digit. Multiplying `y` by ten opens a new ones position, and adding the digit appends it. Floor division removes that digit from the nonnegative `x`.

After `t` iterations:

- `x` is the original number with its last `t` digits removed;
- `y` is those removed digits in reverse order.

Only nonnegative values reach this loop, so Python's `%` and `//` have the familiar last-digit behavior.

**Why `y < x` identifies the halfway point**

Each iteration makes `x` about ten times smaller and `y` about ten times larger. Initially `y = 0`, so the unprocessed side is larger. Once `y` is no longer smaller than `x`, at least half the decimal digits have moved.

The loop is

```python
while y < x:
```

For an even number of digits, a palindrome reaches equality exactly after half its digits move. With `1221`:

| Step | Remaining `x` | Reversed suffix `y` |
|---:|---:|---:|
| Start | `1221` | `0` |
| 1 | `122` | `1` |
| 2 | `12` | `12` |

Now `y < x` is false and `x == y` proves the two halves match.

For an odd number of digits, `y` ends with one extra digit: the original middle digit. With `12321`:

| Step | Remaining `x` | Reversed suffix `y` |
|---:|---:|---:|
| Start | `12321` | `0` |
| 1 | `1232` | `1` |
| 2 | `123` | `12` |
| 3 | `12` | `123` |

The extra `3` is now the ones digit of `y`. Integer division `y // 10` removes it, leaving `12` for comparison with `x`.

**The two final comparisons cover both parities**

The return expression is

```python
return x in (y, y // 10)
```

It is equivalent to

```python
return x == y or x == y // 10
```

- `x == y` accepts an even-length palindrome.
- `x == y // 10` accepts an odd-length palindrome after dropping the middle digit.

For a non-palindrome, the two numeric halves disagree when the loop crosses the halfway point, so neither comparison succeeds.

**Why no palindrome is rejected and no non-palindrome is accepted**

Moving digits preserves their exact decimal order in two complementary forms: `x` retains the left prefix, while `y` reverses the removed right suffix. A palindrome's mirrored halves must therefore meet one of the two final equalities, depending only on whether a middle digit exists.

Conversely, if either equality holds, every digit in the retained left half equals its mirrored digit from the original right half. In the `y // 10` case, the discarded digit is the single center and imposes no cross-position requirement. Combined with the initial rejection of negative signs and unmatched trailing zeros, the original representation must read identically in both directions.

Zero takes no loop iterations and returns `0 in (0, 0)`, which is true.

## Complexity detail

Let $d$ be the number of decimal digits in positive `x`.

- **Time complexity: $O(d) = O(\log x)$.** Each iteration removes one digit, and only about half the digits are processed before `y >= x`. Halving the number of iterations changes a constant factor, not the asymptotic logarithmic bound. Zero and rejected inputs finish in constant time.
- **Space complexity: $O(1)$.** The method stores only `x` and `y` plus constant-sized arithmetic temporaries. It creates no string, array, and no recursion stack.

Because only about half the digits are reversed, `y` remains far smaller than a full reversal. For a signed 32-bit input, it cannot approach the overflow size that motivates avoiding the complete reverse.

## Alternatives and edge cases

- **Reverse the full integer:** Compare the complete reversal with the original. This is simple and still $O(\log x)$ time, but a full reverse can exceed a fixed-width signed range even when the input fits. The half-reversal avoids that risk.
- **Convert to a string:** Compare the text with its reverse or use two character pointers. It is concise but uses $O(d)$ string storage and does not satisfy the arithmetic follow-up.
- **Compare leading and trailing digits:** Repeatedly derive the highest power of ten, compare both ends, and remove them. This can use constant space but requires careful divisor updates and can be more error-prone around zeros.
- **Negative input:** Always returns false because the sign has no matching symbol at the other end.
- **Zero:** Bypasses the trailing-zero rejection, skips the loop, and returns true.
- **Nonzero value ending in zero:** Returns false immediately because an integer cannot have the matching leading zero.
- **One positive digit:** One transfer may occur, after which `x == y // 10`; every single digit is correctly accepted.
- **Even number of digits:** Acceptance uses `x == y` after exactly half the digits move.
- **Odd number of digits:** Acceptance uses `x == y // 10` after `y` receives the center digit.
- **Repeated zeros inside the number:** Internal zeros are ordinary decimal positions and are preserved by multiplication and remainder operations.
- **Local mutation only:** The parameter variable `x` shrinks, but integers are immutable values and the caller's value is unaffected.
