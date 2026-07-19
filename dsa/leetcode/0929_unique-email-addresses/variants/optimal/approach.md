## General
**Keep the domain unchanged.** Split each address once at `@`. The right-hand domain is copied exactly, including all of its periods and any allowed characters, because normalization rules apply only to the local name.

**Canonicalize the local name in rule order.** Discard the first `+` and everything following it from the local portion, then remove every `.` from what remains. Applying the operations in this order makes the ignored suffix irrelevant and produces one canonical local name for every set of equivalent spellings. Combine that local name with `@` and the original domain.

**Count canonical recipients with a set.** Insert each normalized address into a hash set. Equivalent inputs produce the same set entry, whereas a different normalized local name or a different domain remains distinct. The final set size is therefore exactly the number of recipients.

## Complexity detail
Splitting and normalizing examines each of the $S$ input characters a constant number of times, for $O(S)$ time. In the worst case all normalized addresses are distinct and their stored text totals $O(S)$ space.

## Alternatives and edge cases
- **Pairwise normalized comparison:** Store normalized strings in a list and compare each new address with all earlier recipients. It is correct but can become quadratic in the number and length of addresses.
- **Character-by-character parser:** Build the normalized local name while scanning until `@`, skipping periods and ignoring characters after `+`. This has the same asymptotic bounds and can avoid temporary substrings.
- **Periods in the domain:** They must be preserved; removing them would incorrectly merge different domains.
- **Multiple plus characters:** The first plus begins the ignored suffix, so later pluses have no additional effect.
- **No special characters:** The address is already canonical and is still inserted normally.
