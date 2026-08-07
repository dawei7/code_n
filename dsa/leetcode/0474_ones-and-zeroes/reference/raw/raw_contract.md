## Function Contract

**Inputs**

- `strs`: the array of nonempty binary strings
- `m`: the maximum total number of `0` characters available
- `n`: the maximum total number of `1` characters available

**Return value**

- Return the maximum cardinality of a subset whose combined zero and one counts stay within their respective
  budgets.

Unused capacity is allowed. The objective counts selected strings, not their characters, and duplicate strings at
different array positions remain separate selectable elements.
