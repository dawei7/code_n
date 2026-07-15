# Satisfiability of Equality Equations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 990 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Union-Find, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/satisfiability-of-equality-equations/) |

## Problem Description

### Goal

You are given an array of equations describing relationships among one-letter variable names. Every equation has exactly four characters and has one of the forms `"x==y"` or `"x!=y"`, where `x` and `y` are lowercase letters and may even be the same letter.

Determine whether integers can be assigned to all variable names so that every equality and inequality holds simultaneously. Return `true` when such an assignment exists and `false` when the constraints contradict one another.

### Function Contract

**Inputs**

- `equations`: a list of $Q$ strings, where $1\le Q\le500$. Each string has length four, its first and last characters are lowercase letters, its second character is either `'='` or `'!'`, and its third character is `'='`.

**Return value**

- `true` if one integer assignment satisfies every equation; otherwise, `false`.

### Examples

**Example 1**

- Input: `equations = ["a==b", "b!=a"]`
- Output: `false`
- Explanation: The equality requires the two variables to match, while the inequality requires them to differ.

**Example 2**

- Input: `equations = ["b==a", "a==b"]`
- Output: `true`
- Explanation: Assigning the same integer to both variables satisfies both equations.

**Example 3**

- Input: `equations = ["a==b", "b==c", "a!=c"]`
- Output: `false`
- Explanation: The first two equalities imply that `a` and `c` are equal.

### Required Complexity

- **Time:** $O(Q\alpha(26))$
- **Space:** $O(26)$

<details>
<summary>Approach</summary>

#### General

**Treat equality as connectivity:** If two variables are equal, they belong to the same equivalence class. A disjoint-set union structure stores these classes for the 26 lowercase letters. Initialize every letter as its own parent, then process all `"=="` equations and unite their endpoints.

**Delay inequalities until the classes are complete:** An inequality cannot safely be checked before all equalities have been incorporated. For example, `"a!=c"` may look harmless until later equations `"a==b"` and `"b==c"` connect its endpoints. A second pass over the `"!="` equations therefore compares the final representatives. If both endpoints have the same representative, the constraints are contradictory.

If no inequality joins two members of the same equivalence class, assign a distinct integer to each class. Every equality then holds within a class and every inequality crosses between two classes, proving that this construction satisfies all equations.

#### Complexity detail

There are $Q$ equations. Union by size and path compression make each disjoint-set operation take amortized $O(\alpha(26))$ time, so both passes take $O(Q\alpha(26))$ time. The parent and size arrays contain exactly 26 entries, giving $O(26)$ space.

#### Alternatives and edge cases

- **Graph search for each inequality:** Build an equality graph and search for a path between every unequal pair. This is correct, but repeatedly traversing the same equality relationships can take $O(Q^2)$ time.
- **Repeated equality propagation:** Repeatedly scan equations to copy known class labels until nothing changes. It eventually finds the same classes but can also be quadratic.
- **Self-inequality:** An equation such as `"a!=a"` is immediately impossible because both endpoints necessarily have the same representative.
- **Self-equality:** An equation such as `"a==a"` adds no information and remains valid.
- **Equation order:** Equalities and inequalities may appear in any order; the two-pass structure prevents order from affecting the answer.

</details>
