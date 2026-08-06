## Function Contract

**Inputs**

- `intervals`: a sorted list of $n$ disjoint pairs `[a_i,b_i]`, each representing $[a_i,b_i)$.
- `toBeRemoved`: a pair representing the half-open interval to subtract.

**Return value**

- Return a sorted list of disjoint half-open intervals representing the set difference between the original union and `toBeRemoved`.

Because right endpoints are excluded, two intervals that meet only at one interval's right endpoint do not overlap. Every returned interval must be nonempty.
