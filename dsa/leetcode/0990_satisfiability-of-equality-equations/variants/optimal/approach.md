## General
**Treat equality as connectivity:** If two variables are equal, they belong to the same equivalence class. A disjoint-set union structure stores these classes for the 26 lowercase letters. Initialize every letter as its own parent, then process all `"=="` equations and unite their endpoints.

**Delay inequalities until the classes are complete:** An inequality cannot safely be checked before all equalities have been incorporated. For example, `"a!=c"` may look harmless until later equations `"a==b"` and `"b==c"` connect its endpoints. A second pass over the `"!="` equations therefore compares the final representatives. If both endpoints have the same representative, the constraints are contradictory.

If no inequality joins two members of the same equivalence class, assign a distinct integer to each class. Every equality then holds within a class and every inequality crosses between two classes, proving that this construction satisfies all equations.

## Complexity detail
There are $Q$ equations. Union by size and path compression make each disjoint-set operation take amortized $O(\alpha(26))$ time, so both passes take $O(Q\alpha(26))$ time. The parent and size arrays contain exactly 26 entries, giving $O(26)$ space.

## Alternatives and edge cases
- **Graph search for each inequality:** Build an equality graph and search for a path between every unequal pair. This is correct, but repeatedly traversing the same equality relationships can take $O(Q^2)$ time.
- **Repeated equality propagation:** Repeatedly scan equations to copy known class labels until nothing changes. It eventually finds the same classes but can also be quadratic.
- **Self-inequality:** An equation such as `"a!=a"` is immediately impossible because both endpoints necessarily have the same representative.
- **Self-equality:** An equation such as `"a==a"` adds no information and remains valid.
- **Equation order:** Equalities and inequalities may appear in any order; the two-pass structure prevents order from affecting the answer.
