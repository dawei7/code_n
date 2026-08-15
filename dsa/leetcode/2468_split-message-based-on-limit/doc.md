# Split Message Based on Limit

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2468 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/split-message-based-on-limit/) |

## Problem Description

### Goal

Split `message` into one or more ordered parts. If the result contains $b$ parts, part $a$ must end with the suffix `"<a/b>"`, using one-based indices from $1$ through $b$.

Every part except the last must have length exactly `limit` after its suffix is included. The last part may be shorter but cannot exceed `limit`. Removing all suffixes and concatenating the remaining payloads in order must reconstruct `message` exactly.

Return a valid split with as few parts as possible. If no such split exists, return an empty array.

### Function Contract

**Inputs**

- `message`: A nonempty string consisting only of lowercase English letters and spaces.
- `limit`: The maximum length of each suffixed part.

Let $m=\lvert\texttt{message}\rvert$. The constraints are $1\le m\le10^4$ and $1\le\texttt{limit}\le10^4$.

**Return value**

- The minimum-count ordered split with each suffix and length rule satisfied, or `[]` when no split is possible.

### Examples

#### Example 1

- **Input:** `message = "this is really a very awesome message", limit = 9`
- **Output:** `["thi<1/14>","s i<2/14>","s r<3/14>","eal<4/14>","ly <5/14>","a v<6/14>","ery<7/14>"," aw<8/14>","eso<9/14>","me<10/14>"," m<11/14>","es<12/14>","sa<13/14>","ge<14/14>"]`
- **Explanation:** Parts $1$ through $9$ hold three payload characters each, and the two-digit indices in the remaining suffixes leave room for two each.

#### Example 2

- **Input:** `message = "short message", limit = 15`
- **Output:** `["short mess<1/2>","age<2/2>"]`
- **Explanation:** The first part fills the limit, while the final part may be shorter.
