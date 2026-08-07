## Function Contract

**Inputs**

- `s`: The lowercase input string to match in full.
- `p`: A lowercase pattern that may also contain `?` and `*` wildcards.

Let $n = \lvert s \rvert$ and $m = \lvert p \rvert$.

**Return value**

Return `true` if `p` matches all of `s` under the wildcard rules; otherwise return `false`.
