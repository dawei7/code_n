## General

Convert the positive integer to its decimal string and count each character. The frequency table contains exactly the digits present in `n`; absent digits never enter it and therefore cannot incorrectly win with frequency zero.

Choose the table key that minimizes the ordered pair

$$
(\text{frequency of the digit},\ \text{digit value}).
$$

Pair ordering first selects the smallest occurrence count. Only when two counts are equal does it compare the digits, which implements the required smallest-digit tie break. Decimal characters `"0"` through `"9"` have the same ordering as their numeric values, so comparing the character key is sufficient before converting the winner back to an integer.

Every decimal position contributes once to the exact count of its digit. The final minimum considers every and only present digit and uses precisely the contract's two priorities. The returned key is therefore the required digit.

## Complexity detail

Let $d$ be the number of decimal digits in `n`. Conversion and counting take $O(d)$ time. Examining the distinct digit keys takes at most ten comparisons, so total time is $O(d)$. The frequency table has at most ten entries; because the decimal alphabet is fixed, auxiliary space is $O(1)$.

The legal 32-bit input domain has at most ten decimal digits. This range is too small for honest runtime scaling between one-pass counting and slower repeated digit counts. The package uses a bounded-domain certificate proving one count update per digit and at most ten candidate comparisons, with explicit one-digit and ten-digit boundary cases.

## Alternatives and edge cases

- **Repeated arithmetic extraction:** Repeatedly use modulo ten and integer division by ten; this also takes $O(d)$ time and avoids string conversion.
- **Count each possible digit separately:** Ten scans remain bounded here, but they repeat work and obscure the present-digit rule.
- **Absent digits:** Never allow a zero-frequency digit to become a candidate.
- **Single-digit input:** Its only digit is necessarily the answer.
- **All digits equal:** The repeated digit is the only candidate regardless of its frequency.
- **Several one-time digits:** Return the smallest numerical digit among them.
- **Digit zero:** Zero is a normal candidate when it occurs inside the positive integer.
- **Maximum input:** $2^{31}-1$ has ten digits, all handled by the same fixed-size table.
