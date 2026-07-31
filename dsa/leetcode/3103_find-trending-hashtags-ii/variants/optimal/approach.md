## General

**Emit every hashtag occurrence.** A row cannot be reduced to one token because a tweet may contain several hashtags. The native MySQL query starts each tweet at occurrence one and uses a recursive CTE to request occurrence two, three, and so on from `REGEXP_SUBSTR`. Recursion continues while the previously requested occurrence exists. The pattern `#[^ ]+` deliberately stops only at a space: restricting it to letters, digits, or underscores would change valid non-space hashtag tokens.

The app-local SQLite artifact implements the same contract with the functions available in the packaged runtime. Its recursive CTE splits every February tweet into space-delimited words, then keeps every word beginning with `#`. Appending one terminal space makes the final word follow the same transition as every earlier word, and `LTRIM` prevents repeated spaces from producing a stalled recursion.

**Aggregate only after expansion.** The expanded relation has one row per hashtag occurrence, including repeated uses of the same hashtag within one tweet. Group by the complete token and use `COUNT(*)`, so each emitted occurrence contributes exactly once. Tweets without a hashtag emit no grouped row.

Finally, order groups by the count descending and the hashtag descending, then apply `LIMIT 3`. Limiting after aggregation and both sort keys yields the requested global top three and makes ties deterministic. Because expansion emits exactly the source occurrences and grouping partitions them by token equality, every reported count is exact.

## Complexity detail

Let $S$, $h$, and $g$ have the meanings defined in the function contract. Token scanning takes $O(S)$ work, and aggregation processes $h$ emitted occurrences. A general database engine may sort the $g$ groups in $O(glog g)$ time, so the overall bound is $O(S+h+glog g)$. Recursive rows, grouped counts, and sort state require $O(S+h+g)$ working space in the worst case.

## Alternatives and edge cases

- **Extract only one occurrence:** A single `REGEXP_SUBSTR` call per tweet solves the earlier one-hashtag variant but silently ignores later hashtags here.
- **Fixed occurrence numbers:** Unioning the first two or three regex matches fails when a tweet contains more hashtags than the chosen cap.
- **Correlated counting:** Re-expanding all tweets separately for every distinct hashtag is correct but can repeat the full scan and approach quadratic work.
- **Alphanumeric-only pattern:** A pattern such as `#[A-Za-z0-9_]+` truncates a valid hashtag containing another non-space character.
- **Limit before grouping:** Truncating expanded rows cannot determine the most frequent tokens in the complete table.
- **Repeated hashtag in one tweet:** Each occurrence is counted; the query must not deduplicate by `tweet_id` and hashtag.
- **No hashtags:** Such a tweet contributes no occurrence and does not create a null group.
- **Fewer than three groups:** Return every available group without manufacturing extra rows.
- **Equal counts:** The hashtag text is the required descending secondary key.
