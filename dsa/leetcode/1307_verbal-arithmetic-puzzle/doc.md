# Verbal Arithmetic Puzzle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1307 |
| Difficulty | Hard |
| Topics | Array, Math, String, Backtracking |
| Official Link | [LeetCode](https://leetcode.com/problems/verbal-arithmetic-puzzle/) |

## Problem Description
### Goal
A verbal arithmetic equation represents each uppercase letter by one decimal digit. The same letter must always use the same digit, different letters must use different digits, and a word containing more than one character may not begin with 0.

The strings in `words` are the addends and `result` is their sum. After substituting digits for letters, every string is interpreted as an ordinary base-10 integer. Determine whether there is at least one digit assignment for which the sum of all represented addends equals the represented result while satisfying every uniqueness and leading-zero rule.

### Function Contract
**Inputs**

- `words`: between 2 and 5 nonempty uppercase strings.
- `result`: a nonempty uppercase string.
- Every input string has length at most 7.
- Across all addends and the result, there are at most 10 distinct letters.

Let $U$ be the number of distinct letters and $L$ the maximum input-string length. The source bounds give $U\le10$ and $L\le7$.

**Return value**

`true` if a valid one-to-one letter-to-digit assignment makes the represented equation hold; otherwise, `false`.

### Examples
**Example 1**

- Input: `words = ["SEND","MORE"]`, `result = "MONEY"`
- Output: `true`
- Explanation: A valid assignment makes the equation $9567+1085=10652$.

**Example 2**

- Input: `words = ["SIX","SEVEN","SEVEN"]`, `result = "TWENTY"`
- Output: `true`

**Example 3**

- Input: `words = ["LEET","CODE"]`, `result = "POINT"`
- Output: `false`

### Required Complexity
- **Time:** $O(10!)$
- **Space:** $O(U+L)$

<details>
<summary>Approach</summary>

#### General

**Work from the least significant column**

Directly assigning every letter before checking the equation delays almost all useful constraints. Instead, process columns from right to left while carrying a partial sum. Within one column, visit each addend row and add the digit assigned to its letter. If that letter is unassigned, try each unused digit, excluding 0 when the letter leads a multi-character word.

After all addends in the column have contributed, the result letter is forced: its digit must equal the accumulated sum modulo 10, and the quotient becomes the carry into the next column. If the forced digit conflicts with an existing assignment, is already used by another letter, or would create a leading zero, abandon that branch immediately.

**Why column completion is sufficient**

At a completed column, base-10 addition uniquely determines both the result digit and the outgoing carry from the addend digits and incoming carry. Therefore, a branch that violates either value cannot be repaired by choices in more significant columns. Conversely, if all columns are processed and the final carry is zero, every column equation holds, so the complete represented sum holds.

Backtracking restores both the letter assignment and the used-digit mark after a failed choice. A result shorter than the longest addend is impossible, and more than ten distinct letters cannot receive distinct decimal digits; reject both conditions before searching.

The implementation also computes each letter's signed decimal-place coefficient as a search-order heuristic. For two-addend equations, it tries larger digits first for a positive-coefficient letter; this changes only which valid branches are explored first, not which assignments are accepted.

#### Complexity detail

At most ten letters receive digits. In the worst case, the search explores permutations of the ten digits, bounded by $10!$ complete assignments; column constraints usually prune much earlier. Each recursive step performs bounded work because there are at most five addends and seven columns. The assignment state uses $O(U)$ space and the column-wise recursion uses $O(L)$ depth up to constant factors.

The fixed cap $U\le10$ is too narrow for an honest runtime-scaling verdict. The package therefore uses a bounded-domain certificate with an independent coefficient-based oracle on smaller alphametics and explicit satisfiable and impossible cases at the ten-letter boundary.

#### Alternatives and edge cases

- **Enumerate complete assignments:** Trying every digit permutation and evaluating the whole equation is a valid independent oracle, but it misses column carries as early pruning and is much slower in practice.
- **Coefficient equation:** Expanding each letter into its signed decimal-place coefficient turns the puzzle into one weighted sum; it is useful for verification, though a naive permutation search still explores many assignments.
- **Result length:** If `result` is shorter than the longest addend or more than one character longer, the equation cannot hold.
- **Leading zero:** Zero is allowed for a single-character word but forbidden for the first letter of every longer word, including `result`.
- **Repeated letters:** Multiple appearances of one letter reuse one digit; only different letters require different digits.
- **Ten distinct letters:** Every decimal digit is then used exactly once, including zero, while all leading-letter restrictions still apply.
- **Final carry:** Consuming every visible character is not enough; any nonzero carry after the most significant result column makes the branch invalid.

</details>
