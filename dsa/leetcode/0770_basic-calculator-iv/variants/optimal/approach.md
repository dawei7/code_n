## General

**Represent a polynomial canonically**

The evaluator must combine like terms, substitute selected variables, respect precedence, and format remaining variables in a fixed order.

The exact solution represents a polynomial as a dictionary:

- A key is a tuple of free-variable names forming one monomial.
- The tuple is sorted lexicographically and preserves repetition.
- The value is the integer coefficient.

For example, `3*a*a*b` is stored as key `("a", "a", "b")` with coefficient three. A constant uses the empty tuple `()`.

This canonical key makes algebraically identical products combine even if their variables appeared in different input orders.

**Tokenize before parsing**

The regular expression extracts variable names, nonnegative integer literals, parentheses, and operators while ignoring spaces. Multi-letter variables and multi-digit numbers each become one token.

`position` is a shared index into this token list. Recursive parsing consumes tokens exactly once in grammatical order.

**Use three parser levels for precedence**

`parse_expression` handles addition and subtraction. It first parses one term, then repeatedly consumes `+` or `-` followed by another term.

`parse_term` handles multiplication. It parses one factor, then repeatedly multiplies by following factors separated by `*`.

`parse_factor` handles the indivisible units: parenthesized expressions, integer literals, substituted variables, and free variables.

Because an expression asks for complete terms before adding them, multiplication binds more tightly. Recursive factor parsing makes parentheses bind most tightly.

**Create factor polynomials**

A nonzero integer literal becomes `{(): value}`. Zero becomes an empty dictionary because it has no nonzero term.

A variable present in the evaluation map becomes a constant in the same way. An unassigned variable becomes `{(token,): 1}`.

For `(`, the parser recursively reads a complete expression, then advances over its matching `)`.

**Add and subtract like terms**

`add_into(target, source, scale)` walks source terms. Scale one performs addition; scale negative one performs subtraction.

For each monomial it updates the coefficient already in the target. If the result becomes zero, the key is removed. This maintains the invariant that the polynomial dictionary contains no zero-coefficient terms.

**Multiply polynomials distributively**

Every term from the left polynomial multiplies every term from the right. Coefficients multiply. Variable tuples concatenate and are sorted to form a canonical monomial.

If several term pairs produce the same tuple, their coefficients accumulate. Cancellation removes the key when its coefficient reaches zero.

For example, multiplying `(e + 8)` by `(e - 8)` creates `e*e`, `-8e`, `+8e`, and `-64`. The middle terms share key `("e",)` and cancel, leaving `e*e - 64`.

**Apply substitutions at the leaf**

The mapping is built with `dict(zip(evalvars, evalints))`. Substitution happens when a variable token is parsed, before larger operations.

This is algebraically equivalent to simplifying symbolically and substituting later, but it prevents evaluated variables from entering monomial tuples and reduces intermediate expression size.

**Order final terms**

Output requires higher degree first. Tuple length is the degree because repeated variables occupy repeated positions.

The sort key `(-len(monomial), monomial)` therefore orders descending degree, then lexicographically by the already sorted variable tuple. The constant empty tuple has degree zero and comes last.

Each token begins with its coefficient, including coefficients one and negative one. Nonconstant terms append an asterisk and the asterisk-joined variables. Zero terms are already absent.


Each factor representation is exact. The term and expression parsers apply multiplication, addition, and subtraction with the required precedence and left-to-right grouping, while recursive factors respect parentheses.

Dictionary operations implement the distributive polynomial rules and canonicalize every monomial, so like terms combine exactly. Final sorting and rendering follow every output-order rule. Structural induction over the parsed expression proves the returned token list is the required simplified polynomial.

## Complexity detail

Polynomial size can expand through multiplication. Let `P` be the total number of term-pair products performed across all multiplications and `U` the number of final nonzero monomials. Parsing and combination take `O(P)` dictionary work plus the cost of sorting variable tuples in produced monomials.

Final ordering costs `O(U log U)`. A useful output-sensitive description is `O(P + U log U)`, with monomial-length factors included for tuple concatenation and sorting.

The manifest’s compact `O(p log p)` assumes `p` summarizes the produced polynomial work. Literal complexity cannot depend only linearly on input characters because distributive expansion may create many terms.

Stored polynomial dictionaries and recursion use space proportional to intermediate monomials, summarized as `O(P)` in the worst case.

## Alternatives and edge cases

- **Use Python `eval`:** Forbidden and would not produce canonical symbolic polynomial terms.

- **Build an abstract syntax tree first:** It separates parsing and evaluation but adds a full tree allocation.

- **Keep variables in encounter order:** Products such as `a*b` and `b*a` would fail to combine. Sort every monomial key.

- **Retain zero coefficients:** They would violate output rules and waste later work.

- **Zero expression:** Its polynomial dictionary is empty, producing `[]`.

- **Negative results:** Subtraction scales coefficients by negative one naturally.

- **Repeated variables:** Tuple multiplicity records degree correctly, such as `a*a`.

- **Parentheses:** Recursive expression parsing consumes them before surrounding multiplication or addition.
