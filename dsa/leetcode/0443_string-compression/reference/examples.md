## Examples

**Example 1**

- Input: `chars = ["a","a","b","b","c","c","c"]`
- Output: `6`
- Explanation: The consecutive groups are `"aa"`, `"bb"`, and `"ccc"`, which encode as `"a2b2c3"`. After the in-place modification, the meaningful six-character prefix is `["a","2","b","2","c","3"]`.

**Example 2**

- Input: `chars = ["a"]`
- Output: `1`
- Explanation: The only group has length one, so it remains uncompressed. The meaningful prefix is `["a"]`.

**Example 3**

- Input: `chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]`
- Output: `4`
- Explanation: The groups are `"a"` and twelve consecutive `"b"` characters, producing `"ab12"`. The first four positions therefore contain `["a","b","1","2"]`.
