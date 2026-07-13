# Find the Celebrity

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 277 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Two Pointers, Graph Theory, Interactive |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-celebrity/) |

## Problem Description
### Goal
Among `n` people labeled `0` through $n - 1$, a celebrity is known by every other person but does not know any other person. Relationship information is available only through the boolean API `knows(a, b)` in the native problem.

Return the celebrity's index when exactly one person satisfies both conditions, or `-1` when nobody does. A popular person who knows someone else is not a celebrity, and a private person whom someone does not know is not one either. Minimize API calls by eliminating impossible candidates before verifying both directions; the app matrix models the same relationships offline.

### Function Contract
**Inputs**

- `n`: people numbered `0` through $n - 1$
- `knows_matrix`: offline app data where `knows_matrix[a][b]` represents `knows(a,b)`

**Return value**

The celebrity index, or `-1` if no celebrity exists. The native interface receives only `n` and calls the provided `knows(a,b)` API.

### Examples
**Example 1**

- Input: `n = 3, knows_matrix = [[false,true,false],[false,false,false],[false,true,false]]`
- Output: `1`

**Example 2**

- Input: `n = 2, knows_matrix = [[false,true],[true,false]]`
- Output: `-1`

**Example 3**

- Input: `n = 1, knows_matrix = [[false]]`
- Output: `0`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Every acquaintance query eliminates one candidate**

Start with candidate zero. For each other person, if the candidate knows that person, the candidate cannot be the celebrity and the other person becomes the only remaining candidate from the processed prefix.

After processing person `i`, everyone in `0..i` except `candidate` has been disproved by a witnessed relationship. If a celebrity exists in that prefix, it must be the candidate.

**Survival is not proof, so verify both directions**

The elimination pass leaves only a possibility, not proof. Check that the candidate knows nobody else and that every other person knows the candidate.

Each query `knows(candidate, person)` safely eliminates one endpoint: a true result eliminates the candidate, while false eliminates the other person. Therefore a real celebrity survives. Final verification accepts exactly when the survivor satisfies both defining conditions.

No eliminated person can be the celebrity: either they know someone or someone does not know them. Hence a real celebrity, if present, is the sole possible survivor. The second pass checks the two properties that elimination did not establish globally, rejecting the survivor when no celebrity exists.

#### Complexity detail

Elimination uses $n - 1$ queries and verification uses at most $2(n - 1)$, for $O(n)$ time and $O(1)$ space.

#### Alternatives and edge cases

- **Verify every person against everyone:** takes $O(n^2)$ queries.
- A one-person group returns zero; mutual acquaintance does not create a celebrity.

</details>
