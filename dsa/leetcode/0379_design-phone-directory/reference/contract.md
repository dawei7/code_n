## Function Contract

**Inputs**

- `max_numbers`: The cOde(n) form of `maxNumbers`, defining slots `0` through `maxNumbers - 1`.
- `operations`: An ordered list of `["get"]`, `["check", number]`, and `["release", number]` calls.

**Return value**

The app adapter returns results for `get` and `check` calls in order. On LeetCode, construct `PhoneDirectory(maxNumbers)` and invoke its methods directly; `release` has no return value.
