## General
**Build one lookup per precedence level.** Store every exact word in a set. Build a lowercase map from each case-insensitive key to its first `wordlist` entry. Build a vowel-error map similarly, using the lowercase word with every vowel replaced by `*` as its key. Insert with `setdefault` so later collisions never replace the required first match.

**Normalize vowel errors without changing structure.** The signature preserves every consonant and the string length while merging all five vowels. Therefore two words share a vowel-error key exactly when case can be ignored and each vowel position may be changed independently to another vowel; missing or extra letters cannot match.

**Resolve each query in priority order.** First test the original query in the exact set. If absent, test its lowercase key, then its vowel signature, and finally use `""`. Because each lower-priority lookup is attempted only after the earlier one fails, an available exact or capitalization match cannot be displaced by a vowel match.

## Complexity detail
Creating keys and processing all words touches each of the $S$ input characters a constant number of times, so expected time is $O(S)$. The exact set, two maps, normalized keys, and result list use $O(S)$ space.

## Alternatives and edge cases
- **Scan `wordlist` per query:** Perform three complete passes for exact, capitalization, and vowel matching. This preserves precedence but takes quadratic time in the list counts.
- **One combined map:** Assigning every key in a single namespace risks collisions between exact, lowercase, and vowel-normalized forms unless rule types are tagged explicitly.
- **Overwriting normalized keys:** Ordinary assignment returns the last matching word, violating the required first-match rule.
- **Exact match priority:** An exact later entry must beat an earlier case-insensitive or vowel-equivalent entry.
- **Different lengths:** Vowel errors replace characters only; they never insert or remove them.
- **No match:** Append an empty string while retaining the query's position in the output.
