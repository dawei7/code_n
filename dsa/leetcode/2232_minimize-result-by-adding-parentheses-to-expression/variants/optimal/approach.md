## General

**Describe a placement by two cuts**

Let the plus sign separate left and right digit strings. Choose a cut inside or before the left operand for the opening parenthesis, and choose a cut inside or after the right operand for the closing parenthesis. These two choices describe every legal placement exactly once.

For a placement, split the text into four numeric pieces: the optional prefix multiplier, the left addend inside the parentheses, the right addend inside them, and the optional suffix multiplier. A missing outer piece contributes multiplicative identity $1$. The value is

$$
\text{prefix}\,(\text{left addend}+\text{right addend})\,\text{suffix}.
$$

**Enumerate the complete legal choice set**

Try every opening and closing cut, evaluate the four pieces, and remember the text for the smallest value seen. Each retained candidate is syntactically legal because both inside addends remain nonempty and the plus stays within the parentheses.

Since every legal placement appears in the enumeration, the globally minimum placement is evaluated. The algorithm returns a candidate only when it improves the best known value, so the final expression attains that global minimum.

## Complexity detail

The input length is at most ten, leaving at most nine digits and no more than 20 legal boundary pairs. Parsing, evaluating, and reconstructing these fixed-length candidates therefore take $O(1)$ time and $O(1)$ auxiliary space under the legal contract.

The bounded-domain certificate replaces dishonest length scaling with exhaustive and deterministic oracle comparisons across legal expression shapes.

## Alternatives and edge cases

- **Expression parser search:** Building syntax trees is unnecessary because the allowed parenthesis shape is fixed by two cuts.
- **Greedy shortest inner numbers:** Smaller addends do not necessarily minimize the surrounding multipliers, so local cut choices can fail.
- **Omit an outer multiplier:** A missing prefix or suffix represents $1$, not $0$ and not an invalid placement.
- **Parenthesize the whole expression:** Cuts at both outer boundaries are legal.
- **One-digit operand:** Its inside portion is forced, though the other operand may still have several cuts.
- **Tied minima:** Any minimum-valued placement satisfies the contract.
- **No zero digits:** Every parsed digit substring is a positive integer without leading zeros.
