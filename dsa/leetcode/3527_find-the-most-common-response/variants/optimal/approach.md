## General

The frequency is a count of days, not a count of raw entries. Convert each daily list to a set before updating the global frequency map. This ensures that one response adds at most one to its count for a particular day, while naturally allowing it to add again on another day.

After all days are processed, every map value is exactly the number of deduplicated daily lists containing that response. Select the key with the largest frequency. Encoding the ordering key as the negative frequency followed by the response itself turns the requirement into one minimum operation: higher frequencies compare first, and equal frequencies use ordinary lexicographic order.

## Complexity detail

Let $S$ be the total number of response occurrences across all daily lists and $U$ the number of distinct response strings. With expected constant-time hashing and the problem's bounded string length, daily set construction and counting take $O(S)$ expected time. Selecting the winner examines at most $U$ keys, so the total remains $O(S)$. The current daily set and global frequency map contain at most $U$ strings, requiring $O(U)$ auxiliary space.

## Alternatives and edge cases

- **Count every raw entry:** A single day's duplicates would be overcounted and can change the winner, so global counting without daily sets is incorrect.
- **Repeated list scans:** Counting each candidate by scanning all deduplicated responses is correct but can take $O(S^2)$ time.
- **Global deduplication:** Removing duplicates across all days loses the number of distinct days on which a response appeared.
- **Frequency tie:** Compare response strings only after their final frequencies are known; the lexicographically smallest tied response wins.
- **One distinct response:** The frequency map is non-empty under the contract, so the sole response is returned directly by the same selection rule.
