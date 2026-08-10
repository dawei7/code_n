## General

**Reduce each side to one coefficient and one constant**

Every allowed term is either a constant integer or a multiple of `x`. Addition and subtraction are the only operations joining terms. Therefore, regardless of how many terms a side contains, that side can always be simplified to:

`coefficient * x + constant`.

The helper `f(s)` performs exactly that simplification. It returns a pair `(x, y)`, where `x` is the accumulated coefficient of the variable and `y` is the accumulated constant. The local variable named `x` is a number here; it is not the unknown itself.

For example, the side `x+5-3+x` simplifies as follows:

- `x` contributes one to the coefficient;
- `+5` contributes five to the constant;
- `-3` contributes negative three to the constant;
- `+x` contributes one more to the coefficient.

The returned pair is therefore `(2, 2)`, representing `2x + 2`.

**Normalize the first term so every term has an explicit sign**

Terms after the first naturally begin after a plus or minus sign, but the first term may have no leading sign. The parser makes the treatment uniform: if the side does not start with minus, it prepends plus.

After this normalization, the character at the current index is always a sign. The parser records `+1` for plus or `-1` for minus, advances past the sign, and scans forward until the next plus, the next minus, or the end of the side. The substring between those boundaries is exactly one unsigned term.

This design avoids special cases such as “if this is the first term.” A leading negative term already has its sign and is left unchanged; a leading positive term gains the explicit plus that later logic expects.

**Classify a term by its last character**

The permitted syntax makes term classification simple. If a term ends in `x`, it is a variable term. Otherwise, it is a constant.

For a variable term:

- `x` has an omitted coefficient, which means one;
- `2x` has coefficient two;
- the separately parsed sign makes `-x` contribute negative one and `-12x` contribute negative twelve.

The parser checks the term length. If the term consists only of `x`, it uses coefficient one. Otherwise, it converts the portion before the final `x` to an integer. It multiplies the coefficient by the saved sign and adds it to the coefficient total.

For a constant term, it converts the entire term to an integer, multiplies by the sign, and adds it to the constant total.

Because signs are handled outside the term text, integer conversion never has to interpret an embedded plus or minus.

**Move like terms across the equality**

Splitting the equation at `=` gives left side `a` and right side `b`. Suppose parsing returns:

- left: `x1 * x + y1`;
- right: `x2 * x + y2`.

The equation is then `x1 * x + y1 = x2 * x + y2`. Subtracting `x2 * x` from both sides and subtracting `y1` from both sides yields:

`(x1 - x2) * x = y2 - y1`.

This formula explains the exact signs in the final division. The numerator is right constant minus left constant, while the denominator is left coefficient minus right coefficient.

As a concrete example, `2x+3=x+8` parses to `(2, 3)` and `(1, 8)`. The remaining coefficient is `2 - 1 = 1` and the remaining constant is `8 - 3 = 5`, so the solution is `x=5`.

**Distinguish the three possible outcomes**

If `x1 - x2` is nonzero, the equation has one unique solution. Dividing `y2 - y1` by that coefficient gives the value of `x`. The problem guarantees that a unique solution is an integer, so integer division returns the exact requested value.

If `x1` equals `x2`, all variable terms cancel. Two cases remain:

- If `y1` also equals `y2`, both sides simplify to the same expression. Every possible `x` satisfies the equation, so the result is `Infinite solutions`.
- If `y1` differs from `y2`, cancellation leaves a false constant equality such as `3 = 8`. No value of `x` can fix it, so the result is `No solution`.

Testing coefficient equality before division also prevents division by zero.

**Why the parser and algebra are correct**

Within one side, the scanning boundaries separate exactly the original signed terms. Each term is classified correctly because the grammar permits only constants and terms ending in `x`. The saved sign is applied once, so the returned coefficient is the sum of every variable coefficient and the returned constant is the sum of every constant term. Thus `f` produces an algebraically equivalent simplified expression.

Applying the helper independently to both sides preserves the original equality. Moving variable contributions left and constants right uses reversible subtraction. When the remaining coefficient is nonzero, division by it is also reversible, producing the unique satisfying value. When that coefficient is zero, comparing constants exhausts the only two logical possibilities: an identity or a contradiction. Therefore, the returned string represents exactly the solution set of the input equation.

**Subtle behavior of Python integer division**

The exact code uses `//`. Python floor division differs from truncation for negative non-integers, but that distinction cannot affect a valid input with a unique solution because the problem guarantees the quotient is an integer. An exactly divisible negative value has the same result under floor division, truncation, and mathematical integer division. Without that source guarantee, ordinary division plus a rational representation would be safer.

## Complexity detail

Let `N` be the total number of characters in the equation. The equation is split once, and each character in each side is scanned a constant number of times. Parsing terms and accumulating their contributions therefore takes `O(N)` time overall. Python's integer conversions process the term digits; summed across all terms, those digits are still bounded by `N` under the standard fixed-width-value model used for this problem.

The algebra after parsing uses only a constant number of numeric variables, so the abstract streaming parsing algorithm needs `O(1)` auxiliary working space.

The exact Python implementation, however, creates strings: `equation.split("=")` creates side substrings, prepending `+` may create another side string, and `s[i:j]` creates a substring for each term. The term slices are temporary, but the side strings remain while solving. Consequently, its actual peak auxiliary memory is `O(N)` in Python, even though the underlying parsing idea can be implemented in `O(1)` extra space by scanning the original equation with indices and accumulating digits without slicing. This distinction does not change the stated `O(N)` time.

## Alternatives and edge cases

- **Evaluate the entire equation in one pass:** Maintain a side multiplier of plus one before `=` and negative one after it, then accumulate all variable coefficients and constants into one reduced equation. This avoids parsing the two sides separately and can avoid side-string copies, but requires careful sign composition.

- **Regular-expression tokenization:** A pattern can extract signed terms concisely. It still takes linear time, but it hides some of the parsing logic, allocates match objects, and is easier to get wrong around omitted coefficients such as `x` and `-x`.

- **Symbolic algebra library:** A general solver is far more powerful than needed and introduces substantial overhead. The restricted one-variable linear grammar reduces to two integer totals directly.

- **Trying numeric values:** Brute-force substitution has no justified finite search range and cannot cleanly prove infinite or nonexistent solutions. Algebraic reduction is both exact and linear.

- **Omitted coefficient:** `x` means `1x` and `-x` means `-1x`. Treating the empty text before `x` as an integer would fail, so the explicit length check is necessary.

- **Leading plus or no sign:** A side such as `x+1` receives a synthetic leading plus. A side beginning with minus already has the sign needed by the parser.

- **Zero coefficients written explicitly:** A term such as `0x` contributes zero but is still parsed as a variable term. It may help make both aggregate coefficients equal.

- **Terms that cancel on one side:** Expressions such as `x-x+3` naturally produce coefficient zero and constant three. No special cancellation pass is needed.

- **Negative unique answer:** The numerator or denominator may be negative. The exact-divisibility guarantee makes `//` return the correct negative integer.

- **Infinite solutions:** This occurs only when both aggregate coefficients and both aggregate constants match, even if the original sides look very different.

- **No solution:** Equal aggregate coefficients with unequal constants form a contradiction. Checking only whether the original strings differ would be incorrect because distinct strings can be algebraically equivalent.

- **Whitespace or parentheses:** The reference grammar contains neither. The parser assumes every character belongs to a number, `x`, a sign, or the equality marker. Supporting richer algebra would require a different tokenizer and grammar.
