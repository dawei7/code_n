## General

**Filter to addresses ending in the required suffix.** `WHERE email LIKE '%.com'` keeps strings whose final characters are `.com`. The leading percent wildcard can match any preceding text, including the local part and domain prefix.

Because the address itself ends where its domain ends, filtering the complete email suffix is equivalent to filtering extracted domains for valid email input.

**Extract everything after the final at-sign.** MySQL's

`SUBSTRING_INDEX(email, '@', -1)`

splits conceptually on `@` and, because count is $-1$, returns the portion after the last delimiter. For `adcmaf@outlook.com`, this is `outlook.com`.

Valid email addresses contain the separator expected by the task. Using the last at-sign also behaves sensibly if the local portion were ever allowed to contain an at-sign under a broader format.

**Group equal domains.** `GROUP BY 1` groups on the first selected expression, the extracted `email_domain`. Every address with the same domain contributes to the same group.

`COUNT(1)` counts rows in that group, representing individuals because each source row has a unique primary-key `id`. The query counts people/rows, not distinct email strings. If two different IDs share an identical address, both count as individuals.

**Sort the grouped domains.** `ORDER BY 1` orders the extracted domain ascending. The reference says emails contain no uppercase letters, so case-normalization is unnecessary; exact collation details still follow the database's configured string collation.

**A trace.** Addresses `adcmaf@outlook.com` and `zxcf@outlook.com` both survive the suffix filter and extract to `outlook.com`, forming count two. `vrzmwyum@yahoo.com` forms count one. Addresses ending `.edu` or `.org` are removed before grouping.

**Why extraction can appear directly in grouping.** MySQL permits select-list ordinals in `GROUP BY`. There is no need for a CTE that first names the domain, though such a CTE could improve readability. The engine logically evaluates the same deterministic expression for grouping.

**Meaning of “unique domains.”** Unique refers to one output row per domain, not to domains appearing only once. A domain with many individuals remains one group with a larger count.

**Suffix nuance.** The pattern accepts any string ending in the four characters `.com`. It would accept unusual but syntactically possible nested domains such as `service.example.com`, which is correct because that full extracted domain ends in `.com`. It does not accept `example.com.org`.

The exact source does not separately validate that an `@` exists or that the domain is nonempty. It relies on the reference's email-data guarantee.

## Complexity detail

Let $R$ be the number of email rows, $S$ the total number of characters scanned, and $G$ the number of qualifying domains. Suffix matching and extraction cost $O(S)$ logically. Grouping costs expected $O(R)$ with hashing, and ordering $G$ groups costs $O(G\log G)$.

Group state uses $O(G)$ space. Physical MySQL behavior depends on collation, indexes, expression evaluation, and whether grouping/sorting spills to disk.

The query is read-only and returns one row per qualifying domain.

## Alternatives and edge cases

- **CTE for extracted domains:** Compute `email_domain` once, filter it, then group. This can make the operation order clearer but is not required.
- **`RIGHT(email,4)='.com'`:** It expresses the suffix test directly; `LIKE` is concise and equivalent for this literal suffix.
- **Filter after extraction:** It may be clearer semantically, especially if malformed email input is possible.
- **Multiple users on one domain:** They form one row with count equal to their number.
- **Same email under different IDs:** Both rows count because the task asks for individuals.
- **Subdomain ending in .com:** It remains a distinct full domain group, such as `mail.example.com`.
- **Uppercase domain:** The reference excludes uppercase addresses, so no normalization is needed.
- **Missing at-sign:** `SUBSTRING_INDEX` would return the whole string; valid-email assumptions prevent this.
- **No qualifying domains:** The result is empty.
- **Ordering:** `ORDER BY 1` sorts by the selected domain expression ascending.
- **Why the local part is discarded completely:** Individuals are grouped by the organization/provider portion after `@`. Different usernames such as `a@example.com` and `b@example.com` correctly enter the same domain group.
- **Exact suffix, not substring containment:** `example.com.au` contains `.com` but does not end with it and is excluded, while `service.example.com` is included.
- **Primary key role:** Unique `id` values identify source individuals. The query does not need to select or group by IDs because each row contributes exactly one unit to its domain count.
- **Alias `count`:** Although `COUNT` is a function name, using lowercase `count` as a select alias is accepted in this context and matches the requested output column.
- **Collation and uniqueness:** Domains differing only by case could group together under a case-insensitive collation, but the source guarantee that emails contain no uppercase letters removes that ambiguity.
- **Filter-before-group benefit:** Non-.com rows are discarded before aggregation, so they consume no domain-group state and cannot affect counts for qualifying domains.
- **Negative substring index:** The `-1` argument selects the text after the final at-sign, which is the domain portion under the valid-email guarantee.
