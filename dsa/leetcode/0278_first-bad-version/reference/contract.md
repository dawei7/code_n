## Function Contract

**Inputs**

- `n`: The last version number in the range `[1,n]`.
- `bad`: The offline app's hidden boundary used to emulate `isBadVersion`.

**Return value**

Return the first bad version. The native interface receives only `n` and queries the supplied `isBadVersion(version)` API.
