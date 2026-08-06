## Function Contract

**Inputs**

- `s`: the nonempty lowercase English string to encode

**Return value**

- Return a minimum-length valid encoding whose decoded value is exactly `s`.

An encoded region has the form `k[encoded_string]`, where positive integer `k` is the number of consecutive copies
of the decoded bracketed string. Do not use that form for a region unless it is strictly shorter than leaving the
same region literal.
