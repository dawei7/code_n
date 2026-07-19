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
