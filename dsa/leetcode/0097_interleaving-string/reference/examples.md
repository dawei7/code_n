## Examples

**Example 1**

- Input: `s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"`
- Output: `true`
- Explanation: Split `s1` as `"aa" + "bc" + "c"` and `s2` as `"dbbc" + "a"`. Alternating those chunks gives `"aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac"`, exactly `s3`.

```text
s1: [ aa ]        [ bc ]     [ c ]
s2:       [ dbbc ]      [ a ]
    --------------------------------
s3:   aa     dbbc    bc    a     c
```

**Example 2**

- Input: `s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"`
- Output: `false`
- Explanation: No interleaving of `s2` with `s1` can produce `s3` while preserving both source orders.

**Example 3**

- Input: `s1 = "", s2 = "", s3 = ""`
- Output: `true`
