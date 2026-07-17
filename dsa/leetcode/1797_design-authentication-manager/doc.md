# Design Authentication Manager

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/design-authentication-manager/) |
| Frontend ID | 1797 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Linked List, Design, Doubly-Linked List |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Design an authentication system whose tokens remain valid for a fixed number of seconds. Constructing the manager receives `timeToLive`. A token generated with identifier `tokenId` at `currentTime` expires at `currentTime + timeToLive`.

An unexpired token may be renewed, replacing its expiration with `currentTime + timeToLive`. Renewing an identifier that does not exist or has already expired has no effect. A count operation must return how many tokens are still unexpired at its supplied time.

Expiration happens before any action at the same timestamp. Thus a token with expiration time $t$ is invalid when a renewal or count occurs at time $t$. All operation times are strictly increasing, and every generated identifier is unique.

### Function Contract

**Inputs**

- `AuthenticationManager(timeToLive)` creates an empty manager, where $1 \le \texttt{timeToLive} \le 10^8$.
- `generate(tokenId, currentTime)` creates a unique lowercase identifier of length at most five with expiration `currentTime + timeToLive`.
- `renew(tokenId, currentTime)` extends that token only if its current expiration is strictly greater than `currentTime`.
- `countUnexpiredTokens(currentTime)` reports the number of tokens whose expiration is strictly greater than `currentTime`.
- Operation times satisfy $1 \le \texttt{currentTime} \le 10^8$ and are strictly increasing. Let $Q \le 2000$ be the number of method calls and $A$ the maximum number of simultaneously unexpired tokens.

**Return value**

- Construction, generation, and renewal return no value.
- Each count operation returns the current number of unexpired tokens.
- In the app-local sequence interface, return one result per operation, using `null` for methods with no return value.

### Examples

**Example 1**

- Input: `operations = ["AuthenticationManager","renew","generate","countUnexpiredTokens","generate","renew","renew","countUnexpiredTokens"]`
- Arguments: `[[5],["aaa",1],["aaa",2],[6],["bbb",7],["aaa",8],["bbb",10],[15]]`
- Output: `[null,null,null,1,null,null,null,0]`

The missing first renewal is ignored; `"aaa"` later expires, while `"bbb"` is renewed to expire exactly at time `15`.

**Example 2**

- Input: generate `"abc"` at time `1` with TTL `5`, then count at time `6`
- Output: `0`

Expiration at time `6` occurs before the count at that same time.

**Example 3**

- Input: generate at time `1`, renew at time `5`, and count at times `9` and `10` with TTL `5`
- Output: `1` at time `9`, then `0` at time `10`

The renewal replaces the old expiration with time `10`.

### Required Complexity

- **Time:** $O(Q)$
- **Space:** $O(A)$

<details>
<summary>Approach</summary>

#### General

**Exploit increasing operation times**

Every new expiration equals the current operation time plus the fixed TTL. Because operation times strictly increase, expirations assigned by successive generate or renew calls also strictly increase. Tokens can therefore be maintained in expiration order without a heap or a general sort.

Use an insertion-ordered mapping from token identifier to expiration. It provides direct identifier lookup while its first entry is always the next token due to expire.

**Discard only the expired prefix**

Before each public operation, inspect the mapping's first entry. While its expiration is less than or equal to `currentTime`, remove it. Stop at the first greater expiration; every later entry has an even later expiration and must also be unexpired.

This boundary implements the rule that expiration occurs before another action at the same time. Each token entry is removed at most once, so a cleanup that removes several entries charges its work to earlier insertions.

**Renew by moving the token to the end**

After cleanup, a token is renewable exactly when its identifier remains in the mapping. Replace its expiration with `currentTime + timeToLive` and move the entry to the end, where it belongs because the new expiration exceeds all previously assigned expirations.

Generation appends a new unique identifier in the same way. Counting cleans the expired prefix and returns the mapping size. The mapping consequently contains exactly all unexpired tokens after every operation, in increasing expiration order, which proves every renewal decision and count is correct.

#### Complexity detail

Direct lookup, insertion, renewal, moving an entry, and reading the mapping size are $O(1)$ expected time. Cleanup may remove several tokens in one call, but each generated token can be removed only once. Across $Q$ method calls the total cleanup work is $O(Q)$, so each operation is $O(1)$ amortized and the complete sequence takes $O(Q)$ time. Only unexpired token entries are retained, requiring $O(A)$ space.

#### Alternatives and edge cases

- **Hash map plus full count scan:** Generation and renewal are constant-time, but every count examines all stored tokens and can make a long sequence quadratic.
- **Hash map plus min-heap:** Lazy heap entries support $O(\log A)$ updates and expiration, but renewals leave stale entries and the ordering guarantee permits a simpler constant-amortized structure.
- **Deque plus hash map:** Appending expiration records also uses monotonic times, but renewals create stale deque records and can use $O(Q)$ rather than $O(A)$ space.
- **Expiration at the action time:** Treat `expiration <= currentTime` as expired before renewal or counting.
- **Missing or expired renewal:** Ignore it without creating a token.
- **Renewal reordering:** Moving a renewed early token to the end is essential because its new expiration is now the latest.
- **Several expired tokens:** Remove the entire expired prefix, not just one entry.
- **Unique generation IDs:** Generation never replaces an existing token, while renewal is the only operation that updates one.

</details>
