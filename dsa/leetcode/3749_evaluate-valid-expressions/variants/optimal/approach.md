## General

**Parse one complete expression and return where it ends**

`parse(i)` returns a pair:

- The integer value of the valid expression beginning at index `i`.
- The index immediately after that expression.

Returning the ending position lets a parent parse its first operand, skip the comma, then parse the second without searching for matching parentheses globally.

The grammar guarantees every call begins at either an integer literal or an operator name.

**Parse positive and negative literals**

If `expression[i]` is a digit or minus sign, the expression is a literal. A pointer `j` skips an optional minus sign and then advances through every digit. `int(expression[i:j])` converts the exact literal, and `j` already points to its following comma, closing parenthesis, or end of input.

The minus sign cannot be confused with subtraction because the operator is spelled `"sub"` and valid grammar places `'-'` only at a literal start.

**Parse an operation recursively**

Otherwise, the source scans from `i` until `'('`. The substring before it is one of `add`, `sub`, `mul`, or `div`.

After the opening parenthesis:

1. Parse the first operand, receiving `val1` and the comma position.
2. Increment `j` once to skip the comma.
3. Parse the second operand, receiving `val2` and the closing-parenthesis position.
4. Increment `j` once to move past the closing parenthesis.
5. Apply the named operation and return its result with `j`.

Nested structure is handled naturally because each operand call consumes its entire subtree before returning.

For `div(mul(4,sub(9,5)),add(1,1))`, the innermost literal calls return first, `sub` becomes four, `mul` becomes sixteen, `add` becomes two, and the root divides to eight.

**Why delimiters are skipped safely**

A literal parser stops on the first non-digit. In the first-operand position that character is the parent's comma; in the second position it is the parent's closing parenthesis.

A nested operation parser returns after its own closing parenthesis, which again places its parent at the correct delimiter. Valid syntax means no whitespace or malformed separator cases need recovery logic.

**Division behavior**

The source uses Python floor division `val1 // val2`. The contract guarantees every division has an exact integer result. For exact divisibility, floor division equals mathematical integer division even when the quotient is negative, so no truncation ambiguity changes the answer.

**Why each character is consumed once**

Each operator name is scanned by the call owning it, and each literal's digits are scanned by its literal call. Parent calls jump over already parsed operands using returned indices rather than rescanning them. This gives a single left-to-right structural parse.

The outer method returns only `parse(0)[0]` because the full input is guaranteed to contain exactly one valid expression.

**The source is recursive, despite the manifest summary**

The manifest describes explicit stacks, but the exact code uses recursive calls. This matters operationally. A syntactically valid expression of length $10^5$ can have nesting depth well above Python's default recursion limit, causing `RecursionError` even though the grammar and asymptotic algorithm are otherwise valid.

An explicit-stack parser would handle arbitrary allowed nesting. The approach here documents the protected source honestly and treats deep nesting as a material implementation limitation rather than claiming stack safety it does not have.

## Complexity detail

Let `n` be the expression length. Each character participates in constant parsing work, so time complexity is $O(n)$. Integer arithmetic is treated as constant under the signed-long guarantee.

Recursion depth can be proportional to nesting depth and therefore $O(n)$ in the worst case. Stack frames use $O(n)$ auxiliary space. No substring of an entire operand is copied; operator and literal slices together are bounded by parsed token sizes.

The asymptotic manifest space $O(n)$ remains correct, but its “explicit stacks” description is not.

## Alternatives and edge cases

- **Explicit value/operator stacks:** A left-to-right iterative parser avoids Python recursion limits and matches the manifest summary, but it is not the shown source.
- **Evaluate with Python `eval`:** The grammar uses custom function names and untrusted-text evaluation would be inappropriate and harder to constrain safely.
- **Repeatedly find innermost parentheses:** This can rescan the string and become quadratic. Returned end indices avoid that.
- **Single literal:** The first parse branch returns it directly, including negative values.
- **Deep nesting:** The algorithmic recurrence is valid, but Python's runtime recursion limit can reject an otherwise allowed expression.
- **Negative exact division:** Floor division equals the exact quotient because the dividend is guaranteed divisible by the divisor.
- **Subtraction yielding negative values:** Results remain integers and feed parent operations normally.
- **Multi-digit literals:** The digit loop consumes the entire token.
- **No whitespace:** The parser does not skip spaces because the contract says none exist.
- **Valid grammar guarantee:** There is no error handling for unknown operators, missing delimiters, or division by zero.
- **Index after root:** The caller ignores it because validity guarantees the root consumes the complete string.
