## General

**Turn shared factors into connectivity**

Two input values have an edge when they share any factor greater than one. Connected components may also form transitively: four and six share factor two, while six and fifteen share factor three, so all three values belong to one component even though four and fifteen are coprime.

Union-Find is designed to maintain exactly this kind of gradually discovered connectivity.

**Use numeric factors as connector nodes**

The Union-Find structure has one index for every integer from zero through `max(nums)`. Input values and their factors live in the same parent array.

For every input value `v`, the solution tries divisors `i` from two while `i <= v // i`. This integer form checks through the square root without floating-point rounding.

When `v % i == 0`, both `i` and `v // i` are factors. The code performs:

- `union(v, i)`;
- `union(v, v // i)`.

The factor indices act as invisible connector vertices. If two different input values share factor `f`, both become united with index `f` and therefore with each other.

The factor need not be prime. Connecting through composite factors is still correct because sharing a composite factor certainly means sharing a factor greater than one. Trial division also discovers prime factors through divisor pairs.

**Why both factors of a divisor pair are joined**

Suppose `v = 35` and the trial divisor reaches five. The paired factor is seven. Another input value might share seven but not five, so joining only the trial divisor would miss that connection.

Adding both `i` and `v // i` ensures every proper factor discovered by trial division can serve as a connector.

For a perfect square, both expressions may be equal. The second union is then redundant but harmless.

**What happens to prime values and one**

A prime `v` has no divisor between two and its square root. It performs no union and remains its own component root. Another input multiple of `v` will eventually union with factor index `v`, thereby joining the prime value to that component.

Value one has no factor greater than one and must be isolated. Its loop performs no union, exactly matching the graph definition.

**Path compression**

Method `find(x)` recursively follows parent links. On the way back, it assigns every visited node directly to the root.

This path compression makes future root queries nearly constant amortized time. The `union` method does not use rank or size; it simply attaches root `pa` to root `pb`. Path compression alone still supplies the inverse-Ackermann amortized behavior normally cited for this use.

**Counting only actual input vertices**

The parent array contains many factor connector nodes that are not graph vertices from the problem. They must not contribute to component sizes.

The final generator calls `uf.find(v)` only for `v` in `nums`. `Counter` counts how many input values have each root. Factor-only nodes influence which roots match but are never counted as stones or numbers themselves.

Taking the maximum counter value returns the largest component size.


If two input values share factor `f > 1`, processing their divisor pairs connects each value to a factor that lies in the same factor network as `f`. In particular, every prime divisor is exposed either as the tested divisor or its quotient. Hence shared-factor edges place their endpoints in one Union-Find set.

Union-Find is transitive, so a path of shared-factor edges also produces a single set.

Conversely, unions are introduced only between a value and one of its genuine factors. A path through connector nodes therefore represents a sequence of input values linked by common factors. Values in one Union-Find set belong to one graph component.

Thus roots partition input values exactly by graph connectivity, and the largest root frequency is the required answer.

## Complexity detail

Let `N` be the number of input values and `M = max(nums)`.

For each value, trial division performs up to `O(sqrt(M))` iterations. Union-Find operations have amortized `O(alpha(M))` cost because the structure has `M + 1` indices. Total time is `O(N sqrt(M) alpha(M))`, commonly written with the nearly constant inverse Ackermann factor suppressed.

The parent array uses `O(M)` space. The final counter contains at most `N` roots, so total auxiliary space is `O(N + M)`.

## Alternatives and edge cases

- **Prime-factorize each value:** Divide out each discovered prime and union values through a map from prime to representative. This avoids a Union-Find array sized by `M` but requires careful factorization.
- **Compare every pair with gcd:** It directly follows the graph definition but costs `O(N^2 log M)` time.
- **Sieve smallest prime factors:** Preprocessing through `M` makes repeated factorization fast and is useful for many values.
- **All values prime:** Unless one prime divides another input composite, primes remain singleton components.
- **Value one:** It is always isolated because it has no permitted common factor.
- **Perfect squares:** Repeated union with the same square-root factor is harmless.
- **Transitive components:** Direct gcd greater than one is not required between every pair; Union-Find preserves paths.
- **Unique inputs:** Counter entries count different input values without duplicate-value complications.
- **Large maximum with few values:** The `O(M)` parent array may be wasteful; a dictionary-backed factor Union-Find is an alternative.
- **No union by size:** Path compression keeps operations efficient, though adding rank or size would provide the standard strongest bound.
