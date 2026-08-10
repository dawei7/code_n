## General

**Recreate elementary addition one decimal column at a time**

The inputs may contain up to $10^4$ digits, so converting an entire string to a built-in integer is both forbidden and contrary to the purpose of the problem. The optimal method performs the same right-to-left addition taught on paper.

Decimal place values align at the right edge. The final character of each string is the ones digit, the preceding character is the tens digit, and so on. The pointers

`i = len(num1) - 1` and `j = len(num2) - 1`

therefore begin at corresponding least-significant digits. Moving both pointers left after each iteration advances to the next place value.

The result digits are discovered from least significant to most significant. They are appended to `ans` in that convenient discovery order and reversed only once at the end.

**Treat a missing digit as zero**

The two strings need not have equal lengths. While pointer `i` remains valid, `a = int(num1[i])`; once it becomes negative, `a = 0`. The same rule produces `b` from `num2` and pointer `j`.

Converting one character such as `'7'` to the small integer `7` is not converting the input number as a whole. It is exactly the per-digit interpretation required for manual arithmetic. A missing higher place in the shorter input contributes zero, just as writing leading zeros for alignment would do, but the algorithm does not actually allocate padded strings.

**Separate the current digit from the carry**

The variable `c` is the carry entering the current column. Initially it is zero. For digit values `a` and `b`, the column total is `a + b + c`.

The line

`c, v = divmod(a + b + c, 10)`

computes quotient and remainder when that total is divided by ten. The remainder `v` is the output digit for the current place, because it lies from `0` through `9`. The quotient becomes the carry into the next column.

The maximum total is `9 + 9 + 1 = 19`, so the new carry is always either zero or one. For example, adding digits `8` and `7` with incoming carry `1` gives `16`; `divmod(16, 10)` returns `(1, 6)`. The algorithm appends `'6'` now and carries `1` leftward.

The digit is converted back to text with `str(v)` before being appended. As a result, `ans` is a list of string pieces ready for the final join.

**Why the loop condition includes the carry**

The loop continues while `i >= 0 or j >= 0 or c`. The first two conditions ensure every input digit is processed. The final condition handles an overflow beyond both most-significant digits.

For `"999" + "1"`, the three ordinary columns each produce a zero and propagate a carry. After both pointers become negative, `c` is still `1`, so one extra iteration uses `a = 0` and `b = 0`, emits the leading `1`, and clears the carry. Without `or c`, the result would incorrectly lose that new digit.

When no final carry remains, the loop stops immediately after the last input column. This also handles `"0" + "0"`: the first iteration appends one zero, both pointers then expire, and the result is not accidentally empty.

**A complete trace**

For `num1 = "456"` and `num2 = "77"`:

1. Ones column: `6 + 7 + 0 = 13`, so append `'3'` and carry `1`.
2. Tens column: `5 + 7 + 1 = 13`, so append `'3'` and keep carry `1`.
3. Hundreds column: `4 + 0 + 1 = 5`, so append `'5'` and clear the carry.

At this point `ans` is `['3','3','5']`, which is intentionally reversed. The expression `ans[::-1]` gives `['5','3','3']`, and `"".join(...)` returns `"533"`.

**The loop invariant and correctness**

Before each iteration, `ans` contains the correct result digits for every less-significant column already processed, stored in reverse order, and `c` is exactly the carry from those columns into the next one.

The next iteration reads the two digits at the same place value, substituting zero when an input has no digit there. Quotient and remainder division by ten is precisely the base-10 rule that determines the current output digit and next carry. Thus appending `v` and replacing `c` preserves the invariant.

When the loop ends, both inputs are exhausted and no carry remains. Every place value of the mathematical sum has therefore been produced. Reversing restores most-significant-first notation. Since normalized nonnegative inputs never require sign handling or removal of artificial leading zeros, the joined string is the normalized sum.

**About the additional `subStrings` method**

The class also contains a separate `subStrings` method, but `addStrings` never calls it and the problem contract asks only for addition. It does not participate in the execution path or complexity of this solution. The optimal approach described here is the exact `addStrings` digit-and-carry method used for the requested operation.

## Complexity detail

Let $m = \lvert\texttt{num1}\rvert$ and $n = \lvert\texttt{num2}\rvert$. The loop processes one decimal column per iteration and may run once more for a final carry. It therefore executes at most $\max(m,n)+1$ times, giving $O(\max(m,n))$ time. Reversing the digit list and joining it also take linear time in the output length, so the bound is unchanged.

The `ans` list and returned string contain at most $\max(m,n)+1$ digits. Required construction space is therefore $O(\max(m,n))$. Aside from the output representation, the two pointers, two current digits, carry, and current result digit use $O(1)$ auxiliary state.

Building a mutable list is important in Python. Repeatedly prepending to an immutable string could copy an ever-growing prefix on every iteration and degrade to quadratic time. Appending in reverse and performing one final reversal preserves the linear bound.

## Alternatives and edge cases

- **Convert both full strings to integers:** This violates the explicit contract and may rely on arbitrary-precision library behavior the exercise asks the solution to implement.
- **Prepend each new digit to a string:** It mirrors written order but is inefficient with immutable strings because every prepend can copy the accumulated result. A list plus one reversal is linear.
- **Pad the shorter input with leading zeros:** This can simplify indexing and still be correct, but it allocates extra strings unnecessarily. Conditional zero digits provide the same alignment in constant auxiliary state beyond the result.
- **Use character-code subtraction instead of `int` per digit:** `ord(ch) - ord('0')` is equivalent and avoids the digit conversion helper. Both respect the prohibition on converting the complete input.
- **Different input lengths:** Once one pointer is negative, its digit is zero while the other number continues normally.
- **Final carry:** Sums such as `"9" + "1"` need an additional most-significant digit. Including `c` in the loop condition produces it.
- **No final carry:** The loop stops after the last real column and adds no spurious leading zero.
- **Both inputs equal zero:** One column produces `'0'`, and the normalized result is exactly `"0"`.
- **Long chains of carries:** Inputs such as `"9999" + "1"` propagate `c = 1` across every column; the invariant handles each independently.
- **Normalized input guarantee:** Except for `"0"`, inputs have no leading zeros. The algorithm would still compute the numeric sum if leading zeros were present, but normalization of the returned representation relies on the stated contract.
- **Maximum-length inputs:** Work and storage grow linearly with the number of digits; no recursion or whole-number conversion risks numeric overflow.
