## General

**Every acquaintance query eliminates one candidate**

Start with candidate zero. For each other person, if the candidate knows that person, the candidate cannot be the celebrity and the other person becomes the only remaining candidate from the processed prefix.

If the candidate does not know the other person, that other person cannot be the celebrity because the candidate would
then be someone who does not know them. Thus either answer to the query eliminates one endpoint. After processing
person `i`, everyone in `0..i` except `candidate` has been disproved by a witnessed relationship. If a celebrity exists
in that prefix, it must be the candidate.

**Survival is not proof, so verify both directions**

The elimination pass leaves only a possibility, not proof. Check that the candidate knows nobody else and that every other person knows the candidate.

Each elimination query safely removes one endpoint, so a real celebrity can never be discarded. Final verification
accepts exactly when the survivor knows nobody else and every other person knows the survivor.

No eliminated person can be the celebrity: either they know someone or someone does not know them. Hence a real
celebrity, if present, is the sole possible survivor. The second pass checks the two properties that elimination did
not establish globally, rejecting the survivor when no celebrity exists.

LeetCode supplies `knows(a, b)` as a hidden judge API. The offline app receives the same relation as `knows_matrix` and
defines a local `knows` lookup over that fixture; the elimination and verification logic then use the same predicate
calls as the native solution.

## Complexity detail

Elimination uses $n - 1$ queries. Verification makes at most two queries for each of the other $n - 1$ people, so the
total never exceeds $3(n - 1)$ relationship queries. This is $O(n)$ time and $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Verify every person against everyone:** takes $O(n^2)$ queries.
- **No celebrity:** elimination still leaves one survivor, but either direction of the verification condition rejects
  that person.
- **Mutual acquaintance:** two people knowing each other cannot make either one a celebrity because a celebrity knows
  nobody else.
- **One person:** the app-local implementation returns zero defensively, although the source contract requires at least
  two people.
