# Basic Calculator IV

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 770 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Hash Table, Math, String, Stack, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/basic-calculator-iv/) |

## Problem Description

### Goal

Given a valid arithmetic `expression` containing non-negative integers, lowercase variables, parentheses, `+`, `-`, and `*`, substitute each variable in `evalvars` with its corresponding integer from `evalints`. Leave every unlisted variable symbolic and evaluate the expression into a simplified polynomial.

Combine terms with identical sorted variable factors and omit terms whose coefficient becomes zero. Return each remaining term as its coefficient followed by `*variable` factors, ordered first by descending total degree and then lexicographically among equal-degree factor lists. Return an empty list for the zero polynomial.

### Function Contract

**Inputs**

- `expression`: a valid infix expression using integers, variables, spaces, `+`, `-`, `*`, and parentheses.
- `evalvars`: variable names to substitute.
- `evalints`: corresponding integer values, where `evalvars[i]` maps to `evalints[i]`.

**Return value**

- Simplified term strings sorted by descending total degree and then lexicographically by their sorted variable factors. Each string begins with its coefficient, followed by `*variable` factors; return an empty list for the zero polynomial.

### Examples

**Example 1**

- Input: `expression = "e + 8 - a + 5"`, `evalvars = ["e"]`, `evalints = [1]`
- Output: `["-1*a","14"]`
- Explanation: Substituting $e = 1$ leaves $-a + 14$.

**Example 2**

- Input: `expression = "e - 8 + temperature - pressure"`, `evalvars = ["e","temperature"]`, `evalints = [1,12]`
- Output: `["-1*pressure","5"]`
- Explanation: The substituted constants combine while `pressure` remains symbolic.

**Example 3**

- Input: `expression = "(e + 8) * (e - 8)"`, `evalvars = []`, `evalints = []`
- Output: `["1*e*e","-64"]`
- Explanation: Expansion combines the opposite linear terms and cancels them.

### Required Complexity

- **Time:** $O(p \log p)$
- **Space:** $O(p)$

<details>
<summary>Approach</summary>

#### General

**Use canonical monomials as hash keys**

Represent a monomial by a tuple of its variable factors in sorted order: both `a*b*c` and `b*a*c` become `("a", "b", "c")`. A polynomial is a map from these tuples to integer coefficients; the empty tuple represents a constant. This makes like terms share one key automatically.

**Substitute while parsing**

Tokenize variable names, integers, operators, and parentheses. A substituted variable becomes a constant polynomial immediately, while an unknown variable becomes a one-factor monomial. Recursive descent uses three levels: expressions combine terms with `+` or `-`, terms combine factors with `*`, and factors parse numbers, variables, or parenthesized expressions. This enforces multiplication precedence and parentheses without rewriting the input.

**Combine and multiply polynomial maps**

Addition and subtraction update coefficients for matching monomials and remove coefficients that become zero. Multiplication takes every term from the left polynomial with every term from the right, multiplies coefficients, merges and sorts their variable tuples, and accumulates equal products.

Each parsed factor represents exactly its token value after substitution. Map addition, subtraction, and multiplication implement the corresponding algebraic operations and preserve canonical monomial keys, so structural induction over the parsed expression proves the final map is its fully combined polynomial. Formatting nonzero keys in descending degree and lexicographic factor order then produces exactly the required output order.

#### Complexity detail

Let `p` cover the total intermediate monomial products created while expanding the expression, including the final distinct terms. Polynomial multiplication is proportional to those products, and sorting canonical factors and final terms gives a conservative $O(p \log p)$ time bound. Intermediate and final coefficient maps use $O(p)$ space.

#### Alternatives and edge cases

- **Shunting-yard plus polynomial stack:** Converting operator precedence to postfix form evaluates the same polynomial maps iteratively, with similar expansion cost.
- **Build an abstract syntax tree first:** This cleanly separates parsing from evaluation but stores an extra tree before polynomial expansion.
- **Copy a growing map at every addition:** It remains correct but makes a long additive expression quadratic even when no multiplication occurs.
- **All variables substituted:** The result contains at most one constant term.
- **Complete cancellation:** Remove zero coefficients and return an empty list if no terms remain.
- **Repeated variables in a product:** Preserve repeated factors, such as `e*e`, because they determine degree.
- **Negative coefficients:** The sign stays on the leading integer in the formatted term.
- **Ordering:** Higher-degree terms precede lower-degree terms; equal-degree monomials compare their sorted variable tuples lexicographically.

</details>
