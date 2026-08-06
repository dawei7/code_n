## Function Contract

**Inputs**

- `word`: The lowercase English word that the abbreviation must represent.
- `abbr`: A string of lowercase English letters and decimal digits to interpret as an abbreviation.

**Return value**

Return `true` exactly when every literal and replacement length in `abbr` consumes all of `word` under the valid
abbreviation rules; otherwise, return `false`.
