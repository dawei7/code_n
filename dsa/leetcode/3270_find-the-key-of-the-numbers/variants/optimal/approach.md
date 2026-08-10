## General

The key is formed independently at four decimal places. Missing leading digits behave as zeros. Integer division and remainder extract exactly those padded digits without converting the inputs to strings.

Variable `k` is the current place value: one, ten, one hundred, then one thousand. For any number `num`, expression

`num // k % 10`

removes all lower places through integer division and then isolates the current digit with remainder ten. If the number has no digit that high, integer division yields zero, automatically modeling leading-zero padding.

At each of four iterations, `x` is the minimum current-place digit among the three inputs. `ans += x * k` places that digit at the same decimal position in the result. Then `k *= 10` advances to the next place.

The loop processes places from right to left, while the statement may describe digits from left to right. The order does not matter because each positional contribution is independent and addition combines distinct powers of ten.

For `num1=1`, `num2=10`, and `num3=1000`, the units digits are one, zero, and zero, so the key's units digit is zero. At every higher place at least one padded input digit is zero, so all chosen digits are zero and the integer result is zero.

For `987,879,798`, implicit thousands digits are all zero. Hundreds digits are nine, eight, and seven, choosing seven. Tens and units similarly choose seven, producing numeric key 777. The missing leading thousands zero is naturally absent from the returned integer.

**Why returning an integer removes leading zeros.** `ans` is built numerically. A chosen zero in the thousands or hundreds place adds nothing, so Python never represents it as a displayed prefix. This exactly matches returning the key without leading zeros.

The invariant after $t$ iterations is that `ans` has the correct minimum digits in the lowest $t$ positions and zeros above them, while `k=10^t`. The next extraction and addition establishes the next position. After four iterations, all required digits are correct.

No carries can occur between places because each `x` is a single digit and each position is assigned once. Summing `x*k` is equivalent to writing the digits.

The fixed four-iteration loop relies on the input maximum 9999 and the definition of a four-digit padded key. It deliberately ignores no relevant higher digits because legal inputs have none.

## Complexity detail

The loop runs exactly four times, independent of input magnitude. Each iteration performs a fixed number of arithmetic operations, so time complexity is $O(1)$.

Only `ans`, `k`, `x`, and loop state are stored, giving $O(1)$ auxiliary space. Inputs are not modified.

Arithmetic values stay below ten thousand, though Python would safely handle larger intermediates.

## Alternatives and edge cases

- **Zero-pad strings:** Format every input to width four, take coordinate-wise character minima, join, and convert to integer. This is correct but allocates small strings and requires careful numeric character comparison.
- **Extract digits into arrays:** Four-entry arrays make positions explicit but add unnecessary storage when accumulation can happen immediately.
- **Process from thousands downward:** Repeatedly build `ans = ans * 10 + digit`. This is equally correct; the source instead uses place-value addition from units upward.
- **All inputs identical:** Every positional minimum equals that number's digit, so the key equals the input.
- **One-digit inputs:** Higher extracted digits are zero for all numbers, and the result is the minimum units digit.
- **A zero at any padded position:** That position's key digit becomes zero because zero is the minimum possible digit.
- **Key entirely zero:** Returning integer zero correctly represents `"0000"` without leading zeros.
- **Internal zero:** A zero in tens or units position is preserved through its place contribution; only leading zeros disappear in integer display.
- **Maximum inputs:** Four iterations include the thousands place, so values up to 9999 are fully covered.
- **Positive-input guarantee:** Inputs never contain a sign or decimal representation issue. Extending to negative values would require a new digit definition.
- **Fixed width:** If the specification changed to more than four places, the loop bound would need to change; it is not inferred dynamically.
- **Why higher places do not influence lower ones:** Digit selection is coordinate-wise and uses no arithmetic operation on the original numbers beyond extraction. A large thousands digit cannot compensate for or change the minimum units digit.
- **No string lexicographic trap:** Arithmetic extraction compares numeric digits directly. A string solution must compare digit characters consistently, but the integer solution cannot confuse textual ordering with numeric place values.
- **Place multiplier invariant:** `k` is always a power of ten. Updating it only after adding the current contribution prevents placing a chosen digit one column too far left or right.
- **Returning fewer than four displayed digits:** The conceptual key always has four padded positions, but the return type is integer. Numeric representation intentionally omits every leading zero while retaining zeros between nonzero digits.
- **Example with an internal zero:** If positional minima form `"5070"`, accumulation adds five thousand and seven tens. It returns 5070, showing that only leading zeros disappear; internal and trailing zeros retain their positional meaning.
