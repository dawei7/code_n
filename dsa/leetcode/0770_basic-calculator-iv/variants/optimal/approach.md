## General
**Use canonical monomials as hash keys**

Represent a monomial by a tuple of its variable factors in sorted order: both `a*b*c` and `b*a*c` become `("a", "b", "c")`. A polynomial is a map from these tuples to integer coefficients; the empty tuple represents a constant. This makes like terms share one key automatically.

**Substitute while parsing**

Tokenize variable names, integers, operators, and parentheses. A substituted variable becomes a constant polynomial immediately, while an unknown variable becomes a one-factor monomial. Recursive descent uses three levels: expressions combine terms with `+` or `-`, terms combine factors with `*`, and factors parse numbers, variables, or parenthesized expressions. This enforces multiplication precedence and parentheses without rewriting the input.

**Combine and multiply polynomial maps**

Addition and subtraction update coefficients for matching monomials and remove coefficients that become zero. Multiplication takes every term from the left polynomial with every term from the right, multiplies coefficients, merges and sorts their variable tuples, and accumulates equal products.

Each parsed factor represents exactly its token value after substitution. Map addition, subtraction, and multiplication implement the corresponding algebraic operations and preserve canonical monomial keys, so structural induction over the parsed expression proves the final map is its fully combined polynomial. Formatting nonzero keys in descending degree and lexicographic factor order then produces exactly the required output order.

## Complexity detail
Let `p` cover the total intermediate monomial products created while expanding the expression, including the final distinct terms. Polynomial multiplication is proportional to those products, and sorting canonical factors and final terms gives a conservative $O(p \log p)$ time bound. Intermediate and final coefficient maps use $O(p)$ space.

## Alternatives and edge cases
- **Shunting-yard plus polynomial stack:** Converting operator precedence to postfix form evaluates the same polynomial maps iteratively, with similar expansion cost.
- **Build an abstract syntax tree first:** This cleanly separates parsing from evaluation but stores an extra tree before polynomial expansion.
- **Copy a growing map at every addition:** It remains correct but makes a long additive expression quadratic even when no multiplication occurs.
- **All variables substituted:** The result contains at most one constant term.
- **Complete cancellation:** Remove zero coefficients and return an empty list if no terms remain.
- **Repeated variables in a product:** Preserve repeated factors, such as `e*e`, because they determine degree.
- **Negative coefficients:** The sign stays on the leading integer in the formatted term.
- **Ordering:** Higher-degree terms precede lower-degree terms; equal-degree monomials compare their sorted variable tuples lexicographically.
