## Function Contract

**Inputs**

- `s`: A nonempty lowercase English string whose maximal equal-character runs are examined.

Every position belongs to exactly one run. Run identity depends on maximal boundaries and its character, but selection compatibility depends only on run length.

**Return value**

Return the highest frequency of any run length in `s`. Runs may contain different letters; they need only have the same number of characters.
