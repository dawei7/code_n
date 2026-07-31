## Function Contract

**Inputs**

- `n`: The inclusive upper bound of the search range.
- `pick`: Only the app adapter receives the hidden chosen number so it can emulate `guess`; the native LeetCode method receives only `n`.

**Return value**

Return the fixed hidden number identified through the `guess(num)` responses.
