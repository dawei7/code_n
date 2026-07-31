## General

**Accumulate words by sender**

Because each valid message has single separators and no outer spaces, its word
count is one plus its number of spaces. Scan aligned message-sender pairs and
add that count to a hash map keyed by the sender name. Repeated messages from
one sender therefore contribute to the same running total.

**Use the tie rule as part of the ordering**

After aggregation, compare senders by the pair
`(total_word_count, sender_name)`. Maximizing the first component selects the
largest total. When totals tie, maximizing the second component applies the
specified lexicographically larger-name rule directly.

Every message contributes its exact word count once to its actual sender, so
the map totals are correct. The maximum pair then selects precisely the
required sender under both the primary and tie-breaking criteria.

## Complexity detail

Let $L$ be the total number of message characters and $s$ the number of
distinct senders. Counting spaces across all messages takes $O(L)$ time, and
selecting among at most $s \le L$ accumulated entries preserves the $O(L)$
bound. The totals map uses $O(s)$ auxiliary space.

## Alternatives and edge cases

- **Repeated sender rescans:** Searching the complete log separately for every distinct sender is correct but can take $O(ns)$ time.
- **Sort all sender totals:** Sorting works in $O(s \log s)$ after aggregation, but only one maximum is needed.
- **Count spaces:** Under the guaranteed message format, `spaces + 1` is the exact word count without materializing a word list.
- **One sender:** That sender wins regardless of how many messages appear.
- **Equal totals:** The lexicographically larger name wins, not the sender encountered first.
- **Letter case:** Uppercase and lowercase names are distinct, and standard case-sensitive lexicographic ordering applies.
- **Repeated sender:** All of that sender's message counts must be added before comparison.
- **Prefix names:** If one tied name is a prefix of another, the longer name is lexicographically larger.
