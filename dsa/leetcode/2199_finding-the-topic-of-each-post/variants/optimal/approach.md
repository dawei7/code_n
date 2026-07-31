## General

**Turn word boundaries into spaces**

Because post content contains only letters and spaces, a keyword is a complete word exactly when it appears with a space on both sides after the post is padded at both ends. Lowercase both operands for the required case-insensitive comparison. This prevents a keyword such as `war` from matching `warning`, while still matching `WAR`, a first word, or a last word.

Left-join every post to matching keyword rows. The outer join is essential: a post with no match must remain in the result so it can receive `Ambiguous!`.

**Aggregate topics, not keyword matches**

Several words can identify the same topic, and one repeated topic must appear only once. Aggregate distinct `topic_id` values for each post, order them numerically, and join them with commas. If the aggregate is null because the outer join found no keyword, replace it with `Ambiguous!`.

The join condition creates a row exactly when a keyword occurs as a complete case-insensitive word. Therefore the distinct topic IDs associated with each post are precisely its topics. Numeric ordering and comma aggregation produce the required nonduplicated string, while retaining unmatched posts and replacing their null aggregate handles the ambiguous case.

## Complexity detail

Without a specialized full-text index, the join may compare every post with every keyword and scan up to $L$ characters, costing $O(pkL)$. Deduplicating and ordering $t$ matched post-topic pairs costs up to $O(t\log t)$, for total time $O(pkL+t\log t)$.

The materialized matches and aggregation state use $O(t)$ space. Exact query plans and temporary storage remain database-engine dependent.

## Alternatives and edge cases

- **Raw substring matching:** Searching for `%keyword%` without padded spaces incorrectly matches prefixes and embedded text such as `war` in `warning`.
- **Tokenizing posts first:** Splitting every post into rows and joining tokens by equality is also sound, but requires engine-specific tokenization machinery.
- **Inner join:** An inner join silently drops posts without topics instead of labeling them `Ambiguous!`.
- **Multiple keywords for one topic:** Distinct aggregation is required so a post containing two synonymous keywords does not repeat the topic ID.
- **One keyword for multiple topics:** Every associated topic row must survive; the output can contain several IDs from one matched word.
- **Numeric ordering:** Topic IDs must sort as integers, so `2` precedes `10`.
