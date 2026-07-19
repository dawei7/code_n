## General
**Every acquaintance query eliminates one candidate**

Start with candidate zero. For each other person, if the candidate knows that person, the candidate cannot be the celebrity and the other person becomes the only remaining candidate from the processed prefix.

After processing person `i`, everyone in `0..i` except `candidate` has been disproved by a witnessed relationship. If a celebrity exists in that prefix, it must be the candidate.

**Survival is not proof, so verify both directions**

The elimination pass leaves only a possibility, not proof. Check that the candidate knows nobody else and that every other person knows the candidate.

Each query `knows(candidate, person)` safely eliminates one endpoint: a true result eliminates the candidate, while false eliminates the other person. Therefore a real celebrity survives. Final verification accepts exactly when the survivor satisfies both defining conditions.

No eliminated person can be the celebrity: either they know someone or someone does not know them. Hence a real celebrity, if present, is the sole possible survivor. The second pass checks the two properties that elimination did not establish globally, rejecting the survivor when no celebrity exists.

## Complexity detail
Elimination uses $n - 1$ queries and verification uses at most $2(n - 1)$, for $O(n)$ time and $O(1)$ space.

## Alternatives and edge cases
- **Verify every person against everyone:** takes $O(n^2)$ queries.
- A one-person group returns zero; mutual acquaintance does not create a celebrity.
