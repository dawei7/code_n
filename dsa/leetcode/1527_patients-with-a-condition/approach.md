## General

**Condition codes have token boundaries**

`conditions` stores zero or more codes separated by spaces. A Type I Diabetes code is any token whose beginning is `DIAB1`. The text must therefore match in one of two places:

- At the beginning of the entire conditions string.
- Immediately after a separating space.

The stored SQL translates those cases directly:

`conditions LIKE 'DIAB1%'`

or

`conditions LIKE '% DIAB1%'`.

The percent sign in `LIKE` matches any sequence of characters, including an empty sequence.

**Understanding the first pattern**

`'DIAB1%'` requires the string's first five characters to be `DIAB1`. Anything may follow, so codes such as `DIAB100` qualify. This is correct because the rule specifies a prefix, not a complete code equal to five characters.

It rejects `XDIAB100` because the required prefix is not at the string start.

**Understanding the second pattern**

`'% DIAB1%'` finds a literal space followed immediately by `DIAB1` anywhere in the string. The leading wildcard permits earlier condition tokens. The trailing wildcard permits the rest of that code and any later tokens.

For `ACNE DIAB100`, the substring ` DIAB1` exists, so the row qualifies. For `PREDIAB100`, no separating space occurs immediately before `DIAB1`, so it does not match unless the whole string itself begins with the prefix, which it does not.

Multiple spaces before a code still contain some final space directly followed by `DIAB1`, so the second pattern can match.

**Why OR is required**

A first token has no preceding space, so the second pattern alone would miss it. A later token does not begin the whole field, so the first pattern would miss it. `OR` includes either valid token position.

The query selects exactly `patient_id`, `patient_name`, and `conditions`. It adds no ordering because result order is unrestricted.

**Why the patterns are complete**

Any valid matching code is one token in a space-separated list. If it is the first token, its prefix begins at string position zero and the first pattern matches. Otherwise, the token begins immediately after a separator space and the second pattern matches.

Conversely, either pattern guarantees `DIAB1` begins at a valid token boundary. Characters after the prefix belong to the same code or later text, both allowed. Therefore, returned rows have the required condition.

**Case-sensitivity caveat**

MySQL `LIKE` follows the column's collation. Many default collations are case-insensitive, which could make lowercase `diab1` match even though the literal is uppercase.

If the data contract guarantees standardized uppercase condition codes, this does not affect valid inputs. If exact case must be enforced against arbitrary data, a binary collation or `BINARY conditions` should be used. The exact stored query does not request that explicitly.

**Table-name portability**

The source uses lowercase `patients` while the reference calls the table `Patients`. MySQL table-name case sensitivity can depend on operating system and configuration. The expected judge environment accepts the query, but production SQL should use the canonical schema spelling consistently.

**Why no ending boundary is required after DIAB1**

The medical rule says a qualifying code starts with `DIAB1`; it does not say the entire code equals `DIAB1`. Therefore, the query must allow additional code characters immediately afterward. The trailing percent wildcard does exactly that.

The only boundary that matters is before the prefix, where the code token begins. For example, `DIAB100` and `DIAB1ABC` both satisfy the stated prefix rule. Requiring a space or end of string immediately after the digit one would incorrectly reject them. Later spaces are simply consumed by the wildcard along with any following codes.

## Complexity detail

Let $N$ be the number of patient rows and $S$ the total number of characters in all condition strings. Because both patterns begin with or contain wildcards and inspect text, a typical plan scans rows and examines strings, requiring roughly $O(S)$ matching work.

There is no explicit sort, so the manifest's $O(S+N\log N)$ bound is conservative rather than directly caused by an `ORDER BY`. Actual SQL performance depends on collation, storage, indexes, optimizer behavior, and output materialization.

The result can contain $O(N)$ rows. Pattern evaluation itself uses bounded engine state for these simple wildcards, while output storage or transfer scales with matches.

## Alternatives and edge cases

- **Regular expression boundary:** `(^|[[:space:]])DIAB1` expresses the two positions in one pattern and can recognize broader whitespace.
- **Tokenized normalized table:** Store one condition code per row linked to a patient. Queries and indexes become cleaner, but the schema changes substantially.
- **BINARY LIKE:** Apply binary comparison when exact uppercase matching must be guaranteed independently of collation.
- **Condition at string start:** The first pattern finds it without requiring a leading space.
- **Condition after another code:** The second pattern finds the space-delimited prefix.
- **DIAB1 inside another token:** It is rejected because there is no valid boundary immediately before it.
- **Code longer than five characters:** It qualifies because `DIAB1` is a prefix.
- **Empty conditions string:** Neither pattern matches.
- **Null conditions:** Both predicates evaluate to unknown, so the row is excluded.
- **Several matching codes:** The patient row is still returned once because filtering does not join or duplicate rows.
- **Unrestricted order:** No `ORDER BY` is needed.
