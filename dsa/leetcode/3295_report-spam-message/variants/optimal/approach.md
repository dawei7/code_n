## General

Insert every value from `bannedWords` into a hash set so each message word can be tested by exact membership. Duplicate entries in `bannedWords` collapse harmlessly because they do not change which values are banned.

Scan `message` and increment a counter for each word present in the set. Return `true` immediately when the counter reaches two. Each increment corresponds to a distinct message position, so repeated occurrences of one banned value are counted separately exactly as the contract requires. If the scan ends first, at most one message word matched and the answer is `false`.

## Complexity detail

Let $m$ and $b$ be the numbers of message and banned words. Because each word has length at most 15, hashing a word is bounded; expected time is $O(m+b)$ under standard hash-set behavior. The set stores at most $b$ distinct words, giving $O(b)$ auxiliary space.

## Alternatives and edge cases

- **Nested scans:** Comparing every message word with every banned word takes $O(mb)$ time and is unnecessary.
- **Count distinct matching values:** This is incorrect because two message positions containing the same banned word still make the message spam.
- **Duplicate banned entries:** They do not create matches by themselves and naturally collapse in the set.
- **Exactly one match:** One matching position is insufficient, even if that word appears many times in `bannedWords`.
- **Early second match:** Returning immediately avoids scanning the rest of a message once the verdict is fixed.
