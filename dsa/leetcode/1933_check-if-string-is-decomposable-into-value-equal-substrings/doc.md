# Check if String Is Decomposable Into Value-Equal Substrings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1933 |
| Difficulty | Easy |
| Topics | String |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-string-is-decomposable-into-value-equal-substrings/) |

## Problem Description
### Goal
A value-equal string contains only copies of one character. Given a digit
string `s`, split the entire string into consecutive, nonempty substrings, each
of which must be value-equal. Every selected character must remain in its
original position because the pieces are substrings, not subsequences.

Exactly one piece in the decomposition must have length two. Every other piece
must have length three; no piece of another length is allowed. Return whether
at least one decomposition satisfying all of these rules exists.

### Function Contract
**Inputs**

- `s`: a string of $N$ digits from `"0"` through `"9"`, where
  $1 \le N \le 1000$.

**Return value**

- `true` if `s` can be decomposed into exactly one value-equal substring of
  length two and any number of value-equal substrings of length three;
  otherwise `false`.

### Examples
**Example 1**

- Input: `s = "000111000"`
- Output: `false`

The natural three groups all have length three, so no required length-two
piece exists.

**Example 2**

- Input: `s = "00011111222"`
- Output: `true`

One valid decomposition is `["000", "111", "11", "222"]`.

**Example 3**

- Input: `s = "011100022233"`
- Output: `false`

The initial one-character run cannot form an allowed piece.

### Required Complexity
- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Treat each maximal equal-digit run independently**

A value-equal substring cannot cross a boundary between different digits.
Therefore every maximal run of one digit must be partitioned entirely into
pieces of length two and three. Scan the string once to obtain each run length.

**Use the remainder modulo three**

A run whose length is divisible by three can use only length-three pieces. A
run with remainder two can use one length-two piece and fill the rest with
length-three pieces. A run with remainder one cannot participate in a valid
global decomposition: replacing threes with twos would require either two
length-two pieces, as for length four, or leave the same conflict after
removing threes.

Consequently every run must have remainder zero or two, and exactly one run
must have remainder two. That one run supplies the unique length-two piece;
all other characters are covered by length-three pieces. These conditions are
both necessary and sufficient, so the scan can reject remainder one
immediately and count remainder-two runs.

#### Complexity detail

Each of the $N$ characters belongs to exactly one maximal run and is visited
once, giving $O(N)$ time. The scan stores only indices and the number of runs
that require a length-two piece, so it uses $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Dynamic programming over prefix lengths:** Track whether each prefix can
  be covered with zero or one length-two piece. This is correct and linear but
  stores more state than the run-remainder characterization needs.
- **Rescan the full run from every position:** Recovering equal-run boundaries
  independently for each character is correct, but a long uniform string
  causes $O(N^2)$ repeated work.
- A string of length two is valid because its only piece is the required
  length-two substring.
- A string made solely of length-three groups is invalid because the
  length-two piece must exist exactly once.
- Two separate runs with remainder two are invalid because they require two
  length-two pieces.
- A run of length five is valid on its own because it splits into lengths
  three and two.
- Runs of different digits are never allowed to share a piece.

</details>
