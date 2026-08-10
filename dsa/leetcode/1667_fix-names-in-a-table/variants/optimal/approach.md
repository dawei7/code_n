## General

**Normalize the first character separately from the suffix**

The desired name has two case rules:

1. its first character must be uppercase;
2. every remaining character must be lowercase.

The SQL expression constructs those two parts independently and concatenates them:

`CONCAT(UPPER(LEFT(name, 1)), LOWER(SUBSTRING(name, 2)))`.

This is more precise than applying `UPPER` or `LOWER` to the entire name, because neither whole-string operation alone satisfies both requirements.

**Extract and uppercase the first character**

`LEFT(name, 1)` returns the leftmost one-character substring of `name`. Passing that result to `UPPER` ensures it is uppercase. If it was already uppercase, the value is unchanged; if it was lowercase, it is converted.

The input guarantees names consist only of lowercase and uppercase characters, so there are no digits, spaces, punctuation marks, or multiword separators needing a separate policy. SQL’s actual case conversion follows the column’s character set and collation, but for the promised English-style letter data it implements the requested transformation.

**Extract and lowercase everything after it**

MySQL substring positions are one-based. `SUBSTRING(name, 2)` therefore starts at the second character and continues through the end because no length argument is supplied. `LOWER` converts every character of this suffix to lowercase.

For `name = 'aLice'`, the first expression produces `'A'` and the second produces `'lice'`. `CONCAT` joins them into `'Alice'`. For `'bOB'`, the parts become `'B'` and `'ob'`, producing `'Bob'`.

The alias `AS name` is significant. It gives the computed expression the same output column name required by the result schema, rather than exposing a database-generated expression label.

**Preserve identity and produce one row per user**

The query selects `user_id` directly from each row and calculates one normalized `name` from that row’s original value. There is no join, filter, or grouping. Therefore every input user appears exactly once in the result, keeps the same ID, and differs only in name capitalization.

This is a read-only result transformation. It does not execute `UPDATE` and does not modify the stored `Users` table. “Fix” in the problem means return corrected values in the query result.

The source writes `FROM users` with a lowercase table identifier. MySQL table-name case sensitivity depends on the operating system and configuration, but the intended LeetCode environment accepts this reference for the declared `Users` table.

**Guarantee the required order**

`ORDER BY user_id` sorts the final rows by ascending user ID because ascending is SQL’s default direction. The primary-key guarantee means user IDs are unique, so the ordering key has no ties and the result order is fully determined.

Ordering is applied after the select expressions conceptually. It changes only row sequence, not the normalized value computed for any user.

**Why the query is correct**

For each input row, `LEFT(name, 1)` isolates exactly the character that must be uppercase, and `UPPER` establishes that case. `SUBSTRING(name, 2)` isolates exactly all remaining characters, and `LOWER` establishes their required case. `CONCAT` places the two transformed parts back in their original positional order without a separator. Thus the output name has an uppercase first character and a lowercase remainder.

Since the query neither filters nor duplicates rows, this corrected name is paired with exactly its original `user_id`. Finally, `ORDER BY user_id` satisfies the output-order requirement. Those facts prove that every result row and the result sequence are correct.

## Complexity detail

Let `R` be the number of rows and let `C` be the total number of characters across all names. Every name character must be read and case-normalized, so expression evaluation costs $O(C)$ time. If name lengths are treated as bounded, this is often summarized as $O(R)$.

Ordering complexity depends on the physical execution plan. Because `user_id` is the primary key, a database can scan its index in ascending order and produce rows in $O(R + C)$ time without a separate sort. If the optimizer instead reads rows in another order and sorts them, ordering can cost $O(R\log R)$ time and $O(R)$ working space.

The scalar string functions require space proportional to the current transformed name, while the result contains $O(C)$ characters. Under an ordered index scan, the query can stream rows with constant administrative working state apart from the current row and output. The manifest’s $O(1)$ space convention excludes result storage and assumes no materialized sort; physical database memory remains plan dependent.

## Alternatives and edge cases

- **`SUBSTRING(name, 1, 1)` instead of `LEFT`:** This extracts the same first character and matches the editorial formulation; the rest of the query is unchanged.
- **Capitalize-style function:** Some environments provide a direct capitalization helper, but MySQL does not offer the same simple standard function used by Pandas, so composing `UPPER`, `LOWER`, and substrings is portable within MySQL.
- **Update the table:** An `UPDATE` statement would mutate source data and would not itself return the required ordered result. The task asks for a query result, so `SELECT` is appropriate.
- **Already normalized name:** Uppercasing the first character and lowercasing the suffix are idempotent, so a value such as `'Alice'` stays `'Alice'`.
- **All-uppercase input:** The first character remains uppercase and every later character becomes lowercase.
- **All-lowercase input:** Only the first character changes to uppercase.
- **Single-character name:** `LEFT(name, 1)` returns that character, while `SUBSTRING(name, 2)` returns the empty string. Concatenation therefore returns the correctly uppercased one-character name.
- **Empty name outside the stated model:** The local schema text does not give a length bound. If empty strings were allowed, both extracted parts would be empty and the output would remain empty, so no first character could be capitalized.
- **`NULL` name outside the stated model:** MySQL string functions and `CONCAT` would propagate `NULL`. The problem describes each row as containing a name and does not ask for null handling.
- **Unique IDs:** The primary key eliminates ordering ties, so no secondary sort key is necessary.
- **Case-sensitive table identifiers:** Using the declaration’s exact `Users` capitalization would be safer across arbitrary MySQL installations, though the exact source uses `users` and is accepted in its target environment.
- **Result storage:** Even when working memory is described as constant, returning `R` rows and their normalized strings necessarily occupies output space proportional to the result size.
