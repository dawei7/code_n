## Function Contract

**Inputs**

- `dictionary`: The words used to initialize the abbreviation index.
- `words`: The app adapter's sequence of query words; each is passed to native `isUnique`.

**Return value**

Return one boolean per query in `words`. A result is true exactly when the corresponding query meets the native uniqueness rule.
