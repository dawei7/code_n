## General
**Exploit increasing operation times**

Every new expiration equals the current operation time plus the fixed TTL. Because operation times strictly increase, expirations assigned by successive generate or renew calls also strictly increase. Tokens can therefore be maintained in expiration order without a heap or a general sort.

Use an insertion-ordered mapping from token identifier to expiration. It provides direct identifier lookup while its first entry is always the next token due to expire.

**Discard only the expired prefix**

Before each public operation, inspect the mapping's first entry. While its expiration is less than or equal to `currentTime`, remove it. Stop at the first greater expiration; every later entry has an even later expiration and must also be unexpired.

This boundary implements the rule that expiration occurs before another action at the same time. Each token entry is removed at most once, so a cleanup that removes several entries charges its work to earlier insertions.

**Renew by moving the token to the end**

After cleanup, a token is renewable exactly when its identifier remains in the mapping. Replace its expiration with `currentTime + timeToLive` and move the entry to the end, where it belongs because the new expiration exceeds all previously assigned expirations.

Generation appends a new unique identifier in the same way. Counting cleans the expired prefix and returns the mapping size. The mapping consequently contains exactly all unexpired tokens after every operation, in increasing expiration order, which proves every renewal decision and count is correct.

## Complexity detail
Direct lookup, insertion, renewal, moving an entry, and reading the mapping size are $O(1)$ expected time. Cleanup may remove several tokens in one call, but each generated token can be removed only once. Across $Q$ method calls the total cleanup work is $O(Q)$, so each operation is $O(1)$ amortized and the complete sequence takes $O(Q)$ time. Only unexpired token entries are retained, requiring $O(A)$ space.

## Alternatives and edge cases
- **Hash map plus full count scan:** Generation and renewal are constant-time, but every count examines all stored tokens and can make a long sequence quadratic.
- **Hash map plus min-heap:** Lazy heap entries support $O(\log A)$ updates and expiration, but renewals leave stale entries and the ordering guarantee permits a simpler constant-amortized structure.
- **Deque plus hash map:** Appending expiration records also uses monotonic times, but renewals create stale deque records and can use $O(Q)$ rather than $O(A)$ space.
- **Expiration at the action time:** Treat `expiration <= currentTime` as expired before renewal or counting.
- **Missing or expired renewal:** Ignore it without creating a token.
- **Renewal reordering:** Moving a renewed early token to the end is essential because its new expiration is now the latest.
- **Several expired tokens:** Remove the entire expired prefix, not just one entry.
- **Unique generation IDs:** Generation never replaces an existing token, while renewal is the only operation that updates one.
