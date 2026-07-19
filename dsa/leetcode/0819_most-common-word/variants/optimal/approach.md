## General
**Treat every nonletter as a word boundary**

Scan a lowercase version of the paragraph one character at a time. Accumulate consecutive letters into the current word. On punctuation, whitespace, or a sentinel appended after the paragraph, finish that word and clear the buffer. The sentinel ensures the final word is processed even when the paragraph has no trailing punctuation.

**Exclude banned words before counting**

Store the banned words in a hash set. When a token ends, ignore it if it is banned; otherwise increment its frequency in a hash map. Set lookup prevents the banned list from adding a multiplicative scan for every token.

**Maintain the winner while frequencies change**

Whenever a word's count is incremented, compare that count with the best count seen so far and update the answer when it becomes larger. The contract guarantees a unique most frequent allowed word, so no tie-breaking rule is needed. Every paragraph token is normalized and counted exactly once, and the maintained maximum therefore ends at the required word.

## Complexity detail
Let `p` be the paragraph length, `b` the total size of the banned input, and `u` the number of distinct allowed words. Building the banned set and scanning all characters takes $O(p + b)$ expected time. The banned set, frequency map, and current token use $O(u + b)$ entries plus at most one word's characters.

## Alternatives and edge cases
- **Regular-expression tokenization:** Extracting `[a-z]+` after lowercasing is concise and has the same asymptotic behavior, but materializes the complete token list.
- **Count then call `max`:** Building all frequencies before selecting the winner is also linear and may be clearer when streaming is unnecessary.
- **Repeated list counting:** Calling `words.count(word)` for every occurrence is correct but can take $O(w^2)$ for `w` tokens.
- **Mixed case:** Normalize before banned-set lookup and counting.
- **Adjacent punctuation:** Empty buffers between delimiters do not represent words and are ignored.
- **Final word without punctuation:** The sentinel boundary flushes it.
- **Banned frequent word:** Exclude it entirely rather than counting it and choosing the next word afterward.
