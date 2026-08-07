## Function Contract

**Inputs**

- `emails`: A nonempty array of valid email-address strings.

Each address has exactly one `@`, separating a nonempty local name from a
nonempty domain name. Define the total character count

$$
S = \sum_{e \in \texttt{emails}} \lvert e \rvert.
$$

Normalization is case-insensitive in both parts, but the dot-removal and
plus-suffix rules apply only to the local name.

**Return value**

Return the number of distinct normalized addresses, which is the number of
unique email groups.
