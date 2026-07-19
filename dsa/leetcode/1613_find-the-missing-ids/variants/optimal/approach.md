## General
**Generate the complete bounded ID domain.** A recursive common table expression starts with 1 and repeatedly adds 1 while the current value is below `MAX(customer_id)`. This produces exactly the candidates from 1 through $m`: no lower positive ID is omitted, and the stopping condition prevents values above the existing maximum.

**Apply an anti-join against existing customers.** Left join each generated candidate to `Customers` by ID and keep rows whose customer side is `NULL`. A retained candidate has no matching customer row, while every omitted candidate has a witness in the table. Sorting `candidate_ids.ids` then supplies the required ascending output.

The generated relation covers the entire requested domain once, and the anti-join partitions it into present and missing IDs. Selecting the missing partition is therefore both complete and free of IDs outside the contract.

## Complexity detail
Generating $m$ candidates takes $O(m)$ work. Under a portable indexed or comparison-based join model, matching them against $c$ customer rows and ordering the output fits within $O((m+c)\log(c+1))$ time. The recursive relation, join state, and result may occupy $O(m+c)$ space. Database-specific indexing or hashing can reduce the matching portion toward linear expected time.

## Alternatives and edge cases
- **Numbers table:** Joining a permanent integer table against `Customers` is efficient and avoids recursion, but such a helper table is not part of the supplied schema.
- **Correlated count per candidate:** Testing each generated ID with a fresh scan of `Customers` is correct but can take $O(mc)$ time.
- **Detect only gaps between adjacent IDs:** Window functions can locate gap boundaries, but expanding every multi-ID gap still requires a number generator or recursion.
- If ID 1 is absent, the output begins with 1.
- Consecutive customer IDs produce an empty result.
- A gap can contain several consecutive missing values, all of which must be returned.
- The upper bound is the current maximum ID; no larger positive integers belong in the result.
- Results are ordered numerically by `ids`, not by customer name.
