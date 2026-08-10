## General

**Transform every person row independently**

The output keeps `person_id` and replaces the displayed `name` with a formatted string:

$$
\text{name}+\text{"("}+\text{first profession letter}+\text{")"}.
$$

No rows are joined, filtered, grouped, or deduplicated. The source table has one row per unique `person_id`, and every input person should produce exactly one output row.

The `SELECT` list implements this transformation and then the `ORDER BY` clause arranges the finished rows.

**Extract exactly the first profession character**

`SUBSTRING(profession,1,1)` uses MySQL's one-based string positions:

- the first `1` says to begin at the first character;
- the second `1` says to return exactly one character.

Therefore, `"Doctor"` becomes `"D"`, `"Singer"` becomes `"S"`, and so on.

The `profession` column is restricted to the six listed enum values, all of which are non-empty. The extraction always has a first character and needs no conditional handling.

The manifest mentions `LEFT`, and `LEFT(profession,1)` would be equivalent here. The exact stored query uses `SUBSTRING`, so this explanation follows that function.

**Concatenate without spaces**

The expression is

`CONCAT(name,"(",SUBSTRING(profession,1,1),")")`.

`CONCAT` places its arguments directly next to one another. No argument contains a space, so there is no whitespace between the person's name and the opening parenthesis.

For an input row with `name="Tyson"` and `profession="Engineer"`:

1. `SUBSTRING` produces `"E"`;
2. `CONCAT` combines `"Tyson"`, `"("`, `"E"`, and `")"`;
3. the result is `"Tyson(E)"`.

This exactly matches the formatting requirement.

**Why the result is also named `name`**

`AS name` assigns the formatted expression the output-column label `name`. It does not overwrite the source table's stored `name` value. An alias affects only how the query result is presented and how later query clauses may refer to that expression.

The first selected column remains the original `person_id`.

**Order by identifier, not formatted text**

`ORDER BY person_id DESC` sorts rows from the greatest identifier to the smallest. The direction is numeric because `person_id` has integer type.

The formatted name is intentionally not used as the sort key. Alphabetical order could differ completely from the required identifier order.

Because `person_id` is a primary key, no two rows have the same identifier. The requested ordering is therefore fully determined without a secondary tie-breaker.

**Logical query flow**

It is useful to separate two concerns:

1. `FROM Person` provides every source row.
2. `SELECT` projects its identifier and formatted display name.
3. `ORDER BY` arranges the projected result by descending identifier.

Formatting does not affect which rows exist, and sorting does not affect the string generated for any row.

**Walk through the sample**

The source identifiers are 1, 3, 2, 4, 6, and 5. Each row is formatted independently:

- Alex and Singer become `Alex(S)`;
- Alice and Actor become `Alice(A)`;
- Bob and Player become `Bob(P)`;
- Messi and Doctor become `Messi(D)`;
- Tyson and Engineer become `Tyson(E)`;
- Meir and Lawyer become `Meir(L)`.

Descending identifier order then produces 6, 5, 4, 3, 2, 1. The formatting stage and ordering stage together produce the sample table.

**String literals in the exact MySQL query**

The source uses double-quoted literals `"("` and `")"`. In the MySQL mode used by the challenge, these function as string literals. Single quotes are a commonly preferred portable style, but changing quote style is not necessary to understand the stored solution.

**Why no grouping or distinct operation is needed**

The primary-key guarantee means each person appears once. `CONCAT` maps one row to one row and cannot create duplicate identifiers. Even if two people happened to have equal names and professions, they would remain separate output rows because their identifiers differ.

The query should not use `DISTINCT`, which is unnecessary work and could obscure the straightforward row-preserving transformation.

## Complexity detail

Let $r$ be the number of rows and let $C$ be the total number of characters processed from names and professions. Formatting all rows costs $O(C)$ time.

Unless an index can directly provide the required descending order, sorting $r$ rows costs $O(r\log r)$ time and dominates ordinary bounded-length formatting. The database can potentially scan a primary-key index backward, but the portable logical worst-case bound is $O(C+r\log r)$.

Materializing and sorting the result can use $O(r+C)$ space. Exact memory or disk use depends on MySQL's execution plan.

## Alternatives and edge cases

- **`LEFT(profession,1)`:** It is equivalent to the exact `SUBSTRING` call for extracting one leading character.
- **`CONCAT_WS`:** It is unnecessary because no separator should appear between components.
- **Whitespace:** Do not insert a blank before the opening parenthesis.
- **Profession enum:** Every allowed profession is non-empty and contributes one initial.
- **Descending order:** Omitting `DESC` would reverse the required result.
- **Primary-key uniqueness:** No secondary ordering criterion is needed.
- **Same displayed name:** Different `person_id` values still produce separate rows.
- **Alias collision:** `AS name` labels the output and does not mutate the source column.
- **No filtering:** Every person row belongs in the answer.
- **Manifest wording:** The exact query uses `SUBSTRING` rather than `LEFT`, though their result here is the same.
