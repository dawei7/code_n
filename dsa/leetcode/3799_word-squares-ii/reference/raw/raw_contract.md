## Function Contract

**Inputs**

- `words`: An array of distinct lowercase strings, each with length four.

Each returned square must use four different entries from `words`; a word cannot fill more than one side of the same square.

**Return value**

Return a list of all valid four-word arrays in the role order `[top, left, right, bottom]`. Order that outer list lexicographically by those four positions. Return an empty list when no valid square exists.
