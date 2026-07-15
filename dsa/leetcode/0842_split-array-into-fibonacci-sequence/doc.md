# Split Array into Fibonacci Sequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 842 |
| Difficulty | Medium |
| Topics | String, Backtracking |
| Official Link | [LeetCode](https://leetcode.com/problems/split-array-into-fibonacci-sequence/) |

## Problem Description
### Goal
Given a digit string `num`, split all of its characters into a list of non-negative integers. The list must contain at least three values, every value must be smaller than $2^{31}$, and each value from the third onward must equal the sum of the previous two.

Each piece must use its ordinary decimal representation: it may be exactly `"0"`, but a multi-digit piece cannot begin with `0`. Return any Fibonacci-like sequence whose concatenated decimal pieces reproduce the entire input, or return `[]` when no such split exists.

### Function Contract
**Inputs**

- `num`: a string of digits with $1 \leq \lvert\texttt{num}\rvert \leq 200$.

**Return value**

Return any list `f` of at least three integers satisfying $0 \leq f_i < 2^{31}$ and

$$
f_i + f_{i+1} = f_{i+2}
$$

for every valid $i$, with the canonical decimal forms of all entries concatenating to `num`. Return `[]` if no valid list exists.

### Examples
**Example 1**

- Input: `num = "1101111"`
- Output: `[11, 0, 11, 11]`

`[110, 1, 111]` is another valid answer.

**Example 2**

- Input: `num = "112358130"`
- Output: `[]`

**Example 3**

- Input: `num = "0123"`
- Output: `[]`

The split `"01", "2", "3"` is forbidden because `"01"` has an extra leading zero.

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Only the first two boundaries are choices**

Once the first two numbers are fixed, every later value is forced by their sum. Try every legal end position for the first piece and then the second. A 32-bit value has at most ten decimal digits, so each loop has only a constant number of candidates. If a piece begins with `0`, allow only its one-character form; stop extending a candidate as soon as it exceeds $2^{31}-1$.

**Match forced sums directly against the suffix**

For one initial pair, repeatedly compute `sequence[-2] + sequence[-1]`. If it exceeds the limit, abandon the pair. Otherwise convert it to decimal and require `num.startswith(token, position)`. A mismatch cannot be repaired by choosing a different boundary for that term because the Fibonacci value is already determined. On a match, append the value and advance by the token length.

If this process consumes the entire string with at least three numbers, the constructed list satisfies every bound, leading-zero rule, and recurrence by construction. Conversely, any valid answer has some legal first and second boundaries among those enumerated; for that pair, all forced tokens match, so the algorithm finds a valid sequence. Exhausting all pairs therefore proves impossibility.

#### Complexity detail

There are at most ten choices for each of the first two number lengths, a constant imposed by the 32-bit bound. For each pair, matching forced terms advances through at most $n$ digits, so total time is $O(n)$. The returned sequence and temporary decimal tokens occupy $O(n)$ space.

#### Alternatives and edge cases

- **General partition backtracking:** Trying every next substring before checking the recurrence explores unnecessary branches and can be exponential without the forced-sum pruning.
- **Rebuild the whole parsed prefix after each term:** This remains correct but repeatedly concatenates an increasingly long prefix and can cost $O(n^2)$ time.
- **Leading zero:** A piece beginning at `0` must end immediately unless it represents the single value zero.
- **Multiple answers:** Any valid full split is acceptable; callers must validate the recurrence and reconstruction rather than demand one fixed list.
- **32-bit limit:** Both chosen starting values and every later sum must be at most $2^{31}-1$.
- **Minimum length:** Consuming the string as only one or two integers is not a Fibonacci-like sequence.

</details>
