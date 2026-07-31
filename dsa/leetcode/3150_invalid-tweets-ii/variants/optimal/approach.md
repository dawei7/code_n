## General

Evaluate the three invalidity rules as one disjunction. `CHAR_LENGTH(content)` gives the character count directly. To count occurrences of a marker, remove that marker with `REPLACE`; the difference between the original and shortened character lengths is exactly the number removed.

For example,

$$
\operatorname{count}_{@}(c)
= \operatorname{length}(c)-\operatorname{length}(\operatorname{replace}(c, @, \varepsilon)).
$$

Apply the same expression to `#`. Retain a row when the content length is greater than 140, the mention count is greater than three, or the hashtag count is greater than three. Because this is one row filter, a tweet violating multiple rules is still emitted once. Project only `tweet_id` and sort ascending to meet the output contract.

Each returned identifier is invalid because at least one exact predicate held. Conversely, every invalid tweet is scanned and satisfies its defining predicate, so the disjunction retains it. The final projection and ordering therefore produce precisely the requested result.

## Complexity detail

Let $R$ be the number of rows in `Tweets`, and let $S$ be the total number of characters across all `content` values. Character measurement and replacement examine $O(S)$ text. In the absence of an order-providing primary-key scan, sorting the retained identifiers costs $O(R\log R)$, for total time $O(S + R\log R)$.

The database may materialize and sort up to $R$ identifiers, giving $O(R)$ auxiliary working space. Temporary replacement strings are bounded by the content already included in $S$ and do not increase the asymptotic bound.

## Alternatives and edge cases

- **Repeated-marker `LIKE` patterns:** Patterns such as `'%@%@%@%@%'` also recognize at least four markers in one scan, but length differences state the counting operation more directly.
- **Correlated row counting:** Adding a per-tweet subquery or self-join can preserve the result while creating quadratic work; it is the principal slower benchmark comparison.
- **`UNION` three filters:** Querying one rule at a time and unioning identifiers is correct with duplicate elimination, but scans the table repeatedly and makes ordering more cumbersome.
- Every threshold is strict: 140 characters, three mentions, and three hashtags are still valid at that boundary.
- The rules are joined by `OR`; exceeding any one threshold is sufficient.
- A tweet violating several rules appears once because the query filters rows rather than combining separate result sets.
- Physical row order is irrelevant; the final `ORDER BY tweet_id ASC` is mandatory.
- An empty table or a table containing only valid tweets returns the `tweet_id` column with no rows.
