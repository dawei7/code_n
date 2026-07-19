## General
**Model equivalence classes as components:** Create one disjoint-set node for every lowercase letter. For each corresponding pair from `s1` and `s2`, unite their components. Reflexivity is represented by each letter initially being its own parent, while union and transitive root lookup provide symmetry and transitivity.

**Keep the minimum letter as representative:** When two roots are merged, attach the lexicographically larger root to the smaller root. Consequently, the root of every completed component is its smallest character. Path compression makes later root lookups direct without changing that minimum-root rule.

**Minimize each position independently:** Replace every character in `baseStr` with its component root. This replacement is allowed by the equivalence relation. Any other equivalent choice at the first position where two candidate strings differ is no smaller than the root, so choosing the minimum for every position produces the globally lexicographically smallest string.

## Complexity detail
Initializing the parent array costs $O(A)$. The $P$ unions and $B$ conversions use path-compressed disjoint-set operations; because $A=26$ and roots always move toward smaller letters, their cost is bounded by the alphabet size and is constant per character. Total time is $O(P+B+A)$ and auxiliary space is $O(A)$.

## Alternatives and edge cases
- **Graph search for every base character:** Store equivalence edges and search a component separately at each output position, but this can repeat the same traversal and cost $O(PB)$ time.
- **Transitive-closure matrix:** Floyd-Warshall over the alphabet works because $A=26$, but it performs $O(A^3)$ preprocessing and stores $O(A^2)$ relationships.
- **Direct-pair replacement only:** It is incorrect because equivalence is transitive; a character may map to a smaller letter through several pairs.
- **Repeated or reflexive pair:** It leaves the existing component unchanged.
- **Disconnected letter:** A base character absent from every nontrivial equivalence class maps to itself.
- **Pair order:** Union operations may arrive in any order; choosing the smaller root preserves the same final minimum representative.
- **Repeated base character:** Every occurrence uses the same component minimum and benefits from compressed lookup paths.
