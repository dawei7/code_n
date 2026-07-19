## General
**Separate the three fixed-format fields**

Splitting on spaces produces `day`, `month`, and `year`. The year already has the required four digits. A fixed lookup table maps each month abbreviation to its two-digit position, avoiding locale-sensitive date parsing.

The final two characters of the day field are always its ordinal suffix. Remove those characters, parse the remaining one- or two-digit number, and format it with width two. This handles every suffix uniformly: the algorithm does not need separate rules for `st`, `nd`, `rd`, and `th` because the input is guaranteed valid.

Finally, join the unchanged year, mapped month, and padded day with hyphens. Each output field then has exactly the required width and represents the same date.

**Why fixed parsing is sufficient**

There are always three fields in the same order, the month spelling comes from a closed twelve-item set, and the day suffix always occupies exactly two characters. Therefore every extraction uses a guaranteed boundary. The transformation changes only notation; it neither computes weekdays nor validates month lengths.

## Complexity detail
Every legal input has at most 13 characters, and the month table always has twelve entries. Splitting, looking up the month, converting the day, and constructing the ten-character result therefore perform bounded work independent of a scalable input quantity, giving $O(1)$ time.

The parsed fields, fixed month table, and output occupy bounded space, so auxiliary space is $O(1)$. A `bounded_domain` certificate replaces runtime scaling because the source contract cannot produce growing legal inputs.

## Alternatives and edge cases
- **Month-list search:** store the abbreviations in calendar order and use the index plus one. This is still constant time because there are exactly twelve months, though a direct map states the conversion more explicitly.
- **Date-library parsing:** a library can parse and reformat the date, but ordinal suffixes may require preprocessing and locale behavior adds unnecessary complexity.
- **Conditional month chain:** twelve `if` branches avoid a collection but are longer and easier to mistype than a lookup table.
- **Single-digit days:** values such as `6th` must become `06`, not `6`.
- **Ordinal exceptions:** `11th`, `12th`, and `13th` are already valid inputs; removing the final two characters works without reproducing suffix grammar.
- **Boundary years:** years 1900 and 2100 remain unchanged because they already contain four digits.
- **January and December:** the lookup must map the endpoints to `01` and `12`.
- **Calendar validity:** the contract guarantees a real date, so the solution should not reject or normalize the supplied fields.
