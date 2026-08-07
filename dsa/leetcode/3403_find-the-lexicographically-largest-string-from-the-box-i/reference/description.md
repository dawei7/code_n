## Description

You are given a string `word`, and an integer `numFriends`.

Alice is organizing a game for her `numFriends` friends. There are multiple rounds in the game, where in each round:

- `word` is split into `numFriends` **non-empty** strings, such that no previous round has had the **exact** same split.

- All the split words are put into a box.

Find the lexicographically largest string from the box after all the rounds are finished.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** word = "dbca", numFriends = 2

**Output:** "dbc"

**Explanation:**

All possible splits are:

- `"d"` and `"bca"`.

- `"db"` and `"ca"`.

- `"dbc"` and `"a"`.

</div>
#### Example 2

<div class="example-block">
**Input:** word = "gggg", numFriends = 4

**Output:** "g"

**Explanation:**

The only possible split is: `"g"`, `"g"`, `"g"`, and `"g"`.

</div>
### Constraints

- $1 \le \text{word.length} \le 5 * 10^{3}$

- `word` consists only of lowercase English letters.

- $1 \le numFriends \le \text{word.length}$