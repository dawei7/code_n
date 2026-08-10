## General

Write the two input numbers as:

$$
(a_1+b_1i)\quad\text{and}\quad(a_2+b_2i).
$$

Multiplying them by distribution gives:

$$
a_1a_2+a_1b_2i+a_2b_1i+b_1b_2i^2.
$$

Because $i^2=-1$, the last term becomes negative real. Grouping real and imaginary parts yields:

$$
(a_1a_2-b_1b_2)+(a_1b_2+a_2b_1)i.
$$

The implementation performs exactly this parse, calculation, and formatting.

**Remove the trailing imaginary marker.** Each input ends in the literal character `"i"`. The slice `num1[:-1]` removes that final marker, leaving a string of the form `"real+imaginary"`. The same is done for `num2`.

**Split at the required separator.** Calling `.split("+")` produces the real text before the plus sign and the imaginary text after it.

The imaginary part may be negative, as in `"1+-1i"`. Removing `i` gives `"1+-1"`, and splitting on plus produces `["1", "-1"]`. The minus sign stays attached to the imaginary component, so `int` parses it correctly.

The real part can also be negative. In `"-3+2i"`, the leading minus is not the separator and remains with `"-3"`.

The source guarantees valid format, so there is exactly one separating plus sign in the expected logical position. No validation branch is needed.

The expression:

`a1, b1 = map(int, num1[:-1].split("+"))`

converts both pieces to integers and unpacks them into the real and imaginary coefficients. The next line does the same for the second input.

**Compute the real coefficient.** The returned real part is:

`a1 * a2 - b1 * b2`.

The subtraction reflects the `i^2 = -1` term. Using addition here is the most common algebra mistake.

**Compute the imaginary coefficient.** The returned imaginary part is:

`a1 * b2 + a2 * b1`.

These are the two cross-products containing exactly one factor of `i`.

**Format in the mandated representation.** The f-string writes:

`"{real}+{imaginary}i"`.

The separator is always a literal plus sign. If the imaginary result is negative, its decimal conversion includes a leading minus, producing text such as `"0+-2i"`. Although ordinary mathematics might write `"0-2i"`, the problem's required string form uses `real+imaginaryi` and explicitly accepts the plus-minus sequence.

For `"1+1i"` multiplied by `"1+1i"`, the real coefficient is `1 * 1 - 1 * 1 = 0`. The imaginary coefficient is `1 * 1 + 1 * 1 = 2`. Formatting produces `"0+2i"`.

For `"1+-1i"` squared, the real coefficient is `1 - ((-1) * (-1)) = 0`. The imaginary coefficient is `1 * (-1) + 1 * (-1) = -2`. The result is `"0+-2i"`.

As another sign check, multiplying `"-2+3i"` by `"4+-5i"` parses coefficients negative two, three, four, and negative five. The real result is `(-2) * 4 - 3 * (-5) = 7`, while the imaginary result is `(-2) * (-5) + 4 * 3 = 22`. The formatted answer is `"7+22i"`. This trace shows that the same formula handles negative real and imaginary inputs without separate sign cases.

**Why parsing and formatting preserve signs.** Every signed coefficient is parsed by Python's `int`, arithmetic uses signed integers, and the f-string converts the resulting integers back to their canonical decimal forms. The fixed plus separator remains independent of the imaginary coefficient's sign.

**Why the formula is complete.** Distributive multiplication produces four products. The two without exactly one `i` become real after replacing `i^2`, and the two with one `i` become imaginary. No other terms exist, so the returned coefficients equal the mathematical product.

The method returns a string and does not rely on Python's built-in complex-number type. This avoids floating-point formatting and follows the source's exact integer representation.

## Complexity detail

The source bounds both coefficients between minus one hundred and one hundred, so input strings have bounded length. Under those fixed constraints, parsing, arithmetic, and formatting all take $O(1)$ time and $O(1)$ auxiliary space, matching the manifest.

Under a generalized model with arbitrarily many digits, parsing and formatting would scale with input/output digit length, and integer multiplication would not be strictly constant time. That broader model is unnecessary for the stated domain.

The product coefficients remain small enough for ordinary fixed-width integer types under the given bounds; Python integers provide additional safety automatically.

## Alternatives and edge cases

- **Use a regular expression:** It can capture signed components, but the fixed plus-delimited format makes slicing and splitting simpler.
- **Use a built-in complex type:** It introduces floating-point representation and output-format concerns for an integer-only task.
- **Four-term direct string manipulation:** Arithmetic should occur after integer parsing; manipulating signs as text is more error-prone.
- **Negative imaginary input:** The format appears as `"+-"`, and splitting at plus preserves the negative sign.
- **Negative real input:** Its leading minus remains part of the first split component.
- **Zero real part:** Formatting still includes it, such as `"0+2i"`.
- **Zero imaginary part:** The result ends with `"+0i"`.
- **Negative imaginary result:** The required fixed separator produces `"+-"`.
- **Both inputs purely real:** Both imaginary coefficients are zero and the formula reduces to real multiplication.
- **Both inputs purely imaginary:** The product is negative real because `i^2=-1`.
- **Valid-format guarantee:** It allows direct two-value unpacking without error handling.
